# looping dictionary

data_dic = {
    'jd': 'jidan',
    'fy': 'feyfa',
    'fn': 'fena',
    'pp': 'pepeng'
}

# looping first try (data itu adalah key)
for data in data_dic :
    print(data)

# operator untuk mengambil key
keys = data_dic.keys()
print(keys)

for key in data_dic.keys() :
    print(f'{key} = {data_dic.get(key)}')

# operator untuk mengambil values
values = data_dic.values()
print(values)

for value in data_dic.values() :
    print(value)

# operator untuk mengambil items, hasilnya tuples
items = data_dic.items()
print(items)

for item in data_dic.items() :
    print(item)

for key,value in data_dic.items() :
    print(f'{key} = {value}')