import pygame
from pygame.locals import *
from sys import exit
from piano import playNote
from music21 import *
notes = "C2 D2 F2 E2 G2 A2 B2 C3 D3 F3 E3 G3 A3 B3 C4 D4 F4 E4 G4 A4 B4 C5 D5 F5 E5 G5 A5 B5 C6 D6 F6 E6 G6 A6 B6 C7"
notesl = ['C2', 'D2', 'F2', 'E2', 'G2', 'A2', 'B2', 'C3', 'D3', 'F3', 'E3', 'G3', 'A3', 'B3', 'C4', 'D4', 'F4', 'E4', 'G4', 'A4', 'B4', 'C5', 'D5', 'F5', 'E5', 'G5', 'A5', 'B5', 'C6', 'D6', 'F6', 'E6', 'G6', 'A6', 'B6', 'C7']
notess = "C#2 D#2 F#2 G#2 A#2 C#3 D#3 F#3 G#3 A#3 C#4 D#4 F#4 G#4 A#4 C#5 D#5 F#5 G#5 A#5 C#6 D#6 F#6 G#6 A#6"
notessl = ['C#2', 'D#2', 'F#2', 'G#2', 'A#2', 'C#3', 'D#3', 'F#3', 'G#3', 'A#3', 'C#4', 'D#4', 'F#4', 'G#4', 'A#4', 'C#5', 'D#5', 'F#5', 'G#5', 'A#5', 'C#6', 'D#6', 'F#6', 'G#6', 'A#6']
keys = "K_LESS K_w K_x K_c K_v K_b K_n K_COMMA K_SEMICOLON K_COLON K_EXCLAIM K_KMOD_RSHIFT K_q K_s K_d K_f K_g K_h K_j K_k K_l K_m K_ASTERISK K_a K_z K_e K_r K_t K_y K_u K_i K_o K_p K_CARET K_DOLLAR"
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