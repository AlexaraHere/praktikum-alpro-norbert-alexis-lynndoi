
# Pola Sakit Kepala
# Program "Pola Sakit Kepala" ini merupakan implementasi dari sebuah algoritma untuk mencetak pola angka spiral simetris yang bila dilihat menyerupai visualisasi denyut sakit kepala atau radiasi visual yang sering dialami penderita migren. Pola ini memiliki karakteristik khas berupa angka-angka yang membentuk semacam cerminan dari tengah ke luar, menghasilkan efek visual simetris seperti gelombang yang berpusat pada titik tengah (angka 1). Dinamakan "Pola Sakit Kepala" karena bentuknya yang memancar dari pusat menyerupai sensasi denyutan yang dirasakan oleh penderita sakit kepala parah, dimana angka-angka semakin besar saat menjauhi titik tengah, menciptakan ilusi optik yang memvisualisasikan sensasi sakit yang menyebar.

# Fungsi dengan nama pola_sakit_kepala() ini memiliki 2 parameter yaitu panjang dan lebar. Fungsi ini bertujuan untuk mencetak pola angka berbentuk spiral simetris yang memiliki titik terendah di tengah dan memancar keluar dengan nilai yang semakin besar, dengan syarat panjang dan lebar harus sama dan bernilai ganjil.

# Struktur Pola
# Pola yang dihasilkan berbentuk spiral simetris dengan angka terendah (1) di tengah

# Pola angka berulang setelah 9, kembali ke 0, 1, 2. Sederhananya jika angka 10 menjadi 0, 11 menjadi 1, …, 123 menjadi 3, …, 999 menjadi 9. (Diambil angka yang paling kiri jika angka itu berdigit lebih dari 1)

# Contoh: panjang = 7 dan lebar = 7



# Penjelasan Parameter:
# Fungsi memiliki 2 parameter yaitu panjang dan lebar, dipastikan selalu integer dan dibawah 9999.

# panjang = Tipe data Integer, adalah panjang dari pola

# lebar = Tipe data Integer, adalah lebar dari pola

# Validasi Input
# Nilai absolut dari parameter panjang dan lebar diambil, sehingga nilai negatif akan dikonversi menjadi positif

# Fungsi melakukan pengecekan apakah panjang dan lebar sama, jika tidak akan menampilkan pesan "Panjang dan lebar harus sama!!"

# Fungsi melakukan pengecekan apakah panjang dan lebar adalah bilangan ganjil, jika tidak akan menampilkan pesan "Panjang dan lebar harus bilangan ganjil!!"

 

# Catatan Tambahan:
# Jangan lupa baca soal terlebih dahulu, baca dengan teliti, jika masih tidak jelas baru tanyakan pada asdos

# Untuk melakukan print hasil dalam 1 baris dapat menggunakan parameter end.

# Angka terakhir di setiap baris tidak diikuti spasi, menciptakan tepi yang rapi

# Gunakan abs() untuk mendapatkan nilai absolute dari bilangan negatif

# Tidak perlu return (Gunakan print saja)

# Semangat!! Yang buat soal juga pusing kok:)

# For example:

# Test	Result
# pola_sakit_kepala(7, 7)
# 7 6 5 4 5 6 7
# 6 5 4 3 4 5 6
# 5 4 3 2 3 4 5
# 4 3 2 1 2 3 4
# 5 4 3 2 3 4 5
# 6 5 4 3 4 5 6
# 7 6 5 4 5 6 7
# pola_sakit_kepala(4, 4)
# Panjang dan lebar harus bilangan ganjil!!
# pola_sakit_kepala(-4, 4)
# Panjang dan lebar harus bilangan ganjil!!
# pola_sakit_kepala(5, 7)
# Panjang dan lebar harus sama!!
# pola_sakit_kepala(5, -5)
# 5 4 3 4 5
# 4 3 2 3 4
# 3 2 1 2 3
# 4 3 2 3 4
# 5 4 3 4 5


