import pygame
from pygame.locals import *
from sys import exit
from music21 import *
import tkinter as tk
import threading
import time
import mido
background_image_filename = 'background2.png'
enkeys = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'COMMA', 'PERIOD', 'SLASH', 'RSHIFT']
notesl = ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1', 'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6', 'C7', 'D7', 'E7', 'F7', 'G7', 'A7', 'B7', 'C8']
helfnotes = ['A#0', 'C#1', 'D#1', 'F#1', 'G#1', 'A#1', 'C#2', 'D#2', 'F#2', 'G#2', 'A#2', 'C#3', 'D#3', 'F#3', 'G#3', 'A#3', 'C#4', 'D#4', 'F#4', 'G#4', 'A#4', 'C#5', 'D#5', 'F#5', 'G#5', 'A#5', 'C#6', 'D#6', 'F#6', 'G#6', 'A#6', 'C#7', 'D#7', 'F#7', 'G#7', 'A#7']
knm = [['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', '&', 'world 73', '"', "'", '(', '-', 'world 72', '_', 'world 71', 'world 64', 'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'world 89', 'w', 'x', 'c', 'v', 'b', 'n', ',', ';', ':', '!'], ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1', 'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'A6', 'B6', 'C7', 'D7', 'E7', 'F7', 'G7', 'A7', 'B7', 'C8']]

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

pygame.init()
SCREEN_SIZE = (screen_width, screen_height)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
background = pygame.image.load(background_image_filename).convert()
background = pygame.transform.scale(background, SCREEN_SIZE)
		
		
def playnote():
	l = list()
	keyname = pygame.key.name(event.key)
	if keyname in knm[0]:
				note = (knm[1][knm[0].index(keyname)]).upper()
				pygame.mixer.music.load('midies/'+note+'.mid')
				pygame.mixer.music.play()
				m = mido.MidiFile('midies/'+note+'.mid')
				l.append(keyname)
				l.append(note)
				l.append(	m.length)
	return l

def playhalfn(keys):
	l = list()
	for i in range(0,len(keys)):
		if keys[i]:
			keyname = pygame.key.name(i)
			if keyname in knm[0]:
				for i in helfnotes:
					lhn = list(i)
					ln = list((knm[1][knm[0].index(keyname)]).upper())
					if (lhn[0] == ln[0]) and (lhn[2] == ln[1]):
						pygame.mixer.music.load('midies/'+i.upper()+'.mid')
						pygame.mixer.music.play()
						m = mido.MidiFile('midies/'+note+'.mid')
						l.append(keyname)
						l.append(i)
						l.append(m.length)
	return l

def drawrect(screen,ln):
		screen.lock()
		white = (255, 255, 255)
		black = (0,0,0)
		gray = (192,192,192)
		for i in range(0,52):
			if len(ln)>0:
				if ln[1]==notesl[i]:
					pygame.draw.rect(screen, gray, ((screen_width / 52 )* i ,  (screen_height / 3)*2 , (screen_width / 52 ) - 1, screen_height/3))
					pygame.time.delay(750)
					pygame.draw.rect(screen, white, ((screen_width / 52 )* i ,  (screen_height / 3)*2 , (screen_width / 52 ) - 1, screen_height/3))
				else:
					pygame.draw.rect(screen, white, ((screen_width / 52 )* i ,  (screen_height / 3)*2 , (screen_width / 52 ) - 1, screen_height/3))
		j = 0
		hnote = list(helfnotes[j])
		for i in range(0,52):
			note = list(notesl[i])
			if (note[0]==hnote[0]) and (note[1] == hnote[2]):
				j += 1
				if j < len(helfnotes):
					hnote = list(helfnotes[j])
				pygame.draw.rect(screen,black,((screen_width / 52 )* i + (((screen_width / 52 ) - 1)/2),  (screen_height / 3)*2 , (screen_width / 52)-((screen_width / 52)/2), (screen_height/3)-((screen_height/3)/2)))		
		screen.unlock()
screen.blit(background,(0,0))
#to draw piano the intro
lnk = list()
drawrect(screen,lnk)
while True:
	lnk.clear()
	clickednote = ''
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			keys = pygame.key.get_pressed()
			if event.key == K_ESCAPE:
				exit()
			if keys[K_RSHIFT] or keys[K_LSHIFT]:
				lnk=playhalfn(keys)
				print(lnk)
			else:
				lnk=playnote()
				print(lnk)
	threading.Thread(target=drawrect,args=(screen,lnk,)).start()
	pygame.display.update()