marks = {
    "science": 78,
    "english": 91,
    "maths": "dwa",
    "hindi": 84,
}
m = "dawdwadwa"
v = marks.get(m)
if v is not None:
    print(v)
else:
    print("Key does not exists")