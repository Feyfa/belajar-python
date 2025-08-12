dataInteger = 10
dataFloat = 1.23
dataString = "Muhammad Jidan"
dataBoolean = False
dataComplex = complex(5,6) # ini sama saja dengan 5+6j


print(f"value = {dataInteger} , type = {type(dataInteger)}")
print(f"value = {dataFloat} , type = {type(dataFloat)}")
print(f"value = {dataString} , type = {type(dataString)}")
print(f"value = {dataBoolean} , type = {type(dataBoolean)}")
print(f"value = {dataComplex} , type = {type(dataComplex)}")

# untuk menggunakan tipedata seperti di bahasa c
from ctypes import c_double
data_double = c_double(10.5)
print(f"value = {data_double} , type = {type(data_double)}")