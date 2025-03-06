# Oppgave 1)
## a)

Gitt at:
$$ 
 \begin{equation} 
 a \cos(\omega t+\phi)=\mathrm{Re} \{ae^{j(\omega t+\phi)}\} \implies A = ae^{j\phi}
 \end{equation} 
 $$
 Får vi at:
$$ 
 \begin{equation} 
 5\cos(3\pi t)=\mathrm{Re}\{5e^{j3\pi t}\} \implies A=5
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 38\cos\left( 2.5\pi t+\frac{\pi}{3} \right)=\mathrm{Re}\{38e^{j\pi/3}\cdot e^{j2.5\pi t}\} \implies A=38e^{j\pi/3}
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 \cos(8t+2)=\mathrm{Re}\{e^{j 2}\cdot e^{j 8 t}\} \implies A = e^{j 2}
 \end{equation} 
 $$
 ![[1 plot.png]]
 


## b)

Får utrykkene:
$$ 
 \begin{equation} 
 \mathrm{Re} \{7e^{j(\omega t+\pi)}\} =7\cos(\omega t+\pi)
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 \mathrm{Re} \{3e^{j(\omega t+4.3\pi)}\}  =3\cos(\omega t+4.3\pi)
 \end{equation} 
 $$

$$ 
 \begin{equation} 
 \mathrm{Re} \{Ce^{j(\omega t+\beta)}\}  =C\cos(\omega t+\beta)
 \end{equation} 
 $$ 
 $$ 
 \begin{equation} 
 \mathrm{Re} \{(4+j4)e^{j\omega}\}  =4\sqrt{2 }\cos\left( \omega t+\frac{\pi}{4} \right)
 \end{equation} 
$$
## c)

$$ 
 \begin{equation} 
 A) \ A = 1.5
 \end{equation} 
$$
 $$ 
 \begin{equation} 
 B) \ A=2e^{j\frac{\pi}{2}} 
 \end{equation} 
$$
 $$ 
 \begin{equation} 
 C) \ A= \frac{1}{2}e^{-j\frac{\pi}{2}}
 \end{equation} 
$$
 $$ 
 \begin{equation} 
  D) \ A=\frac{1}{2}e^{j\pi}
 \end{equation} 
$$
 
# Oppgave 2)

$$ 
 \begin{equation} 
 x(t)=10\cos(\omega t+0.42)+4.2\cos(wt-1.3)-6\sin(wt+0.38) 
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 x(t)=10e^{j(wt +0.42)}+4.2e^{j(\omega t- 1.3)} -6e^{j(\omega t+0.38+3\pi/2)}
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 x(t)=(10e^{j0.42}+4.2e^{-j1.3}-6e^{j 0.38+3\pi/2})\cdot e^{j\omega t} 
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 x(t)=(8.0289+5.6026j)\cdot e^{j\omega t}
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 x(t)=9.7904e^{j 0.6093} \cdot e^{j\omega t} =9.7904\cos(\omega t+0.6093)
 \end{equation}  
 $$
 


# Oppgave 3)

## a)
Gitt:
$$ 
 \begin{equation} 
 x(t)=a\cos(\omega t)
 \end{equation} 
 $$
 Da blir:
 $$ 
 \begin{equation} 
 x(t-\Delta t)=a\cos(\omega \cdot(t-\Delta t))=a\cos(\omega t-\omega \Delta t) \implies \Delta \varphi = -\omega \Delta t 
 \end{equation} 
 $$

## b)

Gitt at:
$$ 
 \begin{equation} 
 V_{0}=0.5\cos(2\pi \cdot 200t) 
 \end{equation} 
 $$
 Som gir oss at vi må generere et signal med 0.5V amplitude og 200Hz for $V_{0}$ som er på kanal 2 i bildene under:
![[V1 ny.png]]
![[V1 phase.png]]
$V_{1}$ er tilnærmet -39.2 (-0.6841 radianer) graders fase forskyvning og amplitude $\approx 380mV$


![[V2 Ny.png]]
![[V2 Phase.png]]
$V_{2}$ er 49.8 (0.8691) graders fase forskyvning og amplitude $\approx 319mV$
Slik at:
$$ 
 \begin{equation} 
 V_{0}=0.5 
 \end{equation} 
 $$
$$ 
 \begin{equation} 
 V_{1}\approx 380\cdot 10^{-3}\cdot e^{-j 0.6841}
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 V_{2}\approx 319\cdot10^{-3} \cdot e^{j 0.8691}
 \end{equation} 
 $$
 Kan så regne med Kirchoffs spenningslov:
 $$ 
 \begin{equation} 
 V_{0}=V_{1}+V_{2} 
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 V_{0}= 380\cdot 10^{-3} \cos(-0.6841) + 380\cdot 10^{-3} j\sin(-0.6841)
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 + 319\cdot10^{-3}\cos(0.8691) + 319\cdot10^{-3}j\sin(0.8691)
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 V_{0}=500\cdot 10^{-3} +3i \cdot 10^{-3}\approx 500mV
 \end{equation} 
 $$
 Tegner opp de komplekse amplitudene og ser at dette stemmer nokså bra.
![[Plot 3 ny.png]]

 


# Oppgave 4)

$$ 
 \begin{equation} 
 V_{s} = 5
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 Z_{1} =R=100\Omega
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 Z_{2}=\frac{1}{j\omega C} = \frac{1}{j2\pi 10^{-4}} \Omega
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 Z_{3}=j\omega L=j2\pi 10\Omega
 \end{equation} 
 $$
## a)
$$ 
 \begin{equation} 
 V_{1}=\frac{V_{s}}{Z_{1}+Z_{2}||Z_{3}} \cdot Z_{2}||Z_{3}   \ \ \ \ \  \ \ \ \ |  \ Z_{2}||Z_{3}=\frac{Z_{2}\cdot Z_{3}}{Z_{2}+Z_{3}}
 \end{equation} 
 $$
## b)

Putter vi inn tallverdier for utrykket i a) får vi at:
![[ESDA/Øvinger/Øving 3/4 b.png]]
$$ 
 \begin{equation} 
 V_{1}\approx 1.5+2.29j \implies v_{1}(t)= 2.74\cdot \cos(2\pi 10^4t+0.99)
 \end{equation} 
 $$

## c)

Bruker da at:
$$ 
 \begin{equation} 
 I = \frac{V}{Z} 
 \end{equation} 
 $$
 For spole og kondensator og får at:
$$ 
 \begin{equation} 
 I_{2} =\frac{V_{1}}{Z_{2}}=\frac{1.5+2.29j}{\frac{1}{j2\pi 10^{-4}}}= -1.4\cdot 10^{-3}+j 0.9\cdot 10^{-3}
 \end{equation} 
 $$
 
 $$ 
 \begin{equation} 
 I_{3}=\frac{V_{1}}{Z_{3}}=\frac{1.5+2.29j}{j2\pi 10} =36.5\cdot 10^{-3}+j 23.8\cdot 10^{-3}
 \end{equation} 
 $$
 