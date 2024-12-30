import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

class TodoList:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("593x380")
        self.root.resizable(0, 0)

        self.tasks = [[],[],[],[],[],[],[]]
        self.days_key = {"Sunday":0,"Monday":1, "Tuseday":2, "Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
        self.load_tasks()

        self.ct = tk.Frame(self.root)
        self.ct.grid(row=0, column=0,rowspan=2, columnspan=10,sticky='nwes')
        self.ct2 = tk.Frame(self.root)
        self.ct2.grid(row=2, column=0,rowspan=6,columnspan=10, sticky='nwes')
        
        self.label = tk.Label(self.ct, text="Enter a task:", font=("Arial", 15))
        self.label.grid(row=0, column=0, columnspan=2,padx=10, pady=10,sticky='nwes')
        self.task_entry = tk.Entry(self.ct, font=("Arial", 15))
        self.task_entry.grid(row=0, column=2, columnspan=4,padx=10, pady=10,sticky='nwes')
        self.combobox = ttk.Combobox(self.ct, values=["Sunday","Monday", "Tuseday", "Wednesday","Thursday","Friday","Saturday"], font=("Arial", 10))
        self.combobox.current(0)
        self.combobox.grid(row=0, column=6,padx=5, pady=10,sticky='nwes')
        

        self.add_button = tk.Button(self.ct, text="Add Task", font=("Arial", 15), width=10,command=self.add_task)
        self.add_button.grid(row=1, column=0, columnspan=2,padx=10, pady=10,sticky='nwes')

        self.delete_button = tk.Button(self.ct, text="Delete Task", font=("Arial", 15),width=10, command=self.delete_task)
        self.delete_button.grid(row=1, column=2, columnspan=2,padx=10, pady=10,sticky='nwes')

        self.update_button = tk.Button(self.ct, text="Update Task", font=("Arial", 15),width=10, command=self.update_task)
        self.update_button.grid(row=1, column=4, columnspan=2,padx=10, pady=10,sticky='nwes')

        self.task_listbox = tk.Listbox(self.ct2, font=("Arial", 15), width=50, height=10)
        self.task_listbox.grid(row=0, column=0,rowspan=10 ,columnspan=10,padx=10, pady=10,sticky='nwes')
        self.scrollbar = tk.Scrollbar(self.ct2, orient="vertical", command=self.task_listbox.yview)
        self.scrollbar.grid(row=0, column=10,rowspan=10,sticky='nwes')
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.show_tasks()
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks[self.days_key[self.combobox.get()]].append(task)
            self.save_tasks()
            self.show_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[self.days_key[self.combobox.get()]][selected_task_index]
            self.save_tasks()
            self.show_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[self.days_key[self.combobox.get()]][selected_task_index] = new_task
                self.save_tasks()
                self.show_tasks()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks[self.days_key[self.combobox.get()]]:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = [[],[],[],[],[],[],[]]

def select_list():
    pass

if __name__ == "__main__":
    root = tk.Tk()
    Sun = TodoList(root)
    Mon = TodoList(root)
    Tue = TodoList(root)
    Wed = TodoList(root)
    Thu = TodoList(root)
    Fri = TodoList(root)
    Sat = TodoList(root)    
    
    root.mainloop()