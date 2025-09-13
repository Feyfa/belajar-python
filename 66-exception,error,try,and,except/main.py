# exception akan terjadi saat program mengalami error saat runtime

# contoh sederhana untuk menangkap exception

from math import nan

## contoh sederhana
# input_user = int(input("masukan angka: "))
# hasil = 0

# try :
#     hasil = 10 / input_user
# except :
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")

## contoh di aplikasi 

# while True :
#     angka = int(input("masukan angka pembagi: "))
#     try :   
#         hasil = 10 / angka
#         print(f"hasil = {hasil}")
#         is_done = input("apakah mau lanjut (y/n): ")
#         if is_done != 'y' :
#             break
#     except :
#         print('pembagi nol, silahkan masukan input lagi')
# print('akhir dari program')

## contoh di aplikasi untuk membuat file data.txt

try :
    with open("data.txt",'r') as file :
        print(file.read())
except :
    print('file data.txt tidak ditemukan, membuat file baru')
    with open("data.txt",'w',encoding='utf-8') as file :
        file.write('file baru')
print('akhir dari program 2')
