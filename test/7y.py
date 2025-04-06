# Pola Sakit Kepala
# Program "Pola Sakit Kepala" ini merupakan implementasi dari sebuah algoritma untuk mencetak pola angka spiral simetris yang bila dilihat menyerupai visualisasi denyut sakit kepala atau radiasi visual yang sering dialami penderita migren. Pola ini memiliki karakteristik khas berupa angka-angka yang membentuk semacam cerminan dari tengah ke luar, menghasilkan efek visual simetris seperti gelombang yang berpusat pada titik tengah (angka 1). Dinamakan "Pola Sakit Kepala" karena bentuknya yang memancar dari pusat menyerupai sensasi denyutan yang dirasakan oleh penderita sakit kepala parah, dimana angka-angka semakin besar saat menjauhi titik tengah, menciptakan ilusi optik yang memvisualisasikan sensasi sakit yang menyebar.

# Fungsi dengan nama pola_sakit_kepala() ini memiliki 2 parameter yaitu panjang dan lebar. Fungsi ini bertujuan untuk mencetak pola angka berbentuk spiral simetris yang memiliki titik terendah di tengah dan memancar keluar dengan nilai yang semakin besar, dengan syarat panjang dan lebar harus sama dan bernilai ganjil.

# Struktur Pola
# Pola yang dihasilkan berbentuk spiral simetris dengan angka terendah (1) di tengah

# Pola angka berulang setelah 9, kembali ke 0, 1, 2. Sederhananya jika angka 10 menjadi 0, 11 menjadi 1, …, 123 menjadi 3, …, 999 menjadi 9. (Diambil angka yang paling kiri jika angka itu berdigit lebih dari 1)

# Contoh: panjang = 7 dan lebar = 7



# Penjelasan Parameter:
# Fungsi memiliki 2 parameter yaitu panjang dan lebar, dipastikan selalu integer dan dibawah 9999.

# panjang = Tipe data Integer, adalah panjang dari pola

# lebar = Tipe data Integer, adalah lebar dari pola

# Validasi Input
# Nilai absolut dari parameter panjang dan lebar diambil, sehingga nilai negatif akan dikonversi menjadi positif

# Fungsi melakukan pengecekan apakah panjang dan lebar sama, jika tidak akan menampilkan pesan "Panjang dan lebar harus sama!!"

# Fungsi melakukan pengecekan apakah panjang dan lebar adalah bilangan ganjil, jika tidak akan menampilkan pesan "Panjang dan lebar harus bilangan ganjil!!"



# pola_sakit_kepala(7, 7)
# 7 6 5 4 5 6 7
# 6 5 4 3 4 5 6
# 5 4 3 2 3 4 5
# 4 3 2 1 2 3 4
# 5 4 3 2 3 4 5
# 6 5 4 3 4 5 6
# 7 6 5 4 5 6 7
# pola_sakit_kepala(4, 4)
# Panjang dan lebar harus bilangan ganjil!!
# pola_sakit_kepala(-4, 4)
# Panjang dan lebar harus bilangan ganjil!!
# pola_sakit_kepala(5, 7)
# Panjang dan lebar harus sama!!
# pola_sakit_kepala(5, -5)
# 5 4 3 4 5
# 4 3 2 3 4
# 3 2 1 2 3
# 4 3 2 3 4
# 5 4 3 4 5

