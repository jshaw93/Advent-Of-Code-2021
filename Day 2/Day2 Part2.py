with open('directions.txt', 'r') as myFile:
    directions = myFile.readlines()

pos = [0, 0, 0]

for i in directions:
    split_dirs = i.split()
    spaces = int(split_dirs[1])
    direction = split_dirs[0]
    if direction == 'forward':
        pos[0] += spaces
        pos[1] += pos[2] * spaces
    elif direction == 'down':
        # pos[1] += spaces
        pos[2] += spaces
    elif direction == 'up':
        # pos[1] -= spaces
        pos[2] -= spaces

print(pos)
print(pos[0] * pos[1])
