# penggunaan type hints

def functionBebas(namaBangunDatar:str, panjang:float|int, lebar:float|int) -> list : 
    return [namaBangunDatar, panjang, lebar];

print(functionBebas("Jidan", 1, 3))