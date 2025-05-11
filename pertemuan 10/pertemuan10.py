def bilangan_terbaik(bilangan):
    bil = sorted(bilangan, reverse=True)
    bil = bil[:3]
    print(bil)
        
def done():
    hasil = []
    while True:
        bil = input("Masukkan Angka (ketik 'done' untuk berhenti): ").strip().lower()
        if bil == "done":
            break
        try:
            angka = float(bil)
            hasil.append(angka)
            rata_rata = sum(hasil) / len(hasil)
            print(f"Rata-ratanya sekarang: {rata_rata:.2f}")
        except ValueError:
            print("Input tidak valid. Masukkan angka atau 'done'.")
done()


def unik():
    file_path = "LatihanMandiri 10\\berita.txt"
    with open(file_path, 'r') as file:
        isi_teks = file.read()
    unik = []
    sekali = []

    isi_teks = isi_teks.lower()
    daftar_kata = isi_teks.split()

    for kata in set(daftar_kata):
        if daftar_kata.count(kata) > 1:
            unik.append(kata)
        else:
            sekali.append(kata)

    if unik:
        print("Kata lebih dari 1:")
        print(unik)
    if sekali:
        print("Kata muncul 1x:")
        print(sekali)
unik()

