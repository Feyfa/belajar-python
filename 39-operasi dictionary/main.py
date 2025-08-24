# operator dictionary

data_dict = {
    'jd': 'jidan',
    'fy': 'feyfa',
    'fn': 'fena'
}
print(data_dict)

# panjang dictionary
LENDICT = len(data_dict)
print(f'panjang dictionary : {LENDICT}')

# mengecek key exists atau tidak
KEY = 'jd'
KEYEXISTS = KEY in data_dict
print(f'apakah {KEY} ada di data_dict : {KEYEXISTS}')

# mengakses value (read) dengan get
print(data_dict['jd'])
print(data_dict.get('jd'))
print(data_dict.get('sss', 'key not found')) # None, jika key tidak ada hasilnya None dan tidak bikin error juga

# mengupdate data
data_dict['jd'] = 'JIDAN'
print(data_dict)
data_dict.update({'jd': 'Muhammad Jidan'})
print(data_dict)
data_dict.update({'jd123': 'Muhammad Jidan'}) # kalo key nya tidak ada maka akan membuat baru dengan key tersebut 
print(data_dict)

# delete data
del data_dict['jd123']
print(data_dict)