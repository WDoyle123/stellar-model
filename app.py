import matplotlib.pyplot as plt 
import os

plt.figure(figsize=(10, 8), dpi=80)
with os.scandir("/home/will/Documents/Astrophysics/stellar-model/data") as it:
    for entry in it: 

        with open(entry) as datFile:
            next(datFile)
            lum = ([float(data.split()[1]) for data in datFile])
            lum.pop(0)

        with open(entry) as datFile:
            next(datFile)
            teff = ([float(data.split()[2]) for data in datFile])
            teff.pop(0)

        plt.plot(teff,lum, marker =".", ls="dotted" ,label=entry.name)

plt.title("The Physics of Stellar Models - William Doyle")
plt.ylabel("Luminosity, Log L")
plt.xlabel("Log Teff")
ax = plt.gca()
ax.set_xlim(ax.get_xlim()[::-1])

plt.legend()
plt.show()
plt.close()


