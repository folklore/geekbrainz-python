import os
import sys

import json
import csv
import pickle


class Grabber():
    def call(self, path = os.pardir):
        data = []
        self._recury(data, path, '')
        return data


    def _recury(self, data, path, margin):
        total = 0

        for entry in os.scandir(path):
            if entry.is_file():
                total += entry.stat().st_size

                payload = {'name': entry.name, 'type': 'file', 'size': entry.stat().st_size, 'pare': path}
                print(margin, payload, sep='')
                data.append(payload)

            elif entry.is_dir():
                total += self._recury(data, entry.path, margin + '  ')

        pare = os.path.dirname(path)
        name = path.replace(pare, '')

        payload = {'name': name, 'type': 'folder', 'size': total, 'pare': pare}
        print(margin, payload, sep='')
        data.append(payload)

        return total


grabber = Grabber()
data = grabber.call()


class Serializer():
    def __init__(self, data):
        self.data = data


    def to_json(self, name = 'recury'):
        with open(f'{name}.json', 'w') as f:
            f.write(json.dumps(data, indent = 2) )


    def to_csv(self, name = 'recury'):
        with open(f'{name}.csv', 'w') as f:
            w = csv.DictWriter(f, data[0].keys())
            w.writeheader()
            w.writerows(data)


    def to_pickle(self, name = 'recury'):
        with open(f'{name}.pickle', 'wb') as f:
            f.write(pickle.dumps(data))


serializer = Serializer(data)
serializer.to_json()
serializer.to_csv()
serializer.to_pickle()
