def deret(tinggi, lebar):
    if lebar < 1 or tinggi < 1:
        return "Tidak terdefinisikan"
    angka = 1  
    for i in range(tinggi):
        if i % 2 == 0:  
            for j in range(lebar):
                print(f"{angka}", end=" ")
                angka += 1
        else:  
            for j in range(lebar):
                print(f"{angka}", end=" ")
                angka += 1
        print()  
#whatehel knp aku buat i%2???????????????? ini kan ga bolak balek

# a = int(input("masukan tinggi= "))
# b = int(input("masukan lebar = "))
# deret(a, b)

import math

def waa(n):
    for i in range (n,0,-1):
        print(math.factorial(i), end=" ")
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def waaa(n):
    for i in range(n, 0, -1):
        factorial = 1
        for j in range(1, i + 1):
            factorial = factorial * j
        print(factorial, end=" ")
        for k in range(i, 0, -1):
            print(k, end=" ")
        print()


# a = int(input("deret faktorial berapa?  "))

# waaa(a)

# def priwaaaa(n):
#     for i in range(n - 1, 1, -1):
#         prima = True
#         for j in range(2, i):
#             if i % j == 0:
#                 prima = False
#                 break
#         if prima:
#             print(f"Bilangan prima terdekat sebelum {n} adalah {i}")
#             break

# def priwaaaaa(n):
#     if n <= 2:
#         print(f"Tidak ada bilangan prima sebelum {n}")
#     else:
#         for i in range(n - 1, 1, -1):
#             prima = False
#             for j in range(2, i):
#                 if i % j == 0:
#                     prima = False
#                     if i % j != 0:
#                         prima= True
#                         break
#             if prima == True:
#                 print(f"Bilangan prima terdekat sebelum {n} adalah {i}")
#                 break

def priwaaaaa(n):
    if n <= 2:
        return "udah paling kecil lah itu"
    else:
        for i in range(n - 1, 1, -1):
            prima = False
            for j in range(2, i):
                if i % j == 0:
                    prima = False
                    break
                if i % j != 0:
                    prima= True
                    break
            if prima == True:
                ret(f"Bilangan prima terdekat sebelum {n} adalah {i}")
                break

a = int(input("Masukkan nilai n: "))
priwaaaaa(a)
#salah soal nya 9 15 masuk ke prima perulangan nya juga ga jalan