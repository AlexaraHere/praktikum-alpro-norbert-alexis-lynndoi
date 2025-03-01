# umur = input("umur anda? ")
# try:
#     umur = int(umur)
#     if umur <= 18:
#         print("muda")
#     elif umur >= 19: 
#         print("tua")
# except Exception as e:
#     print(e)

#======================================#

umur = input("umur anda? ")
try:
    umur = int(umur)
    if umur <= 18:
        print("muda")
    elif umur >= 19: 
        print("tua")
except:
    print ("masukin angka dongg, jangan yang lain")