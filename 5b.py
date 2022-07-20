dob = input("Enter DOB in dd/mm/yy format: ")
list = dob.split('/')

dict = {}
print('-'.join(list))
dict['day'] = list[0]
dict['month'] = list[1]
dict['year'] = list[2]

print(dict)

'''
Sample Input:
Enter DOB in dd/mm/yy format: 31/3/2002

Sample Output:
31-3-2002
{'day': '31', 'month': '3', 'year': '2002'}
'''
