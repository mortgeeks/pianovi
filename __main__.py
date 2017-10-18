import pygame
from pygame.locals import *
from sys import exit
from music21 import *

enkeys = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'COMMA', 'PERIOD', 'SLASH', 'RSHIFT']
notesl = ['A0', 'B0', 'C1', 'D1', 'F1', 'E1', 'G1', 'A1', 'B1', 'C2', 'D2', 'F2', 'E2', 'G2', 'A2', 'B2', 'C3', 'D3', 'F3', 'E3', 'G3', 'A3', 'B3', 'C4', 'D4', 'F4', 'E4', 'G4', 'A4', 'B4', 'C5', 'D5', 'F5', 'E5', 'G5', 'A5', 'B5', 'C6', 'D6', 'F6', 'E6', 'G6', 'A6', 'B6', 'C7', 'D7', 'F7', 'E7', 'G7', 'A7', 'B7', 'C8']
helfnotes = ['A#0', 'C#1', 'D#1', 'F#1', 'G#1', 'A#1', 'C#2', 'D#2', 'F#2', 'G#2', 'A#2', 'C#3', 'D#3', 'F#3', 'G#3', 'A#3', 'C#4', 'D#4', 'F#4', 'G#4', 'A#4', 'C#5', 'D#5', 'F#5', 'G#5', 'A#5', 'C#6', 'D#6', 'F#6', 'G#6', 'A#6', 'C#7', 'D#7', 'F#7', 'G#7', 'A#7']
knm = [['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', '&', 'world 73', '"', "'", '(', '-', 'world 72', '_', 'world 71', 'world 64', 'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'world 89', 'w', 'x', 'c', 'v', 'b', 'n', ',', ';', ':', '!'], ['A0', 'B0', 'C1', 'D1', 'F1', 'E1', 'G1', 'A1', 'B1', 'C2', 'D2', 'F2', 'E2', 'G2', 'A2', 'B2', 'C3', 'D3', 'F3', 'E3', 'G3', 'A3', 'B3', 'C4', 'D4', 'F4', 'E4', 'G4', 'A4', 'B4', 'C5', 'D5', 'F5', 'E5', 'G5', 'A5', 'B5', 'C6', 'D6', 'F6', 'E6', 'G6', 'A6', 'B6', 'C7', 'D7', 'F7', 'E7', 'G7', 'A7', 'B7', 'C8']]
pygame.init()
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
def playnote():
	l = list()
	keyname = pygame.key.name(event.key)
	l.append(keyname)
	if keyname in knm[0]:
				note = (knm[1][knm[0].index(keyname)]).upper()
				pygame.mixer.music.load('midies/'+note+'.mid')
				pygame.mixer.music.play()
				l.append(note)
	return l
def playhalfn(keys):
	l = list()
	for i in range(0,len(keys)):
		if keys[i]:
			keyname = pygame.key.name(i)
			l.append(keyname)
			if keyname in knm[0]:
				for i in helfnotes:
					lhn = list(i)
					ln = list((knm[1][knm[0].index(keyname)]).upper())
					if (lhn[0] == ln[0]) and (lhn[2] == ln[1]):
						pygame.mixer.music.load('midies/'+i.upper()+'.mid')
						pygame.mixer.music.play()
						l.append(i)
	return l
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			keys = pygame.key.get_pressed()
			if keys[K_RSHIFT] or keys[K_LSHIFT]:
				print(playhalfn(keys))
			else:
				print(playnote())
	screen.fill((255, 255, 255))
	pygame.display.update()