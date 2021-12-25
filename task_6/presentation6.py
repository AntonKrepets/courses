import business_logic6 as bl

def show_message(message):
     print(message)

def get_query(message):
     return input(message)

def calculator():
     expression = input('Enter an expression: ')
     bl.validation(expression)
     show_message(f'Result = {bl.calculator(expression)}')


if __name__ == "__main__":
     while True:
        operation = get_query("Enter 1 for calculate smth or enter ex for exit: ")
        if operation == '1':
            calculator() 
        elif operation == "ex":
            print('See you!')
            break
        else:
            show_message("Try again!")
            continue       