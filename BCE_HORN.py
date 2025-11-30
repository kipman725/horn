#Create a blended conic-exponential horn
from functions import acoustics; #acoustics related functions
import matplotlib.pyplot as plt
import numpy as np

#Parameters
z_res = 10e-3; #z-axis resolution
len = 1; #temp length to plot
A0 = np.pi*(25.4e-3/2)**2; #1" throat area
FcExp = 200; #Exponential horn cutoff frequency
FhBCE = 3000; #Maximum frequency before beaming for BCE horn

ke = acoustics.FcExp(FcExp); #Exponential flare constant


#Flare constants for conic 
ThetaConic = 40;  #included angle of conic horn
ThetaConicR = np.deg2rad(ThetaConic); 
kc1 = np.sqrt(4*np.pi*A0)*np.tan(ThetaConicR/2);
kc2 = np.pi*np.tan(ThetaConicR/2)**2;
MaxThroatD = acoustics.RoundMaxBeam(FhBCE, ThetaConic); #Maximum throat diameter in CE horn for given beaming frequency

#Areas of horns from throat to mouth
z_cords = np.arange(0, len, z_res);
AExp = A0*np.e**(ke*z_cords);
AConic = A0+kc1*z_cords+kc2*(z_cords)**2;
coeff = [kc2, kc1, A0-np.pi*(MaxThroatD/2)**2]; #Find length of lb for BCE
Lb = np.max(np.roots(coeff));
ABCE = np.zeros(z_cords.size);
for x in range(0, z_cords.size):
    if z_cords[x] <= Lb:
        ABCE[x] = (z_cords[x]/Lb)*(A0+kc1*z_cords[x]+kc2*z_cords[x]**2)+(1-z_cords[x]/Lb)*A0*np.e**(ke*z_cords[x]);
    else:
        ABCE[x] = A0+kc1*z_cords[x]+kc2*(z_cords[x])**2;

#Generate wall contours (round horn) 
YExp = np.sqrt(AExp/np.pi);
YConic = np.sqrt(AConic/np.pi);
YBCE = np.sqrt(ABCE/np.pi);

with open("File.txt", "w") as f:   # Opens file and casts as f 
    f.write('\n'); #Write preample 
    f.write('Nodes "Nodes"\n');
    f.write('  Scale=1mm\n')
    for x in range(0, z_cords.size):  
        f.write("%d %f %F\n" % (x, z_cords[x], YBCE[x]));

#plot test horns
fig, ax = plt.subplots(2, 1, layout='constrained')       
ax[0].plot(z_cords, AConic, label='CONIC', );  # Plot some data on the Axes.
ax[0].plot(z_cords, AExp, label='EXP')
ax[0].plot(z_cords, ABCE, label='BCE')
ax[0].set_xlabel("Distance from throat [m]");
ax[0].set_ylabel("Area [m^2]");
ax[0].grid(True);
ax[1].plot(z_cords, YConic, label='CONIC (Y)');
ax[1].plot(z_cords, YExp, label='EXP (Y)');
ax[1].plot(z_cords, YBCE, label='EXP (Y)');
ax[1].set_xlabel("Distance from throat [m]");
ax[1].set_ylabel("y [m]");
ax[1].grid(True);
fig.legend(loc='outside right upper')
plt.show()                           # Show the figure.
         
