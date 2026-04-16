# BCE horns

## Introduction

The aim of this work is to develop a horn contour for midrange horns that has an improved throat acoustic impedance characteristic compared to a conical horn, while still displaying constant directivity characteristics in the frequency band of interest.  To ease construction this horn contour will consist of three sections: throat, middle conical section and the mouth section.  The middle section will be conical to have flat walls, considerably easing construction complexity.  The mouth section will not be considered in this document but is of interest in future work for freestanding horns.    

For ease of comparison of the contours we consider only the simplest case of two section (throat and middle) axisymmetric (round) horns.  For simulation of impedance the finite horns will be terminated in acoustic absorber to eliminate mouth effects.  For assessment of high frequency directivity infinite baffle simulations will be conducted.  Four horns are the compared: conic, exponential, conic-exponential (CE) and the contour proposed in this work, blended conic-exponential (BCE).  

## Exponential horn:

![image](./media/exp.drawio.png)

For an exponential horn with cross sectional area, $A$ and cross sectional radius, $r$:

$$
\begin{align}
A(z)=A_0e^{k_ez}
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

Where $f_c$ is the exponential horn cutoff frequency and C the speed of sound ($343 ms^{-1}$ at $20\degree C$ and at sea level).  For the exponential horn the cutoff frequency is constant over the whole length of the horn.  The area expansion rate is exponential:

$$
\begin{align}
\frac{\text{d}A}{\text{d}z} = A_0k_ee^{k_ez}
\end{align}
$$

## Conic horn:

![image](./media/conic.drawio.png)

The horn contour is considered for axisymmetric conical horns with cross sectional area $A$, included angle $\theta_i$ and cross section radius, $r$:

$$
\begin{align}
r(z) = r_0+z\tan\left(\frac{\theta_i}{2}\right)
\end{align}
$$

$$
\begin{align}
A_0 = \pi (r_0)^2
\end{align}
$$

$$
\begin{align}
r(z) = \sqrt\frac{A_0}{\pi}+z\tan\left(\frac{\theta_i}{2}\right)
\end{align}
$$

$$
\begin{align}
A(z) = \pi r^2 = \pi\left(\frac{A_0}{\pi}+2z\tan\left(\frac{\theta_i}{2}\right)\sqrt\frac{A_0}{\pi}+z^2\tan^2\left(\frac{\theta_i}{2}\right)\right)
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
k_{C1} = 2\pi\tan{\left(\frac{\theta_i}{2}\right)}\sqrt{\frac{A_0}{\pi}} = \tan{\left(\frac{\theta_i}{2}\right)}\sqrt{4\pi A_0}
\end{align}
$$

$$
\begin{align}
k_{C2} = \pi\tan^2\left(\frac{\theta_i}{2}\right)
\end{align}
$$

The area expansion rate of the conic horn is therefore:

$$
\begin{align}
\frac{\text{d}A}{\text{d}z} = k_{C1}+2k_{C2}z
\end{align}
$$

The area expansion rate of the horn is increasing as we move away from the throat towards the mouth, but is not equal to the exponential expansion rate.  This introduces an area expansion rate discontinuity if a conical horn section is directly joined to a exponential horn section.

## Keele CE horns and hyperbolic horns

These horns are described in the paper ["WHAT'S SO SACRED ABOUT EXPONENTIAL HORNS?", D. B. KEELE, JR., 1975](https://dbkeele.com/7-whats-so-sacred-about-exponential-horns/).  For this horn type the throat horn contour is the exponential type which is smoothly joined to a conical horn by matching the wall angle.  From equation (2):

$$
\begin{align}
r_{exp}(z) = \sqrt{\frac{A_0}{\pi}}e^{\frac{1}{2}k_ez}
\end{align}
$$

$$
\begin{align}
\frac{\text{d}r_{exp}}{\text{d}z} = \frac{k_e}{2}\sqrt{\frac{A_0}{\pi}}e^{\frac{1}{2}k_ez}
\end{align}
$$

and for the conic horn, from equation (5):

$$
\begin{align}
\frac{\text{d}r_{conic}}{\text{d}z} = \tan\left(\frac{\theta_i}{2}\right)
\end{align}
$$

therefore the joining point is at:

$$
\begin{align}
\frac{\text{d}r_{exp}}{\text{d}z} = \frac{\text{d}r_{conic}}{\text{d}z}
\end{align}
$$

solving for z, at this point:

$$
\begin{align}
z_{join} = \frac{2\ln\left(\left(\frac{2\tan\left(\frac{\theta_i}{2}\right)}{k_e}\right)\left(\sqrt{\frac{\pi}{2}}\right)\right)}{k_e}
\end{align}
$$

However a complication is that hyperbolic throats are used in most of Keele's examples.  This has the following area expansion: 

$$
\begin{align}
A(z)_{t=1} = A_0\left(\cosh\left(\frac{zk_e}{2}\right)+t\sinh\left(\frac{zk_e}{2}\right)\right)^2 
\end{align}
$$

where t is the hyperbolic parameter, for $t = 1$ the equation reduces to the exponential case:

$$
\begin{align}
A(z)_{t=1} = A_0\left( \cfrac{e^{\cfrac{zk_e}{2}}+e^{\cfrac{zk_e}{2}}}{2} + \cfrac{e^{\cfrac{zk_e}{2}}-e^{\cfrac{zk_e}{2}}}{2}  \right)^2
\end{align}
$$

$$
\begin{align}
A(z)_{t=1} = A_0e^{k_ez}
\end{align}
$$

We can again solve the joining point using wall angle matching for the hyperbolic case:

???

Taking Keele's round axi-symetric example horn C1+ with the following parameters: ??? we can plot the wall contour and area:

??? figures

However if we examine the area with respect to the distance from the throat we see a discontinuity in the area expansion.  As an example the 60 x 40 horn HR6040 sketch from Keele's paper is plot:

(show discontinuity example)

It is observed that the area expansion is discontinuous.

## BCE horn:

In an effort to have both a smooth area expansion and a smooth wall contour we can define a linear blend of the two horns over length, $L_b$, reverting to the conventional conical form beyond the blended section (BCE horn):

$$
\begin{align}
A = \left(\frac{z}{L_b}\right)A_{c}+\left(1-\frac{z}{L_b}\right)A_{e}
\end{align}
$$

$$
\begin{align}
A(z) =
\begin{cases}
\left(\frac{z}{L_b}\right)(A_0+k_{C1}z+k_{C2}z^2)+\left(1-\frac{z}{L_b}\right)A_0e^{k_ez} & \text{if $z\le L_b$} \\
A_0+k_{C1}z+k_{C2}z^2 & \text{if $z > L_b$} \\
\end{cases} 
\end{align}
$$

We can obtain an approximation of length $L_b$, by the using the diameter of the horn at length $L_b$ from the throat.  We can assume the horn is a round piston and constrain the diameter of this piston such that beaming begins at $f_b$, where $f_b$ is the upper frequency limit of our constant directivity behavior.  The choice of this frequency is a balance between loading and usable bandwidth of the horn for off axis listeners. The book [P.G 576-577 High Quality Horn Loudspeaker Systems: History, Theory and Design, 2019, Kolbrek and Thomas](https://hornspeakersystems.info/), gives the equation:

$$
\begin{align}
D_t = \frac{K_{t,r}}{\sin\left(\frac{\theta_i}{2}\right)f_b}
\end{align}
$$

Several values are given for the $K_{t,r}$ constant:

(Values)
