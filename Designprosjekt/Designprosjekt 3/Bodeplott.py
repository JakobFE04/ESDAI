import math
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

## Laster inn ulike csv data filer:

# Frequency (Hz)  Channel 1 Magnitude (dB)  Channel 2 Magnitude (dB)  Channel 2 Phase (deg)
network_data_1_filter = pd.read_csv("Målinger/Network 1 filter.csv")

# Frequency (Hz)  Channel 1 Magnitude (dB)  Channel 2 Magnitude (dB)  Channel 2 Phase (deg)
network_data_2_filter = pd.read_csv("Målinger/Network 2 filter.csv")

# Frequency (Hz)  Trace 2 (dBV)  Phase (deg)  Trace 3 (dBV)  Phase (deg).1  Trace 4 (dBV)  Phase (deg).2
spectrum_data = pd.read_csv("Målinger/Spectrum funker trace 2 original trace 3 1 filter trace 4 2 filter.csv")

# Frequency (Hz), Trace 3 (VHz), Phase (deg) 
network_data_original = pd.read_csv("Målinger/Måling Støy Frekvens.csv")

## Print liste for å teste at data blir lest rett:

# print(network_data_1_filter)
# print(network_data_1_filter['Frequency (Hz)'][0],network_data_1_filter['Channel 2 Magnitude (dB)'][0],network_data_1_filter['Channel 2 Phase (deg)'][0])
# print(network_data_2_filter)
# print(network_data_2_filter['Frequency (Hz)'][0],network_data_2_filter['Channel 2 Magnitude (dB)'][0],network_data_2_filter['Channel 2 Phase (deg)'][0])
# print(spectrum_data)
# print(spectrum_data['Frequency (Hz)'][0],spectrum_data['Trace 2 (dBV)'][0],spectrum_data['Trace 3 (dBV)'][0],spectrum_data['Trace 4 (dBV)'][0])

## Plotting av data
# fig1 = plt.figure(1)
# ax1 = fig1.add_subplot()
# ax1.plot(network_data_1_filter['Frequency (Hz)'], network_data_1_filter['Channel 2 Magnitude (dB)'], label="1 filter")
# ax1.plot(network_data_2_filter['Frequency (Hz)'], network_data_2_filter['Channel 2 Magnitude (dB)'], label="2 filter")
# ax1.vlines(1938.1,-60,0,colors='red',linestyles='dashed',label="Resonance Frequency")
# ax1.set_xscale('log')
# ax1.set_title("Magnitude Bode Plot")
# ax1.set_xlabel("Frequency")
# ax1.set_ylabel("Magnitude [dB]")
# ax1.grid()
# ax1.legend()

# fig2 = plt.figure(2)
# ax2 = fig2.add_subplot()
# ax2.plot(network_data_1_filter['Frequency (Hz)'], network_data_1_filter['Channel 2 Phase (deg)'], label="1 filter")
# ax2.plot(network_data_2_filter['Frequency (Hz)'], network_data_2_filter['Channel 2 Phase (deg)'], label="2 filter")
# ax2.vlines(1938.1,-150,150,colors='red',linestyles='dashed',label="Resonance Frequency")
# ax2.set_xscale('log')
# ax2.set_title("Phase Bode Plot")
# ax2.set_xlabel("Frequency")
# ax2.set_ylabel("Phase [deg]")
# ax2.grid()
# ax2.legend()

fig4 = plt.figure(4)
ax4 = fig4.add_subplot()
ax4.plot(network_data_original['Frequency (Hz)'],network_data_original['Trace 3 (VHz)'], label="")
ax4.vlines(1938.1,0,0.033,colors='red',linestyles='dashed',label="1938.1Hz")
ax4.set_xscale('log')
ax4.set_title("Noice Frequency Measurement")
ax4.set_ylabel("Magnitude [VHz]")
ax4.set_xlabel("Frequency [Hz]")
ax4.grid()
ax4.legend()
#plt.savefig("Bodeplot dB")




plt.show()