# Di sebuah kota kecil, ada seorang guru bernama Pak Andi yang suka memberikan tantangan unik kepada murid-murid di kelasnya. Setiap minggu, dia memberikan tugas untuk menulis angka dalam pola tertentu di papan tulis.

# Pada minggu ini, pak Andi meminta murid-muridnya untuk menulis angka dalam bentuk ular dengan aturan sebagai berikut:

# Angka pertama selalu dimulai dari pojok kiri atas dan di-print sebagai “head”

# Pada baris pertama, angka-angka dituliskan secara berurutan dari kiri ke kanan hingga mencapai panjang yang ditentukan

# Pada baris kedua, angka berikutnya (yaitu angka setelah angka terakhir di baris pertama) dituliskan dari ujung kanan ke kiri

# Pada baris ketiga, angka berikutnya (yaitu angka setelah angka terakhir di baris kedua), kembali dilanjutkan dengan berurutan dari kiri ke kanan

# Pola ini terus berulang hingga mencapai jumlah baris yang ditentukan

# Angka paling terakhir selalu di-print sebagai “tail”

# Fungsi yang digunakan dalam soal ini bernama ularAngka dengan parameter (bawah, samping). Jika belum paham mengenai pola, dipersilahkan untuk melihat output dari test case yang ada.

# Penjelasan Parameter
# Fungsi ularAngka memiliki dua parameter dengan nama dan penjelasan sebagai berikut:

# bawah = jumlah baris dalam pola ular angka (bertipe data integer)

# samping = jumlah kolom dalam pola ular angka (bertipe data integer)

# Catatan Tambahan
# Input harus berupa bilangan bulat positif dan lebih besar dari 0

# Semua output angka ditampilkan dalam dua digit 

# Output menggunakan print, bukan return

# Separator antar output menggunakan dua whitespace (“  ”)

# Dipersilakan untuk membuat variabel tambahan jika memang diperlukan

# Baca soal dan contoh output dengan cermat sebelum bertanya kepada asisten

# For example:

# Test	Result
# ularAngka(3, 4)
# head  02  03  04  
# 08  07  06  05
# 09  10  11  tail
# ularAngka(2, 3)
# head  02  03  
# tail  05  04
        # print("head", end="  ")
        # for i in range(1, bawah+1):
        #     if i % 2 == 1:
        #         for j in range(2,samping+1):
        #             print(f"{angka:02d}", end="  ")
        #             angka= angka+1
        #     else:
        #         angka = angka + samping-1
        #         for j in range(angka):
        #             print(f"{angka:02d}", end="  ")
        #             angka = angka - 1
        #             if angka == samping -1:
        #                     print("tail", end= "  ")
        #             angka = angka + bawah + 1
        #         print()
                
# ularAngka(3, 4)
# head  02  03  04  
# 08  07  06  05
# 09  10  11  tail
# ularAngka(2, 3)
# head  02  03  
# tail  05  04


# def polaular(angka):
#     if angka < 1:
#         print ("tidak terdefiniskan")
#     sangka = 1
#     for i in range(1, angka + 1):
#         if i % 2 == 1:
#             for j in range(angka):
#                 print(f"{sangka:02d}", end=' ')
#                 sangka += 1
#         else:
#             sangka += angka - 1
#             for j in range(angka):
#                 print(f"{sangka:02d}", end=' ')
#                 sangka -= 1
#             sangka += angka + 1
#         print()
        
# polaular(4)

# def ularAngka(bawah, samping):
#     angka = 2
#     a=bawah*samping
#     print("head", end="  ")
#     if bawah < 1 or samping < 1:
#         return ""
#     else:
#         for i in range(1, bawah + 1):
#             if i % 2 == 1:
#                 for j in range(2, samping+1):
#                     if i < 10:
#                         print(f"0{angka}", end="  ")
#                         angka += 1
#             else:
#                 for j in range(angka):
#                     if i < 10:
#                         print(f"0{angka}", end="  ")
#                         angka = angka - 1
#                     if angka == a:
#                             print("tail", end= "  ")
#             print()
# ularAngka(2, 3)

