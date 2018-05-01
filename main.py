def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


if __name__ == '__main__':
    print("Welcome!")
    while True:
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))
        print("Result of addition: ", add(num1, num2))
        print("Result of subtraction: ", sub(num1, num2))
        print("Result of multiplication: ", mul(num1, num2))
        print("Result of division: ", div(num1, num2))
        c = input("Enter q to quit")
        if c == 'q':
            print("Exiting!")
            break
