"""
writen by yeabtakele
Program make a basic calculator
1 Function adds two numbers
2 Function subtracts two numbers
3 Function multiplies two numbers
4  Function divides two numbers
"""


def add(first_number, second_number):
    return first_number + second_number



def subtract(first_number, second_number):
    return first_number - second_number



def multiply(first_number, second_number):
    return first_number * second_number



def divide(first_number, second_number):
    return first_number / second_number 

print('Select options.')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

while True:
    # Take input from the console
    choice = input('Enter choice(1/2/3/4 or n to cancel): ')
    # Check if choice is one of the five options
    if choice in ('1', '2', '3', '4'):
        first_number = float(input('Enter first number: '))
        second_number = float(input('Enter second number: '))

        if choice == '1':
            print(first_number, '+', second_number, '=', add(first_number, second_number))

        elif choice == '2':
            print(first_number, '-', second_number, '=', subtract(first_number, second_number))

        elif choice == '3':
            print(first_number, '*', second_number, '=', multiply(first_number, second_number))

        elif choice == '4':
            print(first_number, '/', second_number, '=', divide(first_number, second_number))
    elif choice == 'n':
        print('Your are successfully logged out!')
        break
    else:
        print('Please enter correct input among these 1/2/3/4/n')
