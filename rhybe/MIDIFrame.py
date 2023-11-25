import customtkinter
from tkinter import filedialog as fd
from .WAVFile import WAVFile
from .MIDIHelper import write_hit_partials_to_midi
from .event import post_event
from .LabledEntry import LabeledEntry

class MIDIFrame:
  def __init__(self, parent_frame):
    self.parent_frame = parent_frame
    self.tempo = 60

  def render(self):
    self.frame = customtkinter.CTkFrame(self.parent_frame)
    self.frame.grid(row=0, column=0, sticky="nsew")

    button = customtkinter.CTkButton(self.frame, text="Open WAV File", font=("Roboto", 16), command=lambda: self.open_wavfile_for_transcription())
    button.grid(row=0, column=0, pady=20, padx=20)

    tempo_entry = LabeledEntry(self.frame, "Tempo", self.tempo, lambda value: self.set_tempo(value))
    tempo_entry.get_widget().grid(row=1, column=0, pady=20, padx=20)

    button = customtkinter.CTkButton(self.frame, text="Generate MIDI", font=("Roboto", 16), command=lambda: self.generate_midi_file())
    button.grid(row=2, column=0)

  def set_tempo(self, tempo):
    self.tempo = tempo

  def open_wavfile_for_transcription(self):
    filename = fd.askopenfilename()
    wavfile = WAVFile(filename)
    post_event("wavfile_opened", {"wavfile": wavfile, "filename": filename})

  def generate_midi_file(self):
    filename = fd.asksaveasfilename(confirmoverwrite=True, defaultextension=".mid")
    write_hit_partials_to_midi(self.rhythm_extractor.get_hit_partials(), 60, filename)