# BCE horns

## Introduction

The aim of this work is to develop a horn contour for midrange horns that has an improved throat acoustic impedance characteristic compared to a conical horn, while still displaying constant directivity chacteristics in the frequency band of interest.  To ease construction this horn contour will consist of three sections: throat, middle conical section and the mouth section.  The middle section will be conical to have flat walls, considerably easing constuction complexity.    

For ease of comparison of the contours we consider only the simpliest case of two section (throat and middle) axisymetric (round) horns.  For simulation purposes the finite horns will be terminated in acoustic absorber to eliminate mouth effects.  Four horns are the compared: conic, exponential, conic-exponential and the contour proposed in this work, blended conic-exponential.

## Exponential horn:

Exponential horn, Area, A and cross section radius, r:

$A(z)=A_0e^{k_eZ}$

$r(z) = \sqrt{\frac{A(z)}{\pi}}$

$k_e = \frac{4\pi f_c}{C}$ 

Where $f_c$ is the exponential horn cuttoff frequency and C the speed of sound ($343 ms^{-1}$ at $20\degree C$ and at sea level).  For the exponential horn the cuttoff frequeny is constant over the whole length of the horn 

## Conic horn:

$r = r_0+z\tan\big(\frac{\theta_i}{2}\big)$

$A_0 = \pi (r_0)^2$

$r(z) = \sqrt\frac{A_0}{\pi}+z\tan\big(\frac{\theta_i}{2}\big)$

$A(z) = \pi r^2 = \pi\big(\frac{A_0}{\pi}+2z\tan\big(\frac{\theta_i}{2}\big)\sqrt\frac{A_0}{\pi}+z^2\tan^2\big(\frac{\theta_i}{2}\big)\big)$

Therefore Let:

$A(z) = A_0 + k_{C1}z+k_{C2}z^2$

$k_{C1} = 2\pi\tan{\big(\frac{\theta_i}{2}\big)}\sqrt{\frac{A_0}{\pi}} = \tan{\big(\frac{\theta_i}{2}\big)}\sqrt{4\pi A_0}$

$k_{C2} = \tan^2\big(\frac{\theta_i}{2}\big)$

The area expansion rate of the conic horn is therfore:

$\frac{dA}{dz}=k_{C1}+2k_{C2}z$

The expansion rate of the horn is increasing as we move away from the throat towards the mouth.

We can then define a linear blend of the two horns over length, $L_b$, reverting to the conventional conical form beyond the blended section:

$A = \big(\frac{z}{L_b}\big)A_{c}+\big(1-\frac{z}{L_b}\big)A_{e}$

$A(z) = \big(\frac{z}{L_b}\big)(A_0+k_{C1}z+k_{C2}z^2)+\big(1-\frac{z}{L_b}\big)A_0e^{k_eZ} \quad \{ \ z \le L_b$

$A(z) = A_0+k_{C1}z+k_{C2}z^2 \quad \{ \ z > L_b$

$$
\begin{align}
  a &= b + c \\
  d &= e + f
\end{align}
$$
$$
X =
\begin{cases}
1 & \text{if $a=0$} \\
1 & \text{if $b=1$} \\
1 & \text{if $c=5$} \\
1 & \text{if $d=9$} \\
0 & \text{otherwise}
\end{cases}
$$