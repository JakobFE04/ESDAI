![[Måling lydsignal v1.png]]
![[Måling lydsignal v2.png]]
1.9381 kHz er støyet.

Har en L = 100mH

Vil lage et bånnstopp filter som vil filtrere vekk 1.9381kHz med liten motstand.

Vil finne kondensatorverdien som gir resonansfrekvens ved 1.9381kHz
$$
 \begin{equation} 
 0=j\omega L-j \frac{1}{\omega C}
 \end{equation} 
$$
$$
 \begin{equation} 
 \frac{1}{\omega C}=\omega L \implies C=\frac{1}{L\omega^2}=\frac{1}{0.100\cdot(2\cdot \pi \cdot1938.1)^2}=67.4nF
 \end{equation} 
$$
$$
 \begin{equation} 
 f = \frac{1}{2\pi\sqrt{ LC }} 
 \end{equation} 
$$

Realisering og test:

Fikk ikke helt korrekt frekvens for resonansfrekvensen når jeg målte med 68nF, så la til 3.3nF, 4,7nF og 470pF i parallell som gir en kapasitans på ca 76,5nF. Dette kommer nok av spolen som har stor usikkerhet. Ved å snu


![[måling screenshot.png]]


![[Bodeplot dB.png]]
![[Phase Bode plot.png]]
![[Magnitude Spectrum.png]]



dB bode plott 2 filter -56.9 dB
phase bode plott 2 filter -32.6 degrees

dB bode plott 1 filter  -29.9 dB
phase bode plott 1 filter -33.6 degrees