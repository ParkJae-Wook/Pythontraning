import tkinter as tk
from tkinter import messagebox
import json

class TodoList:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("600x400")
        self.root.resizable(0, 0)

        self.tasks = []
        self.load_tasks()

        self.task_entry = tk.Entry(self.root, font=("Arial", 15))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", font=("Arial", 15), command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", font=("Arial", 15), command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Task", font=("Arial", 15), command=self.update_task)
        self.update_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, font=("Arial", 15), width=50, height=10)
        self.task_listbox.pack(pady=10)
        self.show_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.save_tasks()
            self.show_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.save_tasks()
            self.show_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.save_tasks()
                self.show_tasks()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoList(root)
    root.mainloop()