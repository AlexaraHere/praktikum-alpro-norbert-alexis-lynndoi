# Yudi Belajar Membaca dan Berhitung
# Yudi merupakan seorang bocah SD yang barusan diajari untuk membaca, menulis, dan berhitung. Saat ini Yudi ingin mengulang materi yang dipelajarinya kemarin, namun ia ingin mempelajarinya sekaligus dalam sekali jalan. Ia ingin menghitung banyaknya huruf vokal yang ada dalam suatu kalimat sehingga ia dapat langsung belajar keduanya.

# Buatlah fungsi bernama hitung_vokal() dengan parameter kalimat. Fungsi ini bertujuan untuk menghitung jumlah huruf vokal yang ada. String bersifat CASE SENSITIVE, “a” dan “A” berbeda.

# Detail dari permintaan soal dijelaskan berikut ini.

# Kalimat
# Kalimat bisa berisi huruf vokal Lowercase maupun Uppercase. Output berupa return jumlah huruf vokal dan jika tidak ada huruf vokal pada kalimat maka akan mengeluarkan String seperti yang ada pada test case.

# Penjelasan Parameter:
# Hanya ada satu parameter dalam fungsi ini, nama parameter tidak harus sama, bebas.

# kalimat = Bertipe data string, berisi suatu kalimat

 

# Catatan Tambahan:
# Baca soal terlebih dahulu sebelum bertanya kepada asdos. Budayakan baca soal ya!

# Boleh menggunakan Logical Expression (and, or, dsb).

# Baca Test Case yang teliti.
# Test	Result
# print(hitung_vokal("Hari ini hari senin."))
# Jumlah Huruf Vokal: 8
# print(hitung_vokal("Ada acara apa hari lni?"))
# Jumlah Huruf Vokal: 10
# print(hitung_vokal("gd hrf vkl ny..."))
# Tidak Ada Huruf Vokal pada kalimat Itu

def hitung_vokal(kalimat):
    hasil = 0
    for i in kalimat:
        if i == "a" or i == "i" or i == "u" or i == "e" or i == "o" or i == "A" or i == "I" or i == "U" or i == "E" or i == "O":
            hasil += 1     
    if hasil == 0:
        return ("Tidak Ada Huruf Vokal pada kalimat Itu")
    return ("Jumlah Huruf Vokal: " + str(hasil))

def hitung_vokal(ohhiiii):
    a = 0
    for i in ohhiiii  :
        if i == "A": a+=1
        elif i == "a": a+=1
        elif i == "I": a+=1
        elif i == "i": a+=1
        elif i == "U": a+=1
        elif i == "u": a+=1
        elif i == "E": a+=1
        elif i == "e": a+=1
        elif i == "O": a+=1
        elif i == "o": a+=1
    if a > 0:
        print(f"Jumlah Huruf Vokal: {a}", end=" ")
    else:
        print ("Tidak Ada Huruf Vokal pada kalimat Itu")
    return""


# Di sebuah negeri yang penuh misteri, terdapat seorang ksatria pemberani yang ingin mengungkap rahasia Gerbang Keabadian. Namun, perjalanannya sangatlah tidak mudah. Ia harus melangkah sejauh mungkin dengan langkah yang sudah ditentukan dan dengan nyawa yang terbatas.

 

# Dalam perjalanan, ia akan menemukan jebakan dan juga keuntungan:

# Jebakan akan muncul di langkah yang bernilai kelipatan 4. Setiap kali menginjakkan langkah di kelipatan 4, nyawa sang ksatria akan berkurang satu. Jika nyawa habis sebelum mencapai Gerbang Keabadian, petualangannya akan gagal.

# Nyawa tambahan akan muncul di langkah yang bernilai kelipatan 6. Setiap kali menginjakkan langkah di kelipatan 6, nyawa sang ksatria akan bertambah satu. 

# Jika ksatria berhasil mencapai Gerbang Keabadian tanpa kehabisan nyawa, maka petualangannya berhasil.

 

# Buatlah fungsi bernama petualanganKsatria yang memiliki parameter-parameter dengan penjelasan berikut ini:

# jarak (int) merupakan jarak (dengan satuan langkah) antara posisi awal Ksatria dan Gerbang Keabadian

# lebar_langkah (int) merupakan lebar dari setiap langkah ksatria dalam sekali melangkah

