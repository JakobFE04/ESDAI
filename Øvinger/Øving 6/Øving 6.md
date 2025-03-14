# Oppgave 1)
## a)
$$
 \begin{equation} 
 v_{D}=V_{DD}-R_{D}\cdot i_{D} 
 \end{equation} 
$$
## b)

![[ESDA/ESDAI/Øvinger/Øving 6/1 b.png|500]]

## c)
![[1 c.png]]

## d)
![[1 d.png]]

## e)
![[1 e tegning|800]]

# Oppgave 2)
## a)
![[ESDA/ESDAI/Øvinger/Øving 6/2 a.png|500]]

## b)
$$
 \begin{equation} 
 I_{D}=\frac{V_{DD}-V_{D}}{R_{D}} =\frac{8-2.5}{100}=55mA
 \end{equation} 
$$
$$
 \begin{equation} 
 V_{G}\approx 2.6V 
 \end{equation} 
$$
Se oppgave 1 e) for merking.

## c)

![[ESDA/ESDAI/Øvinger/Øving 6/2 c.png]]


Gitt at:
$$
 \begin{equation} 
  v_{2}=A_{v_{1}} \implies A=\frac{v_{2}}{v_{1}}=\frac{1.76}{177m}V=9.9\approx 10
 \end{equation} 
$$

## d)
Endrer vi på arbeidspunktet/potensiometeret så endrer vi på hvor stor spenningen $V_{GS}$ blir som gjør at vi minker (øker) $V_{DS}$ ved høyere (lavere) spenning på $V_{GS}$.

## e)
![[2 e.png]]
Når inngangsignalet er å 1V så vil ikke transistoren klare å forsterke  $v_{2}$ noe høyere enn verdien for $V_{DD}$. Signalet går da over i cut-off området og vi får at trekantsignalet blir flatet ut.


# Oppgave 3)
## a-d)
$$
 \begin{equation} 
 V_{GS}=3V 
 \end{equation} 
$$
$$
 \begin{equation} 
i_{D}=\frac{V_{DD}-V_{DS}}{R_{D}}=\frac{8}{10}A-\frac{1}{10}V_{DS}
 \end{equation} 
$$
 ![[3 tegning|800]]
 $$
 \begin{equation} 
 \text{Arbeidspunkt}\begin{cases}
V_{GS}=3V \\
V_{DS}=8.5V \\
I_{D}=0.1A
\end{cases} 
 \end{equation} 
$$
## e)
Endre $R_{G1}=6k\Omega$ og $R_{G2}=4k\Omega$, slik at:
$$
 \begin{equation} 
 \text{Arbeidspunkt}\begin{cases}
V_{GS}=5V \\
V_{DS}=6V \\
I_{D}\approx 0.3

\end{cases} 
 \end{equation} 
$$
![[3 e tegning|800]]

# Oppgave 4)
### Figur 6)
![[4 fig 6.png]]$$
 \begin{equation} 
 V_{G}=\frac{V_{DD}}{R_{G 1}+R_{G 2}}\cdot R_{G 2}=\frac{14}{4M}\cdot 1M =3.5V
 \end{equation} 
$$$$
V_{S}=R_{S}\cdot I_{D}
$$
$$
 \begin{equation} 
 V_{GS}=V_{G}-V_{S} =V_{G}-R_{S}\cdot I_{D}
 \end{equation} 
$$

$$
 \begin{equation} 
  i_{D}=\frac{K}{2}(V_{GS}-V_{T})^2 = \frac{K}{2}(V_{G}-R_{S}\cdot I_{D}-V_{T})^2
 \end{equation} 
$$
Løser for $i_{D}$ og får at:
$$
 \begin{equation} 
 i_{D} = 4mA \ \ \ \text{\&} \ \ \ i_{D}=6.25mA
 \end{equation} 
$$
$$
 \begin{equation} 
V_{DS}=V_{DD}-V_{D}-V_{S}=V_{DD}-i_{D}\cdot (R_{D}+R_{S})
 \end{equation} 
$$
$$
 \begin{equation} 
 V_{DS}= 4V  \ \ | \ i_{D}=4mA \ \ \ \ \text{\&} \ \ \ \ V_{DS}=-1.625V \ \ | \ i_{D}=6.25mA
 \end{equation} 
