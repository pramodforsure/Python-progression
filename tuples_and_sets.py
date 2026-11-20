#question_1
data = (10, 20, 30, 40, 50)

print(data[-1])
print(data[1:4])
print(data[::-1])
#answer_1
50
(20,30,40,50)
(50,40,30,20,10)
#question_2
numbers = (10, 20, 30)

numbers[1] = 100

print(numbers)
#answer_2
TypeError
#question_3
student = ("Pramod", 18, "CSE", 8.5)

name, age, branch, cgpa = student

print(name)
print(branch)
print(cgpa)
#answer_3
Pramod
18
8.5
#question_4
numbers = {10, 20, 30, 10, 20, 40, 50}

numbers.add(60)
numbers.add(20)

print(len(numbers))
#answer_4
6
#question_5
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)
print(A & B)
print(A - B)
print(A ^ B)
#answer_5
{1, 2, 3, 4, 5, 6, 7, 8}
{4, 5}
{1, 2, 3}
{1, 2, 3, 6, 7, 8}
#question_6
A = {10, 20, 30}

A.discard(40)

print(A)
A = {10, 20, 30}

A.remove(40)

print(A)
#answer_6
{10, 20, 30}
KeyError
#question_7
'''Write a Python program that:
1. Creates a list containing duplicate numbers.
2. Converts that list into a set.
3. Removes duplicate elements.
4. Converts the set back into a list.
5. Prints the original list and the new list.'''
#answer_7
numbers = [10, 20, 30, 20, 40, 10, 50, 30]

numberss = set(numbers)
unique_numbers = list(numberss)

print("Original:", numbers)
print("Unique:", unique_numbers)
