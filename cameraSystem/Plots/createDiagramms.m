%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(2)%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%                            Create diagrams                            %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear all
close all

load ('..\MeasuredValues\SNPBCK.mat')
load ('..\MeasuredValues\SNPBCK_IL.mat')
load('..\MeasuredValues\STCH.mat')
load('..\MeasuredValues\STCH_IL.mat')
load('..\MeasuredValues\ZENT.mat')

%% Print

newLables =  ["z","y"];

fig = gcf;
fig.PaperUnits = 'centimeters';
fig.PaperSize = [21 29.7];
fig.PaperPosition = [1 1 20 28];
fig.PaperType = 'a4';

subplot(6,1,1)
plot(STCH_IL.N1_70MET2_ST_IL(:,1,3),STCH_IL.N1_70MET2_ST_IL(:,2,3),'r')
axis equal
ylabel('z-Richtung')
xlabel('y-Richtung')
title('1. Stochastisch MET2 - 70 mm - 0°')
subplot(6,1,2)
stackedplot(STCH_IL.N1_70MET2_ST_IL(:,:,3), 'DisplayLabels',newLables, 'Color','r')
xlabel('Bilder')


subplot(6,1,3)
plot(STCH_IL.N2_70MET2_ST_IL(:,1,3),STCH_IL.N2_70MET2_ST_IL(:,2,3), 'r')
axis equal
ylabel('z-Richtung')
xlabel('y-Richtung')
title('2. Stochastisch MET2 - 70 mm - 0°')
subplot(6,1,4)
stackedplot(STCH_IL.N2_70MET2_ST_IL(:,:,3), 'DisplayLabels',newLables, 'Color','r')
xlabel('Bilder')

subplot(6,1,5)
plot(STCH_IL.N3_70MET2_ST_IL(:,1,3),STCH_IL.N3_70MET2_ST_IL(:,2,3), 'r')
axis equal
ylabel('z-Richtung')
xlabel('y-Richtung')
title('3. Stochastisch MET2 - 70 mm - 0°')
subplot(6,1,6)
stackedplot(STCH_IL.N3_70MET2_ST_IL(:,:,3), 'DisplayLabels',newLables, 'Color','r')
xlabel('Bilder')

print(fig, '70MET2STCH_IL','-dpdf')

clear newLables
close all


