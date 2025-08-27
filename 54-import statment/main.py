# import 

# fungsinya adalah untuk mengambil program dari file external .py

# 1. untuk menyambungkan program dari external 
import program_print
import program_jidan

# 2. import dengan data
import variable
import kucuy

# data ada di namespace variable
print(variable.data)
print(kucuy.data)

# 3. import dengan fungsi
import matematika
hasil = matematika.tambah(2,1)
print(hasil)