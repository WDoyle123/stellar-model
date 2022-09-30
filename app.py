from cProfile import label
from fileinput import filename
import readline
import matplotlib.pyplot as plt 
import pandas as pd
import csv
import os


count = 0
x= ("x")
y= ("y")
with os.scandir("/home/will/Documents/Astrophysics/stellar-model/data") as it:
    for entry in it: 
        with open(entry) as datFile:
            lum = ([data.split()[1] for data in datFile])
            lum.pop(0)
        with open(entry) as datFile:
            teff = ([data.split()[2] for data in datFile])
            teff.pop(0)
        plt.plot(teff,lum, marker = "o", label=entry)


# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True
plt.title("The Physics of Stellar Models")
plt.legend()
plt.ylabel("Luminosity, Log L")
plt.xlabel("Log Teff")
plt.show()



