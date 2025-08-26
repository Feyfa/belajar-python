# Latihan Fungsi

import os

# FUNCTION CALCULATE
def calculatePersegi(calculateType, sisi) :
    sisi = float(sisi)
    return (sisi * 4) if (calculateType == 'keliling') else (sisi ** 2)

def calculatePersegiPanjang(calculateType, panjang, lebar) :
    panjang = float(panjang)
    lebar = float(lebar)
    return ((panjang + lebar) * 2) if (calculateType == 'keliling') else (panjang * lebar)

def calculateLingkaran(calculateType, diameter) :
    diameter = float(diameter)
    phi = 3.14
    radius = diameter / 2 
    return (2 * phi * radius) if (calculateType == 'keliling') else (phi * (radius ** 2))
# FUNCTION CALCULATE

# FUNCTON QUESTION
def questionDimension() :
    result = input('masukan bangun datar yang ingin hitung (persegi/persegi panjang/lingkaran) : ')
    dimensionTypes = ['persegi', 'persegi panjang', 'segitiga', 'lingkaran']

    if result not in dimensionTypes :
        return {'status': 'error', 'message': f"'{result}' bukan bangun data yang valid"}
    else :
        return {'status': 'success', 'result': result}

def questionCalculateType() :
    calculateType = input('masukan jenis perhitungan (keliling/luas) : ')
    calculateTypes = ['keliling','luas']
    
    if calculateType not in calculateTypes :
        return {'status': 'error', 'message': f"'{calculateType}' bukan jenis perhitungan yang valid"}
    else :
        return {'status': 'success', 'result': calculateType}
    
def questionCalculateDimension(dimensionType, calculateType) :
    result = 0
    
    if dimensionType == 'persegi' :
        result = questionCalculateDimensionPersegi(calculateType)
    elif dimensionType == 'persegi panjang' :
        result = questionCalculateDimensionPersegiPanjang(calculateType)
    elif dimensionType == 'lingkaran' :
        result = questionCalculateDimensionLingkaran(calculateType)

    return result
    
def questionCalculateDimensionPersegi(calculateType) :
    sisi = input('masukan sisi : ')
    result = calculatePersegi(calculateType, sisi)
    return result

def questionCalculateDimensionPersegiPanjang(calculateType) :
    panjang = input('masukan panjang : ')
    lebar = input('masukan lebar : ')
    result = calculatePersegiPanjang(calculateType, panjang, lebar)
    return result

def questionCalculateDimensionLingkaran(calculateType) :
    diameter = input('masukan diameter lingkaran : ')
    result = calculateLingkaran(calculateType, diameter)
    return result
# FUNCTON QUESTION

while True :
    os.system('cls')

    print(f'{'PROGRAM MENGHITUNG LUAS DAN KELILING ':^50}')
    print(f'{50*"-"}')

    # question dimension type
    response = questionDimension()
    if(response.get('status') == 'error') :
        print(f'{response.get('message')}')
        break
    dimensionType = response.get('result')
    # question dimension type

    # question calculate type
    response = questionCalculateType()
    if(response.get('status') == 'error') :
        print(f'{response.get('message')}')
        break
    calculateType = response.get('result')
    # question calculate type
    
    # question for calculate dimension
    result = questionCalculateDimension(dimensionType, calculateType)  
    # question for calculate dimension

    print(f'{calculateType} dari {dimensionType} di atas adalah = {result} { 'cm' if calculateType == 'keliling' else 'cm^2'}')
    
    isNext = input('apakah anda ingin menghitung lagi (y/n) : ')
    if(isNext != 'y') :
        break

