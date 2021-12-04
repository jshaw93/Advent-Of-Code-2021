def find_critera(data: list, index: int, flag: bool):
    count_0 = 0
    count_1 = 1
    for i in data:
        if i[index] == '0':
            count_0 += 1
        else:
            count_1 += 1
    if flag:
        return count_1 >= count_0
    else:
        return count_0 >= count_1


def find_value(data: list, index: int, flag: bool):
    while len(data) > 1:
        data = [x for x in data if x[index] == str(int(find_critera(data, index, flag)))]
        index += 1
    return data[0]


with open('binary.txt', 'r') as myFile:
    myData = myFile.readlines()

oxy_rating = int(bin(int(find_value(myData, 0, True), 2)), 2)
co2_rating = int(bin(int(find_value(myData, 0, False), 2)), 2)
print(oxy_rating*co2_rating)
