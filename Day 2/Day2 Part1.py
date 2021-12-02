with open('directions.txt', 'r') as myFile:
    directions = myFile.readlines()

pos = [0, 0]

for i in directions:
    split_dirs = i.split()
    spaces = int(split_dirs[1])
    direction = split_dirs[0]
    if direction == 'forward':
        pos[0] += spaces
    elif direction == 'down':
        pos[1] += spaces
    elif direction == 'up':
        pos[1] -= spaces

print(pos)
