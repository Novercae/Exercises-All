# Check if it is possible to reach the desired sum within the list with 2 numbers.

list = [3, 5, -4, 8, 11, 1, -1, 6]
sum = 10

def array(value):

    for x in value:
        index = 0
        while True:
            if value[index] == x:
                index += 1
            if x + value[index] == sum:
                print(x, value[index])
                index += 1
            else:
                index += 1
            if index >= len(value) - 1:
                break

array(list)
