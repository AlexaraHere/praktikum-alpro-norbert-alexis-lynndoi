
def penjumlahan(n):
    if n > 0:
        hasil = n + penjumlahan(n - 1)
        print(hasil)
    else:
        hasil = 0
    return hasil

penjumlahan(6)
