nilai_siswa = {
    'Aldi': 85,
    'Budi': 70,
    'Citra': 95,
    'Dewi': 60,
    'Eka': 78
}
nilai_tertinggi = max(nilai_siswa.values())
print("Nilai tertinggi adalah:", nilai_tertinggi)
for nama in nilai_siswa:
    if nilai_siswa[nama] == nilai_tertinggi:
        print("Didapat oleh:", nama)