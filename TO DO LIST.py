import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry('450x350')

        FONT='bold'

        self.task_entry = tk.Entry(root, width=40,borderwidth=5)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_option = tk.Button(root, text="Add Task",font=FONT, command=self.add_task,background='light green')
        self.add_option.grid(row=0, column=1, padx=10, pady=10)

        self.task_storebox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_storebox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.update_option = tk.Button(root, text="Update Task",font=FONT, command=self.update_task,background='pink')
        self.update_option.grid(row=2, column=0, padx=10, pady=10)

        self.delete_option = tk.Button(root, text="Delete Task",font=FONT, command=self.remove_task,background='red')
        self.delete_option.grid(row=2, column=1, padx=10, pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_storebox.insert(tk.END, task)
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please Enter Any task")

    def update_task(self):
        selected_index = self.task_storebox.curselection()
        if selected_index:
            task = self.task_entry.get()
            if task:
                self.tasks[selected_index[0]] = task
                self.task_storebox.delete(selected_index[0])
                self.task_storebox.insert(selected_index[0], task)
                self.save_tasks()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a task.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def remove_task(self):
        selected_index = self.task_storebox.curselection()
        if selected_index:
            removed_task = self.tasks.pop(selected_index[0])
            self.task_storebox.delete(selected_index[0])
            self.save_tasks()
            messagebox.showinfo("Task Deleted", f"Task '{removed_task}' Deleted")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to Delete.")

    def save_tasks(self):
        with open("todolist.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("todolist.txt", "r") as file:
                tasks = file.readlines()
                self.tasks = [task.strip() for task in tasks]
                for task in self.tasks:
                    self.task_storebox.insert(tk.END, task)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
