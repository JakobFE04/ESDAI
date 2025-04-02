import math
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

## Laster inn ulike csv data filer:

# Frequency (Hz)  Channel 1 Magnitude (dB)  Channel 2 Magnitude (dB)  Channel 2 Phase (deg)
network_data = pd.read_csv("System network bode network.csv")

# Frequency (Hz)  Channel 1 Magnitude (dB)  Channel 2 Magnitude (dB)  Channel 2 Phase (deg)
scope_data = pd.read_csv("Scope RMS.csv")

# Frequency (Hz)  Trace 2 (dBV)  Phase (deg)  Trace 3 (dBV)  Phase (deg).1  Trace 4 (dBV)  Phase (deg).2
# spectrum_data = pd.read_csv("Målinger/Spectrum funker trace 2 original trace 3 1 filter trace 4 2 filter.csv")


## Print liste for å teste at data blir lest rett:

# print(network_data)
# print(network_data['Frequency (Hz)'][0],network_data['Channel 2 Magnitude (dB)'][0],network_data['Channel 2 Phase (deg)'][0])
# print(scope_data)
# print(scope_data['Frequency (Hz)'][0],scope_data['Channel 2 Magnitude (dB)'][0],scope_data['Channel 2 Phase (deg)'][0])
# print(spectrum_data)
# print(spectrum_data['Frequency (Hz)'][0],spectrum_data['Trace 2 (dBV)'][0],spectrum_data['Trace 3 (dBV)'][0],spectrum_data['Trace 4 (dBV)'][0])

## Plotting av data
fig1 = plt.figure(1)
ax1 = fig1.add_subplot()
ax1.plot(network_data['Frequency (Hz)'], network_data['Channel 2 Magnitude (dB)'], label="System response")
# ax1.plot(scope_data['Frequency (Hz)'], scope_data['Channel 2 Magnitude (dB)'], label="2 filter")
ax1.vlines(7850,-33,0,colors='red',linestyles='dashed',label="Resonance Frequency")
ax1.set_xscale('log')
ax1.set_title("Magnitude Bode Plot")
ax1.set_xlabel("Frequency [Hz]")
ax1.set_ylabel("Magnitude [dB]")
ax1.grid()
ax1.legend()

fig2 = plt.figure(2)
ax2 = fig2.add_subplot()
ax2.plot(network_data['Frequency (Hz)'], network_data['Channel 2 Phase (deg)'], label="System response")
# ax2.plot(scope_data['Frequency (Hz)'], scope_data['Channel 2 Phase (deg)'], label="2 filter")
ax2.vlines(7850,-100,150,colors='red',linestyles='dashed',label="Resonance Frequency")
ax2.set_xscale('log')
ax2.set_title("Phase Bode Plot")
ax2.set_xlabel("Frequency [Hz]")
ax2.set_ylabel("Phase [deg]")
ax2.grid()
ax2.legend()

fig3 = plt.figure(3)
ax3 = fig3.add_subplot()
ax3.plot(scope_data['Time (s)']*1000,scope_data['Channel 1 (V)'], 'orange', label="Input signal")
ax3.plot(scope_data['Time (s)']*1000,scope_data['Channel 2 (V)'], 'blue', label="Output signal")
ax3.set_title("Oscilloscope Measurement")
ax3.set_ylabel("Voltage [V]")
ax3.set_xlabel("Time [ms]")
ax3.grid()
ax3.legend()

plt.show()


