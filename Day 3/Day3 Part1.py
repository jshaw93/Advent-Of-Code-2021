with open('binary.txt', 'r') as myFile:
    data = myFile.readlines()

gamma = ''
epsilon = ''

for i in range(len(data[0])-1):
    count_0 = 0
    count_1 = 0
    for j in data:
        if j[i] == '0':
            count_0 += 1
        else:
            count_1 += 1
    if count_0 > count_1:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
    else:
        gamma = gamma + '1'
        epsilon = epsilon + '0'

gamma = int(bin(int(gamma, 2)), 2)
epsilon = int(bin(int(epsilon, 2)), 2)

print(gamma * epsilon)
