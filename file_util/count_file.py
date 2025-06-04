import os

def count_csv_files(folder_path):
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    print(f"總共有 {len(csv_files)} 個 CSV 檔案")
    return csv_files

if __name__ == "__main__":
    csv_list = count_csv_files('../分別0050')
# 或者
# csv_list = count_csv_files('/home/yourname/datasets/')
