# cara import module untuk ambil function nya langsung
from matematika import tambah, kali

hasil = tambah(1,2,3,4,5)
print(f'hasil tambah = {hasil}')

hasil = kali(1,2,3,4,5)
print(f'hasil tambah = {hasil}')

# cara import module menggunakan alias
from matematika import pangkat as perpangkatan
import matematika as math

hasil = perpangkatan(5,2)
print(f'hasil perpangkatan = {hasil}')

hasil = math.tambah(5,2)
print(f'hasil perpangkatan = {hasil}')