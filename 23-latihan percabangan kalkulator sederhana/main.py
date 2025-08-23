angka1 = float(input('masukan angka 1 : '))
operator = input('operator (+,-,x,*,/) : ')
angka2 = float(input('masukan angka 2 : '))

if (operator == "+") :
    hasil = angka1 + angka2;
    print(f'hasil dari {angka1} {operator} {angka2} = {hasil}')
elif (operator == "-") :
    hasil = angka1 - angka2;
    print(f'hasil dari {angka1} {operator} {angka2} = {hasil}')
elif (operator == "x" or operator == '*') :
    hasil = angka1 * angka2;
    print(f'hasil dari {angka1} {operator} {angka2} = {hasil}')
elif (operator == "/") :
    hasil = angka1 / angka2;
    print(f'hasil dari {angka1} {operator} {angka2} = {hasil}')
else :
    print(f'operator {operator} tidak valid')