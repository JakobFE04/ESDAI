![[Icestudio full systemV2.png]]
![[Prinsipiell tegning kok.png]]

![[Switch fpga.png]]



![[terning.png]]


Har en frekvens på 23.8Hz

|     | Farge | Spenning over motstand | VDD spenning \[V] | Motstandsverdi | AVG spenning over motstand ved telling | VDD spenning ved telling \[V] |
| --- | ----- | ---------------------- | ----------------- | -------------- | -------------------------------------- | ----------------------------- |
| D_1 | Rød   | 0.844                  | 2.92              | 100.0          | 0.415                                  | 2.30                          |
| D_2 | Grønn | 0.865                  | 2.92              | 99.7           | 0.715                                  | 1.45                          |
| D_3 | Grønn | 0.861                  | 2.91              | 100.2          | 0.144                                  | 0.59                          |
| D_4 | Grønn | 0.855                  | 2.91              | 100.0          | 0.133                                  | 0.59                          |
| D_5 | Grønn | 0.825                  | 2.91              | 99.9           | 0.691                                  | 1.45                          |
| D_6 | Rød   | 0.850                  | 2.91              | 99.9           | 0.415                                  | 2.30                          |
| D_7 | Gul   | 1.054                  | 3.06              | 99.7           | 0.515                                  | 1.52                          |

$$ 
 \begin{equation} 
 \Bigg(\begin{array}{c}
 & \text{Farge} & V_{R_{D}}[V] & V_{DD} [V] & R_{D}[\Omega]&  \overline{V_{R_{D}}}[V]  & \overline{V_{DD}}[V] \\
D_{1} & \text{Rød} & 0.844 & 2.92 & 100.0 & 0.415 & 2.30 \\
D_{2} & \text{Grønn} & 0.865 & 2.92 & 99.7 & 0.715 & 1.45 \\
D_{3} & \text{Grønn} & 0.861 & 2.91 & 100.2 & 0.144 & 0.59 \\
D_{4} & \text{Grønn} & 0.855 & 2.91 & 100.0 & 0.133 & 0.59 \\
D_{5} & \text{Grønn} & 0.825 & 2.91 & 99.9 & 0.691 & 1.45 \\
D_{6} & \text{Rød} & 0.850 & 2.921 & 99.9 & 0.415 & 2.30 \\
D_{7} & \text{Gul} & 1.054 & 3.06 & 99.7 & 0.515 & 1.52
\end{array}\Bigg) 
 \end{equation} 
 $$


$$ 
 \begin{equation} 
 I_{} =I_{R}=I_{D}
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 P_{D}=V_{DD}\cdot I_{D}=V_{DD}\cdot \frac{V_{R_{D}}}{R_{D}}
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 P_{x}=\sum_{i}^{x} P_{D_{i}}
 \end{equation} 
 $$

| Diode   | Effekt \[mW] | Total effekt for kast $P_{x}$ | Effekt \[mW] |
| ------- | ------------ | ----------------------------- | ------------ |
| $D_{1}$ | 24.64        | $P_{1}$                       | 32.35        |
| $D_{2}$ | 25.33        | $P_{2}$                       | 49.40        |
| $D_{3}$ | 25.01        | $P_{3}$                       | 81.75        |
| $D_{4}$ | 24.88        | $P_{4}$                       | 98.77        |
| $D_{5}$ | 24.03        | $P_{5}$                       | 131.12       |
| $D_{6}$ | 24.76        | $P_{6}$                       | 148.78       |
| $D_{7}$ | 32.35        | $P_{HOLD}$                    | 49.01        |

$$ 
 \begin{equation} 
 \Bigg(\begin{array}{c}
Diode & P_{D}[mW] & P_{x}[mW]  & \\
D_{1} & 24.64 & P_{1}=32.35 \\
D_{2} & 25.33 & P_{2}=49.40\\
D_{3} & 25.01 & P_{3}=81.75\\
D_{4} & 24.88 & P_{4}=98.77\\
D_{5} & 24.03 & P_{5}=131.12\\
D_{6} & 24.76 & P_{6}=148.78\\
D_{7} & 32.35 & P_{HOLD}=49.01 \\
\end{array}\Bigg) 
 \end{equation} 
 $$


![[Eks terning.png]]



$$ 
 \begin{equation} 
 U_{1}=U_{6}=T_{2} 
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 U_{2}=U_{5}=T_{2}+T_{1} 
 \end{equation} 
 $$
 $$ 
 \begin{equation} 
 U_{3}=U_{4}=T_{2}\cdot T_{1} 
\end{equation}
 $$
$$ 
 \begin{equation} 
 U_{7}=T_{0} 
 \end{equation} 
 $$
 ![[Dekoder ice.png]]

![[Geogebra plot.png]]