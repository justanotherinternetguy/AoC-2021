file = open("input_1.txt", "r")

# list of data in file
num = 0

# Part 1
depth = list(map(int, file.readlines()))

for i in range(len(depth)):
	if depth[i] > depth[i-1]:
		num += 1
print("Part 1: ", num)

# Part 2

a = 0
b = 0
c = 0

d = 0
temp = 0
final = 0
for i in range(len(depth) - 3):
	a = depth[i]
	b = depth[i+1]
	c = depth[i+2]
	temp = a + b + c
	d = depth[i+3]
	temp1 = b + c + d
	if temp1 > temp:
		final += 1

print("Part 2: ", final)
