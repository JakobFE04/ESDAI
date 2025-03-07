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

Realisering og test:

Fikk ikke helt korrekt frekvens for resonansfrekvensen når jeg målte med 68nF, så la til 3.3nF, 4,7nF og 470pF. Dette kommer nok av spolen som har stor usikkerhet.


![[Pasted image 20250307114304.png]]


![[Bodeplot dB.png]]
![[Phase Bode plot.png]]
![[Magnitude Spectrum.png]]

