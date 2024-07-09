'''Saran Joel Marrikanti
 C0933950

 '''

import datetime
#this is the menu where we get to make the choice
def print_menu():
    print("\nWelcome to the Task Manager!\n")
    print("Please choose an option:")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Search for a task by title")
    print("5. Exit")

#adding task to the list tasks
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter task due date (YYYY-MM-DD): ")
#using exceptional handelling for handelling errors
    #using try and execption to chatch errors
    try:
        datetime.datetime.strptime(due_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid due date format. Please use YYYY-MM-DD.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date
    }
    tasks.append(task)#appending the task to list
    print("Task added successfully!")

#Removing tha task based on the title
def remove_task(tasks):
    title = input("Enter the title of the task to remove: ")
    for task in tasks:
        if task["title"].lower() == title.lower():
            tasks.remove(task)
            print("Task removed successfully!")
            return
    print("Task not found.")

#Viewing all the task that are present
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")

#searching for a prticular task in the list
def search_task(tasks):
    title = input("Enter the title of the task to search for: ")
    found_tasks = [task for task in tasks if title.lower() in task["title"].lower()]#we use list comprehension the new list is task is
    #being strored in the list found_task

    if not found_tasks:
        print("No tasks found with that title.")
        return

    for i, task in enumerate(found_tasks, 1):
        print(f"{i}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")

#main this is where teh logic happens it is the strat of the programs
def main():
    tasks = []
    while True:
        print_menu()#calling printmenu funtion
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            search_task(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

#calling the main function
main()
