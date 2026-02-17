import pandas as pd

def load_excel(path, header=0):
    df = pd.read_excel(path, header=header)
    return df.to_numpy()

