nama = "jidan"

def pangkat(angkaValue, pangkatValue) :
    return angkaValue ** pangkatValue

print(pangkat(2,2))
print(pangkat(3,3))
print(pangkat(4,4))

# fungsi dengan return banyak

def operasi_matematika(angka1, angka2) :
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah,kurang,kali,bagi


a,b,c,d = operasi_matematika(10, 2)
print(f'hasil tambah = {a}')
print(f'hasil kurang = {b}')
print(f'hasil kali   = {c}')
print(f'hasil bagi   = {d}')