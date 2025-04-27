# kalimat = "Cerita Rakyat"
# awal = 0
# akhir =6 
# print (len(kalimat))
# print(kalimat[7:len(kalimat)-1])
# print(kalimat[awal:akhir])


# kalimat = "babi"
# kalimat2 = kalimat[0] + 'alah'
# print (kalimat2)


# kalimat = "Saudara-saudara, pada tanggal 17-08-1945 Indonesia merdeka"
# # print(kalimat)

# hasil = kalimat.split(" ")
# print(hasil)

# for kal in hasil:  
#     if kal[0]. isdigit():
#         print(kal)
#         hasil2 = kal.split("-")
#         print (hasil2)
#         print(hasil2[1]+"/"+hasil2[0]+"/"+hasil2[2])

"""untuk menghilangkan spasi"""

# import re
# handle=open('mbox-short.txt')
# count = 0
# for line in handle:
#     line=line.rstrip()
#     if re.search('From:', line):
#         count += 1
#         print(line)
#         print("Count: ",count)


"""Menghitung huruf vokal tidak kapital """
# a_string = "AnTonIus"
# lowercase = a_string.lower()
# total = 0 
# for x in "aiueo":
#     jmlh = lowercase.count(x)
#     total += jmlh
# print(total)



# satu = "Step!1231313   on, On.. pEts??"

# """Untuk mengubah huruf kapital menjadi huruf kecil"""
# satu = satu.lower()
# print(satu)

# """untuk menghilangkan selain alphabet"""
# satu1 = ''.join([i for i in satu if i.isalpha()])
# print(satu1)
# satu2 = ''.join([i for i in satu if i.isdigit()])
# print(satu2)
# satu3 = ''.join([i for i in satu if not i.isalnum()])
# print(satu3)

# def sensor_nohp(kalimat):
#     semua_karakter = ''.join(kalimat.split())

#     angka = ''.join([i for i in semua_karakter if i.isdigit()])
#     panjang = len(angka)
#     awalan = angka[:4]
#     akhiran = angka[-3:]
#     tengah = 'x' * (panjang - 7)
#     return(awalan + tengah + akhiran)

# print(sensor_nohp("081928109280188. ashdouawhdoiqwhdoiqwhiduqw         0878211553999")) 





def cek_anagram(kata1, kata2):
    # Mengubah semua huruf menjadi huruf kecil dan menghapus spasi
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    # Mengecek apakah panjang kedua kata sama
    if len(kata1) != len(kata2):
        return False

    # Mengecek apakah huruf-huruf dalam kedua kata sama setelah diurutkan
    return sorted(kata1) == sorted(kata2)

# # Contoh penggunaan
# kata_pertama = input("Masukkan kata pertama: ")
# kata_kedua = input("Masukkan kata kedua: ")

# if cek_anagram(kata_pertama, kata_kedua):
#     print(f'"{kata_pertama}" adalah anagram dari "{kata_kedua}".')
# else:
#     print(f'"{kata_pertama}" bukan anagram dari "{kata_kedua}".')


# kalimat = "aku    akak     oaoa "
# a =' '.join(kalimat.strip().split())
# print(a) 

# def kata_pendek_panjang(kalimat):
#     # Menghapus spasi berlebih dan memecah kalimat jadi list kata
#     kata_kata = kalimat.strip().split()

#     # Inisialisasi kata terpendek dan terpanjang dengan kata pertama
#     terpendek = kata_kata[0]
#     terpanjang = kata_kata[0]

#     # Loop untuk mencari kata terpendek dan terpanjang
#     for kata in kata_kata:
#         if len(kata) < len(terpendek):
#             terpendek = kata
#         if len(kata) > len(terpanjang):
#             terpanjang = kata
#     return terpendek, terpanjang

# # Contoh penggunaan
# kalimat = input("Masukkan kalimat: ")
# pendek, panjang = kata_pendek_panjang(kalimat)
# print("Kata terpendek:", pendek)
# print("Kata terpanjang:", panjang)


#  Buatlah suatu program yang dapat menghitung frekuensi kemunculan suatu kata
# yang ada pada String. Misal terdapat kalimat "Saya mau makan. Makan itu wajib. Mau siang
# atau malam saya wajib makan". Ditanyakan kata "makan". Output: makan ada 3 buah
# kalimat = "saya mau makan makan makan"
# kalimatdicari = "makan"
# tandabaca = '!@#$%^&*()_+<>?"''":{}'
# teks = kalimat.lower()
# for i in 
# import re
# kalimat = "Test1"
# if re.search(r'[0-9]', kalimat):
#     print(kalimat)