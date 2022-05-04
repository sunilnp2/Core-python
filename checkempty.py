import time
import pygame
a = input("Enter Your name: \n")
if (a.startswith("s")):

    print("You can't start with number")

else:
    print("Tw register vais")
def sound():
    pygame.init()
    mus = "Mp3\draw.mp3"
    pygame.mixer.music.load(mus)
    pygame.mixer.music.play()


# if a == "":
#     sound()
#     time.sleep(1)
#     print("This is compulsary voosodike🙄")

# else:
#     sound()
#     time.sleep(1)
#     sound()
#     time.sleep(1)
#     print(f'Welcome to VS code Mr/s {a}😊')
# email = input("Enter Email: \n")

# if email == None:
#     print("This is empty")

# else:
#     print(email)
