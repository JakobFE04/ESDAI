import matplotlib.pyplot as plt 
import numpy as np 

R = 1000
C = 100 * 10**(-9)

def H_2(f):
    return 1/(1+(2*np.pi*f*R*C)**2)

def angleH_2(f):
    return -np.arctan(R*C*2*np.pi*f)

def H_3(f):
    return 1/(1+(1/(2*np.pi*f*R*C)**2))

def angleH_3(f):
    return -np.arctan(1/(R*C*2*np.pi*f))

f = np.linspace(1,10_000, 100)

plt.figure(1)
plt.plot(f,H_2(f),label="H_2")
plt.legend()
plt.savefig("H_2")
plt.figure(2)
plt.plot(f,angleH_2(f),label="Fase H_2")
plt.legend()
plt.savefig("Fase H_2")
plt.figure(3)
plt.plot(f,H_3(f),label="H_3")
plt.legend()
plt.savefig("H_3")
plt.figure(4)
plt.plot(f,angleH_3(f),label="Fase H_3")
plt.legend()
plt.savefig("Fase H_3")
plt.show()