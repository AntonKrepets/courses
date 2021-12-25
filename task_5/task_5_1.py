def input_list():
    while True:
        try:
            numbers = ([int(numbers) for numbers in input('Enter int numbers of the list without repetitions, comma separated: ').strip(' ').split(',')])
            return numbers
        except:
            print('Smth was wrong, please try again!')
            continue



def binary_search(l, item):
    low = 0
    high = len(l) - 1
    mid = (low + high) // 2
    if item == l[mid]:
        return mid
    elif item > l[mid]:
        return binary_search(l[mid + 1:], item) + (mid + 1)
    return binary_search(l[:mid], item)



if __name__ == '__main__':
    l = input_list()
    print(binary_search(l, 5))





