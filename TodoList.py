def display_menu():
    """Displays the main menu options."""
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

def main():
    tasks = [] 
    
    print("Welcome to your Python To-Do List!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            if not tasks:
                print("\n✨ Your to-do list is currently empty!")
            else:
                print("\n--- Your Tasks ---")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == '2':
            new_task = input("\nEnter the new task: ")
            tasks.append(new_task)
            print(f"✅ '{new_task}' has been added.")
        elif choice == '3':
            if not tasks:
                print("\nThere are no tasks to remove!")
                continue 
            try:
                task_num = int(input("\nEnter the number of the task to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"🗑️ '{removed_task}' has been removed.")
                else:
                    print("⚠️ Invalid task number.")
            except ValueError:
                print("⚠️ Please enter a valid number, not text.")
        elif choice == '4':
            print("\nExiting the To-Do List. Have a highly productive day! 👋")
            break 
        else:
            print("\n⚠️ Invalid choice. Please type 1, 2, 3, or 4.")
if __name__ == "__main__":
    main()