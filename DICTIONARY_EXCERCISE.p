# dictionaries
# question_1
student = {
    "name": "Pramod",
    "age": 18,
    "cgpa": 8.5
}

print(student["name"])
print(student.get("branch", "CSE"))
print(len(student))
# answer_1
Pramod
CSE
3
# question_2
data = {
    "a": 10,
    "b": 20,
    "c": 30
}

data["b"] = 50
data["d"] = 40

print(data)
# answer_2
{'a': 10, 'b': 50, 'c': 30, 'd': 40}
# question_3
student = {
    "name": "Pramod",
    "age": 18
}

print(student["cgpa"])
# answer_3
KeyError: 'cgpa'
# question_4
data = {
    "Python": 90,
    "Java": 80,
    "C++": 75
}

data.pop("Java")

print(data.keys())
print(data.values())
# answer_4
dict_keys(['Python', 'C++'])
dict_values([90, 75])
# question_5
marks = {
    "Maths": 90,
    "Physics": 85,
    "Chemistry": 95
}

for subject, mark in marks.items():
    print(subject, mark)
# answer_5
Maths 90
Physics 85
Chemistry 95
# question_6
numbers = [1, 2, 3, 4, 5]

result = {
    num: num * 10
    for num in numbers
    if num % 2 == 0
}

print(result)
# answer_6
{2: 20, 4: 40}
# question_7
'''Create a dictionary containing the following information:
- Name: Your name
- Age: Your age
- Branch: CSE
- CGPA: Your CGPA
Then:
1. Print the student's name.
2. Update the CGPA.
3. Add a new key called "college".
4. Print all key-value pairs using a for loop.
5. Print the total number of dictionary elements.'''
# answer_7
student = {
    "name": "Pramod",
    "age": 18,
    "branch": "CSE",
    "cgpa": 8.5
}


print(student["name"])


student["cgpa"] = 9.0


student["college"] = "Your College Name"


for key, value in student.items():
    print(key, ":", value)


print("Total elements:", len(student))
