import pygame
pygame.init()
pygame.mixer.music.load('exercicios-python/ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()