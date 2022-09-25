# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
print('='*6, 'DESAFIO 21/AULA08', '='*6)
'''from playsound import playsound
playsound('boyce.mp3')'''
import pygame
pygame.init()
pygame.mixer.music.load('boyce.mp3')
pygame.mixer.music.play()
pygame.event.wait()