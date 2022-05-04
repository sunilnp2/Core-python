import random
import pygame
import time

# def swg():
#     game = ["S","W","G"]
#     cpu = random.choice(game)
#     You_win = 0

#     user = input("Enter 'S' for 'snake', 'W' for 'water' or 'G' for 'gun':")
#     if(user == "S" and cpu == "W" or user == "W" and cpu == "G" or user == "G" and cpu == "S"):
#         print("You Win!😁")
#         print("Cpu choose:",cpu)

#     elif(user == "S" and cpu == "G" or user == "W" and cpu == "S" or user == "G" and cpu == "W"):
#         print("Cpu Win!😐")
#         print("Cpu choose:",cpu)
    
#     else:
#         print("Draw🤗")
#         print("Cpu choose :",cpu)


# for i in range(1,11):

def win():
    pygame.init()
    file = "Mp3\win.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
def lose():
    pygame.init()
    file = "Mp3\lose.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
def dr():
    pygame.init()
    file = "Mp3\draw.mp3"
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
your_score = 0
cpu_score = 0
draw = 0
i = 1
while(i<=5):
    game = ["S","W","G"]
    cpu = random.choice(game)
    You_win = 0
    user = input("Enter 'S' for 'snake', 'W' for 'water' or 'G' for 'gun'::")
    
    # try:
    #     user = input("Enter 'S' for 'snake', 'W' for 'water' or 'G' for 'gun'")
    # except TypeError:
    #     print("sorry You enter wrong key! \\n Play Again",user)

    if(user == "S" and cpu == "W" or user == "W" and cpu == "G" or user == "G" and cpu == "S"):
        print("You Win!")
        print("Cpu choose:",cpu)
        your_score = your_score + 1
        g = f"Your_Score:{your_score} \n Cpu_score: {cpu_score} \n draw: {draw} "
        print(g)
        win()
        time.sleep(3)


    elif(user == "S" and cpu == "G" or user == "W" and cpu == "S" or user == "G" and cpu == "W"):
        print("Cpu Win!")
        print("Cpu choose:",cpu)
        cpu_score = cpu_score + 1
        g = f"Your_Score:{your_score} \n Cpu_score: {cpu_score} \n draw: {draw} "
        print(g)
        lose()
        time.sleep(3)
    
    # if i==5:
    #     time.sleep(3)

    
    else:
        print("Draw")
        print("Cpu choose :",cpu)
        draw = draw + 1
        print(draw)
        g = f"Your_Score:{your_score} \n Cpu_score: {cpu_score} \n draw: {draw} "
        print(g)
        dr()
        time.sleep(5)


    i+= 1
if (your_score > cpu_score):
        win()
        print("\n\nHurrey You win😁")
        score = f" Your_Total_score ={your_score} \n Cpu_Total_score = {cpu_score} \n Draw = {draw} "
        print(score)
        time.sleep(3)
elif(cpu_score > your_score): 
        lose()
        print("Cpu win!😥")
        score = f" Your_Total_score ={your_score} \n Cpu_Total_score = {cpu_score} \n Draw = {draw} "
        print(score)
        time.sleep(3)
else:   
        dr()
        print("Opps game is Draw😶")
        score = f" Your_Total_score ={your_score} \n Cpu_Total_score = {cpu_score} \n Draw = {draw} "
        print(score)

