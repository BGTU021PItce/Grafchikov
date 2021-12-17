x = int(input())
y = int(input())
n = int(input())
z = int(input())

length = z*n
length -= x

step = length//y
if step < 0:
 step = 0
print(step)