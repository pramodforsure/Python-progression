# Python Concept: Lists Fundamentals


# 1. Creating a list
languages = ["Python", "Java", "C++"]

print("All languages:", languages)


# 2. Accessing elements using indexes
print("First language:", languages[0])
print("Last language:", languages[-1])


# 3. Adding an element
languages.append("JavaScript")

print("After append:", languages)


# 4. Updating an element
languages[1] = "C"

print("After updating the second item:", languages)


# 5. Finding the number of elements
print("Number of languages:", len(languages))
