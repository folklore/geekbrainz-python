import os
import sys

import json
import csv
import pickle

data = []

def recury(path, margin):
    total = 0

    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size

            payload = {'name': entry.name, 'type': 'file', 'size': entry.stat().st_size, 'pare': path}
            print(margin, payload, sep='')
            data.append(payload)

        elif entry.is_dir():
            total += recury(entry.path, margin + '  ')

    pare = os.path.dirname(path)
    name = path.replace(pare, '')

    payload = {'name': name, 'type': 'folder', 'size': total, 'pare': pare}
    print(margin, payload, sep='')
    data.append(payload)

    return total

recury(os.pardir, '')


with open('recury.json', 'w') as f:
    f.write(json.dumps(data, indent = 2) )


with open('recury.csv', 'w') as f:
    w = csv.DictWriter(f, data[0].keys())
    w.writeheader()
    w.writerows(data)

with open('recury.pickle', 'wb') as f:
    f.write(pickle.dumps(data))
