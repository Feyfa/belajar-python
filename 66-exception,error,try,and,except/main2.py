# contoh membuat exception

from numbers import Number

def tambah(a,b) :
    if not isinstance(a, Number) or not isinstance(b, Number) :
        raise ValueError("variable harus angka")
    return (a + b)

print(f'tambah = {tambah(5,6)}')

angka = 0
try :
    hasil = 10 / angka
except Exception as error :
    print(error)

try :
    hasil = 10 / angka
except ZeroDivisionError as error :
    print(error)

try :
    tambah(1,"a")
except Exception as error :
    print(error)