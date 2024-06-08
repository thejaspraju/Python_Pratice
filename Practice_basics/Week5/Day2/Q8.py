"""
Write a Python program to combine two dictionary by adding values
for common keys.

"""
def combineDictionary(d1,d2):
    combined_disct = {}

    for key in d1:
        combined_disct[key] = d1[key] + d2.get(key,0)
    
    for key in d2:
        if key not in d1:
            combined_disct[key] = d2[key]
    
    return combined_disct

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
result = combineDictionary(d1, d2)
print(result)


