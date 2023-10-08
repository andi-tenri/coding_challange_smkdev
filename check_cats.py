def checkCats(data_tuti, data_nining):
    # koreksi array dari data tuti
    koreksi_tuti = data_tuti[:]
    # Hapus usia kucing (kucing pertama dan dua kucing terakhir)
    del koreksi_tuti[0] 
    del koreksi_tuti[-2:]
    # Gabungkan data Tuti dan nining yang sudah dikoreksi
    gabungkan_data = koreksi_tuti + data_nining

    # Cek usia
    for i, age in enumerate(gabungkan_data, start=1):
        if age >= 3:
            print(f"Kucing Nomor {i} adalah Kucing Dewasa dan berusia {age} tahun")
        else:
            print(f"Kucing Nomor {i} masih anak-anak dan berusia {age} tahun")

data_tuti_1 = [3, 5, 2, 12, 7]
data_nining_1 = [4, 1, 15, 8, 3]

data_tuti_2 = [9, 16, 6, 8, 3]
data_nining_2 = [10, 5, 6, 1, 4]

print("Hasil untuk Data Uji 1:")
checkCats(data_tuti_1, data_nining_1)

print("\nHasil untuk Data Uji 2:")
checkCats(data_tuti_2, data_nining_2)
