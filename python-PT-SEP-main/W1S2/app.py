# list AKA Array  []

# snake_case
my_arr = ["a", "b", "c", "d", "e"]
print(my_arr)
print(1)
print(my_arr[1])
# print(my_arr[10])
my_arr.append("f")
print(my_arr)
# get the last element in the list
print(my_arr[-1])

# insert at a specific index
my_arr.insert(1, "m")
print(my_arr)
# remove from the end
print(my_arr.pop())
# remove at a specific index
print(my_arr.pop(2))
print(my_arr)
# remove a specific value
print(my_arr.remove("m"))
print(my_arr)

# get elements in range

print(my_arr[10:])
print(my_arr)

my_arr[0] = "rrrr"
# THIS WILL ERROR OUT
# my_arr[10] = "rrrr"
print(my_arr)

# Dictionary === Object in js ==> { }
# key value pair
# key: value
person = {
    "name": "John Doe",
    "age": 20,
    "is_active": True,
    "stacks": ["Python", "MERN"],
    "location": {"state": "ca", "code": "+1"},
}
print(person["name"])
# its more safe to use .get if you dont know
print(person.get("asdasdasd"))
print(person["location"]["code"])
people = []
people.append(person)

# # add OR update
person["age"] = 30
person.update({"age": "10"})

print(person)

## LOOPS


# for loops for List

for char in my_arr:
    print(char)

for i in range(0, len(my_arr)):
    print(i, my_arr[i])

for i in range(len(my_arr)):
    print(i, my_arr[i])

for i in range(0, len(my_arr), 2):
    print(i, my_arr[i])
sum = 0
for num in range(0, 4):
    sum += num
print(sum)

# For loops for Dict

for key in person:
    print("KEY==>", key, "VALUE==>", person[key])


for key, value in person.items():
    print(key, value)

## Tuple
## immutable array ()

my_tuple = (1, 2, 3, 4)
# WE CANT ADD TO THE TUPLE OR REMOVE
# my_tuple[0] = 999
print(my_tuple[0])
print(my_tuple)
