# Pecahan Uang
# Toko kelontong "ALPRO" membutuhkan cara memecah uang nominal tertentu ke dalam uang 10000, 5000, 2000, 1000, 500, 200, dan 100an.

# Contoh: 11600, maka outputnya:
# 1 sepuluh ribuan
# 0 lima ribuan
# 0 dua ribuan
# 1 seribuan
# 1 lima ratusan
# 1  seratusan


# Catatan

# Menggunakan fungsi 
# For example:

# Test	Result
# pecahan_uang(11600)
# 1 sepuluh ribuan
# 0 lima ribuan
# 0 dua ribuan
# 1 seribuan
# 1 limaratusan
# 1 seratusan
# pecahan_uang(7200)
# 0 sepuluh ribuan
# 1 lima ribuan
# 1 dua ribuan
# 0 seribuan
# 0 limaratusan
# 2 seratusan


def pecahan_uang(harga_barang):
    sepuluhribu = harga_barang // 10000
    harga_barang = harga_barang % 10000
    limaribu = harga_barang // 5000
    harga_barang = harga_barang % 5000
    duaribu = harga_barang // 2000
    harga_barang = harga_barang % 2000
    seribu = harga_barang // 1000
    harga_barang = harga_barang % 1000
    limaratus = harga_barang // 500
    harga_barang = harga_barang % 500
    seratus = harga_barang // 100
    print(str(sepuluhribu) + " sepuluh ribuan")
    print(str(limaribu) + " lima ribuan")
    print(str(duaribu) + " dua ribuan")
    print(str(seribu) + " seribuan")
    print(str(limaratus) + " limaratusan")
    print(str(seratus) + " seratusan")


# Fungsi Persamaan Linear
# Diketahui sebuah fungsi fx = x4+2x3+5x2+x+3

# Jika x di asumsikan sebagai bilangan tertentu, tentukan nilai dari fx.

# Catatan

# Menggunakan fungsi 
# For example:

# Test	Result
# print(fungsi(3))
# 186


def fungsi(x):
    fx = x**4+2*x**3+5*x**2+x+3
    return fx



# Belanja Diskon
# Selain menjadi guru matematika, Deni juga seorang pedagang. Saat ini toko Deni sedang mengadakan diskon (dalam persen). Karena banyaknya orderan yang masuk, Deni kerepotan untuk menghitung total belanjaan pelanggannya. Buatlah sebuah program perhitungan bagi toko Deni yang sedang diskon.

# Catatan

# Menggunakan fungsi 
# For example:

# Test	Result
# print(belanja(100000,5,10))
# 450000.0
# print(belanja(1570000,8,55))
# 5652000.0



def belanja(harga_barang, jumlah_barang, diskon):
    total_belanja = harga_barang * jumlah_barang
    potongan_diskon = total_belanja * diskon / 100
    total_belanja_setelah_diskon = total_belanja - potongan_diskon
    return total_belanja_setelah_diskon