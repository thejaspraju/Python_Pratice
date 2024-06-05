"""
Ask a sentence from user. Then ask a integer k from user. 
Print all the words which are greater or equal to k.
"""

def printword(sentence ,k):
    words = sentence.split()
    for word in words:
        if len(word) >= k:
            print(word , end = " ")

sentence = input("Enter the sentence : ")
k = int(input("Enter the number : "))

printword(sentence,k)
