def my_name():
    print("My Name is Azzam")

my_name()

def my_meal(food, drink):
    print(f"I like to eat {food} while drinking {drink}")
my_meal("Pizza", "Pepsi")

def cube(number):
    return print(number * number * number)
cube(1)

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
print(by_three(9))

        

