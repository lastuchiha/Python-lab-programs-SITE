# Q) Sum of Even Valued Terms of fibonacci series upto 4Million

a, b, c = 0, 1, 1
sum = 0
while c < 4000000:
	if c%2 == 0:
		sum += c
	a, b = b, c
	c = a+b
print(sum)

'''
Sample Output:
4613732
'''