def pola_sakit_kepala(panjang, lebar):
    panjang, lebar = abs(panjang), abs(lebar)
    if (panjang != lebar):
        print("Panjang dan lebar harus sama!!")
    elif (panjang % 2 == 0 and lebar % 2 == 0):
        print("Panjang dan lebar harus bilangan ganjil!!")
    else:
        for i in range(lebar // 2 + 1):
            for j in range(panjang, lebar // 2, -1):
                simpan = j - i
                while (simpan) > 9:
                    simpan %= 10
                print(simpan, end=" " if panjang != 1 else "")
            for j in range(panjang - (panjang // 2) + 1, panjang + 1):
                simpan = j - i
                while (simpan) > 9:
                    simpan %= 10
                print(simpan, end=" " if j != panjang else " ")
            print()

        for i in range(lebar // 2):
            for j in range(panjang - (panjang // 2) + 1, 1, -1):
                simpan = j + i
                while (simpan) > 9:
                    simpan %= 10
                print(simpan, end=" ")
            for j in range(3, (panjang // 2) + 3):
                simpan = j + i
                while (simpan) > 9:
                    simpan %= 10
                print(simpan, end=" " if j != (panjang // 2) + 2 else "")
            print()


def pola_sakit_kepala(panjang, lebar):
    panjang = abs(panjang)
    lebar = abs(lebar)
    tengah = panjang // 2
    angka = 1
    if panjang != lebar:
        print("Panjang dan lebar harus sama!!")
    
    elif panjang % 2 == 0 or lebar % 2 == 0:
        print("Panjang dan lebar harus bilangan ganjil!!")
        
    else:
        for i in range(panjang):
            for j in range(lebar):
                angka = abs(tengah - i) + abs(tengah - j) + 1
                angka = angka % 10
                if j != lebar - 1:
                    print(angka, end=" ")
                else:
                    print(angka)



# Di sebuah kota kecil, ada seorang guru bernama Pak Andi yang suka memberikan tantangan unik kepada murid-murid di kelasnya. Setiap minggu, dia memberikan tugas untuk menulis angka dalam pola tertentu di papan tulis.

# Pada minggu ini, pak Andi meminta murid-muridnya untuk menulis angka dalam bentuk ular dengan aturan sebagai berikut:

# Angka pertama selalu dimulai dari pojok kiri atas dan di-print sebagai “head”

# Pada baris pertama, angka-angka dituliskan secara berurutan dari kiri ke kanan hingga mencapai panjang yang ditentukan

# Pada baris kedua, angka berikutnya (yaitu angka setelah angka terakhir di baris pertama) dituliskan dari ujung kanan ke kiri

# Pada baris ketiga, angka berikutnya (yaitu angka setelah angka terakhir di baris kedua), kembali dilanjutkan dengan berurutan dari kiri ke kanan

# Pola ini terus berulang hingga mencapai jumlah baris yang ditentukan

# Angka paling terakhir selalu di-print sebagai “tail”

# Fungsi yang digunakan dalam soal ini bernama ularAngka dengan parameter (bawah, samping). Jika belum paham mengenai pola, dipersilahkan untuk melihat output dari test case yang ada.

# Penjelasan Parameter
# Fungsi ularAngka memiliki dua parameter dengan nama dan penjelasan sebagai berikut:

# bawah = jumlah baris dalam pola ular angka (bertipe data integer)

# samping = jumlah kolom dalam pola ular angka (bertipe data integer)

# Catatan Tambahan
# Input harus berupa bilangan bulat positif dan lebih besar dari 0

# Semua output angka ditampilkan dalam dua digit 

# Output menggunakan print, bukan return

# Separator antar output menggunakan dua whitespace (“  ”)

# Dipersilakan untuk membuat variabel tambahan jika memang diperlukan

# Baca soal dan contoh output dengan cermat sebelum bertanya kepada asisten


# ularAngka(3, 4)
# head  02  03  04  
# 08  07  06  05
# 09  10  11  tail
# ularAngka(2, 3)
# head  02  03  
# tail  05  04


def ularAngka(baris, samping):
    a = baris * samping
    if samping < 1 or baris < 1:
        print ("tidak terdefiniskan")
    sangka = 1
    for i in range(1, baris + 1):
        if i % 2 == 1:
            for j in range(1, samping + 1):
                if sangka == 1:
                    print("head", end="  ")
                elif sangka == a:
                    print("tail", end="  ")
                else:
                    if sangka < 10:
                        print(f"0{sangka}", end="  ")
                    elif sangka >= 10:
                        print(f"{sangka}", end="  ")
                sangka += 1
        else:
            sangka += samping - 1
            for j in range(samping):
                if sangka == a:
                    print("tail", end="  ")
                else:
                    if sangka < 10:
                        print(f"0{sangka}", end="  ")
                    elif sangka >= 10:
                        print(f"{sangka}", end="  ")
                sangka = sangka - 1
            sangka = sangka+ samping + 1
        print()


def ularAngka(bawah, samping):
    count = 1
    baris = 2
    tail = bawah * samping
    titip = 0

    for i in range(bawah):
        if baris % 2 == 0:
            for j in range(samping):        
                if count == 1:
                    print("head", end="  ")
                elif count == tail:
                    print("tail", end="  ")
                else:
                    if count < 10:
                        print(f"0{count}", end="  ")
                    else:
                        print(count, end='  ')
                count += 1
            baris += 1
            print()
        else:
            titip = count + samping - 1
            for j in range(samping):
                if titip == tail:
                    print("tail", end="  ")
                else:
                    if count < 10:
                        print(f"0{titip}", end="  ")
                    else:
                        print(titip, end='  ')
                titip -= 1
                count += 1
            baris += 1
            print()
