def inisial(daftar):
    hitung_inisial = {}  
    for nama in daftar:
        inisial = nama[0]  
        if inisial not in hitung_inisial:
            hitung_inisial[inisial] = 1
        else:
            hitung_inisial[inisial] += 1

        if hitung_inisial[inisial] == 1:
            print(nama)
        else:
            print(f"{nama}{hitung_inisial[inisial]}")


daftar = ("Michael","Viny","Aurelio","Michael",
"Felix","Kevin","Vincen","Vincen","Michael")
inisial(daftar)



def hitung(buku):
    catat={}
    a=len(buku)
    for i in buku:
        if i in catat:
            continue
        else:
            for j in buku:
                if j in catat:
                    catat[j]+=1
                else:
                    catat[j]=1
        
    for j in catat:
        b=catat[j]
        print(f"Buku dengan judul {j} sejumlah {b} buku")
    print(f"Total buku di dalam lemari adalah : {a} buku")

buku = (
    "Renungan Harian","Matematika","Sains","Jaringan","Pemrograman",
    "Renungan Harian","Sains","Jaringan","Majalah Perjodohan"
    )
hitung(buku)

