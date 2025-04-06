# a = int(input("masukin a "))
# b = int(input("masukin b "))
# c = int(input("masukin c "))
# while (a > b) == False:
#     a = a + 1
#     print(a)
# while (b > c) == False:
#     b = b + 1
#     print(b)


# street = []
# street.append(1)
# street.append(2)
# a = int(input("masukin a= "))
# street.append(3)
# b = int(input("Masukin b = "))
# street.append(4)
# c = int(input("Masukkan c = "))
# street.append(5)
# while (a > b) == 0:
#     if street[-1] != 5:
#         street.append(5)
#     a += 1
#     street.append(6)
#     print(a)
#     street.append(7)
# street.append(8)
# while (b > c) == 0:
#     if street[-1] != 5:
#         street.append(8)
#     b += 1
#     street.append(9)
#     print(b)
#     street.append(10)
# street.append(11)
# print(street)
# print(f"Hasil a = {a}")
# print(f"Hasil b = {b}")
# print(f"Hasil c = {c}")

# x = 10
# def a ():
#     x = 20

# print(a())

# def hi(a,b,c):
#     d = a + b
#     print(a)

# a = 3
# b = 7
# c = 8
# print(hi(a,b,c))

# x = 10
# if x > 5:
#     print("aaaa ")

# for i in range(1,3+1):
#     if i == 2:
#         print("dua")
#     else:
#         print("not two")


# x = 7
# if not x > 10:
#     print("apalah")
# else:
#     print("ya")

# i = 5
# while i > 0:
#     if i == 3:
#         break
#     print(i)
#     i-=1

# for i in range(1,10,2):
#     print(i)

# for i in range(3):
#     for j in range(3):
#         if i == j:
#             continue
#         print(i,j,end=" ")

# Memasukkan angka dari tabel
# Data angka dari tabel
numbers = [
    68, 31, 41, 81, 60, 97, 84, 65, 70, 40,
    88, 50, 59, 61, 77, 73, 53, 42, 85, 53,
    62, 89, 95, 52, 46, 52, 83, 71, 55, 72,
    47, 51, 61, 81, 57, 74, 58, 75, 80, 49,
    88, 60, 43, 77, 46, 75, 76, 88, 87, 71,
    65, 51, 64, 52, 64, 67, 57, 79, 85, 54,
    63, 69, 63, 98, 66, 65, 82, 55, 93, 37,
    45, 68, 68, 78, 74, 44, 70, 50, 72, 54,
    70, 60, 71, 77, 59, 73, 67, 78, 86, 86,
    32, 69, 44, 82, 68, 99, 89, 59, 35, 78
]

# Mengurutkan angka dari yang terkecil ke terbesar
sorted_numbers = sorted(numbers)

# Menampilkan hasil
print("Angka terurut dari yang terkecil:")
print(sorted_numbers)