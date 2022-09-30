import pandas as pd
import os

count=0
x = ".csv"
with os.scandir("/home/will/Documents/Astrophysics/physics-of-stellar-models/data") as it:
    for entry in it:
        name = (str(count))
        count +=1
        if entry.name.endswith(".dat") and entry.is_file():
            read_file = pd.read_csv(entry)
            read_file.to_csv (name+x, index=None)
        continue


