def say_hello(name):
    # Prints "Hello, [name]"
    print("Hello,", name)

def say_goodbye(name):
    # Prints "Goodbye, [name]"
    print("Goodbye,", name)

def circle_area(radius):
    # Prints, not returns, the area of a circle of an inputted radius
    print(3.14 * float(radius) ** 2)

def add(a, b):
    # Returns the added value of a and b
    return a + b

def subtract(a, b):
    # Returns the value of a less b
    return a - b

def multiply(a, b):
    # Returns tbhe value of a times b
    return a * b

def divide(a, b):
    # Returns the value of a divided by b
    if b != 0:
        return a / b
    else :
        print("Tried to divide by zero")
        return 0

def temperature_range(temp_list):
    # Takes a list of temperatures, and spits out a tuple containing the min and max temps of the day
    return (min(temp_list), max(temp_list))

def is_weekend(day):
    # Takes an integer input for day of the week, and outputs a boolean depending on if it's the weekend or not
    if day == 6 or day == 7:
        return True
    else:
        return False

def effic_checker(miles, gallons):
    # Inputs miles travelled and gallons used to get there, and returns fuel efficiency
    return miles / gallons

def encoder(to_encrypt):
    # Takes the last digit of an inputted integer, and moves it to the front of the int
    i = to_encrypt % 10
    to_encrypt = to_encrypt // 10

    # Now return the string concatenation of the last digit and the first digits
    return int(str(i) + str(to_encrypt))

def power(a, b):
    # Returns a raised to the power of b
    i = 1
    for c in range(b):
        i *= a
    return i

def minimum(integers):
    # Scrolls through a given list and outputs the minimum integer in the list
    i = integers[0]
    for c in integers:
        if c < i:
            i = c
    return i

def maximum(integers):
     # Scrolls through a given list and outputs the maximum integer in the list
        i = integers[0]
        for c in integers:
            if c > i:
                i = c
        return i

def sum_the_digits(big_num):
    # Takes an integer input, then outputs the sum of the individual digits
    c = 0
    for i in range(big_num // 10):
        c += big_num % 10
        big_num = big_num // 10
    return c


x = 5
y = 3
result = power(x, y) # 5 raised to the 3rd

print(f"The result of Oski Stole Your Power (5, 3) with x = {x} and y = {y} is {result}.")