$$
-1.625V vil ikke stemme så dermed må $i_{D}$ være 4mA;
$$
 \begin{equation} 
  V_{GS}= 500\cdot 4m = 1.5V
 \end{equation} 
$$
Og får dermed at:
$$
 \begin{equation} 
  \text{Arbeidspunkt}\begin{cases}
V_{GS}=1.5V \\
V_{DS}=4V \\
I_{D}=4mA
\end{cases} 
 \end{equation} 
$$

### Figur 7)
![[Fig 7.png]]
$$
 \begin{equation} 
 V_{G}=\frac{V_{DD}}{R_{1}+R_{2}}\cdot R_{2}= \frac{216}{31}V
 \end{equation} 
$$$$
V_{S}=R_{S}\cdot I_{D}
$$
$$
 \begin{equation} 
 V_{GS}=V_{G}-V_{S} =V_{G}-R_{S}\cdot I_{D}
 \end{equation} 
$$

$$
 \begin{equation} 
  i_{D}=\frac{K}{2}(V_{GS}-V_{T})^2 = \frac{K}{2}(V_{G}-R_{S}\cdot I_{D}-V_{T})^2
 \end{equation} 
$$
Løser for $i_{D}$ og får at:
$$
 \begin{equation} 
 i_{D} = 7.94mA \ \ \ \text{\&} \ \ \ i_{D}=17.92mA
 \end{equation} 
$$
$$
 \begin{equation} 
V_{DS}=V_{DD}-V_{D}-V_{S}=V_{DD}-i_{D}\cdot (R_{D}+R_{S})
 \end{equation} 
$$
$$
 \begin{equation} 
 V_{DS}= 8.03V  \ \ | \ i_{D}=7.94mA \ \ \ \ \text{\&} \ \ \ \ V_{DS}=3.04V \ \ | \ i_{D}=17.92mA
 \end{equation} 
$$
$$
 \begin{equation} 
 V_{GS}= 2.99V \ \ |\ 7.94mA \ \ \ \& \ \ \ \ V_{GS}=-1.99V \ \ | \ 17.92mA
 \end{equation} 
$$
Altså får vi (avrundet litt):
$$
 \begin{equation} 
  \text{Arbeidspunkt}\begin{cases}
V_{GS}=3V \\
V_{DS}=8V \\
I_{D}=8mA
\end{cases} 
 \end{equation} 
$$

### Figur 8)
![[Fig 8.png]]

Siden $I_{G}=0$ så vil det ikke være spenning over $R_{F}$, så da får vi at:
$$
 \begin{equation} 
 V_{D}=V_{G} \implies V_{DS}=V_{GS}
 \end{equation} 
$$
$$
 \begin{equation} 
 V_{DS}= V_{DD}-I_{D}(R_{D}+R_{S})
 \end{equation} 
$$
$$
 \begin{equation} 
 I_{D}=\frac{K}{2}(V_{GS}-V_{T}) ^2=\frac{K}{2}(V_{DD}-I_{D}(R_{D}+R_{S})-V_{T})^2
 \end{equation} 
$$
Løser vi for $I_{D}$ får vi:

$$
 \begin{equation} 
 i_{D} = 4mA \ \ \ \text{\&} \ \ \ i_{D}=4.69mA
 \end{equation} 
$$
$$
 \begin{equation} 
V_{DS}=V_{DD}-V_{D}-V_{S}=V_{DD}-i_{D}\cdot (R_{D}+R_{S})
 \end{equation} 
$$
$$
 \begin{equation} 
 V_{DS}= 3V  \ \ | \ i_{D}=4mA \ \ \ \ \text{\&} \ \ \ \ V_{DS}=0.91V \ \ | \ i_{D}=4.69mA
 \end{equation} 
$$
$$
 \begin{equation} 
 V_{GS}= 3V  \ \ | \ i_{D}=4mA \ \ \ \ \text{\&} \ \ \ \ V_{GS}=0.91V \ \ | \ i_{D}=4.69mA
 \end{equation} 
$$

Altså får vi:
$$
 \begin{equation} 
  \text{Arbeidspunkt}\begin{cases}
V_{GS}=3V \\
V_{DS}=3V \\
I_{D}=4mA
\end{cases}  \ \ \text{\& }  \ \  
  \text{Arbeidspunkt}\begin{cases}
V_{GS}=0.91V \\
V_{DS}=0.91V \\
I_{D}=4.69mA
\end{cases} 
 \end{equation} 
$$
