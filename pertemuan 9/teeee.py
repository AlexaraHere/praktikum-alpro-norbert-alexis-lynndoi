f = open("output.txt")
filename = input("\nMasukkan nama buku yang ingin dicari: ")
a = False
for line in f:
    nama_buku = line.split(",")[0]
    print(f"- {nama_buku}")

    """"""
if not a:
    print("done")