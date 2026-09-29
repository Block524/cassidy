# def say_hello(yoink):
#     return "Hello, " + yoink

# def add(a, b):
#     return a + b

# name = input("Enter your name: ")
# print(say_hello(name))

# a = float(input())
# b = float(input())

# print("The sum is:", add(a, b))

# def can_vote(age, is_citizen):
#     if age >= 18 and is_citizen:
#         print("You can vote!")
#     else:
#         print("You cannot vote!")

# can_vote(24, True)

# def is_weekend(day):
#     if(day == "Saturday" or day == "Sunday"):
#         print("It is the weekend")
#     else:
#         print("It is not the weekend")

# is_weekend("Saturday")


# i = 10
# while i >= 0:
#     print(i)
#     i -= 1
    

# for num in range(10):
#     print(num)

# fruit_basket = ["banana", "cherry", "mango"]

# for fruit in fruit_basket:
#     print(fruit)

# def countdown(start_num):
#     while start_num > 0:
#         print(start_num)
#         start_num -= 1

# countdown(10)

# def temp_check(temp):
#     if temp >= 65 and temp <= 80:
#         print("It's warm today")
#     elif temp < 65:
#         print("It's cold today")
#     elif temp > 80:
#         print("It's hot today")

# temp_check(-10)
# temp_check(70)
# temp_check(90)
# temp_check(int(input("give me a number: ")))

# # Lecture check 9/21/2026 code == roller coaster
# fruits = ["apples", "pears"]
# for i in fruits:
#     print(i)

# # Lecture check 9/23/2026 code == boolean
# i = 10
# while i >= 0:
#     print(i)
#     i-=1


# def findHighest(list):
#     return max(list)

# def findLowest(list):
#     return min(list)

# actualList = [40, 80, 10, 30, 50, 20]

# print(findHighest(actualList))

# create a function to determine if a positive integer is a prime number

# def isItPrime(num):
#     i = 2
#     if num <= 0 or type(num) != int:
#         print("Try again with a new number")
#         return False
#     if num == 2:
#         print("2 is a prime number")
#         return True
#     else:
#         while i <= num**(0.5):
#             if (num % i) == 0:
#                 print(i)
#                 return True
#             else:
#                 i += 1
#         print("Your number is not prime")
#         return False


# print(isItPrime(23))
# print(isItPrime(12))
# isItPrime(2)
