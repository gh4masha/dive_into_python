import json

import os
import tempfile

import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

f=open(storage_path, 'a')
if f.tell() ==0:
    storage={}
    f.close()
else:
    f = open(storage_path, 'r')
    storage = json.load(f)
    f.close()
    # print(storage)

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

if args.key != None and args.value != None:
    if storage.get(args.key) == None:
        storage[args.key] = [args.value]
    else:
        t=storage.get(args.key)
        t.append(args.value)
        storage.update({args.key: t})
elif args.key != None and args.value == None:
    if storage.get(args.key)!=None:
        print(', '.join(storage.get(args.key)))
    else:
        print(None)


# print("after:"+str(storage))
with open(storage_path, 'w') as f:
    json.dump(storage, f)
f.close()
