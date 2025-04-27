"8.1"
def cek_anagram(kata1, kata2):
    # Mengubah semua huruf menjadi huruf kecil dan menghapus spasi
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    # Mengecek apakah panjang kedua kata sama
    if len(kata1) != len(kata2):
        return " "

    # Mengecek apakah huruf-huruf dalam kedua kata sama setelah diurutkan
    return sorted(kata1) == sorted(kata2)


kata11 = input("kata pertama: ")
kata22 = input("kata kedua: ")

if cek_anagram(kata11, kata22):
    print(f'"{kata11}" adalah anagram dari "{kata22}".')
else:
    print(f'"{kata11}" bukan anagram dari "{kata22}".')

"8.2"

def frekuensi(kalimat, kata):
    spesial = '.,!?;:()[]{}\'"'
    kalimat = kalimat.lower()
    kata = kata.lower()
    
    for simbol in spesial:
        kalimat = kalimat.replace(simbol, '')
        
    daftar_kata = kalimat.split()
    return daftar_kata.count(kata)

kalimat1 = input("Masukkan kalimat: ")
kata1 = input("Kata yang mau dihitung: ")

jumlah_kemunculan = frekuensi(kalimat1, kata1)
print(f'Kata "{kata1}" muncul sebanyak {jumlah_kemunculan} kali.')

"8.3"
# def penghilang_spasi(kalimat):
#     a =' '.join(kalimat.strip().split())
#     return a

# b = penghilang_spasi(input("Masukkan kalimat: ")) 
# print(b)

"8.4"
def kata_pendek_panjang(kalimat):
    kata_kata = kalimat.strip().split()
    terpendek = kata_kata[0]
    terpanjang = kata_kata[0]

    for kata in kata_kata:
        if len(kata) < len(terpendek):
            terpendek = kata
        if len(kata) > len(terpanjang):
            terpanjang = kata

    return terpendek, terpanjang

a = input("Masukkan kalimat: ")
pendek, panjang = kata_pendek_panjang(a)
print(f"Kata terpendek: {pendek}")
print(f"Kata terpanjang: {panjang}")

"8.5"
import re

def jadihari(teks):
    yyyymmdd = re.findall(r'\d+-\d+-\d+', teks)

    tahun1 = int(input("masukin tahun sekarang bos: "))
    bulan1 = int(input("masukin bulan sekarang bos: "))
    hari1 = int(input("masukin hari sekarang bos: "))

    semuabulan = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    totalhariskrng = tahun1 * 365 + semuabulan[bulan1 - 1] + hari1

    hasil = []

    for i in yyyymmdd:
        pecah = i.split('-')
        tahun = int(pecah[0])
        bulan = int(pecah[1])
        hari = int(pecah[2])

        hari_total = tahun * 365 + semuabulan[bulan - 1] + hari
        selisih = totalhariskrng - hari_total

        hasil.append(f"{i} 00:00:00 selisih {selisih} hari") 
    return hasil

a = jadihari("Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02).")

for j in a:
    print(j)

"8.6"

import re
import random

def kalimat(teks):
    hurufgede = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hurufkecil = "abcdefghijklmnopqrstuvwxyz"
    angka = "0123456789"
    semua_karakter = hurufgede + hurufkecil + angka

    teks = teks.split(" ")
    hasil = []

    for i in teks:
        if "@" in i and "." in i:
            email = i
            username = email.split("@")[0]

            password = ""
            for i in range(8):
                password += random.choice(semua_karakter)

            hasil.append(f"{email} username: {username} password: {password}")

    return hasil

a = kalimat("anton@mail.com dimiliki oleh antonius budi@gmail.co.id dimiliki oleh budi anwari slamet@getnada.com dimiliki oleh slamet slumut matahari@tokopedia.com dimiliki oleh toko matahari")

for j in a:
    print(j)