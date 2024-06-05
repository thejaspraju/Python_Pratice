"""
 Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject with highest marks
scored.
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
highest_sub = ""
for subject,marks in subject_marks.items():
    if marks > highest:
        highest = marks
        highest_sub = subject

print(f"Highest marks scored is {highest} in {highest_sub} subject")
