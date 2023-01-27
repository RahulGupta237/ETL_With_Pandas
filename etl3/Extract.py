import pandas as pd

def readdata(file):
    data = pd.read_csv(file)
    return data