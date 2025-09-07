## Tutorial membaca file external

print(3*"=", "Membaca File txt", 3*"=")
file = open("data.txt",mode='r')

print(f"status read = {file.readable()}")
print(f"status write = {file.writable()}")

## baca semua isi file
# print(file.read()) 

## baca per baris
# print(file.readline(),end="") # baca baris pertama
# print(file.readline(),end="") # baca baris kedua
# print(file.readline(),end="") # baca baris ketiga

## baca semua baris sebagai list
# print(file.readlines())

print(f"apakah fle sudah di close = {file.closed}")
file.close()
print(f"apakah fle sudah di close = {file.closed}")

## salah satu teknik membuka file di python
print(3*"=", "Membaca File txt with", 3*"=")

# kalo pakai with saat sudah selesai otomatis bakal di close connection file nya
with open("data.txt",mode="r") as file :
    content = file.readline()
    print(content,end="")

print(f"apakah fle sudah di close = {file.closed}")
