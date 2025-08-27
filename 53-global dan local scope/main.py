## Global dan local scope

nama_global = "jidan" # <- ini variable global

# akses variable global dalam fungsi
def fungsi1() :
    print(f'fungsi menampilkan {nama_global}')

fungsi1()

# akses variable global dalam looping
for i in range(0,5) :
    print(f'loop ke-{i} {nama_global}')

# percabangan
if (True) :
    print(f'if menampilkan {nama_global}')

## Variable Local Scope

def fungsi2() :
    nama_local = "Muhammad Jidan" # <- variable local scope

fungsi2()
# print(nama_local) # ini tidak bisa dilakukan

## Contoh 1: penggunaan akses variable
def say_hello() :
    print(f'fungsi say hello {nama}')

nama = "Jedun" # ini tidak error karena nama dibuat duluan sebelum say_hello() dijalankan
say_hello()

## Contoh 2: merubah variable global
angka = 0
nama = 'dimas'

def ubah(angka_baru, nama_baru) :
    # angka = nilai_baru # <- variable ini tidak berefek ke global angka, karena sifatnya local
    global angka # digunakan untuk mengakses variable angka dari luar fungsi
    global nama
    angka = angka_baru
    nama = nama_baru

print(f'sebelum diubah {angka, nama}')
ubah(10, 'budi')
print(f'setelah diubah {angka, nama}')

## contoh # for dan if bisa langsung merubah variable global tanpa harus menggunakan keyword global
angka = 0

for i in range(0,5) :
    angka += i
    angka_dummy = 0

if (True) :
    nama_dummy = "abcdefg"

print(angka)
print(angka_dummy)
print(nama_dummy)