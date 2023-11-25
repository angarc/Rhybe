import customtkinter 
from .RhythmFrame import RhythmFrame
from .MIDIFrame import MIDIFrame
from .event import subscribe, post_event
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class RhybeUI():
  rhythm_frame = None
  midi_frame = None
  rhythm_extractor = None
  frame = None
  filename_label = None

  def __init__(self):
    subscribe("wavfile_opened", lambda data: self.handle_wavfile_opened(data))

  def start(self):
    root = customtkinter.CTk()
    root.geometry("860x640")
    root.title("Rhybe")

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)

    self.midi_frame = MIDIFrame(root) 
    self.midi_frame.render()

    self.rhythm_frame = RhythmFrame(root)
    self.rhythm_frame.render()

    root.mainloop() 

  def handle_wavfile_opened(self, data):
    self.rhythm_frame.set_wavfile(data["wavfile"])
    self.rhythm_frame.set_filename_label_text(f"file: {data['filename']}")
    self.rhythm_frame.update_plot()
    self.rhythm_frame.render_paramter_entries()
    
    