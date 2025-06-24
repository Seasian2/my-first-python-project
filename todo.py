tasks = []

def show_menu():
    print("\n --- TO-DO LIST MENU ---")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Delete tasks")
    print("4. Exit")


def add_task():
    task = input("Enter your task:")
    tasks.append(task)
    print("Completed. Task added.")

def view_task():
    if not tasks:
        print("No tasks yet.")

    else:
        for i, task in enumerate(tasks, 1):
            print(f"{1}. {task}")


def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(task):
        removed = tasks.pop(index)
        print(f"Task Removed: {removed}")

    else:
        print("Invalid task number.")


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid option. Try again.")
    