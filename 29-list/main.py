# -----LIST-----

# kumpulan data numbers
data_angka = [1,5,2,3]
print(f'data_angka = {data_angka}')

# kumpulan data string
data_string = ['jidan', 'feyfa', 'ucup']
print(f'data_string = {data_string}')

# kumpulan data boolean
data_boolean = [True, False, True]
print(f'data_boolean = {data_boolean}')

# kumpulan campuran
data_campuran = [1, 'Jidan', 2, False]
print(f'data_campuran = {data_campuran}')

# -----LIST-----


# -----ALTERNATIF MEMBUAT LIST-----

# menggunakan range
data_range = range(0, 10, 2) # range(start, stop, step)
print(f'data_range = {data_range}')
data_list = list(data_range)
print(f'data_list = {data_list}')

# membuat list dengan for loop, list comprehensife
data_list_with_for = [i**2 for i in range(1,11)]
print(f'data_list_with_for = {data_list_with_for}')
data_list_with_for = ["genap" if i % 2 == 0 else "ganjil" for i in range(1,11)]
print(f'data_list_with_for = {data_list_with_for}')

# membuat list pake for pake if
data_list_with_if = [i for i in range(1, 11) if i % 2 == 0]
print(f'data_list_with_if = {data_list_with_if}')

# -----ALTERNATIF MEMBUAT LIST-----