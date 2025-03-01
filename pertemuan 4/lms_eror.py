print("milih boyyy")
jenis = str(input("mau mobil apa motor? "))
waktu = int(input("berapa lama? "))
print("Lama Parkir = ", waktu, "jam")
nambah=0
gabutyee=0
if jenis == "motor":
    if waktu == 1:
        bentardoang=2000
        print("Biaya Parkir = Rp", bentardoang)
    elif waktu >= 2:
        gabutyee = (waktu-1)*1000+2000
        print("Biaya Parkir =  Rp", gabutyee)
    elif waktu >= 14:
        print("mbayar Rp.15000")

elif jenis == "mobil":
    if waktu == 1:
        bentardoang=5000
        print("Biaya Parkir = Rp", bentardoang)
    elif waktu >= 2:
            gabutyee = (waktu-1)*3000+5000
            print("Biaya Parkir =  Rp", gabutyee)
            if waktu > 24:
                nambah = int(nambah)
                nambah = ((waktu-1)*3000+5000)*0,5
                gabutyee = gabutyee + nambah
                print (gabutyee)
    elif waktu >= 21:
        print("mbayar Rp.65000")

