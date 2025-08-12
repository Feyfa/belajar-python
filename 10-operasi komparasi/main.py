# 'is' sebagai operasi object
x = 5 # ini adalah assigment komparasi object identity
y = 5

# python sudah pintar ketika nilai nya sama dan kecil maka akan di tarus di satu memori yang sama
print(f"nilai x = {x} , id = {hex(id(x))}")
print(f"nilai y = {y} , id = {hex(id(y))}")

hasil = x is y
print(f"x is y = {hasil}")

# ===============================

x = 5 # ini adalah assigment komparasi object identity
y = 6

# python sudah pintar ketika nilai nya sama dan kecil maka akan di tarus di satu memori yang sama
print(f"nilai x = {x} , id = {hex(id(x))}")
print(f"nilai y = {y} , id = {hex(id(y))}")

hasil = x is not y
print(f"x is y = {hasil}")