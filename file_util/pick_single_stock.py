import pandas as pd
import sys


if len(sys.argv) < 3:
    print("Usage: python script.py input.pkl output.csv")
    sys.exit(1)
    
file_path = sys.argv[1]
df = pd.read_csv(file_path)

# 篩選出 instrument 為 'NVDA' 的資料
x_df = df[df['instrument'] == sys.argv[2]]

# 將結果寫入新 CSV 檔案（不含 index）
x_df.to_csv(f'{sys.argv[2]}.csv', index=False)
