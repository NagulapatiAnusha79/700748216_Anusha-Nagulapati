# -*- coding: utf-8 -*-
"""ICP2_700748216.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HLg-Fs1_fD9s5_0u2ZDPcSdN_5DMTAR9
"""

#PROGRAM1
# method for full name
def fullname(first_Name,last_Name):  # Take two parameters first and last names
  return f"{first_Name}{last_Name}"  # concatenation of first and last names
def string_alter(full_name):
  return full_name[::2]   # takes full_name parameter and form new string
first_Name =input("Enter first_Name:")
last_Name = input("Enter Second_Name:")
full_name = fullname(first_Name,last_Name) # using fullname function
print("full Name:",full_name)
output = string_alter(full_name)
print("output:",output)


#---------------------------------------------------------------------------------------


#PROGRAM2
f = open("Sample_input.txt","w")
f.write("Python Course\n")
f.write("Deep learning Course\n")
f.close()
f= open("Sample_input.txt","r")
print(f.read())

from collections import Counter

# Read input from input.txt
with open('Sample_input.txt', 'r') as file:
    sentences = file.readlines()

# Count the words in each line by processing
wordcount_each_line = []

for sentence in sentences:
    words = sentence.strip().split()
    wordcount_each_line.append(Counter(words))

# Print the Sentences
for sentence in sentences:
    print(sentence.strip())

# Print the count for each word
print("Word_Count:")
for word, count in Counter(word for wc in wordcount_each_line for word in wc).items():
    print(f"{word}: {count}")

# Store the output in sampleoutput.txt
with open('Sample_output.txt', 'w') as output_file:
    for sentence in sentences:
        output_file.write(sentence)
    output_file.write("Word_Count:\n")
    for word, count in Counter(word for wc in wordcount_each_line for word in wc).items():
        output_file.write(f"{word}: {count}\n")


#---------------------------------------------------------------------------------------

#PROGRAM 3
# code below is the conversion of heights from inches to cms
# using Nested loop & List comprehensions
Listofheights = []
elements = int(input("Enter size of list: "))
for e in range(elements):
    Listofheights.append(float(input()))
tempListofHeights= [2.54 * item for item in Listofheights]
print(tempListofHeights)
