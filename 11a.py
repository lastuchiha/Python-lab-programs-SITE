#Q) Define and print matrix

r, c = map(int, input("Enter no. of rows and cols: ").split())
matrix = [ [0]*c for i in range r ]

print("Enter elements")
for i in range(r):
	for j in range(c):
		matrix[i][j] = int(input())

print(* matrix, sep = "\n")

'''
Sample Input:
Enter no. of rows and cols: 2 3
Enter elements
1
2
3
4
5
6

Sample Output:
[1, 2, 3]
[4, 5, 6]
'''
