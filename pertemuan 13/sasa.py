def kata_unik_spesial(kalimat1, kalimat2):
    kata1 = set(kalimat1.split())
    print(kata1)
    kata2 = set(kalimat2.split())
    print(kata2)
    hasil = set()
    for kata in kata1 & kata2:
        hasil.add(kata + kata)
    for kata in kata1 - kata2:
        hasil.add(kata)
    for kata in kata2 - kata1:
        hasil.add(kata)
    return hasil

hasil = kata_unik_spesial('saya mau makan', 'saya mau mandi')
print(len(hasil))
print(sorted(hasil))