#Q) Find mean, median, mode for the given set of numbers in a list

nums = list(map(int, input("Enter list of numbers: ").split()))
n = len(nums)

mean = sum(nums)/n
nums.sort()
median = nums[n//2] if n%2 != 0 else (nums[n//2 - 1] + nums[n//2])//2
mode = sorted(nums, key = lambda x : nums.count(x))[-1]

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

'''
Sample input:
Enter list of numbers: 1 2 1 4

Sample Output:
Mean: 2.0
Median: 1.5
Mode: 1
'''
