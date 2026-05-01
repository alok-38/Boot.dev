data = {"a": 1, "b": 2, "c": 3}

for key in data:
    if data[key] % 2 == 0:
        data[key] *= 10

