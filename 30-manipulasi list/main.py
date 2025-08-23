# -----OPERASI-----

# index. 0(-3)    1(-2)    2(-1)
data = ['jidan', 'feyfa', 'fena']

# mengambil data dari list ini
data_0 = data[0]
print(f'data pertama (index 0) = {data_0}')

data_terakhir = data[-1]
print(f'data terakhir = {data_terakhir}')

data_feyfa = data[-2]
print(f'data feyfa = {data_feyfa}')

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f'panjang data list = {panjang_data}')

# -----OPERASI-----

# -----MANIPULASI LIST-----

print(f'data sebelum ditambah = {data}')

# menambahkan item pada list sesuai posisi
data.insert(1, 'Agies')
print(f'data sesudah ditambah = {data}')

# menambahkan list di akhir
data.append('kotak')
print(f'data sesudah ditambah = {data}')

# menambahkan list dengan list
data_baru = ['pascol', 'timothy']
data.extend(data_baru)
print(f'data sesudah ditambah = {data}')

# merubah data
data[1] = "ubah data";
print(f'data rubah = {data}')

# remove data
data.remove('kotak') # jika tidak ditemukan akan error
print(f'data remove = {data}')

# remove data paling belakang
data_akhir = data.pop()
print(f'data akhir = {data}')
print(f'data akhir = {data_akhir}')

# -----MANIPULASI LIST-----