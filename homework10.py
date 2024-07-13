MyList = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = -1
while index < len(MyList):
    index += 1
    if MyList[index] > 0:
        print(MyList[index])
    if MyList[index] < 0:
        break
