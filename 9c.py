#Q) Unique elements in list

arr = input("Enter a list: ").split()

for char in arr:
	if arr.count(char) == 1:
		print(char)
		
'''
Sample input:
Enter a list: s o m e r a n d o m c h a r s

Sample Output:
e
n
d
c
h
'''
