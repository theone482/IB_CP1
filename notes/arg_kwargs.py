# Ib 2nd args and kwargs notes 

"""def hello(name="tia", age=29):
    return f"hello {name}! You are {age}"

print(hello())
print(hello("Xavier"))
print(hello(age = 19,name="treyson"))"""
#positional arugements, *args, kewword arguement, ** Kwargs
def hello(*names,last, vlast):
    print(type(names))
    for name in names:
        if name == "Vienna":
            print(f"Hello {name} {last} {vlast}")
        else:
            print(f"Hello {name} {last}")

hello("Alex", "katie", "Andrew", "Vienna", "Tia", "treyson","Xavier", "Jake", last = "LaRose", vlast = "Atkin")


def hello(*names, **last,):
    print(type(names))
    print(names)
    for name in names:
        if name == "Vienna":
            print(f"Hello {name} {last['alast']} {last['vlast']}")
        else:
            print(f"Hello {name} {last['alast']}")

hello("Alex", "katie", "Andrew", "Vienna", "Tia", "treyson","Xavier", "Jake", last = "LaRose", vlast = "Atkin")