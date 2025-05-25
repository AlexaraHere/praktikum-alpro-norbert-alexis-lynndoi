def data_diri(wa):
    list1 = []
    for i in str(wa[0]).split():
        list1.append(i)
    list1.reverse()
    nama = wa[0]
    nim = wa[1]
    alamat = wa[2]
    print(f"NIM: {nim}")
    print(f"NAMA: {nama}")
    print(f"ALAMAT: {alamat}")
    nama_depan = tuple(nama.split()[0].lower())
    nim = tuple(nim)
    print(f"NIM: {nim}")
    print(f"NAMA DEPAN: {nama_depan}")
    print(f"NAMA TERBALIK: {list1}")
data_diri(("norbert alexis lynndoi", "71241082", "sempu, sleman"))