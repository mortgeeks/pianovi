from music21 import *
notes = "A0 B0 C1 D1 F1 E1 G1 A1 B1 C2 D2 F2 E2 G2 A2 B2 C3 D3 F3 E3 G3 A3 B3 C4 D4 F4 E4 G4 A4 B4 C5 D5 F5 E5 G5 A5 B5 C6 D6 F6 E6 G6 A6 B6 C7 D7 F7 E7 G7 A7 B7 C8"
notess = "A#0 C#1 D#1 F#1 G#1 A#1 C#2 D#2 F#2 G#2 A#2 C#3 D#3 F#3 G#3 A#3 C#4 D#4 F#4 G#4 A#4 C#5 D#5 F#5 G#5 A#5 C#6 D#6 F#6 G#6 A#6 C#7 D#7 F#7 G#7 A#7"
notesl = ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1', 'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6', 'C7', 'D7', 'E7', 'F7', 'G7', 'A7', 'B7', 'C8']
notessl = ['A#0', 'C#1', 'D#1', 'F#1', 'G#1', 'A#1', 'C#2', 'D#2', 'F#2', 'G#2', 'A#2', 'C#3', 'D#3', 'F#3', 'G#3', 'A#3', 'C#4', 'D#4', 'F#4', 'G#4', 'A#4', 'C#5', 'D#5', 'F#5', 'G#5', 'A#5', 'C#6', 'D#6', 'F#6', 'G#6', 'A#6', 'C#7', 'D#7', 'F#7', 'G#7', 'A#7']
def gennotes():
	s = stream.Stream()
	for n in notesl:
		ns = note.Note(n)
		s.append(ns)
		mf = midi.translate.streamToMidiFile(s)
		mf.open(n+'.mid', 'wb')
		mf.write()
		mf.close()
		print('created '+ n)
		s.remove(ns)
	for n in notessl:
		ns = note.Note(n)
		s.append(ns)
		mf = midi.translate.streamToMidiFile(s)
		mf.open(n+'.mid', 'wb')
		mf.write()
		mf.close()
		print('created '+ n)
		s.remove(ns)
gennotes()
