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



# def petualangan_hutan():
#     stamina = 10  # Stamina awal
#     langkah = 0  # Langkah awal
#     tujuan = 10  # Target langkah

#     print("Selamat datang di Hutan Terlarang!")
#     print(f"Stamina awal: {stamina}\n")

#     while langkah < tujuan and stamina > 0:
#         print(f"Langkah ke-{langkah + 1}:")
#         print("1. Jalan (kurangi stamina)")
#         print("2. Makan buah (tambah stamina)")
        
#         pilihan = input("Pilihan: ")

#         if pilihan == "1":
#             stamina -= 2  # Berjalan mengurangi stamina
#             langkah += 1
#         elif pilihan == "2":
#             stamina += 5  # Makan buah menambah stamina
#         else:
#             print("Pilihan tidak valid, coba lagi.")
#             continue  # Kembali ke awal loop tanpa menghitung langkah
        
#         if stamina <= 0:
#             print("\nPetualang kelelahan dan tidak bisa melanjutkan perjalanan.")
#             break
        
#         print(f"Stamina tersisa: {stamina}\n")

#     if langkah >= tujuan:
#         print(f"\nPetualang berhasil mencapai akhir perjalanan dengan stamina {stamina}!")
#     else:
#         print("\nPetualangan berakhir di tengah jalan.")


# # Memanggil fungsi petualangan_hutan()
# petualangan_hutan()




# import random

# def pertarungan_monster():
#     darah_pemain = 100  # HP Pemain
#     darah_monster = 80  # HP Monster
#     jumlah_bertahan = 3  # Batas bertahan

#     print("🔥 Petualangan Dimulai! Anda bertemu monster! 🔥")
#     print(f"❤ Darah Anda: {darah_pemain} | 👹 Darah Monster: {darah_monster}\n")

#     while darah_pemain > 0 and darah_monster > 0:
#         print("1. Serang (Mengurangi darah monster)")
#         print(f"2. Bertahan (Kurangi serangan & pulihkan HP) - Sisa {jumlah_bertahan} kali")
#         pilihan = input("Pilihan Anda: ")

#         if pilihan == "1":
#             # Serangan pemain (damage acak antara 15-25)
#             damage_pemain = random.randint(15, 25)
#             darah_monster -= damage_pemain
#             print(f"⚔ Anda menyerang monster! Monster kehilangan {damage_pemain} HP.")
#         elif pilihan == "2":
#             if jumlah_bertahan > 0:
#                 # Mengurangi serangan monster dan memulihkan HP pemain
#                 jumlah_bertahan -= 1
#                 heal = random.randint(5, 15)  # Pemain menyembuhkan diri
#                 darah_pemain += heal
#                 print(f"🛡 Anda bertahan! Serangan monster berkurang setengah.")
#                 print(f"✨ Anda juga menyembuhkan diri sebesar {heal} HP!")
#             else:
#                 print("⚠ Anda sudah tidak bisa bertahan lagi! Pilih aksi lain.")
#                 continue
#         else:
#             print("❌ Pilihan tidak valid, coba lagi.")
#             continue

#         if darah_monster <= 0:
#             print("\n🎉 Anda mengalahkan monster! 🎉")
#             break

#         # Monster menyerang balik
#         damage_monster = random.randint(10, 20)

#         # Jika pemain bertahan, serangan monster berkurang 50%
#         if pilihan == "2":
#             damage_monster //= 2  

#         darah_pemain -= damage_monster
#         print(f"👹 Monster menyerang Anda! Anda kehilangan {damage_monster} HP.")

#         if darah_pemain <= 0:
#             print("\n💀 Anda dikalahkan oleh monster! Petualangan berakhir... 💀")
#             break

#         print(f"\n❤ Darah Anda: {darah_pemain} | 👹 Darah Monster: {darah_monster}\n")

# # Memulai pertarungan
# pertarungan_monster()

# import random

# def petualangan_gua():
#     stamina = 15  # Stamina awal
#     langkah = 0  # Langkah awal
#     tujuan = 15  # Target langkah

#     print("🏔 Selamat datang di Gua Misterius!")
#     print(f"Stamina awal: {stamina}\n")

#     while langkah < tujuan and stamina > 0:
#         print(f"Langkah ke-{langkah + 1}:")
#         print("1. Jalan (kurangi stamina)")
#         print("2. Minum air suci (tambahkan stamina)")
        
#         pilihan = input("Pilihan: ")

#         if pilihan == "1":
#             stamina -= 3  # Berjalan mengurangi stamina
#             langkah += 1

#             # 30% kemungkinan menemukan air suci secara otomatis
#             if random.random() < 0.3:
#                 print("✨ Anda menemukan air suci dan meminumnya! (+7 stamina)")
#                 stamina += 7
#         elif pilihan == "2":
#             stamina += 7  # Minum air suci menambah stamina
#         else:
#             print("Pilihan tidak valid, coba lagi.")
#             continue  # Kembali ke awal loop tanpa menghitung langkah
        
#         if stamina <= 0:
#             print("\n💀 Petualang kelelahan dan tidak bisa melanjutkan perjalanan.")
#             break
        
#         print(f"Stamina tersisa: {stamina}\n")

#     if langkah >= tujuan:
#         print("\n🎉 Petualang berhasil menemukan harta karun dengan stamina", stamina, "!")
#     else:
#         print("\n🏴‍☠ Petualangan berakhir di tengah jalan.")

# # Memanggil fungsi untuk memulai game
# petualangan_gua()