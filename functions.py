#starting to learn functions in Python
def sum_two_numbers(a, b):
    return a + b


x = sum_two_numbers(2, 3)
print(x)


def func():
    print("my first ever function in Python!")


func()


# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together"]


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    for bStr in list_benefits():
        if bStr.__contains__(benefit):
            return benefit + " is a benefit of functions!"


def name_the_benefits_of_functions():
    for benefit in list_benefits():
        print(build_sentence(benefit))


name_the_benefits_of_functions()

