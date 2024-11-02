import os
import glob

# Tentukan path folder
folder_path = os.getcwd() + '/data/Kab Bima/LSTM_Metrics/'
print(folder_path)

# Cari file yang namanya diawali dengan "forecasting_result_KAB_BIMA_"
file_pattern = os.path.join(folder_path, "forecasting_result_KAB_BIMA*")
# Dapatkan daftar semua file yang cocok dengan pola
files_to_rename = glob.glob(file_pattern)

# Loop untuk rename setiap file yang ditemukan
for file_path in files_to_rename:
    try:
        # Ambil nama file saja tanpa path
        file_name = os.path.basename(file_path)
        
        # Hapus "forecasting_result_KAB_BIMA_" dari nama file
        new_file_name = file_name.replace("forecasting_result_KAB_BIMA_", "")
        
        # Buat path baru untuk file dengan nama yang sudah diubah
        new_file_path = os.path.join(folder_path, new_file_name)
        
        # Rename file
        os.rename(file_path, new_file_path)
        print(f"File {file_path} berhasil diubah menjadi {new_file_path}")
    except Exception as e:
        print(f"Gagal mengubah nama file {file_path}. Error: {e}")
