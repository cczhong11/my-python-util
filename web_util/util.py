from __future__ import unicode_literals
import json
import shlex
import os
import uuid
import urllib.request as urllib
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

# input is a dict and return markdown list with sorted result
def get_top(data, top=5):
    # if x is time
    def get_key(x):
        try:
            if ":" in x: 
                k = x.split(":")[0]
                return int(k)
        except:
            return x
    rs = sorted(data.items(), key=lambda x:get_key(x[1]))[::-1]
    top = min(top,len(rs))
    return [f"- {i[0]}: {i[1]}" for i in rs[:top]]

def upload_img(url, data_type=None, folder="cache", name=str(uuid.uuid4().hex)):
    if url is None:
        return
    if "camo.githubusercontent.com" in url:
        prefix = "png"
    elif data_type is None:
        prefix = url.split(".")[-1]
    else:
        prefix = data_type
    filename = f"{name}.{prefix}"
    try:
        f,h = urllib.urlretrieve(url,"/tmp/"+filename)
    except Exception as e:
        print(e)
    os.system(f"aws s3 cp /tmp/{filename} s3://tczimg/{folder}/ --acl public-read")
    os.system(f"rm /tmp/{filename}")
    return f"https://tczimg.s3.amazonaws.com/{folder}/{filename}"
