import csv

# baca semua data dari csv

with open("keuangan.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data) 

 # 1. Tampilkan senua data

print("📌 semua data: ")
for row in data:
    print(f"{row['Tanggal']} | {row['Keterangan']} | {row['Kategori']} | {row['Jumlah']}")

 # 2. Hitung total pengeluaran 
print("\n")

total = sum(int(row["Jumlah"]) for row in data)
print(f"💰 Total pengeluaran: Rp.{total}")