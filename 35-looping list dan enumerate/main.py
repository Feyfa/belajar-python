# looping dari list

# for loop
print('---pakai for loop---')
kumpulan_angka = [4,3,5,4,6,7,9]

for angka in kumpulan_angka :
    print(f'angka = {angka}')

peserta = ['jidan', 'feyfa', 'fena', 'gojo', 'geto']

for nama in peserta :
    print(f'nama = {nama}')

# for loop dan range
print('\n---pakai for loop dan range---')
kumpulan_angka = [10,11,12,13,14,15]
panjang = len(kumpulan_angka)

for i in range(panjang) :
    print(f'angka = {kumpulan_angka[i]}')

# while
print('\n---while loop---')
kumpulan_angka = [10,11,12,13,14,15]
panjang = len(kumpulan_angka)
i = 0

while (i < panjang) :
    print(f'angka = {kumpulan_angka[i]}')
    i += 1

# list comprehension
print('\n---list comprehension---')
data = ['jidan', 'feyfa', 'fena', 1, 2, 3]

[print(f'data = {i}') for i in data]

angka = [1,2,3,4,5]
angka_kuadrat = [i**2 for i in angka]
print(f'angka_kuadrat = {angka_kuadrat}')

# enumerate
print('\n---enumerate---')
data_list = ['jidan', 'feyfa', 'fena', 1, 2, 3]

for index,data in enumerate(data_list) :
    print(f'index = {index} , data = {data}')
