print("MATERI 7C - PYTHON DATA STRUCTURES\n")

# set -> { } -> tidak berurutan, berubah, tidak duplikat 
game_ridho = {"genshin", "mlbb", "delta force"}
game_imam = {"valorant", "point blank"}

# add() -> untuk menambahkan item ke set
game_imam.add("mlbb")
game_imam.add("valorant")# jika ada akan di skip
# .remove() ->menghapus item dari set
game_ridho.remove("mlbb")
# len() -> menghitung jumlah item 
print("ridho ada ",len(game_ridho),"=>",game_ridho )
print("imam ada ",len(game_imam),"=>",game_imam )
# .union() menggabungkan 2 set yg berbeda
game_gabungan = game_imam.union(game_ridho)
total_game = len(game_gabungan)
print("Game Gabungan", total_game,"=>", game_gabungan)
# intersection() mencari item yg kembar  dari 2 set berbeda
# .difference() mencari item yg beda  dari 2 set berbeda
game_kembar = game_ridho.intersection(game_imam)
game_beda = game_ridho.difference(game_imam)
print("Game kembar : ", game_kembar)
print("Game berbeda : ", game_beda)


print("---------------------DICT-----------------------\n")
# dict (dictionary) -> {key:value} / {kunci:isinya}
# berurutan berdasarkan key, key tidak bisa duplikat
daftar_anime = {
    "jujutsu_kaisen": "gojo satoru",
    "one_punch_man": "saitama",
    "naruto": "shikamaru",
    "waifu" : {
        "demon_slayer": "mitsuri",
        "spy_x_family": "anya",
        "naruto": "tsunade",
        }
}

print("Daftar anime: ", daftar_anime)
print("MC ONE PUNCH MAN: ",daftar_anime["one_punch_man"])
print("WAIFU LOLI: ", daftar_anime["waifu"] ["spy_x_family"])
# mengubah item vakue berdasarkan key
daftar_anime["one_punch_man"] = "genos"
daftar_anime["waifu"] ["demon_slayer"] = "nezuko"
print("MC ONE PUNCH MAN BARU: ",daftar_anime["one_punch_man"])
print("WAIFU LOLI BISA GEDE: ", daftar_anime["waifu"] ["demon_slayer"])
# menambahkan item value berdasarkan key
daftar_anime["wind_breaker"] = "sakura"
print("MC WIND BREAKER: ",daftar_anime["wind_breaker"])



