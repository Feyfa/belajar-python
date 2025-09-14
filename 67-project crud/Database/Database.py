from . import Constan as const
import json
import os

def getDbPath() :
    base_dir = os.path.dirname(__file__)
    db_path = os.path.join(base_dir, const.DB_NAME)
    return db_path

def connect() :
    db_path = getDbPath()
    
    if not (os.path.exists(db_path)) :
        with open(db_path, 'w') as file :
            json.dump([], file)

    return db_path

def getData() -> list :
    db_path = connect()
    
    with open(db_path) as file :
        return json.load(file)
    
def getDataById(id) :
    connect()

    data = getData()
    data = next((user for user in data if user.get('id') == id), {})

    return data

def writeData(data) :
    db_path = connect()
    with open(db_path, 'w') as file :
        json.dump(data, file, indent=4)

def create(param) :
    datas = getData()
    datasLength = len(datas) + 1

    while (getDataById(datasLength) != {}) :
        datasLength += 1

    param = {
        'id': datasLength,
        **param
    }
    datas.append(param)

    writeData(datas)

def update(id, param) :
    datas = getData()
    affectedRow = 0

    for data in datas :
        if (data.get('id') == int(id)) :
            if ("penulis" in param) :
                affectedRow = 1
                data['penulis'] = param.get('penulis')
            if ("judul" in param) :
                affectedRow = 1
                data['judul'] = param.get('judul')
            if ("tahun" in param) :
                affectedRow = 1
                data['tahun'] = param.get('tahun')
            break

    writeData(datas)
    return affectedRow

def deleteById(id) :
    datas = getData()
    datasResult = [user for user in datas if user.get('id') != int(id)]
    affectedRow = 1 if (len(datas) != len(datasResult)) else 0

    writeData(datasResult)
    return affectedRow