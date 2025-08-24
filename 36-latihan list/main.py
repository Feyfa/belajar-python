# program list buku

data = [];
while (True) :
    judul = input('Masukan judul buku\t: ')
    penulis = input('Masukan penulis buku\t: ')
    
    data.append([judul, penulis])
    data_length = len(data)
    
    for index,item in enumerate(data) :
        print(20*'-')
        print(f'judul : {item[0]}')
        print(f'penulis : {item[1]}')

        if(index == data_length - 1) :
            print(20*'-')

    isNext = input('\nAPAKAH AND INGIN MENAMBAHKAN BUKU (y/n) : ')
    if(isNext != 'y') :
        break

print('\nPROGRAM SELESAI')



