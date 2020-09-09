studentsCount: int = 1000
rating = 4.99
isPublished = False
courseName = """
    Multiple
    Lines
"""

print(type(studentsCount))

thing: int = 1
thing = "stuff"
print(thing)

print(len(thing))

print(thing[-1])  # first character from end

print(thing[0:3])  # splice
print(thing[:3])  # splice use default

thingfunc = f"{thing} stuff"
print(thingfunc)

age = 22

if age >= 18 and age < 65:
    print("Eligible")

# Chaining
if 18 <= age < 65:
    print("Eligible")

# Ternary operator
# message = age >= 18 ? "Eligible" : "Not eligigle"
message = "Eligible" if age >= 18 else "Not eligible"

for x in "Python":
    print(x)

for x in ['a', 'b', 'c']:
    print(x)

for x in range(5):
    print(x)


# can type hint things
def increment(number: int, by: int) -> int:
    return number + by

# or not


def incrementOther(number, by):
    return number + by


print(increment(2, 3))
# name hint when calling
print(incrementOther(2, by=3))


def fizzBuzz(input):
    return "Fizz" if input % 2 == 0 else "Buzz"
