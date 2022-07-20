list1 = list(input("Enter a list: "))
list2 = list(input("Enter another list: "))

print(dict(zip(list1, list2)))

'''
Sample input:
Enter a list: 123
Enter another list: abc

Sample output:
{'1': 'a', '2': 'b', '3': 'c'}
'''
