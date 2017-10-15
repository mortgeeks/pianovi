from music21 import *
notes = "C2 D2 F2 E2 G2 A2 B2 C3 D3 F3 E3 G3 A3 B3 C4 D4 F4 E4 G4 A4 B4 C5 D5 F5 E5 G5 A5 B5 C6 D6 F6 E6 G6 A6 B6 C7"
notesl = ['C2', 'D2', 'F2', 'E2', 'G2', 'A2', 'B2', 'C3', 'D3', 'F3', 'E3', 'G3', 'A3', 'B3', 'C4', 'D4', 'F4', 'E4', 'G4', 'A4', 'B4', 'C5', 'D5', 'F5', 'E5', 'G5', 'A5', 'B5', 'C6', 'D6', 'F6', 'E6', 'G6', 'A6', 'B6', 'C7']
notess = "C#2 D#2 F#2 G#2 A#2 C#3 D#3 F#3 G#3 A#3 C#4 D#4 F#4 G#4 A#4 C#5 D#5 F#5 G#5 A#5 C#6 D#6 F#6 G#6 A#6"
notessl = ['C#2', 'D#2', 'F#2', 'G#2', 'A#2', 'C#3', 'D#3', 'F#3', 'G#3', 'A#3', 'C#4', 'D#4', 'F#4', 'G#4', 'A#4', 'C#5', 'D#5', 'F#5', 'G#5', 'A#5', 'C#6', 'D#6', 'F#6', 'G#6', 'A#6']

def gennotes():
	s = stream.Stream()
	for n in notesl:
		ns = note.Note(n)
		s.append(ns)
		mf = midi.translate.streamToMidiFile(s)
		mf.open(n+'.mid', 'wb')
		mf.write()
		mf.close()
	for n in notessl:
		ns = note.Note(n)
		s.append(ns)
		mf = midi.translate.streamToMidiFile(s)
		mf.open(n+'.mid', 'wb')
		mf.write()
		mf.close()
gennotes()
