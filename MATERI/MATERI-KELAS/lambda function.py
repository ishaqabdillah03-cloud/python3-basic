print("Materi 9C - python function")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
# def -> fungsi lebih dari 1 baris
def halo_dek(nama):
    # f (format setring) menggunakan {} untuk variabel
    print(f"halo dek {nama}")
    print(f"apa kabar dek {nama}")
    print("-------------------------")
# lambda -> fungsi antonim yg 1 baris aja 
halo_kak = lambda nama: print(f"halo kak {nama}")
# fungsi tidak akan berguna jika tidak dipanggil 

halo_dek("nezuko")
halo_dek("anya")
halo_kak("bilal")
halo_kak("tegar")


# higher order function (map, sorted, filter)
uang_jajan = [100000, 200000, 10000, 50000, 75000]
# map() -> mentranformasi data item 
kurangi_jajan = map (lambda uang: uang - 50000, uang_jajan)
list_kurangi_jajan = list (kurangi_jajan)
print(f"uang jajan : {uang_jajan}")
print(f"kurangi jajan: {list_kurangi_jajan}")

# sorted() -> mengurutkan data 
urutkan_uang = sorted(uang_jajan)
balik_uang = sorted(uang_jajan, reverse=True)
print(f"urutkan uang: {urutkan_uang}")
print(f"urutkan uang terbalik: {balik_uang}")

# filter() -> untuk menyaring data sesuai kondisi
filter_uang_gede = filter(lambda uang: uang > 50000, uang_jajan)
list_uang_gede = list(filter_uang_gede) 
print(f"filter uang gede: {list_uang_gede}")



