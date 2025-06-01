import pandas as pd
import sys
import os
import glob
# 讀取 CSV 檔案


def filter_nan(file_path):
    
    df = pd.read_csv(file_path)

    # 過濾掉含有任何缺值的列
    df_clean = df.dropna()

    # 如果你想把結果存回 CSV
    df_clean.to_csv(file_path, index=False)

    print("過濾後的資料：")
    print(df_clean)
    
if __name__ == "__main__":
    
    folder_path = sys.argv[1]
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
    for file_path in csv_files:
        filter_nan(file_path)