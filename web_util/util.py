from __future__ import unicode_literals
import json
import shlex

def read_json_file(file: str):
    with open(file) as f:
        obj = json.load(f)
    return obj

def dump_json_file(obj, file: str):
    with open(file, "w") as f:
        json.dump(obj, f, ensure_ascii=False)

def parse_curl(curl):
    s = shlex.split(curl)
    url = s[1]
    headers = {}
    for i in range(len(s)-2):
        if s[i+2]=='-H':
            l = s[i+3].split(": ")
            headers[l[0]]=l[1]
            i=i+1
    return url, headers

def get_top(data):
    rs = sorted(data.items(), key=lambda x: x[1])[::-1]
    return [f"- {i[0]}: {i[1]}" for i in rs[:5]]