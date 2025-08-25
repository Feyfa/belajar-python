import datetime
import os;

# template dict mahasiswa
mahasiswas = []

while True :
    os.system('clear')
    print(f'{'SELAMAT DATANG':^20}')
    print(f'{'DATA MAHASISWA':^20}')
    print("-" * 20)

    nama = input('Nama Mahasiswa : ')
    nim = input('NIM Mahasiswa : ')
    sks_lulus = input('SKS Lulus : ')
    tahun_lahir = int(input('Tahun Lahir (YYYY) : '))
    bulan_lahir = int(input('Bulan Lahir (1-12) : '))
    tanggal_lahir = int(input('Tanggal Lahir (1-31) : '))

    mahasiswa = {
        'nama': nama,
        'nim': nim,
        'sks_lulus': sks_lulus,
        'lahir': datetime.datetime(tahun_lahir, bulan_lahir, tanggal_lahir).strftime('%Y/%m/%d')
    }
    mahasiswas.append(mahasiswa)

    print(f'\n{'Nama':<20} {'NIM':<7} {'SKS Lulus':^15} {'Tanggal Lahir':<10}')
    print(f'{60*"-"}')

    for index,item in enumerate(mahasiswas) :
        print(f"{item['nama']:<20} {item['nim']:<7} {item['sks_lulus']:^15} {item['lahir']:<10}")

    isNext = input('\nMau tambah lagi bro (y/n)? ')
    if(isNext != 'y') :
        break
