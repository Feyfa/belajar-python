# list menggunakan []
data_list = [1,2,3,4,5]
print(f'data_list = {data_list}')

# tuples menggunakan (), elemen nya constant tidak dapat dirubah, namun masih bisa ambil elemen dari index nya
data_tuples = (5,4,3,2,1)
print(f'data_tuples = {data_tuples}')
print(f'data_tuples_1 = {data_tuples[1]}')

# tuples tidak bisa melakukan ini
# data_tuples[1] = 1
# data_tuples.append(1)

# sets (himpunan), elemen nya constant tidak dapat dirubah, dan tidak bisa ambil elemen dari index nya
data_sets = {1,2,3,4,5}
print(f'data_sets = {data_sets}')

# sets tidak bisa melakukan ini
# print(f'data_sets_0 = {data_sets[0]}')
# data_sets[0] = 1