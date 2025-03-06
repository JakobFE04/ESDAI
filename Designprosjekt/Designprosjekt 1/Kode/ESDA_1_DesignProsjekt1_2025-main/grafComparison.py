import codecs
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker  

fileHigh = codecs.open(r"./data/data_min.csv", encoding="utf-8", errors="ignore")
fileLow = codecs.open(r"./data/data_max.csv", encoding="utf-8", errors="ignore")
fileFull = codecs.open(r"./data/data_5v_sin.csv",encoding="utf-8",errors="")

high5V = csv.reader(fileHigh.readlines())
low5V = csv.reader(fileLow.readlines())
fileHigh.flush()
fileHigh.close()
fileLow.flush()
fileLow.close()

tSecond:list =[]
tMovedMilliSecond:list =[]
V_min:list = []
# v2HighVolt: list = []
V_max: list = []

skipLines:int = 20

for line in high5V:
    if skipLines==0:
        tSecond.append(float(line[0]))
        V_min.append(float(line[1]))
    else:
        skipLines-=1

skipLines = 20
for line in low5V:
    if skipLines==0:
        V_max.append(float(line[1]))
    else:
        skipLines-=1


startIndex: int  = 0
endIndex: int  = -1

while True:
    if (V_min[startIndex]>0) and (V_min[startIndex+1]<0):
        break
    else:
        startIndex+=1

while True:
    if (V_min[endIndex]<0) and (V_min[endIndex-1]>0):
        break
    else:
        endIndex-=1



def sinFunc(t):
    t = np.array(t)
    return np.sin(t*2*np.pi*1000)

V_min = V_min[startIndex:endIndex]
tSecond = tSecond[startIndex:endIndex]
# v2HighVolt = v2HighVolt[startIndex:endIndex]
V_max = V_max[startIndex:endIndex]



for t in tSecond:
    tMovedMilliSecond.append((t+abs(tSecond[0]))*1000)

goalHigh = sinFunc(tSecond)*5*0.501187
goalLow = sinFunc(tSecond)*5*0.1778279

#plt.style.use("seaborn-v0_8-dark")
# plt.style.use("seaborn-v0_8-poster")
plt.style.use("seaborn-v0_8-bright")
plt.axhline(y = 0,color="black",linestyle="--")
plt.axvline(x=0, color="black",linestyle="--")
plt.plot(tMovedMilliSecond,V_min,label="Vmin(t)")
# plt.plot(tMovedMilliSecond,v2HighVolt,label="V2(t)(minst demping)")
plt.plot(tMovedMilliSecond,V_max,label="Vmax(t)")
# plt.plot(tMovedMilliSecond,goalHigh,linestyle="dotted")
# plt.plot(tMovedMilliSecond,goalLow,linestyle="dotted",marker='o',markersize=0.5)

plt.grid()
plt.yticks(np.linspace(-2,2,11))
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f V'))
plt.gca().xaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f ms'))
plt.title("Måling av Vmin(t) og Vmax(t)")
plt.xlabel("Tid[ms]")
plt.ylabel("Spenning[V]")
plt.legend(frameon=True,edgecolor="dimgray",facecolor="lavender")
plt.savefig(fname="Plot 1", dpi=1000) 
plt.show()