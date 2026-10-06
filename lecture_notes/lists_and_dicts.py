# bugs = {
#     "ants" : ["fire", "soldier"],
#     "flies" : ["horse", "house"]
# }

# print(bugs.values())

# fruits = ["apple", "blueberry", "grape"]

# fruits.insert(0, "cherry")
# fruits.pop()

# print(fruits)

# print(fruits)
# # lecture check code "lock"

# star = {
#     "name" : "Vega",
#     "magnitude": 0.57,
#     "distance": 25.05
# }

# star["class"] = "A0V"
# print(star)
# del star["class"]
# print(star)


# for i in star.values():
#     print(i)

# list1 = list(range(0, 11))

# print(list1[0:5])
# print(list1[::2])
# list1.reverse()
# print(list1)
# print(list1[-1::-1])

a = [2, 4, 6]
b = [8, 10, 12]
c = [14, 16, 18]

nested_list = [a, b, c]

print(nested_list[2][1])

stars_data = {
    "name": ["Sirius", "Vega", "Altair"],
    "magnitude": [-1.46, 0.03, 0.77],
    "distance_ly": [8.6, 25.0, 16.7],
    "constellation": ["Canis Major", "Lyra", "Aquila"]

}

for name in stars_data["name"]:
    print(name)