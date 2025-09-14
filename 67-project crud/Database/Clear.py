import os

def consoleClear() :
    match (os.name) :
        case 'nt': os.system('cls')
        case _: os.system('clear')