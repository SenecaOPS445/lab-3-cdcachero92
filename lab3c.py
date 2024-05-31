#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: cdcachero

def operate(number1, number2, operator):
    # Place logic in this function
    if operator == 'add':
        sum = number1 + number2
        return sum
    elif operator == 'subtract':
        diff = number1 -number2
        return diff
    elif operator == 'multiply':
        prod = number1 * number2
        return prod     
    else:
        errormsg = 'Error: function operator can be "add", "subtract", or "multiply"'
        return errormsg




if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))  
