import csv
import json
with open("graffiti_requests.csv") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    data = [r for r in reader]
spots = {}
for i in data:
    name = i[26]
    spots.update({name:0})
    data.remove(i)
    for i in data :
        if i[26] == name:
            spots[name] += 1
spots.sort(reverse=True)
print(spots)