# **kwargs

def fungsi(nama, tinggi, berat) :
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')

fungsi('Elon Musk', 188, 85)

def fungsi(**kwargs) :
    # tipe datanya adalah dictionary
    nama = kwargs.get('nama')
    tinggi = kwargs.get('tinggi')
    berat = kwargs.get('berat')
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')

fungsi(nama='Elon Musk', tinggi=188, berat=85)

# posisinya harus args, baru kwargs tidak boleh dibalik
def math(*args, **kwargs) :
    if(kwargs.get('option') == 'tambah') :
        result = sum(args)
        print(f'hasil perjumlahan = {result}')
    elif (kwargs.get('option') == 'kali') :
        result = 1
        for i in args :
            result *= i
        print(f'hasil perkalian {result}')
    else :
        print('tidak ada operasi')

math(1,2,3,4,5,option="tambah")
math(1,2,3,4,5,option="kali")
math(1,2,3,4,5,option="abc")