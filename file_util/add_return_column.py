import pandas as pd
import numpy as np


def add_return_col(file_path):
    # 讀取資料
    df = pd.read_csv(file_path, parse_dates=['date'])

    # 按照日期排序（保險）
    df = df.sort_values('date')

    # 計算報酬率（可選：用 log return）
    df['return'] = df['close'].pct_change()  # 一般報酬率
    # df['log_return'] = np.log(df['close'] / df['close'].shift(1))  # 對數報酬率

    # 去除第一行 NaN
    df = df.dropna()
    
    return df
