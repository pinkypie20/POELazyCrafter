import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox

def on_select(event):
    selected_item = event.widget.get()
    print("Selected item:", selected_item)

root = tk.Tk()
root.title("Autocomplete Combobox Example")

# Sample data
data = ["Apple","ABC", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]

# Create an AutocompleteCombobox
combo = AutocompleteCombobox(root, completevalues=data)
combo.pack(padx=10, pady=10)
combo.bind("<<ComboboxSelected>>", on_select)

root.mainloop()