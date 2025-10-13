set1 = {1, 2, 3}
set2 = {3, 4, 5}

if set1 & set2:
    print("They have common elements")
else:
    print("No common elements")

set1 = {1,2,3}
set2 = {2,5,6}

if set1.intersection(set2):
    print("yes")
else:
    print ("no")


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
unique_elements = set1.symmetric_difference(set2)
print(unique_elements)


text = "Divya"
unique_chars = set(text)
count = len(unique_chars)
print("Unique characters:", unique_chars)
print("Count:", count)

text = "hello"
unique_chars = set(text)
print("Number of unique charcters:",len(unique_chars))

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
unique_elements = set1.symmetric_difference(set2)
print(unique_elements)