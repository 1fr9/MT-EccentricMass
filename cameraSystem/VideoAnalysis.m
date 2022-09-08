%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                              Video Analysis                           %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%Tracking for master thesis "Vibrations in cantilevered beams with
% eccentric masses under stocjastic loading"

%% Load video and calibrate camera

V = VideoReader(['\3_70PVC2_STCH-IL.mp4']); % Load video


if exist('cameraParameters') == 2
    numCaliImages = 22;      % Number of calibration images (it is recomended 
    % to use 10-20)
    calibrationImages = cell(1,numCaliImages); % Cell array for the calibration
    % images 
    for i = 1:numCaliImages % Load calibration images
        calibrationImages{i} = fullfile(...
        ['\CalibrationImages'], ...
            sprintf('CalibrationImage%d.jpg',i));
    end
    
    [imagePoints, boardSize] = detectCheckerboardPoints(calibrationImages); % 
    % Detect the checkerboard corners in the images
    squareSize = 15;    % Square size of the chessboard-squares in mm
    worldPoints = generateCheckerboardPoints(boardSize, squareSize); % Generate
    % world points
    
    % Calibrate camera
    I = imread(calibrationImages{1}); % Load one image vor calibration
    imageSize = [size(I, 1), size(I, 2)]; % Get the image size
    [cameraParameters, ~, estimationErrors] = estimateCameraParameters(...
        imagePoints, worldPoints,'ImageSize', imageSize); % Estimate camera 
    % parameters
    
    % Evaluate calibration accuracy.
    figure('Name', 'Calibration accuarcy', 'Position', [25 50 1000 600]); 
%     subplot(1,2,1)
    showReprojectionErrors(cameraParameters);  % Reprojektion error 
    title('Durchschnittlicher Reprojektionsfehler pro Bild')
    xlabel('Bilder')
    ylabel('Durchschnittlicher Fehler in Pixel')
    subplot(1,2,2)
    showExtrinsics(cameraParameters,'CameraCentric'); % Extrinsics 
    title('Extrinsische Parameter der Kamera')
end

n = V.NumFrames; % Number of frames

nFrame = 1; % Frame number initialization

posTag = zeros(n,2,2); % Array for the position of the tag

while(nFrame <= n)

    frame = read(V,nFrame); % Load image to be analyzed

%% Filter image

    [undisFrame, newOrigin] = undistortImage(frame,cameraParameters,...
        'OutputView', 'full'); % Undistore image and generate new origin
     grayFrame = rgb2gray(undisFrame); % Change to gray image to detect red
    % tags   
    subRed = imsubtract(undisFrame(:,:,1), grayFrame); % Get red component 
    % of undisFrame  
    subBckGrnd = imopen(subRed,strel('disk',26)); % Filter Background
    binFrame = imbinarize(subBckGrnd); % Convert the image into binary 
    % image with the RED objects as white
    labeledFrame = bwlabel(binFrame); % Label blobs in binFrame
    blobMeasurement = regionprops(labeledFrame, 'area', 'Centroid',...
        'Circularity'); % Measure the blobs to filter for the tags   
    allAreas = [blobMeasurement.Area]; %Get the area size of the blobs
    allCircularity = [blobMeasurement.Circularity]; % Get the circularity
    % of the blobs
    areaIndex = (allAreas > 5000) & (8000 > allAreas); % Area condition for 
    % the Blobs (Attention: With changed camera position also the size of  
    % the blobs changes)
    circularIndex = (allCircularity > 0.75) & (1.25 > allCircularity); % 
    % Circularity condition for the Blobs 
    keeperIndexes = find(areaIndex & circularIndex); % Filter for blobs
    keeperFrame = ismember(labeledFrame, keeperIndexes); % Filter the tags 
    % from the image
      
   
    %% Calculate positions
    
    [binDetectedTags, numberOfBlobs] = bwlabel(keeperFrame); % Label  
    % detected tag
    tagMeasurement = regionprops(binDetectedTags, 'area', 'Centroid'); % 
    % Measure tag
    if numberOfBlobs == 1
        thisCentroid = [tagMeasurement.Centroid(1), ...
            tagMeasurement.Centroid(2)]; % Determine the canter of the 
        % tags
        posTag(nFrame, 1,1) = thisCentroid(1); % X-position of the 
            % detected tag
        posTag(nFrame, 2,1) = thisCentroid(2); % Y-position of the 
            % detected tag
    else % No detected tag
        posTag(nFrame, 1,1) = NaN;
        posTag(nFrame, 2,1) = NaN;
    end

    nFrame = nFrame + 1
end

%%Inspekt plots to determine the boundary for correction of the initial
%%offset


a = 2000; % Boundary to determine the offset
figure
subplot(3,1,1)
plot(posTag(:,1,1), posTag(:,2,1));
subplot(3,1,2)
hold on
plot(posTag(:,1));
title('x Richtung')
limitX = posTag(a:end,1,1);
xMean = mean(limitX);
yline(xMean)
subplot(3,1,3)
hold on
plot(posTag(:,2,1));
title('y Richtung')
hold on
limitY = posTag(a:end,2,1);
yMean = mean(limitY);
yline(yMean)

posTag(:,1,2) = posTag(:,1,1)-xMean; % Subtract the offset to move the 
% curves to the origin 
posTag(:,2,2) = posTag(:,2,1)-yMean; % 

d = sqrt((allAreas*4)/pi);  % Diameter in pixel
mmPerPix = 19/d;    % mm per pixel

posTag(:,1,3) = mmPerPix * posTag(:,1,2); % Store position in mm z
posTag(:,2,3) = mmPerPix * posTag(:,2,2); % Store position in mm y


figure
plot(posTag(:,1,3),posTag(:,2,3))
axis equal


STCH_IL.N3_70PVC2_ST_IL = posTag;

clearvars -except STCH_IL cameraParameters

save(['\MeasuredValues\STCH_IL.mat'],'STCH_IL', 'cameraParameters'); %
% Save struct




