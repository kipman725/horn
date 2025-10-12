#Create a blended conic-exponential horn
from functions import acoustics; #acoustics related functions
import matplotlib.pyplot as plt
import numpy as np

#Parameters
z_res = 1e-3; #z-axis resolution
len = 1; #temp length to plot
A0 = np.pi*(25.4e-3/2)**2; #1" throat area
FcExp = 200; #Exponential horn cutoff frequency
FhNCE = 6000; #Maximum frequency before beaming for NCE horn

ke = acoustics.FcExp(FcExp); #Exponential flare constant


#Flare constants for conic 
ThetaConic = 90;  #included angle of conic horn
ThetaConicR = np.deg2rad(ThetaConic); 
kc1 = np.sqrt(4*np.pi*A0)*np.tan(ThetaConicR/2);
kc2 = np.pi*np.tan(ThetaConicR/2)**2;
MaxThroat = acoustics.RoundMaxBeam(FhNCE, ThetaConic); #Maximum throat iameter in CE horn for given beaming frequency
#LNCE = (MaxThroat/2-25.4e-3/2)/np.tan(np.deg2rad(ThetaConic/2));
#print(MaxThroat/2);

#Areas of horns from throat to mouth
z_cords = np.arange(0, len, z_res);
AExp = A0*np.e**(ke*z_cords);
AConic = A0+kc1*z_cords+kc2*(z_cords)**2;

#Generate wall contours (round horn) 
YExp = np.sqrt(AExp/np.pi);
YConic = np.sqrt(AConic/np.pi);
YConicAlt = np.sqrt(A0/np.pi)+z_cords*np.tan(ThetaConicR/2);

#plot test horns
fig, ax = plt.subplots(2, 1, layout='constrained')       
ax[0].plot(z_cords, AConic, label='CONIC', );  # Plot some data on the Axes.
ax[0].plot(z_cords, AExp, label='EXP')
ax[0].set_xlabel("Distance from throat [m]");
ax[0].set_ylabel("Area [m^2]");
ax[0].grid(True);
ax[1].plot(z_cords, YConic, label='CONIC (Y)');
ax[1].plot(z_cords, YConicAlt, label='ALT CONIC(Y)');
ax[1].set_xlabel("Distance from throat [m]");
ax[1].set_ylabel("y [m]");
ax[1].grid(True);
fig.legend(loc='outside right upper')
plt.show()                           # Show the figure.
         
