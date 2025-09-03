print("===== PROFIL DIGITAL KAMU =====")
nama = input("Nama lengkap: ")
umur = int(input("Umur: "))
kelas = input("Kelas: ")
hobi = input("Hobi: ")
cita_cita = input("cita-cita: ")
belajar = input("lebih suka belajar pagi/malam: \n")


tahun_sekarang = 2025
hitung_tahunLahir = tahun_sekarang - umur

print("=== TIPE DIGITAL ===")
print("pilih tipe kamu: ")
print("1.gamer")
print("2.wibu")
print("3.k-popers")
print("4.anak nongki")
print("5.anak ngonten")
tipe_digital = input("Masukan tipe anda (ketik nomer nya aja): ")
                     
if tipe_digital == "1":
    tipe = "gamer"                                                                                                                                                                                                                                          
    tambahan = input("Masukan game favorit? ")
    fav = f"game favorit: {tambahan}"
    komentar = f"Pasti kamu jago banget main {tambahan}"

if tipe_digital == "2":
    tipe = "wibu"
    tambahan = input("siapa waifu kamu atau husbando kamu? ")
    fav = f"waifu favorit: {tambahan}"
    komentar = "dih kamu bau bawang, kamu adalah musuh terbesar bagi vampir:)"
if tipe_digital == "3":
    tipe = "k-popers"
    tambahan = input("siapa bias kamu? ")
    fav = f"bias favorit: {tambahan}"
    komentar = f"pasti kamu ngevens banget sama {tambahan} "
if tipe_digital == "4":
    tipe = "anak nongki"
    tambahan = input("nongkrong paling sering dimana? ")
    fav = f"tongkrongan favorit: {tambahan}"
    komentar = f"kamu pasti hampir setiap hari mengunjungi {tambahan}"
if tipe_digital == "5":
    tipe = "anak konten"
    tambahan = input("platrfom favorit kamu?YouTube?TikTok? ")
    fav = f"platfrom favorit: {tambahan}"
    komentar = f"kamu pasti terkenal di {tambahan} \n"


print("===== PROFIL DIGITAL KAMU =====")
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Kelas: {kelas}")
print(f"Hobi: {hobi}")
print(f"cita-cita: {cita_cita}")
print(f"Lebih suka belajar: {belajar}")
print(f"Tahun lahir: {hitung_tahunLahir}\n")

print("=== TIPE DIGITAL ===")
print(f"tipe: {tipe}")
print(fav)
print(f"komentar: {komentar}\n")

print("=== fun check ===")
bau_teman = input("teman disebelah kamu bau? (ketik ya/tidak ): ")
if bau_teman == "ya":
    bau = print("gimana tuh, itu sih harus dikasih parfum darurat!")
else:
    tidak_bau = print("berarti teman kamu bersihan orangnya ")




