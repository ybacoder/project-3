import os
import pandas as pd

els_file_path = os.path.join("data", "ELS-2002", "els_02_12_byf3pststu_v1_0.csv")
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

df = pd.read_csv(els_file_path, index_col="STU_ID", usecols=cols, low_memory=False)

if __name__ == "__main__":
    print(df.head())