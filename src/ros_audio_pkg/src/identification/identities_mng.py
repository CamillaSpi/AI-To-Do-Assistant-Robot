import json
import os
import numpy as np

from json import JSONEncoder


REF_PATH = os.path.dirname(os.path.abspath(__file__))

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


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.integer):
            return int(obj)
        return JSONEncoder.default(self, obj)

def save_identities(features_dataBase,labels,number_of_users):
    to_save = {'features_dataBase':features_dataBase, 'labels':labels,'number_of_users':number_of_users}
    with open(REF_PATH + '/../../dataBase/json_data.json', 'w') as out_file:
        json.dump(to_save,out_file,cls=NumpyArrayEncoder)


def load_identities():
    rospy.loginfo("sono in load speaker")
    try:
        with open(REF_PATH + '/../../dataBase/json_data.json','r') as in_file:
            tmp= json.load(in_file)
        features_dataBase = np.asarray(tmp['features_dataBase'])
        labels = tmp['labels']
        number_of_users = tmp['number_of_users']
        return features_dataBase, labels,number_of_users
    except:
        return [],[],0