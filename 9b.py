#Duplicates in a list

#Time complexity - O(n)

arr = input("Enter a list: ").split()
seen = set()
dups = set()

for char in arr:
	if char not in seen:
		seen.add(char)
		
	elif char not in dups:
		dups.add(char)
		print(char)
		
'''
Sample input:
Enter a list: s o m e r a n d o m c h a r s

Sample output:
o
m
a
r
s
'''
