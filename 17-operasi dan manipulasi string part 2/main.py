# -------merubah case dari string-------

# merubah semua ke upper case
salam = "Hallo";
print(f'normal = {salam}')
print(f'upper  = {salam.upper()}')

# merubah semua ke lower case
sapa = "Halo Abang Abang"
print(f'normal = {sapa}')
print(f'lower  = {sapa.lower()}')

# -------merubah case dari string-------


# -------pengecekan dengan isX method-------

# pengecekan apakah character lower case semua
salam = "test"
print(f'salam = {salam.islower()}')

# pengecekan apakah character upper case semua
salam = "TEST"
print(f'salam = {salam.isupper()}')

# untuk mengecek semuanya huruf, jika terdapat yang bukan huruf maka akan False
salam = "jidan"
print(f'salam = {salam.isalpha()}')
salam = "jidan123"
print(f'salam = {salam.isalpha()}')

# untuk mengecek huruf dan angka, hanya huruf true, hanya angka true. selain 2 itu akan false
salam = "jidan123"
print(f'salam = {salam.isalnum()}')
salam = "1234"
print(f'salam = {salam.isalnum()}')

# untuk mengecek angka saja, selain itu akan false
salam = "123456"
print(f'salam = {salam.isdecimal()}')
salam = "www123"
print(f'salam = {salam.isdecimal()}')

# untuk mengecek apakah hanya spasi, tab, newline \n, jika string kosong false
salam = ""
print(f'salam = {salam.isspace()}')
salam = "   "
print(f'salam = {salam.isspace()}')
salam = "   123"
print(f'salam = {salam.isspace()}')

# untuk mengecek semua kata dimulai dengan huruf kapital
salam = "Mc Laren Lu Warna Apa Bos"
print(f'salam = {salam.istitle()}')

# -------pengecekan dengan isX method-------

# -------pengecekan komponen startsWith() endsWith()-------

# untuk mengecek apakah start dari kalimat nya sama atau tidak
message = "success delete data"
print(f'cek success = {message.startswith('success')}')

# untuk mengecek apakah ends dari kalimat nya sama atau tidak
message = "success create data"
print(f'cek success = {message.endswith('create data')}')

# -------pengecekan komponen startsWith() endsWith()-------

# -------penggabungan komponen split() -> explode() di php, join() -> implode() di php-------
namaBuah = "apel,pisang,orange"
print(f'split = {namaBuah.split()}')

namaBuah = ['apel', 'pisang', 'orange']
delimiter = " | ";
print(f'join = {delimiter.join(namaBuah)}')
# -------penggabungan komponen split() -> explode() di php, join() -> implode() di php-------

# -------alokasi karakter rjust(), ljust(), center()-------

# rjust() membuat rata kanan, 20 itu space atau width nya
kanan = "kanan".rjust(20)
print(f"kanan  = '{kanan}'")
 
# ljust() membuat rata kiri, 20 itu space atau width nya
kiri = "kiri".ljust(20, '.')
print(f"kiri   = '{kiri}'")

# center() membuat rata tengah, 20 itu space atau width nya
center = "center".center(20,'.')
print(f"center = '{center}'")

# strip() untuk menghapus semua character, jika match
strip = "____nama____"
print(f'strip = {strip.strip('_')}')

# -------alokasi karakter rjust(), ljust(), center()-------
