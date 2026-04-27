%Check exponential horn join point

z = [0:1e-3:1]; %horn axis
A0 = pi*(25.4e-3/2)^2; %1" throat
fc = 400; %Cutoff of exponential section
C = 343; %speed of sound
ke = 4*pi*fc/C;
theta_i = deg2rad(90);

%Use joining point equation
z_join = (log(4*pi/A0/ke^2)+2*log(tan(theta_i/2)))/ke;

%Find the area at the join for the offset of the conic 
A_join_exp = A0*e^(ke*z_join);  


kc1 = tan(theta_i/2)*sqrt(4*pi*A_join_exp); %conic starts from exp
kc2 = pi*tan(theta_i/2)^2;

%plot the horn
for loop=1:length(z)
  A_exp(loop) = A0*e^(ke*z(loop));  
  if z(loop) > z_join;
    A_ce(loop) = (A_join_exp+kc1*(z(loop)-z_join)+kc2*(z(loop)-z_join)^2);
  else
    A_ce(loop) = A_exp(loop);
  endif
end;
r_exp = sqrt(A_exp./pi);
r_ce = sqrt(A_ce./pi);


figure(1)
plot(z, gradient(A_ce));
%semilogy(z, A_exp);
%hold;
%semilogy(z, A_ce, 'r');
%hold off;
%grid;
