## Teknik menduplikat list

a = ['jidan', 'feyfa', 'fena']
print(f'a = {a}')

b = a
print(f'b = {b}')

# kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = 'rafeyfa'
b.sort()

print(f'a = {a}')
print(f'b = {b}')

# address dari kedua list
print(f'address a = {hex(id(a))}') # a dan b sama address nya
print(f'address b = {hex(id(b))}') # a dan b sama address nya

# menduplikasi list dengan copy
print(f'membuat list c dengan a.copy()')
c = a.copy()
print(f'address a = {hex(id(a))}') # a dan b sama address nya
print(f'address b = {hex(id(b))}') # a dan b sama address nya
print(f'address c = {hex(id(c))}') # c berbeda address nya dari a dan b

c[0] = 'Muhammad Jidan'
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

