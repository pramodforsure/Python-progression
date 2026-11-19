# day_2_Assesement
# querstion_1
data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(data[0][2])
print(data[1][1])
print(data[2][0])
# ans_1
30
40
70
# question_2
students = [
    ["Pramod", 85],
    ["Rahul", 90],
    ["Arjun", 78]
]

students[0][1] = 95
students[2][0] = "Kiran"

print(students)
# ans_2
[['Pramod', 95], ['Rahul', 90], ['Kiran', 78]]
#question_3
numbers = [2, 4, 6, 8, 10]

result = [num * 2 for num in numbers]

print(result)
#ans_3
[4,8,12,16,20]
#question_4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [num for num in numbers if num % 2 == 0]

print(result)
#ans_4
[2,4,6,8,10]
#question_5
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

result = [num for row in matrix for num in row]

print(result)
#ans_5
[1,2,3,4,5,6]
#question_6
'''Write a Python program that:
1. Creates a list containing numbers from 1 to 20.
2. Extracts all even numbers into a new list.
3. Creates another list containing the squares of all odd numbers.
4. Prints both lists.'''
#ans_6
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even_numbers = [num for num in a if num % 2 == 0]
odd_sq = [num**2 for num in a if num % 2 != 0]

print(even_numbers)
print(odd_sq)

