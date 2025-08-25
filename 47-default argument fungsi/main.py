def LogInfo(message = "") :
    if not message :
        print('message empty')
    else :
        print(message)


LogInfo('Hello World')
LogInfo()

def createMahasiswa(nama = "", nim = "", sks_lulus = "", gender = "", height = 164, birthday = "2005-05-02") :
    LogInfo({
        'nama': nama,
        'nim': nim,
        'sks_lulus': sks_lulus,
        'gender': gender,
        'height': height,
        'birthday': birthday,
    })

createMahasiswa(
    nama = "Muhammad Jidan",
    nim = "123456",
    sks_lulus = 12,
    gender = "Laki Laki"
)