# nyawa_awal (int) merupakan nyawa yang dimiliki Ksatria sebelum melangkah dalam petualangannya

 

# Output
# Output selalu diawali dengan print MULAI sebagai langkah pertama (nilai langkah awal dimulai dari 1)

# Jika langkah bukan merupakan jebakan atau nyawa tambahan, maka print nilai langkah tersebut

# Jika langkah merupakan jebakan, print JEBAKAN

# Jika langkah merupakan nyawa tambahan, maka print NYAWA+

# Jika ksatria berhasil mencapai Gerbang Keabadian, maka print BERHASIL

# Jika nyawa ksatria sudah habis sebelum mencapai Gerbang Keabadian, maka print GAGAL dan langkah dihentikan

# Jarak antar output adalah dua whitespace (“  ”)

# Output diperoleh melalui PRINT, bukan RETURN

# For example:

# Test	Result
# petualanganKsatria(20, 5, 1)
# MULAI  NYAWA+  11  JEBAKAN  BERHASIL
# petualanganKsatria(30, 3, 2)
# MULAI  JEBAKAN  7  10  13  JEBAKAN  GAGAL


def petualanganKsatria(jarak, lebar_langkah, nyawa_awal):
    langkah = 1
    nyawa = nyawa_awal
    
    while langkah < jarak:
        if langkah == 1:
            print("MULAI", end="  ")
        elif langkah % 4 == 0:
            print("JEBAKAN", end="  ")
            nyawa -= 1
            if nyawa <= 0:
                print("GAGAL")
                return
        elif langkah % 6 == 0:
            print("NYAWA+", end="  ")
            nyawa += 1
        else:
            print(langkah, end="  ")

        langkah += lebar_langkah

    if langkah >= jarak:
        print("BERHASIL")









# Lukas adalah seorang anak yang suka berhitung. Suatu hari, ia penasaran dengan jumlah total dari bilangan genap yang ada dalam suatu rentang angka tertentu. Karena masih belajar pemrograman, Lukas ingin Anda membuatkan program yang dapat membantunya menghitung total dari semua bilangan genap dalam rentang yang diberikan.

 

# Fungsi dan Parameter
# Program harus mengimplementasikan sebuah fungsi bernama hitungTotalGenap yang menerima dua parameter. Tujuan dari fungsi ini adalah menghitung dan mengembalikan total dari semua bilangan genap dalam rentang angka yang diberikan.

 

# Perilaku Program
# Fungsi menerima dua bilangan bulat positif bilanganAwal dan bilanganAkhir, dengan syarat bilanganAwal ≤ bilanganAkhir.

# Program akan menjumlahkan semua bilangan genap dalam rentang dari bilangan Awal hingga bilanganAkhir (termasuk bilanganAwal dan bilanganAkhir jika genap).

# Jika tidak ada bilangan genap dalam rentang tersebut, maka fungsi mengembalikan 0.

 

# Penjelasan Parameter
# Fungsi menerima dua parameter:

# bilanganAwal = Bilangan bulat positif sebagai batas awal rentang. (1 ≤ bilanganAwal ≤ 1000)

# bilanganAkhir= Bilangan bulat positif sebagai batas akhir rentang. (A ≤ bilanganAkhir ≤ 1000)
    
# Test	Result
# print(hitungTotalGenap(20,50))
# 560
# print(hitungTotalGenap(20,10))
# 0

def hitungTotalGenap(bilanganAwal, bilanganAkhir):
    a = 0
    for i in range(bilanganAwal, bilanganAkhir + 1):
        if i % 2 == 0:
            a += i
    if bilanganAwal > bilanganAkhir:
        return 0
    return a

def hitungTotalGenap(bilanganAwal,bilanganAkhir):
    # cek apakah bilanganAwal lebih kecil sama dengan bilanganAkhir
    if bilanganAwal <= bilanganAkhir:
        hasil=0
        for i in range(bilanganAwal,bilanganAkhir+1):
            if i%2==0:
                hasil+=i
        return hasil
    else:
        return 0
    





