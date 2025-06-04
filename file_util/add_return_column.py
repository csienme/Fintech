import pandas as pd
import numpy as np

def add_future_return_col(file_path):
    # 讀取資料
    df = pd.read_csv(file_path, parse_dates=['date'])

    df = df.sort_values('date')

    # if 'return' in df.columns:
    #     df = df.drop(columns=['return'])
    
    # 計算未來報酬率（用 open 價）
    df['future_return'] = df['Open'].shift(-2) / df['Open'].shift(-1) - 1

    # 去除最後兩行 NaN（因為 shift(-2) / shift(-1) 造成的空值）
    df = df.dropna()

    return df
