%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                      Stochastic Excitation                            %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Max distance between the two magnets: 140 mm
% Range of the distance between the magnets, in which the magnets move:
% 40-140 mm

close all
clear all

load('Magnete.mat','ave'); % Load magnet curve

maxDis = 239;   % Maximal distanze in the measurement between the two 
% magnets
minDis = 32;    % Minimal distanze in the measurement between the two 
% magnets
measDis = [minDis:1:maxDis]; % Array of the measuret distance between the 
% two magnets
distance = [41:1:140]; % Distance range between the two magnets for the 
% repulsion force in experiment
disScale = zeros(numel(distance),2); % 2D Array, first column ist the 
% distance between the two magnets, second column is the corresponding 
% repulsion force
a = find(distance(1)==measDis); % a is the index for the min distance 
% between the magnets
b = find(distance(end)==measDis); % b is the index for the max distance 
% between the magnets

j=1;
for i = a:b  % Fill the scale array with the distance between the magnets 
    % and the corresponding repulsion force
    disScale(j,1) = measDis(i);
    disScale(j,2) = ave(i);
    j=j+1;
end


%%  Wave force

load ('WaveForces.mat');

%% Force Scale 

fScale = zeros(numel(disScale(:,1)),2);
fScale(:,1) = disScale(:,2);
fScale(:,2) = linspace(min(F),max(F),numel(disScale(:,1)));

for i=1:numel(fScale(:,2))
    g = fScale(:,2);
    h = F(i);  
    [~,idx]=(min(abs(g-h))); % Find min diff between F and fScale
    fktDis(i) = disScale(idx,1);
end

%% Scale motor steps

stepScale = zeros(numel(F),2);
stepScale(:,1) = linspace(0,100,numel(F));
stepScale(:,2) = linspace(0,140,numel(F));

for i = 1: numel(stepScale(:,1))
    g = stepScale(:,2);
    h = fktDis(i);
    [~,idx] = min(abs(g-h));
    motStep(i) = stepScale(idx);
end

motStep = round(motStep);

for i = 1:numel(wave1) % Filter out negative values and replace them with 
    % zero
    if wave1(i) < 0
        motStep2(i) = 0;
    else
        motStep2(i) = motStep(i);
    end
end

chng = find(diff(motStep))+1; % Find index of changes in motSteps
chng = [1 chng]; % Add first value
stepChng = motStep(chng); % Values of motStep without consecutive equal numbers


for i = 1:numel(chng)-1
    x1 = chng(i);
    x2 = chng(i+1);
    y1 = stepChng(i);
    y2 = stepChng(i+1);
    m(i) = (y2-y1)/(x2-x1);
end

mFirst = (stepChng(1)-stepChng(end))/(chng(1)-chng(end)); % Calculate 
% slope from last to first value
m = [mFirst m];

delayScale = zeros(30,2); % Left column: motor delay, right column: mean 
% slope of the interval 
delayScale(:,1) = linspace(0.001,0.01,30);
delayScale(:,2) = linspace(0,max(m),30);


for i = 1:numel(m);
    a = m(i);
    [~,idx]=(min(abs(delayScale(:,2)-a)));    % Find min difference 
    % between m and delayScale
    motDelay(i) = delayScale(idx,1);
end

for i = 1: numel(stepChng)-1
    difStepChng(i) = stepChng(i+1)-stepChng(i);
end

difEndFirst = stepChng(1)-stepChng(end); % Calculate step from last
% to forst step
difStepChng = [difEndFirst difStepChng];
difStepChng = abs(difStepChng);

motDir = sign(m);

for i = 1:numel(motDir)
    if motDir(i) == 1
        cWccW(i) = "CW";
    else
        cWccW(i) = "CCW";
    end
end

B = [cWccW; difStepChng; motDelay];

text1 = ['from time import sleep \nimport ' ...
    'RPi.GPIO as GPIO \n\nDIR = 20' ...
    '   # Direction GPIO Pin \nSTEP = 21  # Step GPIO Pin \nCW= 1   ' ...
    '# Clockwise Rotation \nCCW = 0  # ' ...
    'Counterclockwise Rotation \nSPR = 200' ...
    '   # Steps per Revolution (360 / 1.8) \n\nGPIO.setmode(GPIO.BCM)' ...
    ' \nGPIO.setup(DIR, GPIO.OUT) ' ...
    '\nGPIO.setup(STEP, GPIO.OUT) \n\nMODE' ...
    ' = (14, 15, 18) # Microstep ' ...
    'Resolution GPIO Pins \nGPIO.setup(MODE,' ...
    ' GPIO.OUT) \nRESOLUTION = {''Full'': (0, 0, 0), \n''HALF'':' ...
    ' (1, 0, 0), \n''1/4'': (0, 1, 0),' ...
    '\n''1/8'': (1, 1, 0), \n''1/16'':' ...
    ' (0, 0, 1), \n''1/32'': (1, 0, 1)} \nGPIO.output(MODE,' ...
    ' RESOLUTION[''1/32'']) \n\n'];

text2= ['GPIO.output(DIR, %s) \nSTP =  %1.0f \nDLY = %6.4f ' ...
    '\nstep_count = STP*32 \ndelay = DLY/32 \n ' ...
    '\nfor x in range(step_count):\n    GPIO.output(STEP, GPIO.HIGH) ' ...
    '\n    sleep(delay) \n    GPIO.output(STEP, GPIO.LOW) \n    ' ...
    'sleep(delay) \nsleep(.0001)\n\n'];

text3 = 'GPIO.cleanup()'

fileID = fopen('StochasticExcitation.py','w');
fprintf(fileID, text1);
fprintf(fileID, text2, B(:));
fprintf(fileID,text3);
fclose(fileID);



