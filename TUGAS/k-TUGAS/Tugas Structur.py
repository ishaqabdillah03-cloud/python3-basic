print("------ TUGAS TANTANGAN KE 1 ------")
# tantangan pertama : LIST
masak_hari_ini = ["1. dika", "2. ismail", "kholid"]
print("JADWAL PIKET MASAK HARI INI: ")

for jadwal_piket in masak_hari_ini :
    print(jadwal_piket)


print("------ TUGAS TANTANGAN KE 2 ------")
# tantangan kedua : TUPLE
rukun_islam = ("1. Syahadat", "2. Sholat","3. Zakat","4. Puasa", "5. Haji")
print("DAFTAR RUKUN ISLAM: ")

for rukun in rukun_islam :
    print(rukun)

print("------ TUGAS TANTANGAN KE 3 ------")
# tantangan ketiga : SET
kitab_pelajaran = {"1. tahajji","2. tamhidu as-sabil litholabi an-nabil",""}
print("KITAB YANG DIPELAJARI: ")

for kitab in kitab_pelajaran :
    print(kitab)

print("------ TUGAS TANTANGAN KE 4 ------")
# tantangan keempat : DICTIONARY
biodata_santri = {
    "nama":"ishaq",
    "kelas":"x-C",
    "hafalan juz":"10"
}
print("BIODATA SANTRI: ")

for key, value in biodata_santri.items():
    print(f"{key}: {value}")



