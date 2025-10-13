my_tuple = (11,22,33,22,44,22,55,66,22)
target = 22

indexes = []
for i in range(len(my_tuple)):
    if my_tuple[i] == target:
        indexes.append(i)

print(indexes)

nested_tuple = ((1,2,3),(3,4,9),(5,4,6))
flat_list = []

for t in nested_tuple:
    for num in t:
        flat_list.append(num)

flat_tuple = tuple(flat_list)
print(flat_tuple)



nested_tuple = ((1,2,3),(3,4,9),(5,4,6))
flat_list = []

for t in nested_tuple:
    for num in t:
        flat_list.append(num)

flat_tuple = tuple(flat_list)
print(flat_tuple)

my_tuple = (11,22,33,22,44,22,55,66,22)
swapped_tup = tuple(my_tuple)
print("original:",my_tuple)
print("swapped:",swapped_tup)

