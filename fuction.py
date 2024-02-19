def hello(name):
    print(f"Hello {name}")


hello("Bee")


def area(width, height):
    total = width*height
    return total


area(5, 8)

print(area(5, 8))
print(area(15, 7.5))


def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Language: {lang}")


show_info()
print()
show_info("Bee", 12000, "php")
