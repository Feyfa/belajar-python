# continue pass, break

# pass itu seperti ini if (true) {  } jadi hanya membuat block kosong saja gitu
angka = 0
while (angka < 5) :
    angka += 1
    if(angka == 3) :
        pass # ini tidak akan dieksekusi
    print(f'angka = {angka}')


# continue 
angka = 0
while (angka < 5) :
    angka += 1
    print(f'angka = {angka}')
    if(angka == 3) : 
        print('continue bang')
        continue
    print('System.out.print();')
