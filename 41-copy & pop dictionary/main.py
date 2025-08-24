# copy dictionary

data_dict = {
    'jd': 'jidan', 
    'fy': 'feyfa',
    'fn': 'fena'
}
data_dic_copy = data_dict.copy()

print(f'data_dict = {data_dict}')
print(f'data_dic_copy = {data_dic_copy}')

data_dict['jd'] = 'Muhammad Jidan'

print(f'data_dict = {data_dict}')
print(f'data_dic_copy = {data_dic_copy}')

# pop dictionary, ini akan mengambil value dari key, dan item nya dihapus, return string
data_jidan = data_dic_copy.pop('jd')
print(f'data_jidan = {data_jidan}')
print(f'data_dic_copy = {data_dic_copy}')

# popitem dictionary, ini akan mengambil item terakhir, dan item nya dihapus, return tuple
data_terakhir = data_dic_copy.popitem()
print(f'data_terakhir = {data_terakhir}')
print(f'data_dic_copy = {data_dic_copy}')