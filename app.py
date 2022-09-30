from fileinput import filename
import readline
import matplotlib.pyplot as plt 
import pandas as pd
import csv


star1_lum = []
star1_teff =[]

with open("my_file.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        lum = row["logL"]
        teff = row["logTef"]
        star1_lum.append(lum)
        star1_teff.append(teff)

print(star1_lum)
print(star1_teff)

plt.plot(star1_lum, star1_teff)
plt.title("The Physics of Stellar Models")
plt.ylabel("Luminosity, Log L")
plt.xlabel("Log Teff")
plt.ylim(0,10)
plt.xlim(0,10)
plt.show()



