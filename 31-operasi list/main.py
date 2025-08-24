data_angka = [1,2,3,2,5,6,7,8,4,3,2]

print(f'data_angka = {data_angka}')

# count data

jumlah_data_2 = data_angka.count(2)
jumlah_data_3 = data_angka.count(3)

print(f'jumlah_data_2 = {jumlah_data_2}')
print(f'jumlah_data_3 = {jumlah_data_3}')

# ambil posisi data data (index)

data = ['jidan', 'feyfa', 'fena']

print(f'data = {data}')

index_jidan = data.index('jidan') # jika tidak ada maka akan error
index_feyfa = data.index('feyfa')
index_fena = data.index('fena') 

print(f'posisi jidan adalah = {index_jidan}')
print(f'posisi feyfa adalah = {index_feyfa}')
print(f'posisi fena adalah = {index_fena}')

# mengurutkan list
print(f'data angka sebelum di sort = {data_angka}')
data_angka.sort()
print(f'data angka setelah di sort = {data_angka}')

print(f'data = {data}')
data.sort()
print(f'data sort = {data}')

# balik list nya
data_angka.reverse()
data.reverse()

print(f'data_angka reverse = {data_angka}')
print(f'data reverse = {data}')