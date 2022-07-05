# Q) Store the count of chars in a Dictionary

string = input("Enter a string: ")
dict = {}

for char in string:
  dict[char] = dict.get(char, 0) + 1
  
print(dict)

# Time Complexity - O(n)
# Space Complexity - O(n)

'''
Sample Input:
Enter a string: sasuke

Sample Output:
{ 's' : 2, 'a' : 1, 'u' : 1, 'k' : 1, 'e' : 1 }
'''
