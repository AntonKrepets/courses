def num():
    while True:
        try:
            fib_number = int(input('Enter int number: '))
            if fib_number < 0:
                print('Number must be more than zero')
                continue
        except:
            print('Smth was wrong, please try again!')
            continue
        return fib_number
    


def fibonacci(number, fib1 = 0, fib2 = 1, res = []):
    if number > 0:
        res.append(fib1)
        fibonacci(number - 1, fib2 ,fib1 + fib2, res)
    return res



if __name__ == '__main__':
    print(fibonacci(num()))