import datetime

mahasiswa1 = {
    'nama': 'Muhammad Jidan',
    'nim': '098672112',
    'sks_lulus': 130,
    'beasiswa': True,
    'lahir': datetime.datetime(2005, 2, 5).strftime('/%Y/%m/%d')
}

mahasiswa2 = {
    'nama': 'Rafeyfa Zulfiyani',
    'nim': '098672113',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(2004, 3, 6).strftime('/%Y/%m/%d')
}

mahasiswa3 = {
    'nama': 'Rafena',
    'nim': '098672114',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(2003, 4, 7).strftime('/%Y/%m/%d')
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3,
}

print(f'{'KEY':<6} {'Nama':<20} {'SKS':<5} {'Beasiswa':<9} {'Lahir':<10}')
print(60*"-")

for mahasiswa in data_mahasiswa :
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir']

    print(f'{KEY:<6} {NAMA:<20} {SKS:<5} {BEASISWA:<9} {LAHIR:<10}')