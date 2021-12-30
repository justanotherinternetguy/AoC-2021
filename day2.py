# Get data from file
with open("input_2.txt") as file: 
    data = [line.strip() for line in file ]



# Part 1

forward = 0
depth = 0

for i in data:
	direction = i[:-2]
	moveSteps = int(i[-2:])
	
	if direction == "forward":
		forward += moveSteps
	if direction == "up":
		depth -= moveSteps
	if direction == "down":
		depth += moveSteps

print(forward * depth)




# Part 2

forward = 0
depth = 0
aim = 0

for i in data:
	direction = i[:-2]
	moveSteps = int(i[-2:])
	
	if direction == "down":
		aim += moveSteps
	if direction == "up":
		aim -= moveSteps
	if direction == "forward":
		forward += moveSteps
		depth = depth + (aim * moveSteps)


print(forward * depth)
