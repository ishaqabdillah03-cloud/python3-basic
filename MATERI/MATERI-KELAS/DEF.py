print("struktur function\n")
# buat fungsi dengan 'def' lalu nama fungsi nya  
# parameter 'nama' untuk mengambil nilai dari luar ke isi fungsi
def halo_dunia(nama):
    print("halo dunia")
    print("hello Mr.", nama )
    print("--------------->")
# panggiil nama fungsi disertai ()
halo_dunia("aziz")
halo_dunia("bilal")
halo_dunia("ismail")
halo_dunia("ucok")


# fungsi luas persegi panjamg
def luas_persegi_panjang(panjang, lebar):
    print("P =", panjang)
    print("L =", lebar)
    rumus = panjang * lebar
    print("hasil luas persegi panjang = ", rumus)

luas_persegi_panjang(30, 5)
luas_persegi_panjang(8, 100)

def luas_segitiga(alas, tinggi):
    print("A =", alas)
    print("T =", tinggi)
    rumus = 1/2 * alas * tinggi
    print("hasil luas segitiga = ", rumus)

luas_segitiga(10, 5)
luas_segitiga(50, 25)


