import json
import os
import numpy as np

def get_json(path):
    with open(path) as json_file:
        data = json.load(json_file)

    return data

def get_identities(ids_folder, read_file, id_file_name='ids.json'):

    ids_file = os.path.join(ids_folder, id_file_name)

    json_file = get_json(ids_file)

    X = []
    y = []
    ths = []

    for id in json_file['ids']:
        for file in id['files']:
            file_path = os.path.join(ids_folder, id['folder'], file)
            X.append(read_file(file_path))
            y.append(id['name'])
            ths.append(id['th'])

    return X, y, ths

def save_identities(X,y, path):
    print(type(X),type(y))
    to_save = {'X':X, 'y':y}
    print(type(to_save))
    print("sono in save")
    with open(path + '/json_data.json','w') as out_file:
        json.dump(to_save,out_file)


def load_identities(path):
    print("sono in load")
    try:
        with open(path + '/json_data.json','r') as in_file:
            tmp= json.load(in_file)
        X = tmp['X']
        y = tmp['y']
        return X, y
    except:
        return [],[]