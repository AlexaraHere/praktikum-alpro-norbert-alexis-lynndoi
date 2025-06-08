def f(n):
    if n ==0 or n ==1:
        return 1
    else:
        return f(n-1) * n

print(f(5))


def pertambahan(b1,b2):
    if b2 == 1:
        print("%d = " %(b1), end='')
        return b1
    else:
        print("%d + " %(b1), end='')
        return b1 + pertambahan(b1,b2-1)

print(pertambahan(2,4))

def perkalian(b1,b2):
    if b2 == 1:
        print("%d = " %(b1), end='')
        return b1
    else:
        print("%d + " %(b1), end='')
        return b1 * perkalian(b1,b2-1)

print(perkalian(2,4))


def basis(n,base):
    convert = "0123456789ABCDEF"
    if n < base:
        return convert[n]
    else:
        return basis(n//base,base) + convert[(n-base)//base]

a = int(input("bil "))
b = int(input("basis "))
print(basis(a,b))


def binaryTree(a):
    if a < 1:
        return "Root tidak valid"
    if a == 1:
        return 1
    else:
        kiri = a // 2
        kanan = a - kiri
        return 1 + binaryTree(kiri) + binaryTree(kanan)
    
print(binaryTree(7))


def penjumlahan(n):
    if n > 0:
        hasil = n + penjumlahan(n - 1)
        print(hasil)
    else:
        hasil = 0
    return hasil

penjumlahan(6)
