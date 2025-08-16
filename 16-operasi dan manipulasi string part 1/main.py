# 1 menyambungkan string
nama = "Muhammad Jidan"
umur = "20"
message = "nama = " + nama + " umur = " + umur
print(message)

# 2 untuk menghitung panjang string
print(f'panjang message = {len(message)}')

# 3 operator untuk string

# mengecek apakah ada komponene char atau string di string
# mirip seperti LIKE '%na%' di mysql
char = "na"
exists = char in message
print(f'keyword exists in message = {exists}')

# mengecek apakah tidak ada komponene char atau string di string
char = "na"
exists = char not in message
print(f'keyword exists in message = {exists}')

# mengulang string sebanyak n
ulang = "jidan " * 5
print(ulang)

# indexing
print(f'index ke-0 : {message[0]}')
print(f'index ke-1 : {message[1]}')
print(f'index ke-2 : {message[2]}')
print(f'index ke--1 : {message[-1]}') # ini akan mengambil dari paling kanan
print(f'index ke--2 : {message[-2]}')
# print(f'index ke-31 : {message[31]}') # akan error jika lebih dari len - 1
print(f'ranger dari 0, 3, {message[0:10]}') # start dari 0, end sampai 10. namun yang kemabil dari 0-9
print(f'ranger dari 0, 3, lompat 2 karakter {message[0:10:2]}') # start dari, end sampai 10. namun yang keambil dari 0-9 dan ambil tiap 2 karakter sekali

# item paling kecil 
print(f'paling kecil : {min(message)}')
# item paling besar
print(f'paling besar : {max(message)}')

ascii_code = ord(' ')
print(f'ascii code untuk spasi = {ascii_code}')
ascii_code = ord('u')
print(f'ascii code untuk u = {ascii_code}')

# 4. operator dalam bentuk method
data = "apa itu python"
jumlah = data.count('o')
print(f'jumlah o pada data = {jumlah}')