#question 1
numbers = [10, 20, 30, 40, 50]

print(numbers[-2])
print(numbers[1:4])
print(numbers[::-1])
#answer 1
40
[20, 30, 40]
[50, 40, 30, 20, 10]
#question 2
fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")
fruits.insert(1, "Grapes")
fruits.remove("Mango")

print(fruits)
#answer 2
['Apple', 'Grapes', 'Banana', 'Orange']
#question 3
a = [1, 2, 3]

b = a

c = a.copy()

b.append(4)
c.append(5)

print(a)
print(b)
print(c)
#answer 3
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 5]
#question 4
'''Question:

Write a Python program that:

Creates a list containing five numbers.

Finds the largest number.

Finds the smallest number.

Calculates the sum of all elements.

Prints all three results.'''
#answer 4
a = [1, 2, 3, 4, 5]

largest = max(a)
smallest = min(a)
total = sum(a)

print(largest, "is max")
print(smallest, "is min")
print(total, "is the sum of the elements in the list")
#output for question 4
5 is max
1 is min
15 is the sum of the elements in the list
