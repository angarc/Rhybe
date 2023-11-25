from .WAVFile import WAVFile
from .RhythmExtractor import RhythmExtractor
from .MIDIHelper import write_hit_partials_to_midi
from .RhybeUI import RhybeUI
import argparse
import customtkinter 
from tkinter import filedialog as fd
import sys

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def main():
  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument('--input_filename', metavar='fi', type=str, help='filename for mono .wav file')
  parser.add_argument('--output_filename', metavar='fo', type=str, help='output midi filename')
  parser.add_argument('--min_peak_distance', metavar='pd', type=int, help='minimum distance between signal peaks')
  parser.add_argument('--min_peak_height', metavar='ph', type=int, help='minimum height of signal peaks')
  parser.add_argument('--num_measures', metavar='m', type=int, help='number of measures in the song')
  parser.add_argument('--subdivision', metavar='s', type=int, help='number of subdivisions per measure')
  parser.add_argument('--tempo', metavar='s', type=int, help='desired tempo of output midi track in BPM')
  parser.add_argument('--plot_only', metavar='p', type=bool, help='plot the peaks and signal')

  args = parser.parse_args()

  ui = RhybeUI()
  ui.start() 

def update_plot(min_peak_height, frame, rhythm_extractor):
  rhythm_extractor.set_min_peak_height(int(min_peak_height))
  rhythm_extractor.plot_hits(frame)


def transcribe(args, filename_label, frame, rhythm_extractor):
  filename = fd.askopenfilename()

  filename_label.configure(text=f"file: {filename}")

  wavfile = WAVFile(filename)
  rhythm_extractor = RhythmExtractor(wavfile, args.min_peak_distance, args.min_peak_height, args.num_measures, args.subdivision)
  rhythm_extractor.plot_hits(frame)

  

  # if args.plot_only:
  #   rhythm_extractor.plot_hits()
  # else:
  #   write_hit_partials_to_midi(rhythm_extractor.get_hit_partials(), args.tempo, args.output_filename)


if __name__ == "__main__":  # pragma: no cover
  sys.exit(main())