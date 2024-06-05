"""
 Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the highest marks scored.
"""
from typing import Dict

subject_marks : Dict[str,int] = {
    "Physics" : 67,
    "Chemistry" : 12,
    "english" : 45,
    "Maths" : 96,
    "Kannada" : 80,
}

highest = 0
for marks in subject_marks.values():
    if marks > highest:
        highest = marks

print(highest)