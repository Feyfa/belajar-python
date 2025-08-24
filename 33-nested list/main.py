data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f'data_list_biasa = {data_list_biasa}')

list_2d = [data_0, data_1, data_list_biasa, 10, 11]
print(f'data_2d = {list_2d}')

# contoh penggunaan

peserta_0 = ['jidan', 20, 'laki-laki']
peserta_1 = ['feyfa', 20, 'perempuan']
peserta_2 = ['fena', 20, 'perempuan']

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f'list_peserta = {list_peserta}')

for peserta in list_peserta : 
    print(f'\nnama  : {peserta[0]}')
    print(f'umur  : {peserta[1]}')
    print(f'gender : {peserta[2]}')

list_peserta_copy = list_peserta.copy() # ini hanya mencopy di luar saja. karena list dari peserta_0, peserta_1, peserta_2 itu tidak di copy. makanya ketika peserta_0 dirubah. list_peserta_copy juga berubah
print(f'\nlist_peserta_copy = {list_peserta_copy}')
peserta_0[0] = 'Muhammad Jidan'
print(f'\nlist_peserta_copy = {list_peserta_copy}')
print(f'\nlist_peserta = {list_peserta}')




