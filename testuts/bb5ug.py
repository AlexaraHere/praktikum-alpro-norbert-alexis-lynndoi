# Buat sebuah fungsi hitung_biaya_perawatan yang menghitung total biaya perawatan kendaraan berdasarkan beberapa faktor penting seperti jenis mobil, bahan bakar, usia kendaraan, jenis perawatan, dan biaya tambahan.

# Fungsi ini menerima beberapa parameter sebagai berikut:

# jenis_mobil (str) → Jenis mobil yang akan diservis. Jenis yang didukung:
# "Hatchback"
# "MPV"
# "Luxury"
# "Listrik"
# jarak_tempuh (int) → Jarak tempuh kendaraan dalam kilometer. (Tidak digunakan dalam perhitungan saat ini, tetapi tetap ada untuk fleksibilitas di masa depan.)
# jenis_bahan_bakar (str) → Jenis bahan bakar kendaraan. Pilihan yang tersedia:
# "bensin"
# "diesel"
# "listrik" (khusus untuk kendaraan listrik, yang memiliki perawatan lebih murah.)
# usia_mobil (int) → Usia kendaraan dalam tahun. Jika usia kendaraan lebih dari 5 tahun, maka biaya perawatan dasar akan bertambah sesuai jenis mobil.
# tipe_perawatan (str) → Jenis perawatan yang dilakukan, dengan opsi berikut:
# "rutin" → Perawatan standar seperti penggantian oli, pemeriksaan filter, dsb.
# "darurat" → Perawatan yang lebih kompleks dan mahal, seperti perbaikan mesin atau kelistrikan.
# harga_kendaraan (int) → Harga kendaraan dalam rupiah. Parameter ini wajib diisi karena mempengaruhi biaya penyimpanan kendaraan di bengkel.
# biaya_tambahan (int, opsional, default=0) → Tambahan biaya jika ada perbaikan ekstra.
# waktu_parkir (int, opsional, default=0) → Jumlah hari kendaraan menginap di bengkel. Biaya tambahan dihitung berdasarkan persentase dari harga kendaraan sesuai jenis mobil.
# Ketentuan Perhitungan Biaya:
# Biaya dasar perawatan (sebelum faktor lainnya diterapkan):
# Hatchback → Rp500.000
# MPV → Rp800.000
# Luxury → Rp2.000.000
# Listrik → Rp500.000
# Jika kendaraan menggunakan bahan bakar diesel, biaya dasar naik:
# Hatchback: +10%
# MPV: +15%
# Luxury: +20%
# Jika kendaraan berusia lebih dari 5 tahun, biaya dasar naik:
# Hatchback: +10%
# MPV: +20%
# Luxury: +25%
# Listrik: +10%
# Biaya service berdasarkan tipe perawatan:
# Perawatan rutin:
# Hatchback → Rp75.000
# MPV → Rp150.000
# Luxury → Rp400.000
# Listrik → Rp50.000
# Perawatan darurat:
# Hatchback → Rp150.000
# MPV → Rp300.000
# Luxury → Rp800.000
# Listrik → Rp150.000
# Biaya parkir kendaraan (biaya simpan mobil di bengkel) dihitung sebagai persentase dari harga kendaraan per hari:
# Hatchback → 0.025% per hari
# MPV → 0.03% per hari
# Luxury → 0.067% per hari
# Listrik → 0.02% per hari
# Fungsi hitung_biaya_perawatan harus mengembalikan total biaya perawatan dalam bentuk integer (tanpa pembulatan desimal).

# Catatan Penting: Pertambahan biaya persenan jangan pakai pecahan, pakai decimal. Contoh: 0.02 persen, berarti 0.0002*biaya_dasar, dan tanpa tanda kurung.

# Jika inputan jenis kendaraan tidak valid, kembalikan "Jenis mobil tidak valid"

# Contoh:

# 1. Hatchback, bensin, usia 6 tahun, perawatan rutin, parkir 3 hari, Output: 775000.0
# 2. MPV, diesel, usia 3 tahun, perawatan darurat, ada biaya tambahan Rp50.000, parkir 5 hari, Output: 1870000.0

