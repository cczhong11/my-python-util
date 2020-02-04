from __future__ import unicode_literals
import json
import shlex
import os
import uuid

def read_json_file(file: str):
    with open(file) as f:
        obj = json.load(f)
    return obj

def dump_json_file(obj, file: str):
    oobj = {}
    if os.path.exists(file):
        with open(file) as f:
            oobj = json.load(f)
    for i in obj:
        oobj[i] = obj[i]
    with open(file, "w") as f:
        json.dump(oobj, f, ensure_ascii=False)

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

def get_top(data, top=5):
    rs = sorted(data.items(), key=lambda x: x[1])[::-1]
    return [f"- {i[0]}: {i[1]}" for i in rs[:top]]

def upload_img(url, data_type=None, folder="cache"):
    name = str(uuid.uuid4().hex)
    if "camo.githubusercontent.com" in url:
        prefix = "png"
    elif data_type is None:
        prefix = url.split(".")[-1]
    else:
        prefix = data_type
    filename = f"{name}.{prefix}"
    try:
        f,h = urllib.request.urlretrieve(url,filename)
    except Exception as e:
        print(e)
    os.system(f"aws s3 cp {filename} s3://tczimg/{folder}/ --acl public-read")
    os.system(f"rm {filename}")
    return f"https://tczimg.s3.amazonaws.com/{folder}/{filename}"