import pathlib
import pandas as pd


path_current_dir = pathlib.Path(__file__).parent
path_csv = path_current_dir.joinpath("101.csv")

df = pd.read_csv(path_csv, parse_dates=['Date'], index_col='Date')
print(df.head(3))


if __name__ == '__main__':
    print("stock")