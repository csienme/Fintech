import sys
import os
import glob
from add_return_column import add_future_return_col





def process_all_csv_in_folder(folder_path, save_suffix=""):
    """
    套用 add_return_col 到 folder_path 下所有 .csv 檔案，
    並儲存為新檔案（加上 suffix）。

    Args:
        folder_path (str): 要處理的資料夾路徑
        save_suffix (str): 存檔時新增的尾碼，預設為 "_with_return"
    """
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    print(f"共找到 {len(csv_files)} 個 CSV 檔案")

    for file_path in csv_files:
        print(f"處理中：{file_path}")
        df = add_future_return_col(file_path)

        # 產生新檔案名稱
        base = os.path.basename(file_path)  # e.g. "AAPL.csv"
        name, ext = os.path.splitext(base)
        new_file = os.path.join(folder_path, f"{name}{save_suffix}.csv")

        df.to_csv(new_file, index=False)
        print(f"已儲存：{new_file}")
        
        
        
if __name__ == "__main__":
    
    
    folder = sys.argv[1]  # 替換成你實際的資料夾路徑
    process_all_csv_in_folder(folder)