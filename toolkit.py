import random


def show_menu():
    print("\n========================================")
    print("          PERSONAL MINI-TOOLKIT")
    print("========================================")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Simple Calculator")
    print("4. Name Formatter")
    print("5. Quit")


# Number guessing game: uses a loop and conditionals until the answer is found.
def number_guessing_game():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("\nNumber Guessing Game")
    print("I chose a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1
        if guess < secret_number:
            print(f"Too low! That was guess number {attempts}.")
        elif guess > secret_number:
            print(f"Too high! That was guess number {attempts}.")
        else:
            print(f"You got it! The number was {secret_number}.")
            print(f"You finished in {attempts} attempt(s).")
            break


# To-do list: stores tasks in a list that can grow or shrink.
def todo_list():
    tasks = []

    print("\nTo-Do List")
    while True:
        print("\nTo-Do Options:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
        elif choice == "2":
            task = input("Enter a task: ").strip()
            if task:
                tasks.append(task)
                print(f'Added "{task}" to your list.')
            else:
                print("A task cannot be empty.")
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
                continue

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(input("Enter the task number to remove: "))
                removed_task = tasks.pop(task_number - 1)
                print(f'Removed "{removed_task}".')
            except (ValueError, IndexError):
                print("Please choose a valid task number.")
        elif choice == "4":
            print("Returning to the main menu...")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


# Simple calculator: uses repeated input and conditional operation selection.
def simple_calculator():
    print("\nSimple Calculator")
    print("Enter an operation: +, -, *, or /")

    operation = input("Operation: ").strip()
    if operation not in ("+", "-", "*", "/"):
        print("That operation is not supported.")
        return

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    else:
        if second_number == 0:
            print("Cannot divide by zero.")
            return
        result = first_number / second_number

    print(f"{first_number:g} {operation} {second_number:g} = {result:g}")


# Name formatter: applies a chosen string formatting style using conditionals.
def name_formatter():
    print("\nName Formatter")
    name = input("Enter a name: ").strip()

    if not name:
        print("No name was entered.")
        return

    print("Choose a format:")
    print("1. Title case")
    print("2. Uppercase")
    print("3. Lowercase")
    choice = input("Choose 1, 2, or 3: ").strip()

    if choice == "1":
        print(f"Formatted name: {name.title()}")
    elif choice == "2":
        print(f"Formatted name: {name.upper()}")
    elif choice == "3":
        print(f"Formatted name: {name.lower()}")
    else:
        print("That format choice is invalid.")


def main():
    print("Welcome to the Personal Mini-Toolkit!")

    while True:
        show_menu()
        choice = input("\nChoose a tool: ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            simple_calculator()
        elif choice == "4":
            name_formatter()
        elif choice == "5":
            print("Thanks for using the toolkit. Goodbye!")
            break
        else:
            print(f'Sorry, "{choice}" is not on the menu. Please choose 1-5.')


if __name__ == "__main__":
    main()
