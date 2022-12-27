logo = """
 _____________________
|  _________________  |
| | Captain Will's: | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def calculator():

    def add(n1, n2):
        return n1 + n2


    def divide(n1, n2):
        return n1 / n2


    def subtract(n1, n2):
        return n1 - n2


    def multiply(n1, n2):
        return n1 * n2


    operations_dict = {'+': add,
                       '/': divide,
                       '-': subtract,
                       '*': multiply
                       }
    print(logo)
    first = True
    cont = True
    while first is True:
        num1 = float(input("What is the first number? "))
        cont = True
        while cont is True:
            op_input = input("What operation would you like to choose? ")
            num2 = float(input("What is the next number? "))
            result = operations_dict[op_input]  # operation in question is pulled from the dictionary with following key
            result(num1, num2)  # result == function in question
            print(f"{num1} {op_input} {num2} = {result(num1,num2)}")
            first = False
            again = input(f"'y' to continue calculating with {result(num1,num2)}, or type 'c' to clear or 'n' to exit.: ").lower()
            if again == "y":
                cont = True
                num1 = result(num1, num2)  # set num1 equal to previous result
            elif again == "c":
                cont = False
                first = True
            else:
                cont = False
                exit_op = input("Exit Program? y/n: ").lower()
                if exit_op == "y":
                    first = False
                    cont = False
                else:
                    first = True


calculator()
