#Number of chars words and lines in a file

with open(input("Enter a file name: "), "r") as f:
  lines = f.readlines()
  
words, temp = len(lines), 0

for line in lines:
  words += line.count(' ')
  temp += len(line)
  
chars = temp-word
print("Lines:", len(lines))
print("Words:", words)
print("Characters:", chars)

'''
Sample Input:
Enter a file name: mickey.txt

Sample Output:
Lines: 2
Words: 2
Characters: 13
'''
