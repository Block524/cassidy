# STARTING SECTION 3.1
fav_foods = ["curry", "gyoza", "pizza", "pineapple", "potato"]

print(fav_foods[1])
print(fav_foods[-1])
fav_foods.append("fries")
fav_foods.insert(0, "apple")
fav_foods.pop(2)
print(len(fav_foods))
for i in fav_foods:
    print(i.upper())

new_favs = fav_foods[0:len(fav_foods):len(fav_foods) - 1]
val_t = False
for i in new_favs:
    if i == "potato":
        val_t = True
if val_t:
    print("A potato!")
else:
    print("No potato!")

numbers = []


# STARTING SECTION 3.2
for i in range(0,21):
    numbers.append(i)

def get_first_15(numbers):
    fill_list = numbers.copy()
    while len(fill_list) > 15:
        fill_list.pop()
    return fill_list

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    lst.reverse()
    return lst[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

# STARTING SECTION 3.3
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])

def sum_nested(lst):
    sum = 0
    for i in lst:
        for k in i:
            sum += k
    return sum

print(sum_nested(numbers))

# Makes a 5x5 list which increments to 25
def create_5x5():
    n = 5
    emp_list = [0] * n
    newM = []
    for _ in range(n):
        # Had to make copies of emp_list because 
        # if I just appended emp_list itself every time, 
        # it'd just copy changes to every version of emp_list
        newM.append(emp_list.copy())
    for i in range(n):
        for k in range(n):
            newM[i][k] = i * n + k + 1

    return newM

fun_list = create_5x5()

def dunno_mults_of_three(lst):
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if (lst[i][k] % 3) == 0:
                lst[i][k] = "?"
    return lst

def check_knowns(lst):
    sum = 0
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if lst[i][k] != "?":
                sum += lst[i][k]
    return sum

question_list = dunno_mults_of_three(fun_list)
added_sum = check_knowns(question_list)



# STARTING 4.1
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

for i, k in ages.items():
    print(str(i) + " " + str(k))


fav_function = create_5x5()
print(fav_function)