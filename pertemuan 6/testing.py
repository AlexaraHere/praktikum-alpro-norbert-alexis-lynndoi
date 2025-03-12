# def pembagian(angkaAwal, angkaKedua):
#     hasil = angkaAwal // angkaKedua 
#     print(f"{angkaAwal} ÷ {angkaKedua} = {angkaAwal}", end=" ")
#     if angkaKedua == 0:
#         print("Error: Tidak bisa dibagi dengan nol!")
#         return
#     for i in range(hasil):
#         print(f"- {angkaKedua}", end=" ")

#     print(f"oke jadi {angkaKedua} ada {hasil} kali makanya tuh {angkaAwal} // {angkaKedua} = {hasil}")
# pembagian(3,2)



# def perkalian(angkaAwal, angkaKedua):
#     hasil = angkaAwal//angkaKedua
#     i = 0
#     print(f"{angkaAwal} * {angkaKedua} ",end=" = ")
#     if angkaAwal == 0 or angkaKedua == 0:
#         hasil = angkaAwal*angkaKedua
#         hasil = 0 
#         print(f" {hasil} ")
#     else:
#         hasil = angkaAwal*angkaKedua
#         for i in range (angkaAwal):
#             print(angkaKedua, end="")
#             if i < angkaAwal - 1:
#                 print(" + ", end="")
#         print(f" = {hasil} ")
#         i += 1
# perkalian(3,1)

# attributes = ['Electric', 'Fast']
# cars = ['Tesla', 'Porsche', 'Mercedes']

# for attribute in attributes:
#     for car in cars:
#         print(attribute, car)
#     print("-----")


# def perkalian(angkaAwal, angkaKedua):
#     hasil = angkaAwal*angkaKedua
#     i = 0
#     print(f"{angkaAwal} * {angkaKedua} ",end=" = ")
#     if angkaAwal == 0 or angkaKedua == 0:
#         hasil = angkaAwal*angkaKedua
#         hasil = 0 
#         print(f" {hasil} ")
#     else:
#         hasil = angkaAwal*angkaKedua
#         while i < angkaAwal:
#             print(angkaKedua, end="")
#             if i < angkaAwal - 1:
#                 print(" + ", end="")
#             i += 1
#         print(f" = {hasil} ")

# def tabel_perkalian(n):
#     for i in range(1, n+1):
#         for j in range(1, n+1): 
#             print(i * j, end="\t") 
#         print() 

# def piramida_angka(n):
#     for i in range(1, n+1): 
#         for j in range(1, i+1): 
#             print(j, end="")
#         print()

# def kotak_berbingkai(n):
#     for i in range(n):  
#         for j in range(n): 
#             if i == 0 or i == n-1 or j == 0 or j == n-1:
#                 print("#", end="")
#             else:
#                 print(" ", end="")
#         print()

# def segitiga_terbalik(n):
#     for i in range(n, 0, -1):  
#         for j in range(i):  
#             print("*", end="")
#         print()

def papan_catur(n):
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

# n = int(input("ya "))
# print("Piramida Angka:")
# piramida_angka(n)

# print("Kotak Berbingkai:")
# kotak_berbingkai(n)

# print("Segitiga Terbalik:")
# segitiga_terbalik(n)

print("Papan Catur:")
papan_catur(5)

# aaaaa = int(input("masukin angka perkalian 1 "))
# bbbbb = int(input("masukin angka perkalian 2 "))   
# perkalian(aaaaa,bbbbb)

# ccccc = int(input("Masukkan ukuran tabel perkalian: "))
# tabel_perkalian(ccccc)



# def factorial(n):
#     a = 1
#     for i in range(n):
#         i+=1
#         a = a * i
#         print(i, end=" ")
#         if i < n:
#             print(end=" * ")
#     print(f"= {a} ")

# factorial(5)

# def factorial(n):
#     a = 1
#     for i in range(1, n+1):
#         a = a * i
#         print(i, end=" ")
#         if i < n:
#             print(end=" * ")
#     print(f"= {a} ")

# factorial(9)

# def factorial(n):
#     a = 1
#     i = 0
#     while i < n:
#         i += 1
#         a = a * i
#         print(i, end=" ")
#         if i < n:
#             print(end=" * ")
#     print(f"= {a} ")

# factorial(5)

# tup = ('Geeks')
# n = 5
# for i in range(int(n)):
#     tup = (tup,)
#     print(tup)



# def hitung_total_harga(jumlah_barang):
#     total_harga = 0
#     for i in range(1, jumlah_barang + 1):
#         harga = int(input(f"Masukkan harga barang ke-{i}: "))
#         total_harga += harga
#     return total_harga

# # Input jumlah barang
# jumlah_barang = int(input("Masukkan jumlah barang: "))

# # Hitung total harga menggunakan fungsi
# total_harga = hitung_total_harga(jumlah_barang)

# # Tampilkan hasil
# print(f"Total harga belanjaan: {total_harga}")





# def fibonacci(n):
#     a, b = 0, 1
#     for bebe in range(n - 1):
#         a, b = b, a + b
#     return b

# def digit_pertama(x):
#     while x >= 10:
#         x //= 10
#     return x

# # Input dari pengguna
# n = int(input("Masukkan nilai n: "))

# # Hitung Fibonacci ke-n
# fib_n = fibonacci(n)

# # Cetak hasil
# print(f"Bilangan Fibonacci ke-{n} adalah {fib_n}")
# print(f"Digit pertama dari {fib_n} adalah {digit_pertama(fib_n)}")








