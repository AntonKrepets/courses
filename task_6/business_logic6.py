import data6
import re

brackets = r"\((.+?)\)"  
calc = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
prohibit_symbols = "[^0-9 \.\(\)\-\+\*\/]" 

def validation(expression):
    match = re.search(prohibit_symbols, expression)
    if not match:
        print('Validation completed')
    else:
        print('Try again')
        exit()

def calculator(expression):
    while True:                                   
        match = re.search(brackets, expression)
        if not match:
             break
        expression = expression.replace(match.group(0), calculator(match.group(1)))  

    for digits, funcs in list(data6.funcs.items()): 
        while True:
            match = re.search(calc.format(digits), expression)
            if not match:
                 break
            expression = expression.replace(match.group(0), funcs(*match.groups()))
    return expression