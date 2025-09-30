# BCE horns

## Introduction

The aim of this work is to develop a horn contour for midrange horns that has an improved throat acoustic impedance characteristic compared to a conical horn, while still displaying constant directivity chacteristics in the frequency band of interest.  To ease construction this horn contour will consist of three sections: throat, middle conical section and the mouth section.  The middle section will be conical to have flat walls, considerably easing constuction complexity.    

For ease of comparison of the contours we consider only the simpliest case of two section (throat and middle) axisymetric (round) horns.  For simulation purposes the finite horns will be terminated in acoustic absorber to eliminate mouth effects.  Four horns are the compared: conic, exponential, conic-exponential and the contour proposed in this work, blended conic-exponential.

## Exponential horn:

Exponential horn, Area, A and cross section radius, r:

$$
\begin{align}
A(z)=A_0e^{k_eZ}
\end{align}
$$

$$
\begin{align}
r(z) = \sqrt{\frac{A(z)}{\pi}}
\end{align}
$$

$$
\begin{align}
k_e = \frac{4\pi f_c}{C}
\end{align}
$$

Where $f_c$ is the exponential horn cuttoff frequency and C the speed of sound ($343 ms^{-1}$ at $20\degree C$ and at sea level).  For the exponential horn the cuttoff frequeny is constant over the whole length of the horn.  The area expansion rate is exponential:

$$
\begin{align}
\frac{dA}{dz} = A_0k_ee^{k_eZ}
\end{align}
$$

## Conic horn:

$$
\begin{align}
r = r_0+z\tan\big(\frac{\theta_i}{2}\big)
\end{align}
$$

$$
\begin{align}
A_0 = \pi (r_0)^2
\end{align}
$$

$$
\begin{align}
r(z) = \sqrt\frac{A_0}{\pi}+z\tan\big(\frac{\theta_i}{2}\big)
\end{align}
$$

$$
\begin{align}
A(z) = \pi r^2 = \pi\big(\frac{A_0}{\pi}+2z\tan\big(\frac{\theta_i}{2}\big)\sqrt\frac{A_0}{\pi}+z^2\tan^2\big(\frac{\theta_i}{2}\big)\big)
\end{align}
$$

Therefore Let:

$$
\begin{align}
A(z) = A_0 + k_{C1}z+k_{C2}z^2
\end{align}
$$

$$
\begin{align}
k_{C1} = 2\pi\tan{\big(\frac{\theta_i}{2}\big)}\sqrt{\frac{A_0}{\pi}} = \tan{\big(\frac{\theta_i}{2}\big)}\sqrt{4\pi A_0}
\end{align}
$$

$$
\begin{align}
k_{C2} = \tan^2\big(\frac{\theta_i}{2}\big)
\end{align}
$$

The area expansion rate of the conic horn is therfore:

$$
\begin{align}
\frac{dA}{dz}=k_{C1}+2k_{C2}z
\end{align}
$$

The area expansion rate of the horn is increasing as we move away from the throat towards the mouth, but is not equal to the exponential expansion rate.  This introduces an area expansion rate discontinuity if a conical horn section is directly joined to a exponential horn secion.

## Keele CE horns 

Explain this horn and the joining method and joining point for axisymetric horns. (horn wall angle match)

## BCE horn:

We can then define a linear blend of the two horns over length, $L_b$, reverting to the conventional conical form beyond the blended section (BCE horn):

$$
\begin{align}
A = \big(\frac{z}{L_b}\big)A_{c}+\big(1-\frac{z}{L_b}\big)A_{e}
\end{align}
$$

$$
\begin{align}
A(z) =
\begin{cases}
\big(\frac{z}{L_b}\big)(A_0+k_{C1}z+k_{C2}z^2)+\big(1-\frac{z}{L_b}\big)A_0e^{k_eZ} & \text{if $z\le L_b$} \\
A_0+k_{C1}z+k_{C2}z^2 & \text{if $z > L_b$} \\
\end{cases} 
\end{align}
$$


