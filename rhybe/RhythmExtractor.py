import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import sys
from .WAVFile import WAVFile

class RhythmExtractor:
  def __init__(self, wavfile, min_peak_distance, min_peak_height, num_measures, subdivision):
    self.wavfile = wavfile
    self.min_peak_distance = min_peak_distance
    self.min_peak_height = min_peak_height
    self.num_measures = num_measures
    self.subdivision = subdivision

  def get_hit_times_(self):
      hits, _ = find_peaks(self.wavfile.get_signal(), distance=self.min_peak_distance, height=self.min_peak_height)
      hit_times = np.array(hits / self.wavfile.get_framerate())

      return hit_times
  

  def plot_hits(self):
    hits, _ = find_peaks(self.wavfile.get_signal(), distance=self.min_peak_distance, height=self.min_peak_height)
    time = np.linspace(0, self.wavfile.get_num_total_frames() / self.wavfile.get_framerate(), num=self.wavfile.get_num_total_frames())

    signal = self.wavfile.get_signal()

    plt.plot(time, signal) 
    plt.plot(time[hits], signal[hits], "x")
    plt.show()

  ##
  # Returns the partials for which there was a hit. A partial is a single subdivision of a measure, or a beat.
  # For example, if we have 2 measures with 16 subdivisions, we would have 32 partials.
  # i.e., we would be be looking at thirty-two 16th notes, and which of those 16th notes had a hit during the 2 measures.
  #
  # @return beats: a list of booleans, where True indicates that there was a hit during that partial
  #
  def get_hit_partials(self):
      partials = np.linspace(0, self.wavfile.get_duration(), num=self.subdivision * self.num_measures)
      timed_hits = self.get_hit_times_()

      beats = [False] * len(partials)
      for i, hit in enumerate(timed_hits):
          distance = float('inf')
          partial_i = -1
          for j, partial in enumerate(partials):
              cur_dist = abs(hit - partial)
              if cur_dist < distance and beats[j] == False:
                  distance = cur_dist
                  partial_i = j


          beats[partial_i] = True    

      return beats 
