with open('radarfile.txt', 'r') as myFile:
    radars = myFile.readlines()

count = 0
last_num = None
measurements = []
summation = 0

# Little bit messy, just experimenting a lot here
for i in range(len(radars)):
    num = int(radars[i].replace('\n', ''))
    for j in range(2):
        try:
            num += int(radars[i+j+1].replace('\n', ''))
        except IndexError:
            break
    measurements.append(num)

for i in measurements:
    if last_num is None:
        last_num = i
        continue
    if i > last_num:
        count += 1
    last_num = i

print(count)
