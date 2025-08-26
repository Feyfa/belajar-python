# kegunaan *args
def fungsi(*datas) :
    # tipe datanya adalah tuple
    for data in datas :
        print(data)

fungsi('satu', 'dua', 'tiga')
fungsi(1,2,3,4,5,6,7,8,9,10)