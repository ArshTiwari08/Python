tasks = []

while True:
    print("\nTO-DO LIST MENU")
    print("1. Add Task  2. View Tasks  3. Remove Task  4. Exit")

    choice = input("Enter choice: ").strip().lower()

    if choice in ['1', 'add']:
        tasks.append(input("Enter a task: "))
        print("Task added!")

    elif choice in ['2', 'view']:
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice in ['3', 'remove']:
        if not tasks:
            print("No tasks to remove.")
        else:
            try:
                num = int(input("Task number to remove: "))
                if 1 <= num <= len(tasks):
                    print(f"Removed '{tasks.pop(num - 1)}'")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

    elif choice in ['4', 'exit']:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Use 1-4 or add/view/remove/exit.")
