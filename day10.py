
my_set = {1,2,3}
my_set.add(4)
print("after add:",my_set)

my_set = {1,2}
my_set.update([3,4,5],[5,6,7])
print("after update:",my_set)

my_set = {1,2,3}
my_set.remove(2)
print("after remove:",my_set)

my_set = {1,2,3}
my_set.discard(3)
print("after discard:",my_set)

my_set = {10,20,30}
removed_item = my_set.pop()
print("removed item:", removed_item)
print("After pop:",my_set)

set1 = {1,2,3}
set2 = {3,4,5}
result = set1.union(set2)
print("union:",result)

set1 = {1,2,3}
set2 = {2,3,4}
result = set1.intersection(set2)
print("intersection:",result)

set1 = {1,2,3}
set2 = {2,3,4}
result = set1.symmetric_difference(set2)
print("symmetric difference:",result)

set1 = {1,2,3}
set2 = {2,3,4}
result = set1.difference(set2)
print("difference:",result)

set1 = {1,2}
set2 = {1,2,3}
print("is set1 subset of set2?",set1.issubset(set2))

set1 = {1,2,3}
set2 = {2,3}
print("is set1 subset of set2?",set1.issubset(set2))


arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7]

set1 = set(arr1)
set2 = set(arr2)

print("Only in arr1:", list(set1 - set2))
print("Only in arr2:", list(set2 - set1))

arr = [100, 4, 200, 1, 3, 2]
nums = set(arr)
longest = 0

for n in nums:
    if n - 1 not in nums:   # start of sequence
        length = 1
        while n + length in nums:
            length += 1
        longest = max(longest, length)

print("Longest consecutive length:", longest)