import pathlib
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt



class TechnicalAnalysis():
    def __init__(self) -> None:
        pass

    def csv2df(self, path_csv:pathlib.Path) -> pd.core.frame.DataFrame:
        df = pd.read_csv(path_csv, parse_dates=['Date'], index_col='Date')
        return df


    def macd(self, df:pd.DataFrame, short_span:int=12, long_span:int=26, signal_span:int=9) -> pd.DataFrame:
        ''' MACD : Moving Average Convergence Divergence '''
        short_ema = df['Close'].ewm(span=short_span, adjust=False).mean()
        long_ema = df['Close'].ewm(span=long_span, adjust=False).mean()
        macd = short_ema - long_ema
        signal_line = macd.ewm(span=signal_span, adjust=False).mean()
        histgram = macd - signal_line

        df['MACD'] = macd
        df['SignalLine'] = signal_line
        df['Histgram'] = histgram
        return df
    
    
    def rsi(self, df:pd.DataFrame, span:int=14):
        ''' RSI : Relative Strength Index '''
        up = df["Close"].diff().clip(lower=0).rolling(span).mean()
        down = df["Close"].diff().clip(upper=0).rolling(span).mean()
        rsi = 100 - 100 / ( 1 - up / down )
        df["RSI"] = rsi
        return df


    def plot(self, df:pd.DataFrame):
        # df[['MACD', 'SignalLine']].plot(figsize=(10, 5))
        df[['RSI']].plot(figsize=(10, 5))
        plt.show()



if __name__ == '__main__':
    path_current_dir = pathlib.Path(__file__).parent
    path_csv = path_current_dir.joinpath("data", "101.csv")

    ta = TechnicalAnalysis()
    df = ta.csv2df(path_csv)

    df = ta.macd(df)
    df = ta.rsi(df, 14)


    print(df)

    # ta.plot(df.loc["2022":"2023"])