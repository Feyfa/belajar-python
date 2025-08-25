def info(message = '') :
    if not message :
       print('Data Kosong')
    else :
       print(message)

info('Nama Saya Muhammad Jidan')
info(['nama', 'saya', 'muhammad', 'jidan'])
info({'message': 'Created Account Successfully'})
info()
