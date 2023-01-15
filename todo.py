import json

class ToDoList:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.completed_tasks = []
        self.num_tasks = 0
        self.read_tasks_from_file()

    def add_task(self, task):
        self.tasks.append(task)
        self.num_tasks += 1
        self.write_tasks_to_file()

    def mark_task_complete(self, task):
        self.tasks.remove(task)
        self.completed_tasks.append(task)
        self.num_tasks -= 1
        self.write_tasks_to_file()

    def display_tasks(self):
        print("Tasks in list '{}':".format(self.name))
        for task in self.tasks:
            print("- {}".format(task))

    def display_completed_tasks(self):
        print("Completed Tasks in list '{}':".format(self.name))
        for task in self.completed_tasks:
            print("- {}".format(task))

    def write_tasks_to_file(self):
        tasks = {'tasks': self.tasks, 'completed_tasks': self.completed_tasks}
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file)
    def read_tasks_from_file(self):
        try:
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)
                self.tasks = tasks['tasks']
                self.completed_tasks = tasks['completed_tasks']
                self.num_tasks = len(self.tasks)
        except FileNotFoundError:
            # If the file doesn't exist, it means that no tasks have been added yet
            pass

if __name__ == "__main__":
    my_list = ToDoList("My To-Do List")

    while True:
        print("1. Add task")
        print("2. Mark task as complete")
        print("3. Display tasks")
        print("4. Display completed tasks")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter task: ")
            my_list.add_task(task)
        elif choice == 2:
            task = input("Enter task to mark as complete: ")
            my_list.mark_task_complete(task)
        elif choice == 3:
            my_list.display_tasks()
        elif choice == 4:
            my_list.display_completed_tasks()
        elif choice == 5:
            break
        else:
            print("Invalid choice.")










