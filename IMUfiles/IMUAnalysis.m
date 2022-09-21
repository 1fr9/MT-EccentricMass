%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                          Analysis IMU 9250                            %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
close all
clear all

filename = [' D:\Uni_Bremen\03_Master_PT\05_Master-Arbeit\' ...
    '11_Messungen\01_Snapback\H70\90\PVC2\3_70PVC2_69.csv'];

%% Set up the Import Options and import the data
opts = delimitedTextImportOptions("NumVariables", 14);

% Specify range and delimiter
opts.DataLines = [1, Inf];
opts.Delimiter = [" ", ",", ";"];

% Specify column names and types
opts.VariableNames = ["Date", "Time", "UnixEpoch", "Uptime", "Temp",...
    "rAccX", "rAccY", "rAccZ", "tAccX", "tAccY", "tAccZ", "Var12",...
    "Var13", "Var14"];
opts.SelectedVariableNames = ["Date", "Time", "UnixEpoch", "Uptime",...
    "Temp", "rAccX", "rAccY", "rAccZ", "tAccX", "tAccY", "tAccZ"];
opts.VariableTypes = ["datetime", "char", "double", "double",...
    "double", "double", "double", "double", "double", "double",...
    "double", "char", "char", "char"];

% Specify file level properties
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";
opts.ConsecutiveDelimitersRule = "join";

% Specify variable properties
opts = setvaropts(opts, ["Time", "Var12", "Var13", "Var14"],...
    "WhitespaceRule", "preserve");
opts = setvaropts(opts, ["Time", "Var12", "Var13", "Var14"],...
    "EmptyFieldRule", "auto");
opts = setvaropts(opts, "Date", "InputFormat", "yyyy-MM-dd");

% Import the data
tbl = readtable(filename, opts);

%% Convert to output type
Date = tbl.Date;
Time = tbl.Time;
UnixEpoch = tbl.UnixEpoch;
Uptime = tbl.Uptime;
Temp = tbl.Temp;
rAccX = tbl.rAccX;
rAccY = tbl.rAccY;
rAccZ = tbl.rAccZ;
tAccX = tbl.tAccX;
tAccY = tbl.tAccY;
tAccZ = tbl.tAccZ;

%% Clear temporary variables
clear opts tbl

%% Closer look in signals

strtX = findchangepts(tAccX); % Find start of experiment in x values
strtY = findchangepts(tAccY); % Find start of experiment in y values
strtZ = findchangepts(tAccZ); % Find start of experiment in z values

strtIdx = round(mean(strtY,strtZ)); % Calculate starting index

forerunX = tAccX(1:strtIdx); % Array vector with values before discharge
mForerunX = mean(forerunX); % Mean value of forerun
forerunY = tAccY(1:strtIdx);
mForerunY = mean(forerunY);
forerunZ = tAccZ(1:strtIdx);
mForerunZ = mean(forerunZ);

%% Convert time steps

timeStamp = datetime(UnixEpoch, 'convertfrom', 'posixtime', ...
    'Format', 'mm.ss.SSSS');

for i = 1:numel(tAccZ(strtIdx:end))
   t(i) = UnixEpoch(i)-UnixEpoch(1);  % Time of the experiment
end


%% Eigenfrequency

yMin = min(tAccY); % Set starting index after the release impuls
minStrtIdx = find(tAccY==yMin); 

meanTY = mean(tAccY(minStrtIdx:end)); % Move oscillation to origin
newAccY = tAccY(minStrtIdx:end)-meanTY;

for i = 1:numel(tAccZ(minStrtIdx:end))
   newT(i) = UnixEpoch(i)-UnixEpoch(1);  % Time of the experiment
end

Fs = 1/(mean(diff(newT))); %Frequency of the recorded data points in Hz
T = 1/Fs;             % Sampling period 
L = numel(newAccY);             % Length of signal
Y = fft(newAccY);    % Fast fourier transformation
P2y = abs(Y/L);% Two seided spectrum
P1y = P2y (1: L / 2 + 1);% One sided spectrum
P1y(2:end-1) = 2*P1y(2:end-1);
fy = Fs*(0:(L/2))/L;% Domain frequency for the acceleration in y direktion

figure
plot(fy,P1y)
xlabel('f (Hz)')
hold on
my = find(P1y==max(P1y));
plot(fy(my),P1y(my),'or');
natFeqy = fy(my);
labely = {strcat('   Eigenfrequenz = ', num2str(natFeqy))};
text(fy(my),P1y(my),labely,'HorizontalAlignment','left');




