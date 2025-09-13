import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

# print(list_a ** 2) # ini tidak bisa dilakukan
print(f'list_a = {list_a}')
print(f'vector_a = {vector_a}')
print(f'vector_a pangkaat 2 = {vector_a ** 2}')

matrix_b = np.array([(1,2),(3,4)])
print(f'matrix_b = {matrix_b}')
print(f'matrix_b pangkat 2 = {matrix_b ** 2}')

zeros_c = np.zeros((2,2))
print(f'zeros_c = {zeros_c}')

ones_d = np.ones((2,2))
print(f'ones_d = {ones_d}')

matrix_1 = np.array([(1,2),(3,4)])
matrix_2 = np.array([(5,6),(7,8)])
print(f'penjumlahan matrix 1 dan 2 adalah = {matrix_1 + matrix_2}')