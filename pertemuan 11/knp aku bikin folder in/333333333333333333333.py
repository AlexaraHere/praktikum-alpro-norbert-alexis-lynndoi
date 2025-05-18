nama_file = input("Masukkan nama file: ")

try:
    file = open(nama_file)
except:
    print("File tidak bisa dibuka:", nama_file)
    exit()
jumlah_kata = {}

for baris in file:
    kata_kata = baris.split()
    for kata in kata_kata:
        if kata in jumlah_kata:
            jumlah_kata[kata] += 1 
        else:
            jumlah_kata[kata] = 1
print("\nJumlah kata dalam file:")
for kata, jumlah in jumlah_kata.items():
    print(f"{kata}: {jumlah}")