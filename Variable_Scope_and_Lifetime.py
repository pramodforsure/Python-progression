# Python Concept: Variable Scope and Lifetime

# 1. Local Scope
def local_scope():
    number = 25
    print("Inside the function:", number)


print("===== LOCAL SCOPE =====")
local_scope()


# 2. Global Scope
message = "Hello from the global scope!"


def global_scope():
    print(message)


print("\n===== GLOBAL SCOPE =====")
global_scope()


# 3. Local vs. Global Variables
number = 10


def compare_scope():
    number = 20
    print("Inside the function:", number)


print("\n===== LOCAL VS GLOBAL =====")
compare_scope()
print("Outside the function:", number)


# 4. Parameters and Return Values
def update_score(score, points):
    score = score + points
    return score


print("\n===== PARAMETERS AND RETURN VALUES =====")
score = 50
new_score = update_score(score, 25)

print("Original score:", score)
print("Updated score:", new_score)
