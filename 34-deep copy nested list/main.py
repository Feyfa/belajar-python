data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0, data_1, 10]
data_2d_copy = data_2d.copy()

print(f'data_2d = {data_2d}')
print(f'data_2d_copy = {data_2d_copy}')

# mengambil data dari nested list

data = data_2d[0][0]
print(f'data = {data}\n')

# address semuanya

print(f'address asli = {hex(id(data_2d))}')
print(f'address copy = {hex(id(data_2d_copy))}\n')

print(f'address dari member ke-1')
print(f'address asli = {hex(id(data_2d[0]))}')
print(f'address copy = {hex(id(data_2d_copy[0]))}\n')

data_2d[1][0] = 11
data_2d[2] = 123
print(f'data_2d = {data_2d}')
print(f'data_2d_copy = {data_2d_copy}\n')

# kita menggunakan deepcopy

from copy import deepcopy

data_2d = [data_0, data_1, 10]
data_2d_deepcopy = deepcopy(data_2d)

print(f'address asli = {hex(id(data_2d))}')
print(f'address copy = {hex(id(data_2d_deepcopy))}\n')

print(f'address dari member ke-1')
print(f'address asli = {hex(id(data_2d[0]))}')
print(f'address copy = {hex(id(data_2d_deepcopy[0]))}\n')

data_2d[1][0] = 9999

print(f'data_2d = {data_2d}')
print(f'data_2d_copy = {data_2d_copy}')
print(f'data_2d_deepcopy = {data_2d_deepcopy}')

