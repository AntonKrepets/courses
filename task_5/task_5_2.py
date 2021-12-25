l = [1, 2, [2, 4, [[7, 8], 4, 6]]]


def nested_list(arr):
    sum = 0
    for i in arr:
        try:
            sum += nested_list(i)
        except:
            sum += i
    return sum
    


if __name__ == '__main__':
    print(nested_list(l))
