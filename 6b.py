#Program to find frequency of characters in a given file and find the type of file based on count.

with open(input("Enter a file name: "), "r") as f:
  file_content = f.read()
  
count = {}
for char in file_content:
  count[char] = file_content.get(char, 0) + 1
  
print("Chars count:", count)

if count.get(';', 0) > 0:
  print("Given file is a C file")
  
elif count.get('=', 0) > 0:
  print("Given file is a Python file")
 
else:
  print("Given file is a text file")
  
  
'''
Sample Input:
Enter a file name: mickey.txt
  
Sample output:
Chars count: {"M": 1, "G" : 1}
Given file is a text file
'''
  
