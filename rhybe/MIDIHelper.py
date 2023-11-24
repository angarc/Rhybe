from midiutil import MIDIFile

def write_hit_partials_to_midi(hit_partials, tempo, output_filename):
    track    = 0
    channel  = 0
    time     = 0    # In beats
    duration = 1    # In beats
    volume   = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
    MyMIDI.addTempo(track, time, tempo)

    for i, beat in enumerate(hit_partials):
        if beat:
            MyMIDI.addNote(track, channel, 38, i/4.0, duration, volume)

    with open(output_filename, "wb") as output_file:
        MyMIDI.writeFile(output_file)