import customtkinter
from tkinter import messagebox

class LabeledEntry:
  def __init__(self, parent_frame, label_text, placeholder_text, on_change):
    self.parent_frame = parent_frame
    self.label_text = label_text
    self.placeholder_text = placeholder_text
    self.on_change = on_change

    self.frame = customtkinter.CTkFrame(self.parent_frame, fg_color="transparent")

    self.label = customtkinter.CTkLabel(self.frame, text=self.label_text, font=("Roboto", 12), anchor="nw")
    self.label.grid(row=0, column=0, sticky="ew")

    self.entry = customtkinter.CTkEntry(self.frame, font=("Roboto", 16), placeholder_text=self.placeholder_text, fg_color="transparent")
    self.entry.bind("<Return>", lambda event: self.handler(self.entry.get()))
    self.entry.grid(row=1, column=0)

  def handler(self, value):
    if not value.isdigit():
      messagebox.showerror("Error", "Value must be a number")
      return

    self.on_change(int(value))

  def get_widget(self):
    return self.frame