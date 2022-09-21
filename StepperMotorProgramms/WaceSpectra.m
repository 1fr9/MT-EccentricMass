%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%               JONSWAP and PIERSON-MOSKOWITZ Sepctrum                  %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

close all;      % Close all open plots and images
clear all;            % Clear the workspace
%% Sea parameter 

Hs = 1.34;       % Signivicant wave height in m
Tp = 6.975;       % Spectral peak periode in s
wd = 30;        % Water depth in m
L = 50;     % Wavelength in m
k = (2*pi)/L;   % Wavenumber in 1/m
D = 5;  % Tower diameter
rho = 1024.7;     % Water density
Cd = 1.2;   % Drag coefficient
Cm = 2;     % Hydrodynamic mass
A = (pi*D^2)/4; % Cross sectional area
omega = linspace(0.01,3,100);    % Frequency bandwidth
omegaP = (2*pi)/Tp;     % Angular spectral peak period
t = linspace(1, 120, length(omega));     % Time array

SpecPM = zeros(numel(omega), 1);    % Array for Pierson-Moskowitz spectrum
SpecJONSWAP = zeros(numel(omega), 1);       % Array for JONSWAP spectrum

%% PIERSON-MOSKOWITZ Spectrum

for i = 1:numel(omega)
    SpecPM(i,1) = (5/16) * Hs^2 * omegaP^4 * omega(i)^-5 * exp(-(5/4) * ...
        (omega(i)/omegaP)^-4); % Equation for Pierson-Moskowitz spectrum 
    % from DNVGL-RP-C205 page 64-66
end

%% JONSWAP Spectrum

gamma = 3.3;     % Non-dimensional peak shape parameter, average value for 
% JONSWAP experimental data
gammaA = 1 - 0.287 * log(gamma);        % Normalizing factor
sigma = [];     % Spectral width parameter
sigmaA = 0.07;      % Avarverage value for JONSWAP experimental data
sigmaB = 0.09;      % Avarverage value for JONSWAP experimental data

if omega <= omegaP
    sigma = sigmaA;
else 
    sigma = sigmaB;
end

for i = 1:numel(omega)
    SpecJONSWAP(i,1) = gammaA * SpecPM(i,1) * ...
    gamma^exp(-0.5*(((omega(i)-omegaP)/(sigma*omegaP))^2)); % Equation for 
    % JONSWAP spectrum from DNVGL-RP-C205 page 64-66
end

%% Modeling of irregular linear waves according to DNVGL-RP-C205

deltaOmega = omega(2) - omega(1);       % Frequency step size
t = t';

Ak = sqrt(2 * SpecJONSWAP * deltaOmega);   % Amplitude Rayleigh distributed
ek = 2 * pi * rand(length(Ak), 1);  % Random phase between 0 and 2*pi

wave1 = sum(Ak .* cos(omega .* t + ek)); % Irregular linear random long-
% crested wave model according to DNVGL-RP-C205 page 51


%% Plot wave spectra and wave

figure('Name', 'Wave Spectra and modelled waves', 'Position', [25 50 ...
    1000 500]);
subplot(2,1,1)
title('Wave Spectra')
plot(omega, SpecPM);
hold on% Plot Pierson-Moskowitz spectrum 
xlabel('Omega (rad/s)');
ylabel('Spectrum (m^2.s)');
plot(omega, SpecJONSWAP);      % Plot JONSWAP spectrum 
xlabel('Omega (rad/s)');
ylabel('Spectrum (m^2 s)');
legend('Pierson-Moskowitz spectrum', 'JONSWAP spectrum');
subplot(2,1,2)
title('Modelled irrefular waves')
plot(t, wave1);
xlabel('Time (s)');
ylabel('Wave height (m)');

for i = 1:numel(t)
    Fd(i) = [1/8 *Cd * rho * D * wave1(i)^2 * omegaP^2 * wd*...
        ((sinh(2*k*wd)+2*k*wd)/(k*wd*(cosh(2*k*wd)-1)))*...
        abs(omegaP*i)*cos(omegaP*i)];
    Fm(i) = 1/8 *Cm * rho* A* wave1(i) * omegaP^2 * 1/k * sin(omegaP*i);
end
F = Fd +Fm;

figure
subplot(2,1,1)
plot(t,wave1)
xlabel('Zeit [s]')
ylabel('Wellenhöhe [m]')
subplot(2,1,2)
plot(t,Fd)
hold on
plot(t,Fm)
plot(t,F)
xlabel('Zeit [s]')
ylabel('Kraft [N]')
legend('Kraft infolge des Strömungswiderstandes', ['Kraft infolge der' ...
    ' Beschnleunigung'], 'Resultierende Kraft');
yline(0)

save('3WaveForces120s.mat','wave1', 'Hs','Tp','t','wd','L','k','D','rho', ...
    'Cd', 'Cm', 'A','omega','omegaP','F','Fd','Fm');
