'''calculator that stores history
input: to get user operation or command
conditionals:to organize code
file handling:to save,load,clear history in .txt file
while loop:to keep program running until user exits
'''
history_file = "history.txt"

def show_history():
    try:
        with open(history_file, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("File has no data")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found")

def clear_history():
    with open(history_file, 'w') as file:
        pass
    print("File cleared")

def save_history(equation, result):
    with open(history_file, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid equation (use: num1 operator num2)")
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers")
        return

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use + - * /")
        return

    if result.is_integer():
        result = int(result)

    print("Result:", result)
    save_history(user_input, result)

def main():
    print("------- SIMPLE CALCULATOR ---------")
    print("Type equations like: 5 + 3")
    print("Commands: history | clear | exit")

    while True:
        user_input = input("\nEnter calculation or command: ").strip().lower()

        if user_input == 'exit':
            print("Goodbye!")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)
main()
