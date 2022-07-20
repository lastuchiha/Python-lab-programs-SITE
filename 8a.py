#Q) Function that returns will balls collide or not

def collide(p1, p2):
	x1, y1, r1 = p1
	x2, y2, r2 = p2
	
	return (x2 - x1)**2 + (y2 - y1)**2 <= (r1 + r2) ** 2

p1 = tuple(map(int, input("Enter (x, y, z) of ball-1").split()))
p2 = tuple(map(int, input("Enter (x, y, z) of ball-2").split()))

print("The balls will collide") if collide(p1, p2) else print("The balls won't collide")

'''
Sample input:
Enter (x, y, z) of ball-1: 0 0 5
Enter (x, y, z) of ball-2: 10 10 3

Sample Output:
The balls won't collide
'''
