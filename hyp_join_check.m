%test joining of hyperbolics

z = [0:1e-3:0.6]; %horn axis
A0 = pi*(25.4e-3/2)^2; %1" throat
fc = 300; %Cutoff of exponential section
C = 343; %speed of sound
ke = 4*pi*fc/C;
theta_i = deg2rad(90);
t = 0.5;

%Use joining point equation
z_join_exp = (log(4*pi/A0/ke^2)+2*log(tan(theta_i/2)))/ke;
z_join_hyp = log((-A0*ke**2*t**2 + A0*ke**2 + 4*sqrt(pi)* ...
sqrt(-A0*ke**2*t**2 + A0*ke**2 + 4*pi*tan(theta_i/2)**2)*tan(theta_i/2) ...
 + 8*pi*tan(theta_i/2)**2)/(A0*ke**2*(t**2 + 2*t + 1)))/ke;

%find areas at the join 
A_join_hyp = A0*(cosh(ke*z_join_hyp/2)+t*sinh(ke*z_join_hyp/2))^2;  
A_join_exp = A0*e^(ke*z_join_exp);  


kc1_hyp = tan(theta_i/2)*sqrt(4*pi*A_join_hyp); %conic starts from exp
kc1_exp = tan(theta_i/2)*sqrt(4*pi*A_join_exp);
kc2 = pi*tan(theta_i/2)^2;

%Add in horn plotting for visual checks!!

%plot the horns
for loop=1:length(z)
  A_hyp(loop) = A0.*(cosh(ke.*z(loop)/2)+t*sinh(ke.*z(loop)/2)).^2;
  A_exp(loop) = A0*e^(ke*z(loop));    
  if (z(loop) > z_join_hyp)
    A_hyp(loop) = (A_join_hyp+kc1_hyp*(z(loop)-z_join_hyp)+kc2*(z(loop)-z_join_hyp)^2);
  else
    A_hyp(loop) = A_hyp(loop);
  endif
  if z(loop) > z_join_exp
    A_exp(loop) = (A_join_exp+kc1_exp*(z(loop)-z_join_exp)+kc2*(z(loop)-z_join_exp)^2);
  else
    A_exp(loop) = A_exp(loop);
  endif
end;
r_hyp = sqrt(A_hyp./pi);
r_exp = sqrt(A_exp./pi);


figure(1)
%plot(z, gradient(A_ce));
plot(z, r_hyp, 'r');
hold;
plot(z, r_exp, 'b');
hold off;

figure(2)
plot(z, gradient(r_hyp, 1e-3), 'r');
hold;
plot(z, gradient(r_exp, 1e-3), 'b');
hold off;

figure(3)
plot(z, A_hyp, 'r');
hold;
plot(z, A_exp, 'b');
hold off;

figure(4)
plot(z, gradient(A_hyp, 1e-3), 'r');
hold;
plot(z, gradient(A_exp, 1e-3), 'b');
hold off;

%semilogy(z, A_exp);
%hold;
%semilogy(z, A_ce, 'r');
%hold off;
%grid;
