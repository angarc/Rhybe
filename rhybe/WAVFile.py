import wave
import numpy as np
import sys

class WAVFile:
    def __init__(self, filename):
        wav_obj = wave.open(filename, 'rb')
        if wav_obj.getnchannels() == 2:
            print("Mono files only")
            sys.exit(0)

        self.framerate_ = wav_obj.getframerate()
        self.num_total_frames_ = wav_obj.getnframes()
        self.frames_ = np.frombuffer(wav_obj.readframes(-1), dtype=np.int16)

        wav_obj.close()

    def get_signal(self):
        return self.frames_

    def get_duration(self):
        return self.num_total_frames_/self.framerate_

    def get_framerate(self):
        return self.framerate_
    
    def get_num_total_frames(self):
        return self.num_total_frames_