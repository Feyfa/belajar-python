import datetime

data_waktu = datetime.datetime.now()
print(f'datetime now : {data_waktu}')
print(f'tanggal : {data_waktu.strftime('%A')}')
print(f'tanggal : {data_waktu.day}')
print(f'bulan : {data_waktu.month}')
print(f'tahun : {data_waktu.year}')

from collections import Counter

data = ['a','b','c','b','c','c']
data_count = Counter(data)

print(f'data_counter = {data_count}')
print(f'jumlah a = {data_count.get('a')}')
print(f'jumlah b = {data_count.get('b')}')
print(f'jumlah c = {data_count.get('c')}')

import io

file = io.open("file_text.txt", "r")
print(file.read())