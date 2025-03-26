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