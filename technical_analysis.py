import pathlib
import pandas as pd


class TechnicalAnalysis():
    def __init__(self, path_csv:pathlib.Path) -> None:
        self.df = self._read_csv(path_csv)


    def _read_csv(self, path_csv:pathlib.Path) -> pd.core.frame.DataFrame:
        df = pd.read_csv(path_csv, parse_dates=['Date'], index_col='Date')
        return df






if __name__ == '__main__':
    path_current_dir = pathlib.Path(__file__).parent
    path_csv = path_current_dir.joinpath("data", "101.csv")

    ta = TechnicalAnalysis(path_csv)
    print(ta.df)