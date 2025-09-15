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

# LNCE = np.log(MaxThroat/A0)/ke; #Length of throat adaptor using this size
# print(LNCE);



#Flare constants for conic 
ThetaConic = 45;  #included angle of conic horn
kc1 = np.sqrt(4*A0/np.pi)*np.tan(np.deg2rad(ThetaConic));
kc2 = (np.tan(np.deg2rad(ThetaConic)))**2;
MaxThroat = acoustics.RoundMaxBeam(6000, 40); #Maximum throat iameter in CE horn for given beaming frequency
LNCE = (MaxThroat/2-25.4e-3/2)/np.tan(np.deg2rad(ThetaConic/2));
print(MaxThroat/2);
print(LNCE);

#test of finding roots x^2+x+c
#roots = np.roots([np.tan(np.deg2rad(ThetaConic))**2, np.sqrt(4*A0/np.pi)*np.tan(np.deg2rad(ThetaConic)), A0-MaxThroat])
#print(MaxThroat);
#print(roots);


#Areas of horns from throat to mouth
z_cords = np.arange(0, len, z_res);
AExp = A0*np.e**(ke*z_cords);
AConic = A0+kc1*z_cords+kc2*(z_cords)**2;

#Generate wall contours (round horn) 
YExp = np.sqrt(AExp/np.pi);
YConic = np.sqrt(AConic/np.pi);
YConicAlt = np.sqrt(A0/np.pi)+z_cords*np.tan(ThetaConic/2);

#plot test horns
fig, ax = plt.subplots(2, 1, layout='constrained')       
ax[0].plot(z_cords, AConic, z_cords, AExp);  # Plot some data on the Axes.
ax[0].set_xlabel("Distance from throat [m]");
ax[0].set_ylabel("Area [m^2]");
ax[0].grid(True);
ax[1].plot(z_cords, YConic, z_cords, YConicAlt);
ax[1].set_xlabel("Distance from throat [m]");
ax[1].set_ylabel("y [m]");
ax[1].grid(True);
plt.show()                           # Show the figure.
         
