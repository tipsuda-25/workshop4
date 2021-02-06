thisdict = {"brand": "Ford", "model": "Mustang","year": 1964}

for key in thisdict:
    print(key)

thisdict = {"brand": "Ford", "model": "Mustang","year": 1964}

for key in thisdict.keys():
    print(key)


thisdict = {"brand": "Ford", "model": "Mustang","year": 1964}
for value in thisdict.values():
    print(value)


thisdict = {"brand": "Ford", "model": "Mustang","year": 1964}
for key, value in thisdict.items():
    print(key, value)