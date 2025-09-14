import Database as db
import time

## FUNCTION
def printBeautyData(datas) :
    tolerantContent = 10
    tolerantStrip = 13

    # Hitung lebar kolom (supaya tabel rapi)
    id_width = max(len(str(row.get("id"))) for row in datas) + tolerantContent
    penulis_width = max(len(row.get("penulis")) for row in datas) + tolerantContent
    judul_width = max(len(row.get("judul")) for row in datas) + tolerantContent
    tahun_width = max(len(row.get("tahun")) for row in datas) + tolerantContent

    # Cetak header
    print("\n" + "-" * (id_width + penulis_width + judul_width + tahun_width + tolerantStrip))
    print(f"| {'id'.ljust(id_width)} | { 'penulis'.ljust(penulis_width)} | { 'judul'.ljust(judul_width)} | { 'tahun'.ljust(tahun_width)} |")
    print("-" * (id_width + penulis_width + judul_width + tahun_width + tolerantStrip))

    # Cetak isi
    for row in datas:
        print(f"| {str(row.get('id')).ljust(id_width)} | {row.get('penulis').ljust(penulis_width)} | {row.get('judul').ljust(judul_width)} | {row.get('tahun').ljust(tahun_width)} |")

    print("-" * (id_width + penulis_width + judul_width + tahun_width + tolerantStrip))

def operationRead() :
    datas = db.getData()
    printBeautyData(datas)

def operationCreate() :
    penulis = input("\nmasukan penulis : ")
    judul = input("masukan judul buku : ")
    tahun = input("masukan tahun terbit : ")

    db.create({
        "penulis": penulis,
        "judul": judul,
        "tahun": tahun,
    })
    print('\nData Berhasil Ditambahkan')

def operationUpdate() :
    id = input("\nmasukan id : ")
    penulis = input("masukan penulis : ")
    judul = input("masukan judul buku : ")
    tahun = input("masukan tahun terbit : ")

    affectedRow = db.update(id, {
        "penulis": penulis,
        "judul": judul,
        "tahun": tahun,
    })
    print(f"\naffected rows {affectedRow}")

def operationDelete() :
    id = input("\nmasukan id : ")
    affectedRow = db.deleteById(id)
    print(f"\naffected rows {affectedRow}")
## FUNCTION

## SETU DB
db.connect()
## SETU DB

while (True) :
    db.consoleClear()

    print("DATABASE BUKU".center(20))
    print("="*20)

    operations = ['read', 'create', 'update', 'delete']
    for (index, operation) in enumerate(operations) :
        print(f'{index + 1}. {operation}')

    operation = input('\nmasukan operasi (1,2,3,4) : ')
    match (operation) :
        case "1" :
            operationRead()
        case "2" :
            operationCreate()
        case "3" :
            operationUpdate()
        case "4" :
            operationDelete()
        case _ :
            print('\noperasi tidak ditemukan, silahkan pilih lagi')
            time.sleep(1)
            continue

    isDone = input('\napakah anda sudah selesai (y/n) : ')
    if (isDone == 'y') : break
    
print("\nProgram Selesai, Terima Kasihh\n")