# Deret GWS
# Di suatu pagi yang cerah di Sekolah Baktiojo, sang guru matematika memberikan sebuah tugas harian kepada murid-muridnya. Tugas harian tersebut adalah menuliskan deret kelipatan bilangan. Ikin merasa tugas tersebut terlalu mudah untuk dikerjakan secara manual, jadi dia membuat program untuk tugas tersebut, tetapi dengan tambahan fitur. Fitur yang dikembangkan Ikin adalah menggantikan bilangan kelipatan tertentu dengan kata tertentu.

# Ikin membuat sebuah fungsi bernama deret_gws. Fungsi tersebut menerima 7 parameter: jumlah_bilangan, kelipatan, angka_gws1, angka_gws2, kata_gws1, kata_gws2, kata_gws_spesial. Jumlah_bilangan adalah berapa banyak bilangan kelipatan yang mau ditampilkan. Kelipatan menentukan kelipatan deret bilangan yang ditampilkan. Parameter angka_gws1 dan angka_gws2, kata_gws1, kata_gws2, dan kata_spesial adalah parameter tambahan untuk fitur yang dikembangkan Ikin.

# Cara kerja deret bilangan yang dikembangkan oleh Ikin adalah menampilkan deret bilangan berkelipatan, dan menggantikan bilangan kelipatan tertentu dengan kata yang diberikan. Bilangan yang merupakan kelipatan angka_gws1 akan menampilkan kata_gws1, bilangan kelipatan angka_gws2 menampilkan kata_gws2, dan ketika bilangan adalah kelipatan angka_gws1 dan angka_gws2, program akan menampilkan kata_spesial. Semua hasil deret bilangan tersebut ditampilkan dalam 1 baris.

# Ketentuan Deret BIlangan GWS
# Ada dalam cerita diatas.

# Dan ada dalam penjelasan parameter di bawah.

# Penjelasan Parameter:
# Ada 7 parameter untuk fungsi ini. Parameter jumlah_bilangan, kelipatan, angka_gws1, dan angka_gws2  harus berupa bilangan bulat positif. Angka_gws1 dan angka_gws 2 harus bernilai lebih kecil atau sama dengan jumlah_bilangan. Kata_gws1, kata_gws2, dan kata_spesial harus berupa string. Apabila input parameter tidak memenuhi kriteria, maka fungsi harus menampilkan pesan "TIDAK VALID”. Nama parameter harus sesuai dengan ketentuan.

# Format : 
# jumlah_bilangan = Menentukan berapa banyak bilangan kelipatan yang mau ditampilkan

# kelipatan = Menentukan kelipatan deret bilangan

# angka_gws1 = Menentukan kapan hasil perkalian harus digantikan kata_gws1

# angka_gws2 = Menentukan kapan hasil perkalian harus digantikan kata_gws2

# kata_gws1 = Kata untuk menggantikan hasil perkalian yang habis dibagi angka_gws1 saja.

# kata_gws2 = Kata untuk menggantikan hasil perkalian yang habis dibagi angka_gws2 saja.

# kata_spesial = Kata untuk menggantikan hasil perkalian yang habis dibagi angka_gws1 dan angka_gws2


# Test	Result
# deret_gws(20,2,3,5,"halo","hai","bye")
# 2 4 halo 8 hai halo 14 16 halo hai 22 halo 26 28 bye 32 34 halo 38 hai 
# deret_gws(30,1,5,10,"DOR","BOOM","DUAR")
# 1 2 3 4 DOR 6 7 8 9 DUAR 11 12 13 14 DOR 16 17 18 19 DUAR 21 22 23 24 DOR 26 27 28 29 DUAR

def deret_gws(jumlah_bilangan, kelipatan, angka_gws1, angka_gws2, kata_gws1, kata_gws2, kata_gws_spesial):
    try:
        if jumlah_bilangan > 0 and kelipatan > 0 and angka_gws1 <= jumlah_bilangan and angka_gws2 <= jumlah_bilangan:
            for i in range(1,jumlah_bilangan +1):
                if i*kelipatan % angka_gws1 == 0 and i*kelipatan % angka_gws2 == 0:
                    print(kata_gws_spesial, end=" ")
                elif i*kelipatan % angka_gws1 == 0:
                    print(kata_gws1, end=" ")
                elif i*kelipatan % angka_gws2 ==0:
                    print(kata_gws2, end=" ")
                else:
                    print(i*kelipatan, end=" ")
        else:
            print("TIDAK VALID")
    except TypeError:
        print("TIDAK VALID")
    return 0
