import json

print("----- MATERI 12-JSON -----")
print("------------------------------------")

file_json_path = r"C:\SMAIT HSI\python\MATERI-KELAS\JSON\rukun_islam.json"
with open(file_json_path, "r") as file_json:
    data_json = json.load(file_json)
    print(f"Judul file : {data_json['judul']}")
    print(f"Jumlah rukun islam : {data_json['jumlah']}")
    print(f"Daftar rukun islam :")
    for item_rukun in data_json['rukun']:
        print(item_rukun)


    print("-"*45) # buat garis panjang
    print("Daftar 3 Surah di AL-Qur'an")
    print("-"*45)
    # tampilkan surah sebagai tabel
    # keys: nomor,nama,jumlah_ayat,tempat_turun
    print("| Na | Nama | Jumlah Ayat | Tempat Turun")
    print("-"*45)
    for surah in data_json['surah']:
        print(f"| {surah['nomer']} | {surah['nama']} | {surah['jumlah_ayat']} | {surah['tempat_turun']} | ")