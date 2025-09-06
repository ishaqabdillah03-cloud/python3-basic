import csv

print("MATERI 10-C FILE HANDLING")
print("-----------------------------------------")



file_path = r"C:\SMAIT HSI\python\pesan.txt"
# buka file target dengan mode tertentu
file_pesan = open (file_path, "r") # r = read only
baca_pesan = file_pesan.read()
print(f"isi pesanya: {baca_pesan}")
# tutup file
file_pesan.close

# print('-------------open-----------------')
# csv_alamat_path = r"C:\SMAIT HSI\python\PERCOBAAN\File handing\alamat.csv"
# with open(csv_alamat_path, "r") as file_alamat:
#     baca_alamat = csv.reader(file_alamat)
#     list_alamat = list(baca_alamat) # ubah csv object ke list
#     print(f"Daftar alamat: {list_alamat}")

# print('-------------ADD ROW CSV-----------------')
# alamat_kholid = [11, "kholid", "sukabumi"]
# print(f"Alamat baru: {alamat_kholid}")
# with open(csv_alamat_path, "a", newline="") as file_alamat:
#     tulis_alamat = csv.writer(file_alamat)
#     tulis_alamat.writerow(alamat_kholid)
#     print("---> selesai menambah baris baru ke csv\n")


print('------------- UPDATE ROW CSV-----------------')
# open -> baca file -> ambil datanya, jadikan list
# buat ulang semua baris file csv dengan mode "w"
csv_alamat_path = r"C:\SMAIT HSI\python\PERCOBAAN\File handing\alamat.csv"
# buat list kosong untuk menampung data dari csv
 = csv.reader(file_alamat)
    for item_alamat in baca_alamat:
        data_alamat.append(item_alamat)

# ekstrak list data alamat dengan for loop
for item in data_alamat:
    # cek kolom nama (index 1)
    if item[1] == 'surya':
        print("Data surya ditemukan, ganti alamat...")
        item[2] = "bandung" # index 2 (kolom alamat)
    else:
        print("skip... bukan data surya! ")

# ubah data alamat (index 2)
print(f"list data alamat: {data_alamat}")

# buka file dengan mode "w" (write) -> menulis ulang semuanya
# beserta newline/baris barunya kosong atau ""
with open(csv_alamat_path, "w", newline="") as file_alamat:
    tulis_alamat = csv.writer(file_alamat) # targetnya file 
    tulis_alamat.writerows(data_alamat) # tambah baris baru
    print("---> selesai membuat ulang data csv\n")

data_alamat = []
with open(csv_alamat_path, "r") as file_alamat:
    baca_alamat