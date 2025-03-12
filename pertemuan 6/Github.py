# def int_to_string(angka):
#     # Kamus untuk mengubah angka menjadi kata
#     kamus = {'0': 'nol','1': 'satu','2': 'dua','3': 'tiga','4': 'empat','5': 'lima','6': 'enam','7': 'tujuh','8': 'delapan','9': 'sembilan'}


#     angka_str = str(angka)
#     hasil = ""
#     for digit in angka_str:
#         kata = kamus[digit]
#         if hasil != "": 
#             hasil = hasil + " "  
#         hasil = hasil + kata  
#     return hasil
# angka = 7732

# print(int_to_string(8283))  

# def int_to_string(angka):
   
#     for i in angka  :
#         if i == '0': print("Nol", end=" ")
#         elif i == '1': print("Satu", end = " ")   
#         elif i == '2': print("Dua", end=" ")
#         elif i == '3': print("Tiga", end=" ")
#         elif i == '4': print("Empat", end=" ")
#         elif i == '5': print("Lima", end=" ")
#         elif i == '6': print("Enam", end=" ")
#         elif i == '7': print("Tujuh", end=" ")
#         elif i == '8': print("Delapan", end=" ")
#         elif i == '9': print("Sembilan", end=" ")

# int_to_string('222')



# def perkalian(angkaAwal, angkaKedua):
#     hasil = angkaAwal*angkaKedua
#     i = 0
#     print(f"{angkaAwal} * {angkaKedua} ",end=" = ")

#     for i in range (angkaAwal):
#         print(angkaKedua, end=" ")

#         if i < angkaAwal - 1:
#             print(" + ", end="")
#         i += 1

#     print(f" = {hasil} ")

# perkalian(10,2)


# def ganjil(batasBawah,batasAtas):
    
#     if batasBawah < batasAtas:
#         for i in range(batasBawah, batasAtas + 1):
#             if i %2 != 0:
#                 print (i, end=",")
#     else: 
            
            
#         for i in range(batasBawah,batasAtas-1 , -1):
#             if i % 2 !=0: 
#                 print(i,end=", ")
        
# batasBawah = int(input("Masukkan Batas Bawah : "))
# batasAtas = int(input("Masukkan Batas Atas: "))

# ganjil(batasBawah,batasAtas)



# outputnya bilangan genap 1 sampai 20 : 110 
# Fungsi untuk menghitung total bilangan genap
# def hitung_total_genap(n):
#     total = 0
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             total += i
#     return total

# # Input dari user
# n = int(input("Masukkan bilangan n: "))
# hasil = hitung_total_genap(n)

# # Output
# print(f"Total bilangan genap dari 1 sampai {n} adalah: {hasil}")



# output nya yang Bilangan genap dari 1 sampai 20: 2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20 = 110

# # # Fungsi untuk menghitung total bilangan genap dan mencetak prosesnya
# def hitung_total_genap(n):
#     total = 0
#     proses = ""  # Untuk menyimpan proses perhitungan sebagai string
    
#     for i in range(1, n + 1):
#         if i % 2 == 0:  # Cek bilangan genap
#             if total > 0:
#                 proses += " + "  # Tambah tanda + jika bukan bilangan pertama
#             proses += str(i)  # Tambah bilangan genap ke proses
#             total += i
    
#     return total, proses

# # Input dari user
# n = int(input("Masukkan bilangan n: "))
# hasil, proses = hitung_total_genap(n)

# # Tanpa input
# # Fungsi untuk menghitung total bilangan genap dan menampilkan prosesnya
# def hitung_total_genap(n):
#     total = 0
#     proses = ""  # Untuk menyimpan proses perhitungan sebagai string
    
#     for i in range(1, n + 1):
#         if i % 2 == 0:  # Cek bilangan genap
#             if total > 0:
#                 proses += " + "  # Tambah tanda + jika bukan bilangan pertama
#             proses += str(i)  # Tambah bilangan genap ke proses
#             total += i
    
#     return total, proses

# # Nilai n langsung ditentukan di sini
# n = 10
# hasil, proses = hitung_total_genap(n)

# # Output
# print(f"Bilangan genap dari 1 sampai {n}: {proses} = {hasil}")


# # Fungsi untuk mengubah kata menjadi huruf indah
# def ubah_huruf_indah(kata):
#     vokal = "aiueoAIUEO"
#     hasil = ""
    
#     for huruf in kata:
#         if huruf in vokal:  # Jika huruf vokal, gandakan
#             hasil += huruf * 2
#         else:  # Jika konsonan, tetap
#             hasil += huruf
            
#     return hasil

# # Kata langsung ditentukan di sini
# kata = "anak ayam"
# hasil = ubah_huruf_indah(kata)

# # Output
# print(f"Kata asli: {kata}")
# print(f"Huruf indah: {hasil}")

# # Output
# print(f"Bilangan genap dari 1 sampai {n} =  {proses} = {hasil}")


# def fibo(batas):
#     bil1 = 1
#     bil2 = 1
#     if bil1 < batas:
#         print(bil1, end=' ')
#         print(bil2, end=' ')
#     suku_baru = bil1 + bil2
#     while suku_baru < batas:
#         print(suku_baru, end=' ')
#         bil1 = bil2
#         bil2 = suku_baru
#         suku_baru = bil1 + bil2

# batas = int(input('Masukkan batas dari deret fibonacci: '))
# fibo(batas)

# def average():
#     total = 0
#     count = 0
#     while True:
#         input_user = int(input('Masukkan nilai (nol atau negatif untuk berhenti): '))
#         if input_user < 1: # negatif atau nol
#             break
#         else:
#             total = total + input_user
#             count = count + 1
#     if count > 0:
#         return total / count
#     else:
#         return 0
# # bagian utama program
# hasil = average()
# print('Rata-rata: ', hasil)    



