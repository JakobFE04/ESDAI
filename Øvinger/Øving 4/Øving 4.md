# Oppgave 1)
## a) 
![[ESDA/Øvinger/Øving 4/1 a.png]]
![[1 a 2.png]]

Signalet blir dempet ca 50% og det er en ca 58.3 graders faseforskyvning mellom ut og inngangssignalene.

## b)
![[ESDA/Øvinger/Øving 4/1 b.png]]

$$
 \begin{equation} 
 V_{2_{10Hz}} = 6.3 mV
 \end{equation} 
$$
$$
 \begin{equation} 
  V_{2_{100Hz}} = 60mV
 \end{equation} 
$$
$$
 \begin{equation} 
  V_{2_{1kHz}} = 510mV
 \end{equation} 
$$
$$
 \begin{equation} 
  V_{2_{10kHz}} = 0.99V
 \end{equation} 
$$
$$
 \begin{equation} 
  V_{2_{100kHz}} = 1V
 \end{equation} 
$$
Dempingen på systemet vil være lik $V_{2}$ siden $\frac{|V_{2}|}{|V_{1}|}=|V_{2}|$.
Dempingen går mot 1 desto høyere frekvensen blir, og fase forskyvningen går mot 0 grader desto høyere frekvensen blir.

## c)

- Se bilde i b for fase forskyvningen.
- Vi kan se av grafene at ved 1kHz så har signalet $V_{2}$ ca 60 graders fase forskyvning og en fordempning på -5dB. Vet ikke helt hva mer mener med "fysisk" tolkning av grafene.
- Kretsen fungerer som et høypassfilter som demper lavere frekvens signaler og slipper igjennom høyere frekvens signaler.

# Oppgave 2)

![[ESDA/ESDAI/Øvinger/Øving 4/2 a.png]]
Den komplekse amplituden vil jo variere med frekvens så jeg tegnet en ved en vilkårlig høyere frekvens. Den vil bli negativt faseforskyvd siden kretsen er kapasativ og spenningen over kondensatoren vil minke jo høyere frekvens signalet har, altså et lavpass filter.

## b)
![[2 b.png]]Som forventet, så fungerer det som et lavpass filter fordi lave frekvenser passer igjennom mens høye frekvenser blir filtrert vekk.

## c)
Fra formelen vet vi at signalet $V_{1}$ har en kompleks amplitude = 5V og en frekvens på 2kHz. Fra grafen ser det ut som at ved 2kHz har $V_{2}$ en ca -5dB fordempning og en faseforskyvning på ca -45 grader. Det gir at:
$$
 \begin{equation} 
 V_{2}=2.8e^{-j\pi/4}e^{4000\pi t} =2.8\cos\left( 4000\pi t-\frac{\pi}{4} \right)
 \end{equation} 
$$
![[ESDA/ESDAI/Øvinger/Øving 4/2 c.png]]

Ikke så lett å lese av bilde i b) så litt off. Mer reelt utrykk for $V_{2}$ er:
$$
 \begin{equation} 
  V_{2}=3.1\cos(4000\pi t-0.87)
 \end{equation} 
$$
# Oppgave 3)

Gitt systemet i figuren og kirchoffs lover kan vi finne utrykk for $V_{2}$:
$$
 \begin{equation} 
 V_{2}=I\cdot Z_{2} 
 \end{equation} 
$$
$$
 \begin{equation} 
 V_{2}= \frac{V}{Z_{1}+Z_{2}}\cdot Z_{2}
 \end{equation} 
$$
$$
 \begin{equation} 
 V = V
 \end{equation} 
$$
$$
 \begin{equation} 
 H=\frac{V_{2}}{V}= \frac{\frac{V}{Z_{1}+Z_{2}}\cdot Z_{2}}{V}=\frac{Z_{2}}{Z_{1}+Z_{2}}
 \end{equation} 
$$

# Oppgave 4)
## a & b)
### I)

![[I).png]]
$$
 \begin{equation} 
 H(\omega)=\frac{V_{2}}{V_{1}}=\frac{Z_{2}}{Z_{1}+Z_{2}}=\frac{j\omega L}{R+j\omega L}=\frac{1}{1+\frac{R}{j\omega L}}=\frac{1}{1+\frac{1}{j\omega \tau}}
 \end{equation} 
$$
$$
 \begin{equation} 
 |H(\omega)|=\frac{1}{\sqrt{ 1+\left( \frac{1}{\omega \tau} \right)^2 }}
 \end{equation} 
$$
$$
 \begin{equation} 
\frac{1\cdot \left( 1-\frac{1}{j\omega \tau} \right)}{\left(1+ \frac{1}{j\omega \tau} \right)\cdot\left( 1-\frac{1}{j\omega \tau} \right)}=\frac{1-\frac{1}{j\omega \tau}}{\left( 1+\left( \frac{1}{\omega \tau} \right)^2 \right)}=\frac{1}{1+\left( \frac{1}{\omega \tau} \right)^2}-\frac{\frac{1}{j\omega \tau}}{1+\left( \frac{1}{\omega \tau} \right)^2}
 \end{equation} 
$$
$$
 \begin{equation} 
  \angle H(\omega) = -\arctan\left( \frac{1}{\omega \tau} \right)
 \end{equation} 
$$

### II)

