# File created by: Zander Collins 
# created for Git Hub

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

# globalizes the set of variables used across the code
global player_choice
global computer_choice
player_choice = ""
computer_choice = ""
# variabel that is a string of the 3 choices
choices = ["Rock", "Paper", "Scissors"]

# function that randomly chooses for the computer
def cpu_randchoice():
    computer_choice = (choices[randint(0,2)])
    print("The computer randomly chose " + computer_choice + ".")
    return computer_choice 

# function that allows for text to be displayed in the screen
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
# allows for the image data (pixel location,number,color) to be changed
# same classification and loading for all 6 images used
rock_image = pg.image.load(os.path.join(game_folder,'Rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()

cpu_rock_image = pg.image.load(os.path.join(game_folder,'Rock_cpu.jpg')).convert()
cpu_rock_image_rect = cpu_rock_image.get_rect()

paper_image = pg.image.load(os.path.join(game_folder,'Paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()

cpu_paper_image = pg.image.load(os.path.join(game_folder,'Paper_cpu.jpg')).convert()
cpu_paper_image_rect = cpu_paper_image.get_rect()

scissors_image = pg.image.load(os.path.join(game_folder,'Scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()

cpu_scissors_image = pg.image.load(os.path.join(game_folder,'Scissors_cpu.jpg')).convert()
cpu_scissors_image_rect = cpu_scissors_image.get_rect()

play_again_image = pg.image.load(os.path.join(game_folder,'play_again.png')).convert()
play_again_image_rect = play_again_image.get_rect()


# boolean value for if the program is running
running = True 
# boolean value for if the game has started
game_start = True

# while loop, runs the program
while running: 
    clock.tick(FPS) 

    # close loop and game when quit event occurs
    for event in pg.event.get(): 
        # listening for quiting event 
        if event.type == pg.QUIT: 
            # if quit, program stops 
            running = False 

        # assigns event to when mouse botton is clicked 
        if event.type == pg.MOUSEBUTTONUP: 
            # prints and stores the first or x value of the coordinate touple
            print(pg.mouse.get_pos()[0])
            # prints and stores the second or y value of the coordinate touple
            print(pg.mouse.get_pos()[1])
            # assigns variable to mouse coordinate touple
            mouse_coords = pg.mouse.get_pos()
            # returns boolean value for clicking on image
            # assigns player choice based on coordinates of mouse click 
            # also has computer choose randomly when player chooses 
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("Player choice = Rock ")
                player_choice = "Rock"
                computer_choice = cpu_randchoice()
            elif paper_image_rect.collidepoint(mouse_coords):
                print("Player choice = Paper ")
                player_choice = "Paper"
                computer_choice = cpu_randchoice()
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("Player choice = Scissors ")
                player_choice = "Scissors"
                computer_choice = cpu_randchoice()
            else: 
                print("You did not click on anything... ")
            print(paper_image_rect.collidepoint(mouse_coords))
            print(scissors_image_rect.collidepoint(mouse_coords))
    
    ######## draw ###########
    # fill background with black 
    screen.fill(BLACK)

    # sets the location data for the images when the program starts 
    if  game_start == True: 
        screen.blit(rock_image, rock_image_rect)
        rock_image_rect.x = 50
        rock_image_rect.y = 50
        screen.blit(paper_image, paper_image_rect)
        paper_image_rect.x = 800
        paper_image_rect.y = 50
        screen.blit(scissors_image, scissors_image_rect)
        scissors_image_rect.x = 400
        scissors_image_rect.y = 400

    # sets the location data for the images and text if the player clicks on nothing 
    # draws text on screen to tell player to pick a choice
    if player_choice == "": 
        screen.blit(rock_image, rock_image_rect)
        rock_image_rect.x = 50
        rock_image_rect.y = 50
        screen.blit(paper_image, paper_image_rect)
        paper_image_rect.x = 800
        paper_image_rect.y = 50
        screen.blit(scissors_image, scissors_image_rect)
        scissors_image_rect.x = 400
        scissors_image_rect.y = 400
        draw_text("Click to choose:", 30, WHITE, 625, 200)

    # sets the location of the images if the player chooses rock 
    if player_choice == "Rock": 
        rock_image_rect.x = 100
        rock_image_rect.y = 150
        paper_image_rect.x = 2000
        paper_image_rect.y = 2000
        scissors_image_rect.x = 2000 
        scissors_image_rect.y = 2000
        # sets the image location based on if the computer chooses rock, paper, or scissors
        # draws text that gives the results of the game based on the comparison of the user and computer choice 
        # the three below handle the result of each choice combination
        if computer_choice == "Rock":
            cpu_rock_image_rect.x = 700
            cpu_rock_image_rect.y = 150 
            screen.blit(rock_image,cpu_rock_image_rect)
            draw_text("ties with", 20 , WHITE , 600, 300)
            draw_text("Tie Game!", 20 , WHITE, 600, 500)
     
        if computer_choice == "Paper":
            cpu_paper_image_rect.x = 700
            cpu_paper_image_rect.y = 150 
            screen.blit(paper_image,cpu_paper_image_rect)
            draw_text("loses to", 20 , WHITE , 600, 300)
            draw_text("You lost! :( ", 20 , WHITE, 600, 500)
             
        if computer_choice == "Scissors": 
            cpu_scissors_image_rect.x = 700
            cpu_scissors_image_rect.y = 150 
            screen.blit(scissors_image,cpu_scissors_image_rect)
            draw_text("beats", 20 , WHITE , 600, 300)
            draw_text("You Won! :) ", 20 , WHITE , 600, 500) 
            
    # sets the location of the images if the player chooses paper 
    if player_choice == "Paper": 
        paper_image_rect.x = 100
        paper_image_rect.y = 150
        rock_image_rect.x = 2000
        rock_image_rect.y = 2000
        scissors_image_rect.x = 2000 
        scissors_image_rect.y = 2000
        # sets the image location based on if the computer chooses rock, paper, or scissors
        # draws text that gives the results of the game based on the comparison of the user and computer choice 
        # the three below handle the result of each choice combination
        if computer_choice == "Paper":
            cpu_paper_image_rect.x = 700
            cpu_paper_image_rect.y = 150 
            screen.blit(paper_image,cpu_paper_image_rect)
            draw_text("ties with", 20 , WHITE , 600, 300)
            draw_text("Tie Game!", 20 , WHITE, 600, 500)
             
        if computer_choice == "Scissors":
            cpu_scissors_image_rect.x = 700
            cpu_paper_image_rect.y = 150
            screen.blit(scissors_image,cpu_scissors_image_rect)
            draw_text("loses to", 20 , WHITE , 600, 300)
            draw_text("You lost! :( ", 20 , WHITE, 600, 500)
            
        if computer_choice == "Rock": 
            cpu_rock_image_rect.x = 700
            cpu_rock_image_rect.y = 150 
            screen.blit(rock_image,cpu_rock_image_rect)
            draw_text("beats", 20 , WHITE , 600, 300)
            draw_text("You Won! :) ", 20 , WHITE , 600, 500) 
            
    # sets the location of the images if the player chooses scissors
    if player_choice == "Scissors": 
        scissors_image_rect.x = 100
        scissors_image_rect.y = 150
        rock_image_rect.x = 2000
        rock_image_rect.y = 2000
        paper_image_rect.x = 2000 
        paper_image_rect.y = 2000
        # sets the image location based on if the computer chooses rock, paper, or scissors
        # draws text that gives the results of the game based on the comparison of the user and computer choice 
        # the three chunks below handle the result of each choice combination
        if computer_choice == "Scissors":
            cpu_scissors_image_rect.x = 700
            cpu_scissors_image_rect.y = 150 
            screen.blit(scissors_image,cpu_scissors_image_rect)
            draw_text("ties with", 20 , WHITE , 600, 300)
            draw_text("Tie Game!", 20 , WHITE, 600, 500)
             
        if computer_choice == "Rock":
            cpu_rock_image_rect.x = 700
            cpu_rock_image_rect.y = 150 
            screen.blit(rock_image,cpu_rock_image_rect)
            draw_text("loses to", 20 , WHITE , 600, 300)
            draw_text("You lost! :( ", 20 , WHITE, 600, 500)
             
        if computer_choice == "Paper": 
            cpu_paper_image_rect.x = 700
            cpu_paper_image_rect.y = 150 
            screen.blit(paper_image,cpu_paper_image_rect)
            draw_text("beats", 20 , WHITE , 600, 300)
            draw_text("You Won! :) ", 20 , WHITE , 600, 500)
             

    pg.display.flip()
    # quits the program 
    pg.QUIT 