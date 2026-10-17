%Compare effective cutoff frequency of conical horn along its length 

z = [0:1e-3:0.5]; %horn axis
A0 = pi*(25.4e-3/2)^2; %1" throat
fc = 600; %Cutoff of exponential
C = 343; %speed of sound
ke = 4*pi*fc/C;
theta_i = deg2rad(60);

%Plot horns over 1m
kc1 = tan(theta_i/2)*sqrt(4*pi*A0);
kc2 = pi*tan(theta_i/2);
A_conic = A0+kc1.*z+kc2*z.^2; 
r_conic =  sqrt(A_conic/pi);
A_exp = A0*e.^(ke.*z);  
r_exp =  sqrt(A_exp/pi);

%Calculate gradient of horns area
g_conic = gradient(A_conic, 1e-3);
g_exp = gradient(A_exp, 1e-3);

%Analytical gradient calculation
ga_conic = kc1+2*kc2*z;
ga_exp = A0*ke*e.^(ke.*z)

%plot horns
figure(1)
plot(z,r_conic);
hold;
plot(z,r_exp);
hold off;
grid;

%plot horns
figure(2)
plot(z,ga_conic);
hold;
plot(z,ga_exp);
hold off;
grid;

