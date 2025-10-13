# Initial list of integers
nums = [10, 20, 30, 10, 40, 50, 10]

print("Original List:", nums)
nums.append(100)
print("After appending 100:", nums)
nums.insert(2, 50)
print("After inserting 50 at index 2:", nums)
if 20 in nums:
    nums.remove(20)
print("After removing first occurrence of 20:", nums)
count_10 = nums.count(10)
print("Count of 10:", count_10)
nums.reverse()
print("After reversing:", nums)
nums.sort()
print("After sorting:", nums)
maximum = max(nums)
minimum = min(nums)
print("Maximum:", maximum)
print("Minimum:", minimum)
total_sum = sum(nums)
print("Sum of all elements:", total_sum)