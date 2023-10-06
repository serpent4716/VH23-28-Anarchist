import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Drop-down List Example")

# Function to be executed when the selection changes
def on_selection_change(event):
    selected_item = combo_box.get()
    label.config(text=f"You selected: {selected_item}")

# Create a label
label = tk.Label(root, text="Explore Your way through!")
label.pack(pady=10)

# Create a list of items for the drop-down
items = ["Java", "Python", "Prolog", "Pearl", "C++"]

# Create a drop-down list
combo_box = ttk.Combobox(root, values=items)
combo_box.pack(pady=10)
combo_box.set(items[0])  # Set the default selected item

# Bind the function to the drop-down list's <<ComboboxSelected>> event
combo_box.bind("<<ComboboxSelected>>", on_selection_change)

# Start the main loop
root.mainloop()
