import os
import glob
import pandas as pd
import sys

def rename_datetime_to_date(folder_path):
    """
    將 folder_path 資料夾下所有 .csv 檔案中的 'datetime' 欄位改為 'date'。
    """
    csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

    for file_path in csv_files:
        df = pd.read_csv(file_path)

        if 'datetime' in df.columns:
            df = df.rename(columns={'datetime': 'date'})
            df.to_csv(file_path, index=False)
            print(f"✅ 已修改並儲存：{file_path}")
        else:
            print(f"⚠️ 檔案未包含 datetime 欄位：{file_path}")
            
            
if __name__ == "__main__":
    rename_datetime_to_date(sys.argv[1])