import matplotlib.pyplot as plt 
import numpy as np 

R = 1000 
L = 0.1
C = 100*10**(-9)
f = np.linspace(1,10_000,100)
w = 2*np.pi*f

def absH_b(w):
    return 20*np.log10(1/(np.sqrt((1-1/(L*C*w**2))**2)+(1/(w*L/R)**2)))

def absH_c(w):
    return 20*np.log(1/np.sqrt((1-w**2*L*C)**2+(w*R*C)**2))

plt.plot(f,absH_b(w),label="H_b")
plt.plot(f,absH_c(w),label="H_c")
plt.legend
plt.show()