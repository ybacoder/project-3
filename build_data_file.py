import os
import pandas as pd

def import_data(file_path, cols, index_col="STU_ID", low_memory=False):
    
    df = pd.read_csv(file_path, index_col=index_col, usecols=cols, low_memory=low_memory)
    
    return df

els_file_path = os.path.join("data", "ELS-2002", "els_02_12_byf3pststu_v1_0.csv")
nels_file_path = os.path.join("data", "NELS-1988", "nels_88_00_byf4stu_v1_0.csv")

cols = [
    "STU_ID",
    "BYSEX",
    "BYRACE",
    "BYSTLANG",
    "BYPARED",
    "BYINCOME",
    "BYURBAN",
    "BYREGION",
    "BYRISKFC",
    "BYHMWRK",
    "BYWRKHRS",
    "BYS42",
    "BYS43",
    "BYTVVIGM",
    "BYS46B",
    "BYS44C",
    "BYS20E",
    "BYS87C",
    "BYS20D",
    "BYS23C",
    "BYS37",
    "BYS27I",
    "BYS90D",
    "BYS38A",
    "BYS20J",
    "BYS24C",
    "BYS24D",
    "BYS54I",
    "BYS84D",
    "BYS84I",
    "BYS85A",
    "F2HSSTAT",
    "F2EVERDO",
    "F1RGPP2"
    ]


df = import_data(els_file_path, cols)

if __name__ == "__main__":
    print(df)


df_valid = df >= 0 # remove all invalid entries of data
df = df[df_valid.all(axis=1)]

df = df[df["BYTVVIGM"] != 99] # remove top_coded BYTVVIGM values

if __name__ == "__main__":
    print(df)

