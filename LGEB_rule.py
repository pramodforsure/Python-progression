name = "Global"


def outer():
    name = "Enclosing"

    def inner():
        name = "Local"
        print("Inside inner:", name)

    inner()
    print("Inside outer:", name)


outer()

print("At global level:", name)
