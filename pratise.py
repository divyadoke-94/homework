my_tuple = (10,20,30,40)
temp = list(my_tuple)

temp[0], temp[-1] = temp[-1],temp[0]

new_tuple = tuple(temp)
print(new_tuple)

my_tuple = (10,20,30,40)
sorted_tuple = sorted(my_tuple,reverse=True)
second_largest = sorted_tuple[1]
print(second_largest)


    
 