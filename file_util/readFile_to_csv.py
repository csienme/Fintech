import os
import pandas as pd

# 1. 指定 pickle 檔案路徑
pkl_path = 'csi300.pkl'

# 2. 指定 CSV 輸出資料夾
csv_dir = 'csv_output'
os.makedirs(csv_dir, exist_ok=True)

try:
    df = pd.read_pickle(pkl_path)
except Exception as e:
    print(f'⚠️ 读取失败：{e}')
    exit(1)

# 3. 判斷是否 MultiIndex，並重置索引
if isinstance(df.index, pd.MultiIndex):
    df = df.reset_index()  # 會多出 instrument 和 datetime
else:
    df = df.reset_index().rename(columns={'index': 'datetime'})

# 4. 把 'instrument' 和 'datetime' 放前面（如果存在）
cols = df.columns.tolist()
for col in ['instrument', 'datetime']:
    if col in cols:
        cols.insert(0, cols.pop(cols.index(col)))
df = df[cols]

# 5. 生成 csv 檔名（與 pkl 同名，副檔名改成 csv）
base_name = os.path.splitext(os.path.basename(pkl_path))[0]
csv_path = os.path.join(csv_dir, base_name + '.csv')

# 6. 寫出 CSV（不含索引）
df.to_csv(csv_path, index=False)
print(f'✅ 已保存包含 instrument & datetime 的 CSV 檔案：{csv_path}')
