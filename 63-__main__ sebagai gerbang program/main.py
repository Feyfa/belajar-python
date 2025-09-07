# __main__ adalah top level code environment

# __name__ == "__main__" akan terjadi jika ada di program utama

## __name__ pada file program utama
print(f"nilai __name__ pada main.py = '{__name__}'")

## __name__ pada file fungsi.py
import fungsi

## contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a:int, b:int) -> int :
    return (a + b)

# fungsi
if __name__ == '__main__' :
    print(f"1 + 1 = {fungsi_tambah(1,1)}")



## import package
import package