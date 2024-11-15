import tkinter as tk
from tkinter import ttk
from tkinter import font



window=tk.Tk()
window.title("My Todo List")
window.configure(bg="grey")

window.geometry("500x550")

def add_task():
    task = entry_task.get()
    if task:
        
        add_task_item(task)
        entry_task.delete(0,tk.END)
    else:
        entry_task.delete(0, tk.END)
        entry_task.insert(0, "Write your task here:")
        entry_task.configure(fg="black")

def add_task_item(task):      
    # Create a frame inside the task_list_frame to hold each task and its buttons
    task_frame = tk.Frame(task_list_frame, bg="white")
    task_frame.pack(fill=tk.X, pady=2)

# label for the task

    task_label = tk.Label(task_frame, text=task, font=("Garamond",16), bg= "white", anchor="w", width=20, height=1)
    task_label.pack(side=tk.LEFT, fill= tk.X, padx= 5, anchor = "w")

# edit button

    edit_button = tk.Button(task_frame, text="Edit", command=lambda t=task: edit_task(t), bg="#E31248", fg="white", height=1, width = 8, font=("Roboto",10) , relief=tk.FLAT)
    edit_button.pack(side=tk.RIGHT,padx=5, pady=2)

# delete button

    delete_button = tk.Button(task_frame, text="Delete", command=lambda f= task_frame, l = task_label.cget("text"): delete_task(f, l), bg="blue", fg="white", height=1, width = 10, font=("Roboto",11) , relief=tk.FLAT)
    delete_button.pack(side=tk.RIGHT,padx=5, pady=2) 

    # checkbox to mark task as completed

    checkbutton = ttk.Checkbutton(task_frame, text="", command=lambda label = task_label: toggle_strike(label))
    checkbutton.pack(side=tk.RIGHT)

    # Update the canvas scroll region
    task_list_canvas.update_idletasks()
    task_list_canvas.config(scrollregion=task_list_canvas.bbox("all"))


def edit_task(task):
    entry_task.delete(0, tk.END)
    entry_task.insert(0, task)

def delete_task(task_frame, task_label_text):
    task_frame.destroy()
   # Update the canvas scroll region
    task_list_canvas.update_idletasks()
    task_list_canvas.config(scrollregion=task_list_canvas.bbox("all"))

def toggle_strike(label):
    current_font = label.cget("font")
    if "overstrike" in current_font:
        new_font = current_font.replace("overstrike", "")
    else:
        new_font = current_font+" overstrike"    
        label.config(font=new_font)

def on_entry_click(event):
    if entry_task.get() == "Write your task here:":
        entry_task.delete(0, tk.END)
        entry_task.configure(fg="black")

def on_focus_out(event):
    if not entry_task.get().strip():
        entry_task.delete(0, tk.END)
        entry_task.insert(0, "Write your task here:")
        entry_task.configure(fg="black")



# create a heading font
heading_font = font.Font(family = "Garamond", size = 20, weight= "bold")
#  creating a heading label
heading_label = tk.Label(window, text = "My Todo List", font = heading_font, bg="grey")
heading_label.pack(pady = 20)

frame = tk.Frame(window)
frame.configure(bg="grey")
frame.pack(pady=20)

entry_task = tk.Entry(frame, font= ("Garamond", 10), relief=tk.FLAT, bg= "white")
entry_task.insert(0,"write your task here:")
entry_task.bind("<FocusIn>", on_entry_click)
entry_task.bind("<FocusOut>", on_focus_out)
entry_task.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task, bg="#E31248", fg="white", height=1, width = 10, font=("Roboto",11) , relief=tk.FLAT)
add_button.pack(side=tk.LEFT,padx=0)

# Canvas for scrolling task list
task_list_canvas = tk.Canvas(window, bg="white", height=300, bd=0, highlightthickness=0)
task_list_canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Scrollbar for the task list
scrollbar = tk.Scrollbar(window, orient="vertical", command=task_list_canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Frame to hold the tasks inside the canvas
task_list_frame = tk.Frame(task_list_canvas, bg="white")
task_list_canvas.create_window((0, 0), window=task_list_frame, anchor="nw")
task_list_canvas.config(yscrollcommand=scrollbar.set)


window.mainloop()
