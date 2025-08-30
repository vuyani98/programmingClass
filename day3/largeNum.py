
listD = [2, 4, 1, 0 , 230, 10, 15]

max_num = listD[0]

# range(start, end) -> end-1

for i in range(1, 7):

    if listD[i] > max_num:
        max_num = listD[i]

print("Max number is: ", max_num)