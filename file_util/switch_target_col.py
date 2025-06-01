import pandas as pd
import sys

def reorder_csv_columns(file_path):
    """
    讀取 CSV 檔案，移除 'instrument' 欄位，並將 'close' 欄位移動到最後，再儲存回原檔。
    """
    # 讀取原始資料
    df = pd.read_csv(file_path)

    # 移除 instrument 欄位（若存在）
    if "instrument" in df.columns:
        df = df.drop(columns=["instrument"])

    # 將 close 欄位移到最後（若存在）
    if "close" in df.columns:
        close_col = df.pop("close")
        df["close"] = close_col

    # 儲存回原檔案
    df.to_csv(file_path, index=False)
    print(f"✅ 已處理並儲存：{file_path}")

if __name__ == "__main__":
    void