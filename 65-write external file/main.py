## 1. mode write

# dia akan membuat file baru jika tidak ada
# lalu akan menimpa atau overwrite isinya

with open("data_1.txt",mode="w",encoding="utf-8") as file :
    file.write("Muhammad Jidan")

with open("data_1.txt",mode="w",encoding="utf-8") as file :
    file.write("Rafeyfa Zulfiyani")

## 2. mode append

with open("data_2.txt",mode="a",encoding="utf-8") as file :
    file.write("Muhammad Jidan\n")
with open("data_2.txt",mode="a",encoding="utf-8") as file :
    file.write("Rafeyfa Zulfiyani\n")

## 3. mode r+

with open("data_3.txt",mode="w",encoding="utf-8") as file : 
    file.write("data ke-3\n")
with open("data_3.txt",mode="r+",encoding="utf-8") as file : 
    file.write("baris-1\n")
    file.write("baris-2\n")
with open("data_3.txt",mode="r+",encoding="utf-8") as file : 
    data = file.read()
    print(data)
with open("data_3.txt",mode="r+",encoding="utf-8") as file : 
    file.write("well") # menimpa isi text sesuai dengan panjang data
