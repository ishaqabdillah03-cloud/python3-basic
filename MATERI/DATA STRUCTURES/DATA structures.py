print("python data structures\n")
# list -> [ ] -> berurutan. berubah, boleh duplikat

daftar_belanja = [
    "pisang kembung",# index 0
    "es teh desa",# index 1
    "gabin"# index 2
]
print("---------------------------------------")
print("tas belanja",daftar_belanja)

# akses item dengan index
print(daftar_belanja [1] )
# append untuk menambah item ke akhir list
daftar_belanja.append("tahu goolek")
daftar_belanja.append("batagor")
# insert () untuk menambah item ke index tertentu
daftar_belanja.insert(2, "jus alpukat")
daftar_belanja.insert(0, "roti")
# remove () untuk menghapus item
daftar_belanja.remove("gabin")
daftar_belanja.reverse("tahu golek")
print("tas belanja skr",daftar_belanja)
print("---------------------------------------")

# menggabungkan list dengan +
jajanan_asep = ["olive chiken","seblak","roti aoka"]
jajanan_bilal = ["naspad","es teh","gorengan"]
titip_belanjaan = jajanan_asep + jajanan_bilal
print("titipan belanja", titip_belanjaan)
# megandakan item list dengan *
print("bilal nambah: ", jajanan_bilal)

# list bercabang (list multi dimensi)
daftar_menu = [
    ["kopi","teh","susu jahe"],
    ["jus mangga","jus jeruk","jus alpukat","jus naga"],
    ["es teler","es dewet"]
]
print("---------------------------------------")
print("DAFTAR MENU", daftar_menu)
print(daftar_menu [1] [2] )

print("----------------- TUPLE ----------------------")

# TUPLE -> ( ) -> berurutan, tidak berubah, boleh duplikat
ttl = ("purworjo", 21, "januari", 2009)
print("TTL: ",ttl)
print("Bulan lahir: ", ttl [2])
# unpacking variabel (mengekstak tuple ke variabel baru sesuai urutan )
tempat_lahir, tgl_lahir, bln_lahir, thn_lahir = ttl
print("TAHUN LAHIR: ", thn_lahir)