![[II).png]]
$$
 \begin{equation} 
 H(\omega)=\frac{V_{2}}{V_{1}} =\frac{Z_{2}}{Z_{1}+Z_{2}}=\frac{\frac{1}{j\omega C}}{R+\frac{1}{j\omega C}}=\frac{1}{1+j\omega RC}=\frac{1}{1+j\omega \tau}
 \end{equation} 
$$
$$
 \begin{equation} 
 |H(\omega)| = \frac{1}{\sqrt{1+ (\omega \tau)^2 }}
 \end{equation}   
$$
$$
 \begin{equation} 
 \angle H(\omega)=-\arctan(\omega \tau) 
 \end{equation} 
$$
### III)
![[III).png]]

$$
 \begin{equation} 
 H(\omega)=\frac{V_{2}}{V_{1}}=\frac{Z_{2}}{Z_{1}+Z_{2}}=\frac{R}{\frac{1}{j\omega C}+R}=\frac{1}{1+\frac{1}{j\omega RC}}=\frac{1}{1+\frac{1}{j\omega \tau}} 
 \end{equation} 
$$
$$
 \begin{equation} 
 |H(\omega)|=\frac{1}{\sqrt{ 1+\frac{1}{(\omega \tau)^2} }} 
 \end{equation} 
$$
$$
 \begin{equation} 
 \angle H(\omega)=- \arctan\left( \frac{1}{\omega \tau} \right)
 \end{equation} 
$$
## c)

![[H_2.png]]
![[Fase H_2.png]]
![[H_3.png]]
![[Fase H_3.png]]
Plottene er like, eneste er hva mål og hvor strekt ut de er er ulikt. 

# Oppgave 5)
## a)

$$
 \begin{equation} 
 V_{2}=|H(\omega)|\cdot V_{1} 
 \end{equation} 
$$
$$
 \begin{equation} 
 V_{2}=\frac{V_{1}}{2}=\frac{1}{\sqrt{ 1+(2\pi f \tau)^2 }} \cdot V_{1}
 \end{equation} 
$$
$$
 \begin{equation} 
 \frac{1}{2}= \frac{1}{\sqrt{ 1+(2\pi f \tau)^2 }}
 \end{equation} 
$$
$$
 \begin{equation} 
\sqrt{ 1+(2\pi f \tau)^2 }=2
 \end{equation} 
$$
$$
 \begin{equation} 
 1+(2\pi f\tau)^2=4 
 \end{equation} 
$$
$$
 \begin{equation} 
 2\pi f\tau=\sqrt{ 3 } 
 \end{equation} 
$$
$$
 \begin{equation} 
 R=\frac{\sqrt{ 3 }}{2\pi fC}=\frac{\sqrt{ 3 }}{2\pi \cdot 275\cdot 100\cdot 10^{-9}} = 10024.6 \Omega \approx 10k\Omega
 \end{equation} 
$$

## b)

![[5 b.png]]

Koblet opp med en 10kohm motstand, litt usikkerhet i den som vanlig, men får ca 50% demping ved 275Hz eller ca -6dB.


## c)

![[5 c.png]]
Sammenlignet med grafene i oppgave 2 så faller amplituden/endrer faseforskyvningen seg mye raskere med 10kohm. Dette systemet vil altså kunn slippe igjennom ekstremt lave frekvenser. Den større motstanden gjør at det blir mindre strøm. Da vil spenningen over kondensatoren bli mindre siden endringen i strømmen vil bli mye mindre ved høyere frekvenser når det er redusert strøm i forhold til 1kohm kretsen.

# Oppgave 6)
## a)

![[6 a.png]]

$$
 \begin{equation} 
 H(\omega)=\frac{V}{V_{R}}=\frac{Z_{R}}{Z_{L}+Z_{R}}=\frac{R}{j\omega L+R}=\frac{1}{1+j\omega  \frac{L}{R}}=\frac{1}{1+j\omega \tau} 
 \end{equation} 
$$
$$
 \begin{equation} 
 |H(\omega)| = \frac{1}{\sqrt{1+ (\omega \tau)^2 }} 
 \end{equation}   
$$
$$
 \begin{equation} 
 \angle H(\omega)=-\arctan(\omega \tau) 
  \end{equation} 
$$

## b)
Samme utrykk som 5 a) bare $\tau=\frac{L}{R}$ så får da:

$$
 \begin{equation} 
 2\pi f \tau=\sqrt{ 3 } 
 \end{equation} 
$$
$$
\begin{equation} 
 R=\frac{2\pi f L}{\sqrt{ 3 }}=\frac{2\pi \cdot 275 \cdot 10 \cdot 10^{-3}}{\sqrt{ 3 }}= 99.75 \Omega \approx 100\Omega
 \end{equation} 
$$
## c)

$$
 \begin{equation} 
  |H_{RC}(f)|=0.5
 \end{equation} 
$$
$$
 \begin{equation} 
 \angle H_{RC}(f) =-1.05
 \end{equation} 
$$

$$
 \begin{equation} 
  |H_{LR}(f)|=0.5
 \end{equation} 
$$
$$
 \begin{equation} 
 \angle H_{LR}(f)=-1.05 
 \end{equation} 
$$
Ja de er helt like.

## d)
Jeg ville heller brukt RC kretsen enn LR kretsen, siden 100mH er en ganske stor spole og 100ohm er en ganske liten motstand. RC kretsen kan lages mye mer kompakt og er mer brukt i praksis. 

