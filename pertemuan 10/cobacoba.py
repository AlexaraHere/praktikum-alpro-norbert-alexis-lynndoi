# def ada_elemen_sama(list1, list2):
#     return any(elemen in list2 for elemen in list1)
# list_a = [1, 2, 0, 4]
# list_b = [5, 6, 3, 8]
# hasil = ada_elemen_sama(list_a, list_b)
# print(hasil)


# def cari_terbesar_kedua(data):
#     if len(data) < 2:
#         raise ValueError("List harus memiliki minimal dua elemen.")
#     unik = list((data)) # Menghapus duplikat
#     if len(unik) < 2:
#         raise ValueError("List tidak memiliki cukup bilangan unik.")
#     unik.sort(reverse=True)
#     return unik[1]
# angka = [10, 5, 8, 20, 20, 4]
# hasil = cari_terbesar_kedua(angka)
# print(hasil) # Output: 10



# def filter_duplikasi(list, batas):
#     hasil = []
#     for i in list:
#         if hasil.count(i) < batas:
#             hasil.append(i)
#     print(hasil)

# filter_duplikasi([1, 2, 4, 2, 1, 2, 3, 2], 2)





# kalimat = [
#     "saya suka python",
#     "python sangat menyenangkan",
#     "saya suka belajar"
# ]

# semua_kalimat = " ".join(kalimat)       # Gabungkan semua kalimat jadi 1 string
# kata_unik = list(set(semua_kalimat.split()))  # Split jadi kata, lalu ubah ke set

# print("Kata unik:", kata_unik)
# print("Jumlah kata unik:", len(kata_unik))



# def hitung_kata_unik(kalimat_list):
#     semua_kalimat = " ".join(kalimat_list)
#     kata_unik = list(set(semua_kalimat.split()))
#     print(kata_unik) 
#     a = len(kata_unik)
#     print(a)

# kalimat = [
#     "saya saya saya saya suka python",
#     "python sangat menyenangkan",
#     "saya suka belajar"
# ]
# b = hitung_kata_unik(kalimat)
# print(b)

# def huruf_duplikat(teks):
#     counter = {}
#     urutan = []
    
#     for char in teks:
#         if char != " ":  # Mengabaikan spasi
#             counter[char] = counter.get(char, 0) + 1
    
#     # Ambil huruf yang muncul lebih dari sekali, dalam urutan kemunculannya pertama kali
#     for char in teks:
#         if char != " " and counter[char] > 1 and char not in urutan:
#             urutan.append(char)
    
#     return urutan
# hasil = huruf_duplikat("Belajar Belajar")
# print("Huruf duplikat (urut berdasarkan kemunculan):", hasil)




# def huruf_unik_pertama(teks):
#     teks_bersih = teks.replace(" ", "")
#     for char in teks_bersih:
#         if teks_bersih.lower().count(char.lower()) == 1:
#             return char
#     return "Tidak ada huruf unik"
# teks = "aAbBABac"
# hasil = huruf_unik_pertama(teks)
# print("Huruf unik pertama:", hasil)


def balik_kata_genap(teks):
    kata_list = teks.split()
    hasil = []

    for i in range(len(kata_list)):
        if i % 2 == 0:
            hasil.append(kata_list[i][::-1])  # Balik kata di posisi genap
        else:
            hasil.append(kata_list[i])        # Biarkan kata di posisi ganjil

    return ' '.join(hasil)

teks = "Belajar Python itu menyenangkan sekali bukan"
print(balik_kata_genap(teks))