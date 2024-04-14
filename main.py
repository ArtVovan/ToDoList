import datetime


# Function to add a task to the list
def addTask(tasks):
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")


# Function to list tasks from the list
def listTasks(tasks):
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"Task #{index}: {task}")


# Function to delete a task from the list
def deleteTask(tasks):
    listTasks(tasks)
    try:
        taskToDelete = int(input("Enter the task number to delete: ")) - 1
        if 0 <= taskToDelete < len(tasks):
            deleted_task = tasks.pop(taskToDelete)
            print(f"Task '{deleted_task}' has been removed.")
        else:
            print(f"Task #{taskToDelete + 1} does not exist.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Function to save tasks to a file
def saveTasks(name, date, tasks):
    try:
        with open('tasks.txt', 'a') as f:
            f.write(f'{name} - {date.strftime("%Y-%m-%d %H:%M:%S")} \nTasks:\n')
            for task in tasks:
                f.write(f'- {task}\n')
        print("Tasks saved to \"tasks.txt\"")
    except Exception as e:
        print(f"An error occurred while saving tasks: {str(e)}")


if __name__ == "__main__":
    name = input("Hello, let's start. To begin, enter your name: ").strip().capitalize()
    current_datetime = datetime.datetime.now()
    tasks = []

    print(f'Welcome to the to-do list, {name} :)')

    while True:
        print("\nPlease select one of the following options:")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask(tasks)
        elif choice == "2":
            deleteTask(tasks)
        elif choice == "3":
            listTasks(tasks)
        elif choice == "4":
            saveTasks(name, current_datetime, tasks)
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye 👋👋")
