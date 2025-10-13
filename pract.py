

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