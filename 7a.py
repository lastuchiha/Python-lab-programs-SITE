#Print each line of a file in reverse order

with open(input("Enter a file name: "), 'r') as f:
	lines = f.readlines()
	
for line in lines:
	print(line[::-1]
				
'''
Sample input:
Enter a file name: mickey.txt

Sample output:
nurat
akimhsar
'''
