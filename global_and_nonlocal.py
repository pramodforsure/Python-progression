# Python Concept: global and nonlocal


# 1. Using global
score = 10


def update_global_score():
    global score
    score = score + 5


update_global_score()

print("Global score:", score)


# 2. Using nonlocal
def outer():
    count = 0

    def increase():
        nonlocal count
        count = count + 1

    increase()
    increase()

    print("Enclosing count:", count)


outer()


# 3. A safer alternative using parameters and return values
def add_points(current_score, points):
    return current_score + points


original = 10
updated = add_points(original, 5)

print("Original score:", original)
print("Updated score:", updated)
