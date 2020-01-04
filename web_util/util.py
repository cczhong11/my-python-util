import json

def read_json_file(file: str):
    with open(file) as f:
        obj = json.load(f)
    return obj

def dump_json_file(obj, file: str):
    with open(file, "w") as f:
        json.dump(obj, f)