# def ularAngka(baris, samping):
#     a = baris * samping
#     if samping < 1 or baris < 1:
#         print ("tidak terdefiniskan")
#     sangka = 1
#     for i in range(1, baris + 1):
#         if i % 2 == 1:
#             for j in range(1, samping + 1):
#                 if sangka == 1:
#                     print("head", end="  ")
#                 elif sangka == a:
#                     print("tail", end="  ")
#                 else:
#                     if sangka < 10:
#                         print(f"0{sangka}", end="  ")
#                     elif sangka >= 10:
#                         print(f"{sangka}", end="  ")
#                 sangka += 1
#         else:
#             sangka += samping - 1
#             for j in range(samping):
#                 if sangka == a:
#                     print("tail", end="  ")
#                 else:
#                     if sangka < 10:
#                         print(f"0{sangka}", end="  ")
#                     elif sangka >= 10:
#                         print(f"{sangka}", end="  ")
#                 sangka = sangka - 1
#             sangka = sangka+ samping + 1
#         print()
# ularAngka(4, 2)
# # head  02  03  04  
# # 08  07  06  05
# # 09  10  11  tail
# ularAngka(2, 3)
# head  02  03  
# tail  05  04


# def ularAngka(baris, samping):
#     a = baris * samping
#     if samping < 1 or baris < 1:
#         print ("tidak terdefiniskan")
#     sangka = 2
#     for i in range(1, baris + 1):
#         if i % 2 == 1:
#             if i == 1:
#                 print("head", end=" ")
#             for j in range(samping -1):
#                 if sangka < 10:
#                     print(f"0{sangka}", end="  ")
#                 elif sangka >= 10:
#                     print(f"{sangka}", end="  ")
#                 if sangka == a-1:
#                     print("tail", end=" ")
#                 sangka += 1
#         else:
#             sangka += samping - 1
#             for j in range(samping):
#                 if sangka < 10:
#                     print(f"0{sangka}", end="  ")
#                 elif sangka >= 10:
#                     print(f"{sangka}", end="  ")
#                 sangka = sangka - 1
#                 if sangka == a-1:
#                     print("tail", end=" ")
#             sangka += samping + 1
#         print()


# def pola_sakit_kepala(panjang, lebar):
#     if panjang % 2 == 0 or lebar % 2 == 0:
#         print("Panjang dan lebar harus bilangan ganjil!!")
#     elif panjang != lebar:
#         print("Panjang dan lebar harus sama!!")
#     elif panjang > 9999 
#     else:
        
#             print()
# abs()

# pola_sakit_kepala(7,7)
# 7 6 5 4 5 6 7
# 6 5 4 3 4 5 6
# 5 4 3 2 3 4 5
# 4 3 2 1 2 3 4
# 5 4 3 2 3 4 5
# 6 5 4 3 4 5 6
# 7 6 5 4 5 6 7


def pola_sakit_kepala(panjang, lebar):
    panjang = abs(panjang)
    lebar = abs(lebar)
    tengah = panjang // 2
    angka = 1
    if panjang != lebar:
        print("Panjang dan lebar harus sama!!")
    elif panjang % 2 == 0 or lebar % 2 == 0:
        print("Panjang dan lebar harus bilangan ganjil!!")
    else:
        for i in range(panjang):
            for j in range(lebar):
                angka = abs(tengah - i) + abs(tengah - j) + 1
                angka = angka % 10
                if j != lebar - 1:
                    print(angka, end=" ")
                else:
                    print(angka)

pola_sakit_kepala(-15, 15)
pola_sakit_kepala(11, 11)
pola_sakit_kepala(7, 7)
pola_sakit_kepala(4, 4)
pola_sakit_kepala(-4, 4)
pola_sakit_kepala(5, 7)
pola_sakit_kepala(5, -5)

#         1
#     1   2   1
# 1   2   3   2   1




