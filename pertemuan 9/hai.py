# """Input buku"""

# judulDiCari = input("masukkan judul buku yang dicaari : ")
# state = False
# with open("file.txt") as file :
#     for line in file:
#         linetemp = line.split(',')
#         if linetemp[0].lower()== judulDiCari.lower():
#             print(f"""
# BUKU ditemukan 
# Nama : {linetemp[0].strip()}
# Kode : {linetemp[1].strip()}
# Tahun : {linetemp[2].strip()}
# Deskripsi : {linetemp[3].strip()}""")
#             state = True
#             break
# if not state:
#     print("Judul buku tidak ditemukan")


def compare(file1, file2):
    with open(file1, "r") as file:
        lines1 = file.readlines()
    
    with open(file2, "r") as file:
        lines2 = file.readlines()
    
    maxlen = max(len(lines1), len(lines2))
    hasil = []
    total_beda = 0

    for i in range(maxlen):
        if i < len(lines1):
            line1 = lines1[i].strip()
        else:
            line1 = ""

        if i < len(lines2):
            line2 = lines2[i].strip()
        else:
            line2 = ""
        
        if line1 != line2:
            total_beda += 1
            # Output detail
            hasil.append(f"Beda pada baris ke-{i+1}:")
            hasil.append(f"  file1: {line1}")
            hasil.append(f"  file2: {line2}")

    hasil.append(f"Total beda: {total_beda}")

    # Tulis ke hasil.txt
    with open("BedaBaris/hasil.txt", "w") as output:
        for item in hasil:
            output.write(item + "\n")

    # Cetak ke layar juga (optional)
    for item in hasil:
        print(item)

# Pemanggilan fungsi
compare('output.txt', 'mbox-short.txt')






# '''
# Diberikan file teks artikel.txt.
# Hitung:
# Jumlah karakter (termasuk spasi),
# Jumlah kata,
# Cetak hasilnya di JumlahKata.txt.
# '''

# def hitung_artikel():
#     with open("Artikel/artikel.txt","r") as file:
#         files = file.read()
#         kata = len(files.split())
#         karakter = len([i for i in files])
#         print(f"Karakter: {karakter}")
#         print(f"Kata: {kata}")
#         file.close()

# hitung_artikel() 
# # output (didalam file JumlahKata.txt):
# # Karakter: 409
# # Kata: 54
