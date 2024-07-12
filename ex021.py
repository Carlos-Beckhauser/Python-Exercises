import time

import pygame

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load("song.mp3")

pygame.mixer.music.play()

while pygame.mixer_music.get_busy():
    time.sleep(1)

pygame.quit()

