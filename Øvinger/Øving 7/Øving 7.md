# Oppgave 1)
![[ESDA/ESDAI/Øvinger/Øving 7/Oppgave 1.jpg]]

# Oppgave 2)
## a)

Vil øke $V_{G}$ med ca 0.5V for utifra grafene virker arbeidspunktet litt lavt. Får da:
$$
 \begin{equation} 
 5\cdot \frac{R_{2}}{33k+R_{2}}=3 \implies R_{2} \approx 50k\Omega 
 \end{equation} 
$$
Bytter ut motstanden og får da når jeg måler:
![[ESDA/ESDAI/Øvinger/Øving 7/2 a.png]]
Som gir SFDR = 48.65 dB
![[Spektrum 2 a.png]]

## b)

Måler $V_{S}$ til 1.087V. Kan så regne ut strømmen fra:
$$
 \begin{equation} 
 I_{D}=\frac{V_{S}}{R_{S}}=\frac{1.087}{10000}=108.7 \micro A 
 \end{equation} 
$$
Og finne $R_{o}$ ved:
$$
 \begin{equation} 
 I_{D}\cdot R_{o}||R_{L}=V_{S}\implies R_{o}\approx10 \Omega 
 \end{equation} 
$$

## c)

Siden signalet har en amplitude lik 1V vil den minste amplituden vi tilater være 0.707V (-3dB). Kan da bruke amplituderesponsen til å regne en minimum verdi for kondensatoren:
$$
 \begin{equation} 
 |H(\omega)|=\frac{1}{\sqrt{ 1+ \frac{1}{(\omega \tau)^2} }}\implies 0.707=\frac{1}{\sqrt{ 1+ \frac{1}{(200\pi \cdot 20000\cdot C)} }} \implies C_{min}\approx 80nF
 \end{equation} 
$$
Testet med en 100nF kondensator og fikk:
![[2 c scope.png]]
Men så håper jeg at Laurentius Lie innser at han kan få nesten hvilken som helst kondensatorverdi så liten som han bare vil, og at $1 \micro F$ hadde funket helt fint og kan fås i 0201 størrelse om han ville det.