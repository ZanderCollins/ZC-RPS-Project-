# File created by: Zander Collins 

# import from libraires

# a library that allows for time to be intergected into code 
from time import sleep 

# a libary that allows for the computer to take a random value from within a list
from random import randint

# comprehensive game library for the use of python 
import pygame as pg

# allows for the management of files and folders 
import os 

game_folder = os.path.dirname(__file__)
print(game_folder)

global player_choice
global computer_choice
player_choice = ""
computer_choice = ""
choices = ["Rock", "Paper", "Scissors"]

def cpu_randchoice():
    computer_choice = (choices[randint(0,2)])
    print("The computer randomly chose " + computer_choice + ".")
    return computer_choice 

def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('times new roman')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

# game settings
WIDTH = 1280
HEIGHT = 720
FPS = 30 

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pg.init()
pg.mixer.init()
# sets dimensions for screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors")
# aligns the clock time with fps time
clock = pg.time.Clock()
# loads the chosen file and stores the image data
rock_image = pg.image.load(os.path.join(game_folder,'Rock.jpg')).convert()
# allows for the image data (pixel location,number,color) to be changed
rock_image_rect = rock_image.get_rect()

paper_image = pg.image.load(os.path.join(game_folder,'Paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()

scissors_image = pg.image.load(os.path.join(game_folder,'Scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()

# boulean loop for if the program is running
running = True 
game_start = True 

while running: 
    clock.tick(FPS) 
    
    # close loop and game when quit event occurs
    for event in pg.event.get(): 
        # listening for quiting event 
        if event.type == pg.QUIT: 
            # if quit, program stops 
            running = False 
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("The game started")
                game_start = True

        # assigns event to when mouse botton is clicked 
        if event.type == pg.MOUSEBUTTONUP: 
            # prints and stores the first or x value of the coordinate touple
            print(pg.mouse.get_pos()[0])
            # prints and stores the second or y value of the coordinate touple
            print(pg.mouse.get_pos()[1])
            # assigns variable to mouse coordinate touple
            mouse_coords = pg.mouse.get_pos()
            # returns boolean value for clicking on image 
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("You clicked on Rock... ")
                player_choice = "Rock"
            elif paper_image_rect.collidepoint(mouse_coords):
                print("You clicked on Paper... ")
                player_choice = "Paper"
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("You clicked on Scissors... ")
                player_choice = "Scissors"
            else: 
                print("You did not click on anything... ")
            print(paper_image_rect.collidepoint(mouse_coords))
            print(scissors_image_rect.collidepoint(mouse_coords))
    
    ######## draw ###########
    # fill background with black 
    screen.fill(BLACK)

    if  game_start == True:
        draw_text("Press space to play rock paper scissors.", 16, WHITE, 600, 300)
        rock_image_rect.x = 2000
        paper_image_rect.x = 2000
        scissors_image_rect.x = 2000
    
    if  game_start == True and player_choice == "": 
        screen.blit(rock_image, rock_image_rect)
        rock_image_rect.x = 50
        rock_image_rect.y = 50
        screen.blit(paper_image, paper_image_rect)
        paper_image_rect.x = 800
        paper_image_rect.y = 50
        screen.blit(scissors_image, scissors_image_rect)
        scissors_image_rect.x = 400
        scissors_image_rect.y = 400
    
    '''
    
    ######## User input ##########
    if player_choice == "":
        screen.blit(rock_image, rock_image_rect) 
        screen.blit(paper_image, paper_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
    elif player_choice == "Rock":
        screen.blit(rock_image,rock_image_rect)
        rock_image_rect.x = 100
        rock_image_rect.y = 150
        paper_image_rect.x = 2000
        paper_image_rect.y = 2000
        scissors_image_rect.x = 2000
        scissors_image_rect.y = 2000
        computer_choice = cpu_randchoice() 
    elif player_choice == "Paper":
        screen.blit(paper_image,paper_image_rect)
        paper_image_rect.x = 100
        paper_image_rect.y = 150
        rock_image_rect.x = 2000
        rock_image_rect.y = 2000
        scissors_image_rect.x = 2000
        scissors_image_rect.y = 2000
        computer_choice = cpu_randchoice() 
    elif player_choice == "Scissors":
        screen.blit(scissors_image,scissors_image_rect)
        scissors_image_rect.x = 100
        scissors_image_rect.y = 150
        rock_image_rect.x = 2000
        rock_image_rect.y = 2000
        scissors_image_rect.x = 2000
        scissors_image_rect.y = 2000
        computer_choice = cpu_randchoice() 
    else: 
        print("Please pick a choice... ")
        

    if computer_choice == choices[0]:
        screen.blit(rock_image,rock_image_rect)
        rock_image_rect.x = 800
        rock_image_rect.y = 150 
    elif computer_choice == choices[1]:
        screen.blit(paper_image,paper_image_rect)
        paper_image_rect.x = 800
        paper_image_rect.y = 150 
    elif computer_choice == choices[2]:
        screen.blit(scissors_image,scissors_image_rect)
        scissors_image_rect.x = 800
        scissors_image_rect.y = 150 
    else: 
        break
            
    '''

    pg.QUIT 


 




    
    
    

        

