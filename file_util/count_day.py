import pandas as pd
import sys
# 讀取包含多種 instrument 的 CSV

file_path = sys.argv[1]
df = pd.read_csv(file_path)

# 計算每個 instrument 的行數
counts = df['instrument'].value_counts().reset_index()
counts.columns = ['instrument', 'row_count']

# 輸出結果到新的 CSV
counts.to_csv(f'{file_path}_counts.csv', index=False)
