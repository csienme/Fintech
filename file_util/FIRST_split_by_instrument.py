import os
import pandas as pd
import sys
from switch_target_col import reorder_csv_columns

# 🟡 修改這裡：輸入檔案與輸出資料夾
file_path = sys.argv[1]
input_csv =  file_path # e.g. 'all_data.csv'
output_dir = f'{sys.argv[1]}_split_by_instrument'

# ✅ 確保輸出資料夾存在
os.makedirs(output_dir, exist_ok=True)

# 🔄 讀取 CSV 檔案
df = pd.read_csv(input_csv)

# ✅ 根據 instrument 分組，並各自寫出
for inst, group in df.groupby('instrument'):
    out_path = os.path.join(output_dir, f"{inst}.csv")
    group.to_csv(out_path, index=False)
    
    reorder_csv_columns(out_path)#更換target col順序
    
    print(f"✅ 已寫出 {out_path}")
