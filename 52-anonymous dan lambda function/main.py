# lambda function

def functionKuadrat(angka) :
    return (angka ** 2)

print(functionKuadrat(5))

# kita coba lamda function
# lambda itu akan selalu mengembalikan/mereturn sesuatu
# output = lambda argument: expresion
lambdaKuadrat = lambda angka: (angka ** 2)
print(lambdaKuadrat(5))

lambdaPangkat = lambda num,pow : (num ** pow)
print(lambdaPangkat(2,4))

# kegunaan nya untuk apa bang

# sorting untuk list biasa
data_list = ['Muhammad Jidan', 'Rafeyfa Zulfiyani', 'Sayang Akuu']
data_list.sort()
print(f'\ndata_list = {data_list}')

# sorting dia pakai panjang
def panjang_nama(nama) :
    return len(nama)
data_list.sort(key=panjang_nama)
print(f'sorted list by panjang asc  = {data_list}')
data_list.sort(key=panjang_nama, reverse=True)
print(f'sorted list by panjang desc = {data_list}')

# sorting pakai lambda
data_list = ['Muhammad Jidan', 'Rafeyfa Zulfiyani', 'Sayang Akuu']

data_list.sort(key=lambda nama: len(nama))
print(f'sorted list by panjang asc  = {data_list}')
data_list.sort(key=lambda nama: len(nama), reverse=True)
print(f'sorted list by panjang desc = {data_list}\n')

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka) :
    return angka < 5;
data_angka_baru = list(filter(kurang_dari_lima, data_angka))
print(data_angka_baru)

data_angka_baru = list(filter(lambda x: x < 5, data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x: x % 2 == 0, data_angka))
print(data_genap) 

# kasus ganjil
data_ganjil = list(filter(lambda x: x % 2 != 0, data_angka))
print(f'{data_ganjil}\n') 

# anonymous function
# curry <- Haskel Curry

def pangkat(angka, pow) :
    hasil = (angka ** pow)
    return hasil
data_hasil = pangkat(5,2)
print(data_hasil)

# dengan currying menjadi
def pangkat(n) :
    return lambda angka: (angka ** n)
pangkat2 = pangkat(2)
print(f'pangkat 2 = {pangkat2(5)}')
pangkat3 = pangkat(3)
print(f'pangkat 3 = {pangkat3(5)}')
print(f'10 pangkat 2 = {pangkat(2)(10)}')


