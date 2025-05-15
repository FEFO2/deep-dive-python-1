import csv

# 0 - Welcome function (only beginning) 
def welcome():
    print()
    print()
    print("Welcome! ¿What would you like to do today?")

# 0 - Main Menu function
def main_menu():
    while True:
        print()
        print("   1. Add one task")
        print("   2. Delete a task")
        print("   3. Print current list of tasks")
        print("   4. Save to todos.csv")
        print("   5. Load from todos.csv")
        print("   6. Exit")
        print()
        # Solicita al usuario una opción
        choice = input("Select an option: ")
        if choice.isdigit():
            number = int(choice)
            if 1 <= number <= 6:
                return number
        print()
        print("Invalid option, try again")

# 1 - Add task function
def add_one_task(title):
    todo_list.append(title)
    print()
    print("¡task added successfully!")

# 2 - Delete task function
def delete_task(number_to_delete):
    while True:
        if number_to_delete.isdigit():
            choice = int(number_to_delete)
            if 0 < choice <= len(todo_list):
                todo_list.pop(choice -1)
                print()
                print("¡Task deleted successfully!")
                return
        print("Invalid option, try again")
        print()
        number_to_delete = input("Which task would you like to delete? ")

# 3 - Print todo list function
def print_list():
    if len(todo_list) == 1:
            print(f"This is your only task for today: ")
            print()
            for i, x in enumerate(todo_list,start=1):
                print(f"{i}. {x}")   
    else: 
        print(f"This is your TODO list for today ({len(todo_list)}):")
        print()
        for i, x in enumerate(todo_list,start=1):
            print(f"{i}. {x}")   

#  4 - Export todo list function:
def save_todos(list):
    with open("to_do_list/todos.csv",mode="w",newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(list)
    print("TODO list saved successfully!")

#  5 - Import todo list function:
def load_todos():
    try:
        with open("to_do_list/todos.csv",mode="r",encoding="utf-8") as file:
            lector = list(csv.reader(file))
            result = lector[0]
            print("TODO list loaded successfully!")
            return result
    except FileNotFoundError: 
        print("Sorry, there is no TODO list available")
# ---------------------
welcome()
todo_list = []
while True:
    number = main_menu()
    if number == 1:
        print()
        add_one_task(input("¿What is your task title? "))   
    elif number == 2:
        if len(todo_list) != 0:
            print()
            print_list()
            print()
            delete_task(input("Which task would you like to delete? "))
        else:
            print()
            print("There are no tasks to delete.")
    elif number == 3:
        if len(todo_list) != 0:
            print()
            print_list()
        else: 
            print()
            print("There are no tasks to display.")
    elif number == 4:
        if len(todo_list) != 0:
            print()
            save_todos(todo_list)
        else: 
            print()
            print("¡There is no TODO list to save!")
    elif number == 5:
        print()
        todo_list = load_todos()
    elif number == 6:
        print()
        print("See you next time!")
        print()
        break
