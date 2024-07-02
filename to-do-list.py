import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        # Create task listbox
        self.task_listbox = tk.Listbox(self.root, width=50, height=10, borderwidth=2, relief="groove")
        self.task_listbox.pack(pady=10)

        # Create entry for new task
        self.new_task_entry = tk.Entry(self.root, width=50, borderwidth=2, relief="groove")
        self.new_task_entry.pack()

        # Create buttons
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_task_button.pack()

        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack()

        self.track_task_button = tk.Button(self.root, text="Track Task", command=self.track_task)
        self.track_task_button.pack()

    def add_task(self):
        task_description = self.new_task_entry.get().strip()
        if task_description:
            self.tasks.append(task_description)
            self.task_listbox.insert(tk.END, task_description)
            self.new_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            updated_description = self.new_task_entry.get().strip()
            if updated_description:
                self.tasks[selected_task_index] = updated_description
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, updated_description)
                self.new_task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Updated task description cannot be empty.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def track_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task_description = self.tasks[selected_task_index]
            messagebox.showinfo("Task Details", f"Task: {task_description}")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to track.")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
