import random,string

enc = []

thing = {}

for _ in range(20):
    while len(list(thing.keys())) != 64:
        key = random.choice(f"{string.ascii_letters}{string.digits}_=")
        value = random.choice(f"{string.ascii_letters}{string.digits}_=")
        if not key in list(thing.keys()):
            if not value in list(thing.values()):
                thing[key] = value

    enc.append(thing)
    thing = {}

print(enc)
