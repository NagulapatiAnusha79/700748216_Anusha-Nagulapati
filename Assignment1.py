# program 1
# Enter the string "Python"  from the console
input_str = list(input("Enter the string: "))

# Delete at least 2 characters (assuming the input string has more than 2 characters)
if len(input_str) >= 4:
    del input_str[0]
    del input_str[-2:]
else:f
    print("Input string should have at least 4 characters.")

# Reverse the resultant string
final_str = input_str[::-1]

# Print the reversed string
print("Reversed Resultant String:", "".join(final_str))

#-------------------------------------------------------------------------------------

# Program 2
num1 = float(input("Enter first number: ")) # user input
num2 = float(input("Enter second number: ")) # user input

#Printing the result for four arithmetic operations
print("Addition: ",num1 + num2) # Addition
print("Subtraction: ",num1 - num2) # Subtraction
print("Multiplication: ",num1 * num2) # Multiplication
print("Division: ",num1 / num2) # simple Division

#-------------------------------------------------------------------------------------

# Program 3
# Enter the sentence from the user
sentence = input("Enter a sentence: ")

# Replace each occurrence of 'python' with 'pythons'
update_sentence = sentence.replace('python', 'pythons')

# Print the updated sentence
print("Modified Sentence:", update_sentence)

#-------------------------------------------------------------------------------------

# Program 4
 # Accept the class score from the user
student_score = float(input("Enter the score: "))

# calculate the  grade based on the grading scheme
if 90 <= student_score <= 100:
    grade = 'A'
elif 80 <= student_score  < 90:
    grade = 'B'
elif 70 <= student_score  < 80:
    grade = 'C'
elif 60 <= student_score  < 70:
    grade = 'D'
else:
    grade = 'F'

# Print the grade
print(f"The grade for the student_score {student_score} is: {grade}")
