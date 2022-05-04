# import pygame
# from time import *

# ct = localtime()
# print(ct)
# from datetime import datetime
# dt = datetime.today()
# print(dt)


import pygame
import time

def add():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a+b
    print(c)

def py_pygame():
    pygame.init()
    file = "Mp3\win.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

for i in range(5):
    add()
    py_pygame()
    time.sleep(2)


