# Oppgave 1)
## Teoretisk del;
![[Oppgave 1 utregning]]
Koder opp:
```python
import numpy as np
import matplotlib.pyplot as plt
  
a = 0.2
V_0 = 1
  
c = np.zeros(11)
ks = np.zeros(11)
for k in range(0,11):
    c[k] = abs(a*V_0*np.sinc(a*k))
    ks[k] = k
plt.stem(ks,c)
plt.show()
```
og får ut:
![[oppgave 1 plot.png]]

## Eksperimentell del;
Måler med analog discoveryen:
![[Spektrum måling opg 1.png]]

Som ser ut til å passe ganske bra med grafen min over.

# Oppgave 2)
## Teoretisk del;
![[Oppgave 2 tegning]]
Liten endring i koden:
```python
import numpy as np
import matplotlib.pyplot as plt
  
a = 0.2
V_0 = 1
  
c = np.zeros(11)
c_y = np.zeros(11)
ks = np.zeros(11)
for k in range(0,11):
    c[k] = abs(a*V_0*np.sinc(a*k))
    c_y[k] = abs(a*V_0*np.sinc(a*k)/(np.sqrt(1+k**2)))
    ks[k] = k
plt.stem(ks,c,label="Ufiltrert")
plt.stem(ks,c_y,label="Filtrert",linefmt="r")
plt.legend()
plt.show()
```
Og får ut:
![[oppgave 2 plot.png]]

## Eksperimentell del;
Regner ut at jeg kan bruke ca $16k\Omega$ og $10nF$ for å få en knekkfrekkvens på 1kHz.
![[Network oppgave 2.png]]

Får da spektrumet:
![[Spektrumoppgave 2.png]]

Stemmer ganske bra!

Kobling:
![[Kobling.png]]