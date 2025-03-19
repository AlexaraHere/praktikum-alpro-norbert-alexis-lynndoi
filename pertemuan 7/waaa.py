# for i in range(3):
#     for j in range(3):
#         if i == j :
#             continue
#         print(i,j, end=" ")


# x = 10
# while x > 5:
#     x -= 2
#     print(x, end=" ")


# for i in range (10, 0, -2):
#     print(i, end= " ")


# for i in range (1,6):
#     print("*" * i)


# n = int(input("masukkan n = ")) # kedalaman nya berapa
# for i in range (1, n+1):
#     for j in range(1,i+1):
#         print(i, " ", end=" ")
#     print()

# n=int(input("Masukkan n = "))
# for i in range(1,n+1):
#     if i%2==1:
#         for j in range(1,n+1):
#             print(j," ",end='')
#     else:
#         for j in range(n,0,-1):
#             print(j," ",end='')
#     print()

# n = int(input("masukkan n = "))
# for i in range(0, n + 1):
#     for j in range(1, n -i+1):
#         if j%2==1:
#             print("X", end=" ")
#         else:
#             print("o", end=" ")
#     print()



# n = int(input("wooooooooo "))
# hasil = 1
# for i in range(n, 0, -1):
#     hasil 
#     print(i, end=" ")

# def capitalh(baris, kolom):
#     tengah = round(baris//2)
#     if baris < 2 or baris % 2 == 0 or kolom < 2:
#         print("dimensi tidak sesuai")
#     elif baris % 2 != 0 and baris >= 3 and kolom >=3:
#         for i in range(baris):
#             for j in range(kolom):
#                 if j == 0 or j == baris - 1 or i == baris // 2:
#                     print('#', end='')
#                 else:
#                     print(' ', end='')
#         print() 


# def capitalh(baris, kolom):
#     if baris < 3 or baris % 2 == 0:  # Pastikan jumlah baris ganjil dan minimal 3
#         print("dimensi tidak sesuai")
#         return

#     for i in range(baris):
#         if i == baris // 2:
#             print("#" * kolom)  # Baris tengah penuh
#         else:
#             print("#" + " " * (kolom - 2) + "#")  # Sisi kiri dan kanan


# def capitalh(baris, kolom):
#     tengah = round(baris // 2)
#     if baris < 2 or baris % 2 == 0 or kolom < 2:
#         print("dimensi tidak sesuai")
#     else:
#         for i in range(baris - 1):
#             if i == tengah:
#                 print("#" * kolom)
#             for j in range(kolom):
#                 if j == 0 or j == kolom - 1: 
#                     print("#", end="")
#                 else:
#                     print(" ", end="")  
#             print()
# capitalh(5,4)

# def is_prime(bilangan):
#     bilangan2 = 2
#     if bilangan == 2:
#         return("prima")
#     elif bilangan < 2:
#         return("bukan prima")
#     else:    
#         while bilangan2 <= bilangan:
#             i = bilangan%bilangan2
#             bilangan2 = bilangan2 + 1
#             if i != 0:
#                 if bilangan2 == bilangan:
#                     return("prima")
#             else:
#                 return("bukan prima")
# print(is_prime(12))

# def polaular(angka):
#     if angka < 1:
#         print ("tidak terdefiniskan")
#     sangka = 1
#     for i in range(1, angka + 1):
#         if i % 2 == 1:
#             for j in range(angka):
#                 print(f"{current_number:02d}", end=' ')
#                 sangka += 1
#         else:
#             sangka += angka - 1
#             for j in range(angka):
#                 print(f"{current_number:02d}", end=' ')
#                 sangka -= 1
#             sangka += angka + 1
#         print()


# def print_h(height):
#     if height < 3:
#         print("Tinggi harus minimal 3 untuk membentuk huruf H.")
#         return

#     for i in range(height):  # Loop untuk baris
#         for j in range(height):  # Loop untuk kolom
#             # Cetak '#' jika di kolom pertama, kolom terakhir, atau baris tengah
#             if j == 0 or j == height - 1 or i == height // 2:
#                 print('#', end='')
#             else:
#                 print(' ', end='')  # Cetak spasi untuk bagian kosong
#         print()  # Pindah ke baris baru setelah selesai mencetak satu baris

# # Contoh penggunaan
# tinggi = 7  # Anda bisa mengubah tinggi sesuai keinginan
# print_h(tinggi)

