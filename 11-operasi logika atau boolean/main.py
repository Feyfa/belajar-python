# NOT
print('===NOT===')
a = True
c = not a # di c++ -> c = !a
print(f'data a = {a}')
print('-------------NOT')
print(f'data c = {c}')

# OR
print('\n===OR===')
a = False
b = False
c = a or b
print(f'{a} OR {b} = {c}')
a = False
b = True
c = a or b
print(f'{a} OR {b} = {c}')
a = True
b = False
c = a or b
print(f'{a} OR {b} = {c}')
a = True
b = True
c = a or b
print(f'{a} OR {b} = {c}')


# and
print('\n===AND===')
a = False
b = False
c = a and b
print(f'{a} AND {b} = {c}')
a = False
b = True
c = a and b
print(f'{a} AND {b} = {c}')
a = True
b = False
c = a and b
print(f'{a} AND {b} = {c}')
a = True
b = True
c = a and b
print(f'{a} AND {b} = {c}')

# xor jika ada satu yang true, maka akan true
print('\n===XOR===')
a = False
b = False
c = a ^ b
print(f'{a} ^ {b} = {c}')
a = False
b = True
c = a ^ b
print(f'{a} ^ {b} = {c}')
a = True
b = False
c = a ^ b
print(f'{a} ^ {b} = {c}')
a = True
b = True
c = a ^ b
print(f'{a} ^ {b} = {c}')