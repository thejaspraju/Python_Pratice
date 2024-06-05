marks = {
    "science" : 78,
    "english" : 91,
    "maths" : 56,
    "hindi" : 84,
}
#update / Add
print(marks)
marks["maths"] = 100
marks["xyz"] = 74
print(marks)

#delete
del marks["science"]
print(marks)