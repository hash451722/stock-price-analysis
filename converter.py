import pathlib
import pandas as pd

import numpy as np


def convert_csv():
    path_csv = pathlib.Path("stockchart_101_n225_20230304.csv")
    df = pd.read_csv(path_csv, parse_dates=['日付'])
    df = df.rename(columns={"日付":"date","銘柄名":"Name", "銘柄コード": "Code", "始値":"Open", "高値":"High", "安値":"Low", "終値":"Close", "出来高":"Volume"})
    df = df.loc[:,["date", "Code", "Name", "Open", "High", "Low", "Close", "Volume"]]
    # df['Code'] = df['Code'].astype(str).str[:-1].astype(int)
    df.set_index("date", inplace = True)
    df.to_csv('101.csv')


def read_csv(path_csv:pathlib.Path) -> pd.core.frame.DataFrame:
    df = pd.read_csv(path_csv, parse_dates=['Date'], index_col='Date')
    print(df.head(3))
    print(df.loc["2011"].head(3))
    print(df.loc["2012":].head(3))
    print(type(df))

    return df


if __name__ == '__main__':
    path_current_dir = pathlib.Path(__file__).parent
    path_csv = path_current_dir.joinpath("data", "101.csv")
    
    print("stock")
    read_csv(path_csv)