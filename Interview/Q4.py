"""
String segmentation

You are provided with a large string and a dictionary of the words. 
You have to find if the input string can be segmented into words using the dictionary or not.
"""
def segment_str(s,dictionary):
    for i in range(1,len(s)+1):
        first_str = s[0:i]
        print(f"The first string is : {first_str}")
        if first_str in dictionary:
            second_str = s[i:]
            print(f"The secnd string is : {second_str}")
            if(
                not second_str
                or second_str in dictionary
                or segment_str(second_str,dictionary)
            ):
                return True
    return False

s = "datacamp"
dictionary = ["data", "camp", "cam", "lack"]
print(segment_str(s, dictionary))
