# Oppgave 0)

![[Opg 0.png]]
Satte opp en RL krets med $R=1k\Omega$ og målte dempningen ved 1kHz.
Regnet så fram til at spolen min har en verdi på $0.1000477H\approx 100mH$. 


# Oppgave 1)
## a)

Resonansfrekvensen er gitt ved formelen: 
$$
 \begin{equation} 
 \omega_{0}=\frac{1}{\sqrt{ LC }}=\frac{1}{\sqrt{ 0.1\cdot 100\cdot 10^{-9} }} = 10kHz
 \end{equation} 
$$
## b)
![[opg 1 kobling.png]]
![[opg 1 b.png]]
Ved 10kHz så ser vi at spenningen over motstanden er tilnærmet lik inngangsignalet.
![[ESDA/Øvinger/Øving 5/1 b.png]]

## c)
![[opg 1 c.png]]Reduseres motstanden veldig mye så vil den bli faseforskyvd fram til du får en kortslutning hvor det er null spenning.

![[1 c 1.png]]![[1 c 2.png]]

Ved veldig lave motstand så blir |VL| forsterket og faseforskjøvet i forhold til |V|. Summen av |VL| og |VC| vil da bli lik |V| som stemmer med Kirchhoffs spenningslov. Dette er fordi de er ulikt og motsatt faseforskjøvet og forsterket slik at når det er ingen spenning over motstanden (R = 0) så vil summen av de bli lik |V|.

# Oppgave 2)
## a)

a) = Høypass
b) = Båndstopp
c) = Båndpass

## b)
### Figur 3 a)
![[Opg 2 fig 3a.png]]
- Nei det var et båndpassfilter 
- Resonansfrekvensen er de frekvensene som slipper igjennom filteret
- Den får null faseforskyving ved ca 11.39kHz som er resonansfrekvensen.
### c)
![[Opg 2 c fig 3a.png]]
Ved mindre motstandsverdier så blir formen mer spiss mot resonansfrekvensen, og signalene rundt blir mer dempet.

### Figur 3 b)
![[Opg 2 fig 3b.png]]
- Nei det ble båndpass
- Resonansfrekvensen er når signalet er 90 grader faseforskjøvet
- Får null faseforskyving ved ca 500kHz fordi det er et stort høypassfilter
### c)
![[Opg 2 fig 3b c.png]]

### Figur 3 c)
![[Opg 2 fig 3c.png]]
- Nei det ble et lavpass filter
- Resonansfrekvensen er når signalet er -90 graders faseforskjøvet
- Får null faseforskyving ved lave frekvenser.
### c)
![[Opg 2 fig 3c c.png]]Får en mye brattere faseforskyvning må signaler med høyere frekvens enn 10kHz  som dempes veldig fort, mens frekvenser under blir tilnærmet uendret.

## e)
### a)

$$
 \begin{equation} 
 V_{2} = H(\omega)\cdot V_{1}
 \end{equation} 
$$
$$
 \begin{equation} 
  H(\omega)=\frac{R}{R+ j\omega L+ \frac{1}{j\omega C}}=\frac{1}{1+j\left( \omega  \frac{L}{R} - \frac{1}{\omega RC}\right)} 
 \end{equation} 
$$
$$
 \begin{equation} 
 |H(\omega)| = \frac{1}{\sqrt{ 1+\left( \omega  \frac{L}{R} -\frac{1}{\omega RC}\right)^2 }} 
 \end{equation} 
$$
### b)
$$
 \begin{equation} 
 H(\omega)=\frac{j\omega L}{R+j\omega L+ \frac{1}{j\omega C}}=\frac{1}{1-\frac{1}{LC\omega^2}-j\frac{1}{\omega  \frac{L}{R}}} 
 \end{equation} 
$$
$$
 \begin{equation} 
 |H(\omega)|=\frac{1}{\sqrt{ \left( 1-\frac{1}{LC\omega^2} \right)^2+\left( \frac{1}{\omega  \frac{L}{R}} \right)^2} } 
 \end{equation} 
$$
$$
 \begin{equation} 
 |H(\omega)| [dB]=20\log(H(\omega))=20\left[ 0-\log \left(\left( 1-\frac{1}{LC\omega^2} \right)^2+\left( \frac{1}{\omega  \frac{L}{R}} \right)^2\right)^{\frac{1}{2}} \right] 
 \end{equation} 
$$
$$
 \begin{equation} 
 = -10\log\left(\left( 1-\frac{1}{LC\omega^2} \right)^2+\left( \frac{1}{\omega  \frac{L}{R}} \right)^2\right) 
 \end{equation} 
$$

### c)
$$
 \begin{equation} 
 H(\omega)=\frac{\frac{1}{j\omega C}}{R+j\omega L+ \frac{1}{j\omega C}} =\frac{1}{1-\omega^2LC+j\omega RC}
 \end{equation} 
$$
$$
 \begin{equation} 
 |H(\omega)|=\frac{1}{\sqrt{ (1-\omega^2LC)^2+(\omega RC)^2 }} 
 \end{equation} 
$$




# Oppgave 3)

$$
 \begin{equation} 
 v(t)=A\cos(\omega_{0}t) =A\cos\left( \frac{R}{L}t \right)
 \end{equation} 
$$
$$
 \begin{equation} 
 Z_{Th}=R||j\omega_{0} L =\frac{R\cdot j\omega_{0}L}{R+j\omega_{0}L}=\frac{R\cdot j\omega_{0}L\cdot(R-j\omega_{0}L)}{(R+j\omega_{0}L)\cdot(R-j\omega_{0}L)}
 \end{equation} 
$$
$$
 \begin{equation} 
 = \frac{jR^2\omega_{0}L+R\omega_{0}^2L^2}{R^2+\omega_{0}^2L^2}=\frac{jR^3+R^3}{2R^2}=\frac{R^3}{2R^2}+\frac{jR^3}{2R^2}=\frac{R}{2}+j\frac{R}{2}
 \end{equation} 
$$





