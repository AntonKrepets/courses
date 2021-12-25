import random

def input_length():
    
    while True:
        try:
            number_of_symbols = int(input('Please enter number of symbols in your password: '))
            break
        except:
            print('It is not digits, try again')
            continue
    return number_of_symbols
def input_spec():        
    while True:
        spec_symbols = input('Do you want special characters in the password (Y - yes, N - no): ')
        if spec_symbols == 'y':
            break
        elif spec_symbols == 'n':
            break
        else:
            print('Smth went wrong, try again please!')
            continue
    return spec_symbols
    
def password_gen(length, spec_bool):
    password = []
    symbols = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'
    spec = '[]{}()*;/,._-@#$%!^<>\/?"§±'
    for i in range(length):
        if spec_bool.lower() == 'y':
            password.append(random.choice(symbols + spec))
        elif spec_bool.lower() == 'n':
            password.append(random.choice(symbols))
    
    return ''.join(password)

def output(length, spec_bool):
     while True:
         yield password_gen(length, spec_bool)

if __name__ == '__main__':
    while True:
        k = input('If you want to generate password enter 1 if no enter exit: ')
        if k == '1':
            while True:
                try:
                    number = int(input('Enter number of passwords you want: '))
                    break
                except:
                    print('Smth went wrong, try again please!')
                    continue
            s = iter(output(input_length(), input_spec()))
            for i in range(number):
                print(next(s))
        elif k == 'exit':
            print('See you!')
            break
        else:
            print('Smth went wrong, try again please!')
            continue

    

