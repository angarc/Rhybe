![screenshot of Rhybe UI](https://raw.githubusercontent.com/angarc/Rhybe/main/.github/images/rhybe_ui.png)

# Rhybe

i.e., A Rhythm Transcriber.

A tool that takes mono WAVE files, and converts them to MIDI but only takes into account rhythm.

So all notes in the MIDI file will be middle C.

You can then open this MIDI file and in a notation program like MuseScore and have the rhythm portion of the transcription process done

_at least, that's the idea anyway_

## Why?

I like to transcribe drum videos I like on YouTube. I thought it would be great to have at least the rhythm work done for me, and then I can decide which drums (or cymbals) the individual notes should be meant for. 

## How?

The way it works is by taking a all the samples in the given wave file, and searching for maxima. Then it takes the locations of maxima, and places them into equally divided time slots (I call them "Partials") in the new midi file, roughly corresponding to where they are in the audio file.

You correctly set these partials by providing the number of measures in the audio file, and the number of subdivisions for each measure. 

Ideally, you should set this as close as possible to the actual audio file. For example, if the audio file is two measures of drumming, and the drummer never plays anything more complicated than 16th notes, then you should set the arguments `num_measures=2` and `subdivisions=16` to get the best results. 


## Usage

```
python -m rhybe
```

* `min_peak_height`

There will always be "noise" in the signal. So as to not accidentally take them into account, you can specify a minimum height for which any maxima will have to be greater than for Rhybe to place in a Partial.

* `min_peak_distance`

Distance (or time) between peaks, but measured in frames.

* `num_measures` 

Number of measures in the audio file. This is something you figure out just by listening to it and intuitively figuring out for yourself.

* `subdivision`

Try to keep this number as low as possible. If you only hear 8th notes, then set this to 8. Setting this higher than necessary might place certain notes in the wrong Partials. 

* `tempo`

Desired tempo of the output MIDI file in BPM

