Lage et dempeledd med Amin = -10dB og Amax = -25db
$f=1000\text{Hz}$
$R_{k}\approx_{0}$
$R_{L}\approx \infty$
$R_{p}=0-10k\Omega$
![[Koblingsskjema]]

$$v_{2}(t)=Av_{1}(t)$$ Dersom $v_{1}=1 \text{ og }A_{2}\leq A \leq A_{2}:$
$$
v_{2}=A_{1}\cdot v_{1}=R_{2}\cdot\frac{v_{1}}{R+R_{1}+R_{2}}\implies A_{2}=\frac{R_{2}}{R+R_{1}+R_{2}}
$$
$$
v_{2}=A_{2}\cdot v_{1}=(R+R_{2})\cdot\frac{v_{1}}{R+R_{1}+R_{2}}\implies A_{2}=\frac{(R+R_{2})}{R+R_{1}+R_{2}}
$$Setter opp ligningsettet og løser for $R_{1}$ og $R_{2}$:
$$
A_{2}(R+R_{1}+R_{2})=R_{2} \implies R_{1}=\frac{R_{2}}{A_{2}}-R-R_{2}
$$
$$
A_{1}(R+R_{1}+R_{2})=R+R_{2} \implies \frac{A_{1}\cdot R_{2}}{A_{2}}=R+R_{2}\implies \frac{A_{1}}{A_{2}}-1=\frac{R}{R_{2}}\implies R_{2}=\frac{R}{\frac{A_{1}}{A_{2}}-1}
$$
Kan da regne ut verdiene for $A_{1}\text{ og }A_{2}$ med formelen:
$$A[dB]=20lg(A)$$
$$-10=20\cdot \log(A_{1})\implies A_{1}=0.31623$$
$$-25=20\cdot \log(A_{2})\implies A_{2}=0.05623$$
Og sette inn for å regne $R_{2} \text{ og }R_{2}$:
$$
R_{2}=\frac{10000}{\frac{0.31623}{0.05623}-1}=2162.69231\Omega
$$ $$
R_{1}=\frac{2162.69231}{0.05623}-10000-2162.69231=26298.85\Omega
$$Kan så finne et sett med motstander utifra standard motstands verdier som jeg kobler i serie for å få en tilnærmet ekvivalent motstand for $R_{2} \text{ og }R_{2}$:$$
R_{1}=22k\Omega+3k 3\Omega+1k\Omega \text{ \& }R_{2}=1k8\Omega+330\Omega+33\Omega
$$$$
R_{1}=26.3k\Omega \text{ \& }R_{2}=2163\Omega
$$
Ved bruk av utrykket for $A_{1} \text{ og }A_{2}$ som fant tidligere kan regne tilbake og se om disse motstandene er innenfor systemkravene om at $A_{1} \text{ og }A_{2}$ skal være mindre enn 0.1dB fra hendholdsvis -10dB og -25dB:$$
A_{1}=\frac{2163+10000}{10000+2163+26300}=0.31623
$$$$
A_{1}[dB]=20\cdot \log(0.31623)=-10.00005dB
$$$$
A_{2}=\frac{2163}{10000+2163+26300}=0.05624
$$$$
A_{2}[dB]=20\cdot \log(0.05624)=-24.99973dB
$$Ligger dermed gått innenfor systemkravene for systemet og kan begynne å teste.

$$ 
 \begin{equation} 
 2+2=5 
 \end{equation} 
 $$