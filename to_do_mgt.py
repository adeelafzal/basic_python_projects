import json

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks":[]}


def save_task(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file)
    except Exception as e:
        print("Failed to save", e)


def view_taks(tasks):
    print("\nAll Tasks")
    for index, task in enumerate(tasks["tasks"]):
        print(f"{index+1}: {task["desc"]} Status: {task["completed"]}")


def create_task(tasks):
    desc = input("Enter task description: ").strip()
    if desc:
        tasks["tasks"].append({"desc":desc, "completed": False})
        save_task(tasks)
        print("Task saved")
    else:
        print("Description cannot be empty")


def mark_task_complete(tasks):
    view_taks(tasks)
    choice = input("Enter the task number for complete: ")
    if choice.isdigit:
        user_choice = int(choice)
        tasks["tasks"][user_choice-1]["completed"] = True
        save_task(tasks)
    else:
        print("Invalid choice")


def main():
    tasks = load_tasks()

    while True:
        print("\nToDoList Manger")
        print("1. View taks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_taks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("\nGood Bye")
            break
        else:
            print("\nInvalid input")


main()