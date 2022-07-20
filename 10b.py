#Q) Reverse a list without using reverse function

def reverse(arr):
	for i in range(len(arr)//2):
		arr[i], arr[-(i+1)] = arr[-(i+1)], arr[i]
		
arr = list(input("Enter a list: ").split())
print("Before reversing:", arr)
reverse(arr)
print("After reversing:", arr)

'''
Sample Input:
Enter a list: t a r u n

Sample Output:
Before reversing: ['t', 'a', 'r', 'u', 'n']
After reversing: ['n', 'u', 'r', 'a', 't']
'''
