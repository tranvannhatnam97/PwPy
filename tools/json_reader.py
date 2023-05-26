import json
def read_json_from_filepath(filepath):
    print(filepath)
    f = open(filepath, 'r', encoding='utf-8')
    data = json.load(f)
    f.close()
    return data