#Q) Check whether two string are equal with a single mutation.

#Time complexity - O(n)
#Space Complexity - O(1)

def nearly_equal(A, B):
	lenA = len(A)
	lenB = len(B)
	
	if abs(lenA - lenB) > 1:
		return False
	
	misMatch = i = j = 0
	while i < lenA and j < lenB:
		if A[i] != B[j]:
			misMatch += 1
			if lenA < lenB:
				i -= 1
			elif lenB < lenA:
				j -= 1
				
		if misMatch > 2:
			return False
		i += 1
		j += 1
		
	return True

A = input("Enter a String: ")
B = input("Enter another String: ")

print("Strings are nearly equal") if nearly_equal(A, B) else print("Strings aren't nearly equal")

'''
Sample Input:
Enter a String: okay
Enter another String: omkay

Sample Output:
Strings are nearly equal
'''
