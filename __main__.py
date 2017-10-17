import pygame
from pygame.locals import *
from sys import exit
from music21 import *
notes = "A0 B0 C1 D1 F1 E1 G1 A1 B1 C2 D2 F2 E2 G2 A2 B2 C3 D3 F3 E3 G3 A3 B3 C4 D4 F4 E4 G4 A4 B4 C5 D5 F5 E5 G5 A5 B5 C6 D6 F6 E6 G6 A6 B6 C7 D7 F7 E7 G7 A7 B7 C8"
notess = "A#0 C#1 D#1 F#1 G#1 A#1 C#2 D#2 F#2 G#2 A#2 C#3 D#3 F#3 G#3 A#3 C#4 D#4 F#4 G#4 A#4 C#5 D#5 F#5 G#5 A#5 C#6 D#6 F#6 G#6 A#6 C#7 D#7 F#7 G#7 A#7"
enkeys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'MINUS', 'EQUALS', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'LEFTBRACKET', 'RIGHTBRACKET', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'SEMICOLON', 'BACKSLASH', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'COMMA', 'PERIOD', 'SLASH']
pygame.init()
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_a:
				pygame.mixer.music.load("midies/C2.mid")
				pygame.mixer.music.play()

	screen.fill((255, 255, 255))
	pygame.display.update()