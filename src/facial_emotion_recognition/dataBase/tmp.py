import numpy as np
import json

def load_identities(file):
    print("sono in load")
    try:
        with open('/home/nando/Desktop/DefinitivoCog/DefinitivoCog/src/facial_emotion_recognition/dataBase/'+file, 'r') as in_file:
            tmp = json.load(in_file)
        dataset = np.asarray(tmp['dataset'])
        labels = np.asarray(tmp['labels'])
        number_of_users = tmp['number_of_users']
        return dataset, labels,number_of_users
    except Exception as e:
        print(e)
        return np.array([]), np.array([]),0

db , lista , _ =load_identities('json_data.json')
db2 , lista2 , _ =load_identities('old_json_data.json')
print(db.shape, db2.shape)
print(len(lista), len(lista2))