def hitung_biaya_perawatan(jenis_mobil, jarak_tempuh, jenis_bahan_bakar, usia_mobil, tipe_perawatan, harga_kendaraan, biaya_tambahan=0, waktu_parkir=0):
    if jenis_mobil == "Hatchback":
        biaya_dasar = 500000
        if jenis_bahan_bakar == "diesel":
            biaya_dasar += biaya_dasar * 0.10
        if usia_mobil > 5:
            biaya_dasar += biaya_dasar * 0.10
        biaya_tambahan_perawatan = 75000 if tipe_perawatan == "rutin" else 150000
        biaya_keep = harga_kendaraan * 0.00025 * waktu_parkir
    elif jenis_mobil == "MPV":
        biaya_dasar = 800000
        if jenis_bahan_bakar == "diesel":
            biaya_dasar += biaya_dasar * 0.15
        if usia_mobil > 5:
            biaya_dasar += biaya_dasar * 0.20
        biaya_tambahan_perawatan = 150000 if tipe_perawatan == "rutin" else 300000
        biaya_keep = harga_kendaraan * 0.0003 * waktu_parkir
    elif jenis_mobil == "Luxury":
        biaya_dasar = 2000000
        if jenis_bahan_bakar == "diesel":
            biaya_dasar += biaya_dasar * 0.20
        if usia_mobil > 5:
            biaya_dasar += biaya_dasar * 0.25
        biaya_tambahan_perawatan = 400000 if tipe_perawatan == "rutin" else 800000
        biaya_keep = harga_kendaraan * 0.00067 * waktu_parkir
    elif jenis_mobil == "Listrik":
        biaya_dasar = 500000
        if usia_mobil > 5:
            biaya_dasar += biaya_dasar * 0.10
        biaya_tambahan_perawatan = 50000 if tipe_perawatan == "rutin" else 150000
        biaya_keep = harga_kendaraan * 0.0002 * waktu_parkir
    else:
        return "Jenis mobil tidak valid"
    
    biaya_total = biaya_dasar + biaya_tambahan_perawatan + biaya_tambahan + biaya_keep
    
    return biaya_total


# Kalkulator Rusak 

# Karel, seorang pecinta matematika, memiliki sebuah program kalkulator perkalian yang sedikit unik. Kalkulator tersebut akan mengalikan digit paling kiri dari bilangan-bilangan yang diinput. 

# Dengan kata lain, jika kita menginput :

# Angka1 = 3214
# Angka2 = 12
# Angka3 = 8235
# Maka, kalkulator akan menampilkan digit paling kiri dari ketiga bilangan tersebut, lalu mengalikannya.

# Digit Kiri Angka1 = 3
# Digit Kiri Angka2 = 1
# Digit Kiri Angka3 = 8
# Dengan begitu, hasil yang akan keluar adalah angka 24 (hasil perkalian dari 3*1*8).

# Jika dari ketiga angka tersebut ada yang angka-nya 0, maka sistem akan mengeluarkan pesan error berupa string "Error, angka tidak boleh 0", kemudian akan langsung return 0.

# Sayangnya, program kalkulator perkalian milik Karel itu hilang. Hati Karel sangat sedih, tugas kalian adalah membantu  Karel untuk membuat kembali program kalkulator perkalian tersebut.

       

# Buatlah fungsi kalkulatorRusak(angka1, angka2, angka3) yang memiliki parameter tersebut. Mohon baca terlebih dahulu penjelasan parameter dibawah ini

# Penjelasan Parameter

# angka1 : Angka pertama (akan selalu integer)
# angka2 : Angka kedua (akan selalu integer)
# angka3 : Angka ketiga (akan selalu integer)
# Catatan Penting

# Fungsi ini tidak melakukan return (langsung print)
# Perhatikan lagi huruf kapital dan format output yang diinginkan (ini case-sensitive, jadi beda 1 karakter bisa salah, hati-hati!)
 
# Test	Result
# kalkulatorRusak(3214,12,8235)
# Digit Kiri Angka1 : 3
# Digit Kiri Angka2 : 1
# Digit Kiri Angka3 : 8
# Hasil : 24
# kalkulatorRusak(42,145,236)
# Digit Kiri Angka1 : 4
# Digit Kiri Angka2 : 1
# Digit Kiri Angka3 : 2
# Hasil : 8

