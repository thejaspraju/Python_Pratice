marks = {
    "science": 78,
    "english": 91,
    "maths": "dwa",
    "hindi": 84,
    "married": None,
}
# h = marks.pop("hindi")
# print(h)
# print(marks)

# marks.clear()
# print(marks)
print(marks)

# x = marks.get("hindiii",-1)
# print(x) 

# m = "married"
# if m in marks:
#     print(marks[m])
# else:
#     print("Key does not exists")

v = marks.get("maths")  # None
if v is not None:
    print(v)
else:
    print("Key does not exists")