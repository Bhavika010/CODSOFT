import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", width=48, command=self.add_task)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(root, text="Edit Task", width=48, command=self.edit_task)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", width=48, command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.load_button = tk.Button(root, text="Load Tasks", width=48, command=self.load_tasks)
        self.load_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Tasks", width=48, command=self.save_tasks)
        self.save_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def edit_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            new_task = simpledialog.askstring("Edit Task", "Edit the selected task:", initialvalue=self.tasks[selected_task_index])
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, new_task)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = file.read().splitlines()
                self.listbox.delete(0, tk.END)
                for task in self.tasks:
                    self.listbox.insert(tk.END, task)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No saved tasks found.")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        messagebox.showinfo("Info", "Tasks saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