def kalkulatorRusak(angka1,angka2,angka3):
    digitkiri1 = 0
    digitkiri2 = 0
    digitkiri3 = 0
    
    if angka1 == 0 or angka2 == 0 or angka3 == 0:
        print("Error, angka tidak boleh 0")
        return 0
    
    if angka1 > 9:
        while angka1 > 9:
            angka1 = angka1 // 10
            digitkiri1 = angka1
    else:
        digitkiri1 = angka1
    
    if angka2 > 9:
        while angka2 > 9:
            angka2 = angka2 // 10
            digitkiri2 = angka2
    else:
        digitkiri2 = angka2
    
    if angka3 > 9:
        while angka3 > 9:
            angka3 = angka3 // 10
            digitkiri3 = angka3
    else:
        digitkiri3 = angka3
    
    hasil = digitkiri1 * digitkiri2 * digitkiri3
    
    print(f"Digit Kiri Angka1 : {digitkiri1}")
    print(f"Digit Kiri Angka2 : {digitkiri2}")
    print(f"Digit Kiri Angka3 : {digitkiri3}")
    print(f"Hasil : {hasil}")

# Andi adalah seorang pebisnis ternak lele yang baru ingin merintis usahanya. Ia memiliki sebuah bidang tanah yang lapang untuk beternak lele. Ia ingin melihat berapa banyaknya keuntungan yang akan ia dapat selama 3 bulan.
# Untuk itu, Andi perlu memperhatikan beberapa faktor yang akan mempengaruhi bisnisnya, antara lain:
# Jumlah benih lele yang dibeli (dalam kg).
# Harga beli benih lele per kg.
# Harga jual lele per kg pada saat panen.
# Biaya pakan selama sebulan.
# Biaya Perawatan per minggu (yaitu obat-obatan).
# Persentase lele berhasil bertumbuh (dalam 1 bulan)
# Rumus :
# Keuntungan Akhir =(Jumlah lele yang berhasil bertumbuh selama 3 bulan x Harga jual per kg) - (Total modal)
# Jumlah lele yang berhasil tumbuh = (jumlah lele bulan sebelumnya) + (persentase keberhasil selama 1 bulan x jumlah lele bulan sebelumnya)
# Total modal = (Total harga beli benih lele) + (total biaya pakan) + (total biaya perawatan)
# Contoh :
# Test Case 1
# andiTernakLele(100,350_000,380_000,25_000,15_000,85)
# output : "Rp. 205346749"
# Test Case 2
# print(andiTernakLele(50, 500_000, 300_000, 50_000, 20_000, 10))
# output : "Merugi le"
# Test Case 3
# print(andiTernakLele(80, 400_000, 395_000, 30_000, 10_000, 35))
# output : "Rp. 45537850"
# BATASAN:
# Harus menggunakan fungsi bernama andiTernakLele yang menerima parameter :
# jumlah_benih : float
# harga_beli : int
# harga_jual : int
# biaya_pakan : int
# biaya_perawatan : int
# persentase keberhasilan : int
# Fungsi harus mengembalikan satu nilai berupa string (total keuntungan Andi).
# Persentase keberhasilan harus positif. Jika negatif maka mengeluarkan pesan "Persentase harus positif".

# Test	Result
# print(andiTernakLele(100, 350_000, 380_000, 25_000, 15_000, 85))
# Rp. 205346749
# print(andiTernakLele(50, 500_000, 300_000, 50_000, 20_000, 10))
# Merugi le



def andiTernakLele(jumlah_benih: float, harga_beli: int, harga_jual: int, 
                   biaya_pakan: int, biaya_perawatan: int, 
                   persentase_keberhasilan: int) -> str:
    if (persentase_keberhasilan>=0) :
        # Konversi persentase keberhasilan ke faktor pertumbuhan
        konversi_persentase=(persentase_keberhasilan)/100
        # Hitung total harga beli benih lele
        total_harga_beli = jumlah_benih * harga_beli

        # Hitung total biaya pakan selama 3 bulan
        total_biaya_pakan = biaya_pakan * 3

        # Hitung total biaya perawatan selama 3 bulan (4 minggu per bulan)
        total_biaya_perawatan = biaya_perawatan * 3 * 4

        # Hitung jumlah lele yang berhasil tumbuh setelah 3 bulan
        for _ in range(3):
            jumlah_benih = jumlah_benih+(jumlah_benih*konversi_persentase)

        # Hitung total modal
        total_modal = total_harga_beli + total_biaya_pakan + total_biaya_perawatan

        # Hitung total pendapatan dari hasil panen
        total_pendapatan = jumlah_benih * harga_jual

        # Hitung keuntungan akhir
        keuntungan = int(total_pendapatan - total_modal)

        return f"Rp. {keuntungan}" if keuntungan > 0 else "Merugi le"
    else:
        return "Persentase harus positif"