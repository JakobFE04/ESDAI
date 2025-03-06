# Oppgave 1
## a) 
![[ESDA/Øvinger/Øving 1/1 a.png]]
Tidskonstanten (T) er 100ms.

## b)
![[ESDA/Øvinger/Øving 1/1 b.png]]
Oppkobling:
![[Oppkobling 1 b.png]]
## c)
Utlandingen vil ta mye lengre tid fordi det ikke er en lukket krets når vi slipper bryteren, så da er det bare lekasjestrømmen til kondensatoren.

# Oppgave 2

$$ 
 \begin{equation} 
 R_{1}=200\Omega, R_{2}=470\Omega,R_{3}=220\Omega,R_{4}=300\Omega,C=10nF,V=5V
 \end{equation} 
 $$
 Vil finne en ekvivalent motstand for kretsen:
 $$ 
 \begin{equation} 
 R_{Th}=R_{4}+R_{2}||R_{3}
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 R_{Th}=300+\frac{470\cdot220}{470+220}=450\Omega 
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
   τ=R_{Th}\cdot C=450\cdot 10\cdot 10^{-9}=4.5\micro s
 \end{equation} 
 $$
# Oppgave 3

## a)
Finner Theveninekvivalenten til kretsen:
$$ 
 \begin{equation} 
  R_{Th}=1k||1k=500\Omega
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 V_{Th}=V_{R_{2}}=1k\cdot \frac{1}{1k+1k} =0.5V
 \end{equation} 
 $$
 Får da at:
$$ 
 \begin{equation} 
 τ=R_{Th}\cdot C=500\Omega \cdot 100\micro F= 0.05
 \end{equation} 
 $$
$$ 
 \begin{equation} 
 V_{C} (t)=(V_{C}(0)-V)\cdot e^{-t/τ}+V=0.5(1-e^{-t/0.05})
 \end{equation} 
 $$
## b) 
Ved  $V_{C(6τ)}=0.5V$
Finner da den nye Theveninkretsen:
$$ 
 \begin{equation} 
 R_{Th}=500||1000 =333.3\Omega
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 V_{Th}= V_{R_{3}}=1000\cdot \frac{0.5}{500+1000}=\frac{1}{3}V
 \end{equation} 
 $$
 
Får da at den nye τ:
$$ 
 \begin{equation} 
 τ=R\cdot C=333.3\Omega \cdot100 \micro F=0.033
 \end{equation} 
 $$
 Slik at 
 $$ 
 \begin{equation} 
 V_{C}(t)=(V_{C}(6\cdotτ)-V)\cdot e^{-t/τ}+V= \left( 0.5-\frac{1}{3} \right)\cdot e^{-t/0.033)}+\frac{1}{3}|t\geq 6\cdotτ
 \end{equation} 
 $$
## c)

 $$ 
 \begin{equation} 
 V_{C}(0.5\cdotτ)=0.2V 
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 V_{C}(t)=(V_{C}(0.5\cdotτ)-V)\cdot e^{-t/τ}+V= \left( 0.2-\frac{1}{3} \right)\cdot e^{-t/0.033)}+\frac{1}{3}|t\geq 0.5\cdotτ
 \end{equation} 
 $$
# Oppgave 4)
## a) 
$$ 
 \begin{equation} 
  τ=RC=1000\cdot 10\cdot 10^{-9}=10\micro s
  
 \end{equation} 
 $$
## 4 b) 
![[ESDA/Øvinger/Øving 1/4 b.png]]
![[4 b regning.png]]
## c)

![[4 c.png]]

## d) 

Måling ved 5kHz
![[4 d_1.png]]
Måling med 5kHz med inngansignal:
![[4 d_2.png]]
Ser at dette stemmer veldig bra med grafen min fra oppgave b).

Oppkobling:
![[Oppkobling 4 d_b.png]]

Måling ved 30kHz
![[4 d_c.png]]
Måling med 30kHz inngangsignal
![[4 d_c_2.png]]
Ser at jeg plotta grafen med litt feil periode i c), men at ellers stemmer grafen ganske bra med målingene.

## e) 

Utifra utrykket:
$$ 
 \begin{equation} 
 V_{C}(t)=(V_{C}-V)\cdot e^{-\frac{t}{\tau}}+V
 \end{equation} 
 $$
 Kan vi sette opp to utrykk for $V_{C}$ og for $\tau$:
 $$ 
 \begin{equation} 
 0.8=(V_{C}-1)\cdot e^{-\frac{100\cdot 10^{-6}}{\tau}} \text{ \& } V_{C}=0.8\cdot e^{-\frac{100\cdot 10^{-6}}{\tau}} 
 \end{equation} 
 $$
 Får da at: 
 $$ 
 \begin{equation} 
 \tau= 72.13\micro s \implies R=\frac{\tau}{C}=\frac{72.13\micro s}{10nF}=7213 \Omega
 \end{equation} 
 $$
 
  Kobler en $3.3k\Omega$ motstand i serie med en $3.9k\Omega$ motstand for å få ca riktig motstand:
![[4 e.png]]
Får da at signalet går til tilnærmet lik 0.8V ved maks oppladning.

Oppkobling:
![[4 e oppkobling.png]]
