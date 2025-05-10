## Tema 1
Formler:

$$
 \begin{equation} 
 I_{D}=\frac{k}{2}(V_{GS}-V_{T})^2 
 \end{equation} 
$$
$$
 \begin{equation} 
 V_{GS}=V_{G}-V_{S}\implies \begin{cases}
V_{G}=\frac{V_{DD}}{R_{G_{1}}-R_{G_{2}}}\cdot R_{G_{2}} \\
V_{S}=I_{D}\cdot R_{S}
\end{cases} 
 \end{equation} 
$$
$$
 \begin{equation} 
 I_{D}=\frac{k}{2}\left( \frac{V_{DD}}{R_{G_{1}}-R_{G_{2}}}\cdot R_{G_{2}}-I_{D}\cdot R_{S} -V_{T}\right)^2 
 \end{equation} 
$$
$$
 \begin{equation} 
 V_{DS}=V_{DD}-I_{D}(R_{S}+R_{D}) 
 \end{equation} 
$$
Lastlinje: Vi tenker de punktene når transistoren er fullt åpen og lukket
$$
 \begin{equation} 
 \text{Åpen}=\left( 0, \frac{V_{DD}}{R_{S}+R_{D}} \right) 
 \end{equation} 
$$
$$
 \begin{equation} 
 \text{Lukket}=(V_{DD},0) 
 \end{equation} 
$$
Når den er åpen er det ingen spenning over transistoren og den maks strømmen basert på RS og RD, når den er lukket er spenningen over RD lik VDD siden det går null strøm.

Triode, Metning, Cutoff

## Tema 2:
Samme som Tema 1 men $R_{D}=0$.

## Tema 3:

Motstanden gjør at $V_{DS}=V_{GS}$ siden det ikke går noe strøm inn på gaten, og det blir ingen spenningsfall mellom drain og gaten. Får dermed at:

$$
 \begin{equation} 
 I_{D}=\frac{k}{2}(V_{DD}-I_{D}(R_{S}+R_{D})-V_{T})^2 
 \end{equation} 
$$
Løs for $I_{D}$ 

## Tema 4:

Lavpass
$$
 \begin{equation} 
  H(\omega)=\frac{V_{2}}{V_{1}}=\frac{Z_{1}}{Z_{2}}=\frac{\left( \frac{1}{j\omega C} \right)}{R+\frac{1}{j\omega C}+j\omega L}=\frac{1}{1+{j\omega RC}-\omega^2LC}
 \end{equation} 
$$
## Tema 5:

Båndpass
$$
 \begin{equation} 
  H(\omega)=\frac{V_{2}}{V_{1}}=\frac{Z_{1}}{Z_{2}}=\frac{R}{R+\frac{1}{j\omega C}+j\omega L}=\frac{1}{1+\frac{1}{j\omega RC}+j\omega  \frac{L}{R}}
 \end{equation} 
$$

## Tema 6:

Båndstopp

$$
 \begin{equation} 
 H(\omega)=\frac{V_{2}}{V_{1}}=\frac{Z_{1}}{Z_{2}}=\frac{ \frac{1}{j\omega C}+j\omega L }{R+\frac{1}{j\omega C}+j\omega L}=\frac{j\left( \omega L-\frac{1}{\omega C} \right)}{R+j\left( \omega L-\frac{1}{\omega C} \right)} 
 \end{equation} 
$$

## Tema 7:

Høypass
$$
 \begin{equation} 
  H(\omega)=\frac{V_{2}}{V_{1}}=\frac{Z_{1}}{Z_{2}}=\frac{j\omega L}{R+\frac{1}{j\omega C}+j\omega L}=\frac{1}{\frac{1}{j\omega  \frac{L}{R}}-\frac{1}{\omega^2LC}+1}
 \end{equation}  
$$
## Tema 8:

Båndpass

$$
 \begin{equation} 
 H(\omega)=\frac{{\frac{1}{\frac{1}{j\omega L}+j\omega C}}}{R+\frac{1}{\frac{1}{j\omega L}+j\omega C}}=\frac{{R+\frac{1}{j\left( \omega C- \frac{1}{\omega L} \right)}}}{j\left( \omega C- \frac{1}{\omega L} \right)} 
 \end{equation} 
$$
## Tema 9:
Se bilde

## Tema 10:
Lag to båndstoppfilter med buffer i mellom for hver av f

## Tema 11:

Opamp med signal til + og - til jord vil lage en firkantpuls. Koble dette istedet for diode slik som i D4 og du vil få frekvenskomponenter lik 0,1,3,5,7... 
Se "Praktisk spektrumanalyse" på blackboard for utregning.














