# question_1
def display(name, age, branch):
    print(name)
    print(age)
    print(branch)


display("Pramod", branch="CSE", age=18)
# answer_1
Pramod
18
CSE
# question_2


def calculate(a, b=10, c=5):
    return a + b + c


print(calculate(20))
print(calculate(20, 30))
print(calculate(20, 30, 40))
# answer_2
35
55
90
# question_3


def analyze(*numbers):
    print(numbers)
    print(type(numbers))
    print(sum(numbers))


analyze(10, 20, 30, 40)
# answer_3
(10, 20, 30, 40)
<class 'tuple' >
100
# question_4


def profile(**details):
    for key, value in details.items():
        print(key, ":", value)


profile(name="Pramod", age=18, branch="CSE")
# answer_4
name: Pramod
age: 18
branch: CSE
# question_5
x = 100


def test():
    x = 50
    print(x)


test()
print(x)
# answer_5
50
100
# question_6
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 3, numbers))

print(result)
# answer_6
[3, 6, 9, 12, 15]
# question_7
numbers = [10, 15, 20, 25, 30, 35]

result = list(filter(lambda x: x > 20, numbers))

print(result)
# answer_7
[25, 30, 35]
# question_8
'''Write a function called student_result() that:
1. Accepts a student's name as a normal argument.
2. Accepts any number of marks using *args.
3. Calculates the total marks.
4. Calculates the average marks.
5. Prints the student's name, total and average.'''
# answer_8


def student_result(name, *args):
    total = sum(args)
    average = total / len(args)

    print(f"Student Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average}")


student_result("Pramod", 85, 90, 78, 92, 88)
