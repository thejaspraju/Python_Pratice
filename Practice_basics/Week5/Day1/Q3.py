"""
Make a dictionary with keys as subject name (physics, chemistry, etc.) 
and values as their marks. 
Print the name of the subject which has marks more than passing marks (above 33).
"""
from typing import Dict

subject_marks : Dict[str,int] = {
    "Physics" : 67,
    "Chemistry" : 12,
    "english" : 45,
    "Maths" : 96,
    "Kannada" : 80,
}

for subject, marks in subject_marks.items():
    if marks >= 33:
        print(subject)