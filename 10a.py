#Commulative product of a list of numbers

def cummulative_product(nums):
	prod = 1
	res = []
	for num in nums:
	    prod *= num
	    res.append(prod)
	return res

nums = list(map(int, input("Enter numbers: ").split()))
print(cummulative_product(nums))

'''
Sample Input:
Enter numbers: 1 4 5 6

Sample Output:
[1, 4, 20, 120]
'''
