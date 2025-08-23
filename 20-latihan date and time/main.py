# Date and time (latihan)

import datetime as dt

hari_ini = dt.date.today() # untuk ambil hari ini
tanggal = dt.date(2005, 5, 2) # untuk parse tanggal

print(f'hari_ini = {hari_ini}')
print(f'hari_ini = {hari_ini:%A}') # untuk ambil hari nya
print(f'tanggal = {tanggal}')

print(f'masukan tanggal, bulan, dan tahun')
tanggal = int(input('Tanggal\t: '))
bulan = int(input('Bulan\t: '))
tahun = int(input('Tahun\t: '))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f'tanggal_lahir = {tanggal_lahir}')
print(f'hari nya adalah = {tanggal_lahir:%A}') # untuk ambil hari nya
print(f'bulan nya adalah = {tanggal_lahir:%B}') # untuk ambil hari nya 

umur = (hari_ini - tanggal_lahir)
umur_value = umur.days // 365
umur_sisa = (umur.days % 365) // 30
print(f'umur saya adalah = {umur_value} tahun {umur_sisa} bulan')