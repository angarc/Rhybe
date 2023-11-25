import customtkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
from .RhythmExtractor import RhythmExtractor
from .LabledEntry import LabeledEntry

class RhythmFrame:
  def __init__(self, parent_frame):
    self.parent_frame = parent_frame
    self.rhythm_extractor = None
    self.filename_label = None
    self.default_rhythm_extractor_opts = {
      "min_peak_distance": 5000,
      "min_peak_height": 5000,
      "num_measures": 1,
      "subdivision": 16
    }

    self.plot_frame = None
    self.plot_canvas = None
    self.toolbar = None

  def render(self):
    self.frame = customtkinter.CTkFrame(self.parent_frame, width=200, fg_color="transparent")
    self.frame.grid(row=0, column=1, sticky="nsew", padx=20)
    self.frame.grid_columnconfigure(0, weight=1)

    self.plot_frame = customtkinter.CTkFrame(self.frame)
    self.plot_frame.grid(row=0, column=0, sticky="nsew")

    self.filename_label = customtkinter.CTkLabel(self.frame, text="", font=("Roboto", 12))
    self.filename_label.grid(row=1, column=0)

    self.parameters_frame = customtkinter.CTkFrame(self.frame)

    height_entry = LabeledEntry(self.parameters_frame, "Min peak height", self.default_rhythm_extractor_opts["min_peak_height"], self.set_min_peak_height)
    height_entry.get_widget().grid(row=0, column=0)

    distance_entry = LabeledEntry(self.parameters_frame, "Min peak distance", self.default_rhythm_extractor_opts["min_peak_distance"], self.set_min_peak_distance)
    distance_entry.get_widget().grid(row=0, column=1)

    measure_entry = LabeledEntry(self.parameters_frame, "Number of measures", self.default_rhythm_extractor_opts["num_measures"], self.set_num_measures)
    measure_entry.get_widget().grid(row=0, column=2)

    subdivision_entry = LabeledEntry(self.parameters_frame, "Subdivision", self.default_rhythm_extractor_opts["subdivision"], self.set_subdivision)
    subdivision_entry.get_widget().grid(row=0, column=3)

    self.parameters_frame.grid_columnconfigure(0, weight=1)
    self.parameters_frame.grid_columnconfigure(1, weight=1)
    self.parameters_frame.grid_columnconfigure(2, weight=1)
    self.parameters_frame.grid_columnconfigure(3, weight=1)
    self.parameters_frame.grid_rowconfigure(0, weight=1)

  def render_paramter_entries(self):
    self.parameters_frame.grid(row=2, column=0, ipady=10, ipadx=15, sticky="ew")

  def set_wavfile(self, wavfile):
    self.rhythm_extractor = RhythmExtractor(
      wavfile, 
      self.default_rhythm_extractor_opts["min_peak_distance"],
      self.default_rhythm_extractor_opts["min_peak_height"],
      self.default_rhythm_extractor_opts["num_measures"], 
      self.default_rhythm_extractor_opts["subdivision"])

  def set_filename_label_text(self, text):
    self.filename_label.configure(text=text)

  def set_min_peak_height(self, min_peak_height):
    self.rhythm_extractor.set_min_peak_height(min_peak_height)
    self.update_plot()

  def set_min_peak_distance(self, min_peak_distance):
    self.rhythm_extractor.set_min_peak_distance(min_peak_distance)
    self.update_plot()

  def set_num_measures(self, num_measures):
    self.rhythm_extractor.set_num_measures(num_measures)
    self.update_plot()

  def set_subdivision(self, subdivision):
    self.rhythm_extractor.set_subdivision(subdivision)
    self.update_plot()

  def update_plot(self):
    fig = self.rhythm_extractor.get_plot_figure()

    if self.plot_canvas is not None:
      self.plot_canvas.get_tk_widget().destroy()

    self.plot_frame.grid_columnconfigure(0, weight=1)
    self.plot_canvas = FigureCanvasTkAgg(fig, master = self.plot_frame)

    if self.toolbar is not None:
      self.toolbar.destroy()

    self.toolbar_frame = customtkinter.CTkFrame(self.plot_frame)
    self.toolbar_frame.grid(row=1, column=0, sticky="nsew")

    self.toolbar = NavigationToolbar2Tk(self.plot_canvas, self.toolbar_frame) 
    self.plot_canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew") 
    self.toolbar.update()
