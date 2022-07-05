# Q) Fibonnacci Series

a,b = 0, 1
for i in range(int(input())):
	c = a+b
	print(c, end = " ")
	a, b = b, c
	
# Time Complexity - O(n)
# Space Complexity - O(1)

'''
Sample Input:
5
Sample Output:
1 2 3 5 8
'''
