Båndpassfilter:
![[Filter.png]]

Resonansfrekvens:
$$
 \begin{equation} 
 f_{0}=\frac{1}{\sqrt{ LC }}\cdot \frac{1}{2\pi}=3925\cdot 2
 \end{equation} 
$$
$$
 \begin{equation} 
 Q=\frac{f_{0}}{B}=\sqrt{ \frac{L}{CR^2} } = 10.14
 \end{equation} 
$$
$$
 \begin{equation} 
 L=100mH 
 \end{equation} 
$$
$$
 \begin{equation} 
 C=4.11nF \implies 4.4nF 
 \end{equation} 
$$
$$
 \begin{equation} 
 R=470\Omega 
 \end{equation} 
$$



 10

![[Scope RMS.png]]
![[Spectrum RMS.png]]

Målte effektivverdien (RMS)  med oscilloskop  for $V_{\hat{x}_{k}}=254.5mV$.
Deretter kan vi finne effektivverdien for den ønskelige frekvensen $V_{x_{k}}$ ved bruk av spektrumsanalysator. Målte verdien for $V_{x_{k}}=245.2mV$.

$$
 \begin{equation} 
 SDR=\frac{V^2_{x_{k}}}{V_{\hat{x}_{k}}^2-V_{x_{k}}^2}=\frac{245.2^2}{254.5^2-245.2^2}=12.94
 \end{equation} 
$$
$$
 \begin{equation} 
 SDR[dB]=10\log\left(\frac{V^2_{x_{k}}}{V_{\hat{x}_{k}}^2-V_{x_{k}}^2} \right) =11.12dB
 \end{equation} 
$$
C