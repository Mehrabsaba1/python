import csv
import os

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Priority: {self.priority}"

class ToDoList:
    def __init__(self, filename="tasks.csv"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                print(f"Task '{task_name}' removed successfully.")
                return
        print(f"Task '{task_name}' not found.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        print("\nCurrent tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def save_tasks(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'description', 'priority'])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority])
        print("Tasks saved to file.")

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.tasks = []
            for row in reader:
                task = Task(row['name'], row['description'], row['priority'])
                self.tasks.append(task)

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Save tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Task name: ").strip()
            description = input("Task description: ").strip()
            priority = input("Priority (High/Medium/Low): ").strip().capitalize()
            if priority not in ['High', 'Medium', 'Low']:
                print("Invalid priority. Setting priority to 'Low' by default.")
                priority = 'Low'
            task = Task(name, description, priority)
            todo_list.add_task(task)

        elif choice == '2':
            name = input("Enter the name of the task to remove: ").strip()
            todo_list.remove_task(name)

        elif choice == '3':
            todo_list.show_tasks()

        elif choice == '4':
            todo_list.save_tasks()

        elif choice == '5':
            todo_list.save_tasks()
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
