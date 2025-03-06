import numpy as np 
import matplotlib.pyplot as plt 

R = 1000
C = 100*10**(-6)
T = R*C

print(f"Tidskonstanten T = {T}")

def V_C(t):
    return -5*np.e**(-t/T)+5

t = np.linspace(0,1,100)
V = []

for i in range(len(t)):
    V.append(V_C(t[i]))
    
plt.plot(t,V,label="V_C(t)")
plt.xticks(np.arange(0, 1, step=0.1),labels=[f"{i}T" for i in range(10)])
plt.legend()
plt.show()