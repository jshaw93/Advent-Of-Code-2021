with open('radarfile.txt', 'r') as myFile:
    radars = myFile.readlines()

count = 0

last_num = None

for i in radars:
    num = int(i.replace('\n', ''))
    if last_num is None:
        last_num = num
        continue
    if num > last_num:
        count += 1
    last_num = num

print(count)
