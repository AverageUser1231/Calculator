def calculator():
    print("🧮 Simple Calculator")
    print("You can add, subtract, multiply, or divide two numbers.")
    print("Type 'exit' anytime to quit.\n")

    while True:
        num1 = input("Enter the first number: ").strip()
        if num1.lower() == 'exit':
            print("Goodbye! 👋")
            break
        num2 = input("Enter the second number: ").strip()
        if num2.lower() == 'exit':
            print("Goodbye! 👋")
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("❌ Please enter valid numbers!\n")
            continue

        print("Choose an operation:")
        print(" +  Add")
        print(" -  Subtract")
        print(" *  Multiply")
        print(" /  Divide")
        op = input("Your choice: ").strip()

        if op == 'exit':
            print("Goodbye! 👋")
            break

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("🚫 Cannot divide by zero!\n")
                continue
            result = num1 / num2
        else:
            print("❌ Invalid operation! Choose +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")

calculator()
