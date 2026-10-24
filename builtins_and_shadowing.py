# Python Concept: Built-in Names and Name Shadowing


# 1. Using built-in functions
items = ["pen", "book", "ruler"]

print("Number of items:", len(items))
print("Item names:", items)


# 2. Using sum(), max(), and min()
numbers = [4, 7, 2]

print("Total:", sum(numbers))
print("Largest:", max(numbers))
print("Smallest:", min(numbers))


# 3. Avoid shadowing built-in names
# Avoid naming your variables list, str, sum, or max.
# Doing so can hide the corresponding built-in name.

# Bad example — do not uncomment:
# list = [1, 2, 3]
# print(list("abc"))


# Better approach
my_list = [1, 2, 3]

print("My list:", my_list)
print("Length:", len(my_list))
