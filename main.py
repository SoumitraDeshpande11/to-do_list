

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def delete_task(task_number):
    try:
        removed_task = tasks.pop(task_number - 1)
        print(f"Deleted task: {removed_task}")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a task: ")
            add_task(task)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
