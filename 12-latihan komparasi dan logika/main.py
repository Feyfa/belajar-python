# membuat gabungan area rentang dari angka

# +++++3------10+++++
# inputUser = input('masukan angka yang bernilai kurang dari 3 atau lebih besar dari 10 = ')
# inputUser = float(inputUser)
# print(f'{'Anda Benar' if (inputUser < 3 or inputUser > 10) else 'Anda Salah'}')


# 1. -----0+++++5--------8+++++++11-------
# inputUser = float(input('masukan angka = '))
# if(
#     (inputUser > 0 and inputUser < 5) or
#     (inputUser > 8 and inputUser < 11)
# ) :
#     print('anda benar')
# else :
#     print('anda salah')


# 2. +++++0-----5++++++++8-------11+++++++
inputUser = float(input('masukan angka = '))
if(
    (inputUser < 0) or
    (inputUser > 5 and inputUser < 8) or
    (inputUser > 11)
) :
    print('anda benar')
else :
    print('anda salah')