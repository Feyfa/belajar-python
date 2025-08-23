# menghentikan pertanyaan
retry = True
while (retry) : 
    data = input('masukan angka untuk menghentikan pertanyaan : ')

    if(data.isdigit()) :
        print(f'{data} merupakan angka, selamat anda berhasil mengehentikan pertanyaan ini')
        break
    else : 
        print(f'{data} bukan angka, silahkan coba lagi')