#Q) find gcd, lcm of two numbers in a single line

def gcd(a, b):
	return a if b == 0 else gcd(b, a%b)

def lcm(a, b):
	return a*b//gcd(a, b)

a, b = map(int, input("Enter two numbers: ").split())
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))

'''
Sample Input:
Enter two numbers: 5 20

Sample Output:
GCD: 5
LCM: 20
'''
