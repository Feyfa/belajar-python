# inti dari tutorialnya adalan f'test = {value:format}'
# contoh format
# :d → integer (decimal)
# :x → integer dalam hexadecimal (huruf kecil)
# :X → integer dalam hexadecimal (huruf besar)
# :b → integer dalam binary
# :o → integer dalam octal
# :f → float dengan format fixed-point
# :.2f → float dengan 2 angka di belakang koma

# boolean
boolean = False
print(f'boolean = {boolean}')

# angka
angka = 2005.5
print(f'angka = {angka}')

# bilangan bulat
bilangan_bulat = 20
print(f'bilangan_bulat = {bilangan_bulat}')

# bilangan ribuan
bilangan_ribuan = 2000000
print(f'bilangan_ribuan = {bilangan_ribuan:,}') # format ribuan

# bilangan desimal
bilangan_decimal = 2005.51234567
print(f'bilangan_decimal = {bilangan_decimal:.1f}') # ambil 1 decimal saja
print(f'bilangan_decimal = {bilangan_decimal:.2f}') # ambil 2 decimal saja
print(f'bilangan_decimal = {bilangan_decimal:.3f}') # ambil 3 decimal saja

# menampilkan leading zero
leading_zero = 2005.12345
print(f'leading_zero = {leading_zero:010.3f}') # memaximalkan panjang nya jadi 10 karakter. nah karakter yang kosong akan pakai 0

# untuk menampilkan tanda + dan -
bilangan_positif = 10
bilangan_decimal_positif = 10.12345
bilangan_negatif = -10

print(f'bilangan_positif = {bilangan_positif:+d}')
print(f'bilangan_decimal_positif = {bilangan_decimal_positif:+.2f}')
print(f'bilangan_negatif = {bilangan_negatif}')

# memformat persen
persentase = 0.045
print(f'persentase = {persentase:.2%}')

# di dalam kurung bisa melaukan operasi aritmatika, menggunakan method dan lain lain
print(f'1 + 1 = {1 + 1}')
print(f'upper = {"jidan".upper()}')