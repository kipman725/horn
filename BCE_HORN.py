#Create a blended conic-exponential horn
from functions import acoustics; #acoustics related functions
import matplotlib.pyplot as plt
import numpy as np

#Parameters
z_res = 1e-3; #z-axis resolution
len = 1; #temp length to plot
A0 = np.pi*(25.4e-3/2)**2;

#Tests a function call
test_var = acoustics.SlotMaxBeam(6000, 40);
print(test_var);

ke = acoustics.FcExp(200);
print(ke);

z_cords = np.arange(0, len, z_res);
AExp = A0*np.e**(ke*z_cords);

#plot test horn
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(z_cords, AExp)  # Plot some data on the Axes.
ax.set_xlabel("Distance from throat [m]");
ax.set_ylabel("Area [m^2]");
plt.grid();
plt.show()                           # Show the figure.