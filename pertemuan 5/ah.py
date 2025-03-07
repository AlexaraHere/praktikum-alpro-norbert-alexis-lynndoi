# def tetot(angka1, angka2):
#     if angka1 - angka2 == 0:
#         return "wow"
#     else:
#         return "jelek"


# print(tetot(angka2=10, angka1=10))

# def is_kabisat(tahun):
#     if tahun % 4 == 0 and tahun % 100 != 0:
#         return True
#     elif tahun % 400 == 0:
#         return True
#     else:
#         return False



# def konversi_waktu(jam,menit,format_24 = True):
#     if format_24 == False:
#         if jam == 0:
#             jam = jam + 12
#             if menit < 10:
#                 return f"{jam}:0{menit} AM"
#             else:
#                 return f"{jam}:{menit} AM"
#         elif jam < 12:
#             if menit < 10:
#                 return f"{jam}:0{menit} AM"
#             else:
#                 return f"{jam}:{menit} AM"
#         elif jam == 12:
#             if menit < 10:
#                 return f"{jam}:0{menit} PM"
#             else:
#                 return f"{jam}:{menit} PM"
#         else:
#             if menit < 10:
#                 jam = jam - 12
#                 return f"{jam}:0{menit} PM"
#             else:
#                 jam = jam - 12
#                 return f"{jam}:{menit} PM"
#     elif format_24 == True:
#         if jam < 10:
#             if menit < 10:
#                 return f"0{jam}:0{menit}"
#             else:
#                 return f"0{jam}:{menit}"
#         else:
#             if menit < 10:
#                 return f"{jam}:0{menit}"
#             else:
#                 return f"{jam}:{menit}"


# def konversi_waktu(jam, menit, format_24=True):
#     if format_24:  
#         if jam == 12:  
#             jam_24 = 0  
#         else:
#             jam_24 = jam
#         return f"{jam_24:02}:{menit:02}"
    
#     else:  
#         periode = "AM"
#         if jam >= 12:
#             periode = "PM"
#             if jam > 12:
#                 jam -= 12
#         elif jam == 0:
#             jam = 12
#         return f"{jam}:{menit:02} {periode}"

# print(konversi_waktu(14, 30, format_24=False))

# print(konversi_waktu(2, 30, format_24=True))

# print(konversi_waktu(12, 15, format_24=False))

# print(konversi_waktu(0, 45, format_24=False))

# print(konversi_waktu(13, 25, format_24=True))

# print(konversi_waktu(9, 25, format_24=True))

# print(konversi_waktu(19, 25, format_24=False))

# print(konversi_waktu(23, 9, format_24=False))