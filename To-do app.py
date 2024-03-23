import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        tk.Label(master, text="Task:").grid(row=0, column=0, padx=5, pady=5)
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(master, text="Due Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(master, width=20)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(master, text="Due Time (HH:MM):").grid(row=2, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(master, width=10)
        self.time_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        self.task_list = tk.Listbox(master, width=50)
        self.task_list.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=4, column=0, padx=5, pady=5)

        self.done_button = tk.Button(master, text="Mark as Done", command=self.mark_as_done)
        self.done_button.grid(row=4, column=1, padx=5, pady=5)

        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=4, column=2, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        due_date = self.date_entry.get().strip()
        due_time = self.time_entry.get().strip()
        
        if task:
            due_datetime = None
            if due_date and due_time:
                try:
                    due_datetime = datetime.strptime(due_date + " " + due_time, "%Y-%m-%d %H:%M")
                except ValueError:
                    messagebox.showwarning("Warning", "Invalid date or time format! Please use YYYY-MM-DD for date and HH:MM for time.")
                    return
            
            task_with_datetime = (task, due_datetime)
            self.tasks.append(task_with_datetime)
            self.task_list.insert(tk.END, f"{task} (Due: {due_datetime})" if due_datetime else task)
            self.task_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            self.task_list.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def mark_as_done(self):
        try:
            index = self.task_list.curselection()[0]
            task, due_datetime = self.tasks[index]
            if due_datetime:
                task = f"{task} (Done - Due: {due_datetime})"
            else:
                task = f"{task} (Done)"
            self.task_list.delete(index)
            self.task_list.insert(index, task)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as done!")

    def clear_tasks(self):
        self.task_list.delete(0, tk.END)
        self.tasks = []

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()