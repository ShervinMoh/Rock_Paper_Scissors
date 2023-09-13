import pygame, time, random
from pygame import mixer

pygame.init()  # Initializing the pygame module

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))  # Creating a pygame window
pygame.display.set_caption("Rock Paper Scissor By ShervinMoh")  # Setting the caption of the window

# Define color variables
black = (1, 4, 4)
red = (255, 0, 0)
green = (117, 162, 131)
green2 = (2, 154, 191)
blue = (7, 59, 205)
white = (254, 254, 254)
white2 = (171, 209, 218)

error_font = pygame.font.SysFont("bahnschrift", 25)  # Font for error messages
font_style = pygame.font.SysFont("bahnschrift", 30)  # Main font style used in the game
score_font = pygame.font.SysFont("leelawadeeui", 35)  # Font for displaying scores

button_font = pygame.font.SysFont("Corbel", 35)  # Font for buttons text
Start = button_font.render("Start", True, white)  # Start button text
Quit = button_font.render("Quit", True, white)  # Quit button text

# Load and set the volume for sound effects
mouse_sound = pygame.mixer.Sound("Musices\mouseclicksound.mp3")
mouse_sound.set_volume(1.0)
card_sound = pygame.mixer.Sound("Musices\card.mp3")
card_sound.set_volume(1.0)
winround_sound = pygame.mixer.Sound("Musices\winround.mp3")
winround_sound.set_volume(1.0)
lose_sound = pygame.mixer.Sound("Musices\lose.mp3")
lose_sound.set_volume(1.0)
draw_sound = pygame.mixer.Sound("Musices\draw.mp3")
draw_sound.set_volume(0.5)
error_sound = pygame.mixer.Sound("Musices\error.mp3")
error_sound.set_volume(0.5)
gameover_sound = pygame.mixer.Sound("Musices\gameover.mp3")
gameover_sound.set_volume(0.05)
wingame_sound = pygame.mixer.Sound("Musices\wingame.mp3")
wingame_sound.set_volume(0.05)

# Load and resize images used in the game
rock_img = pygame.image.load("rock.png").convert()
rock_img = pygame.transform.scale(rock_img, (150, 110))
paper_img = pygame.image.load("paper.png").convert()
paper_img = pygame.transform.scale(paper_img, (150, 100))
scissor_img = pygame.image.load("scissor.png").convert()
scissor_img = pygame.transform.scale(scissor_img, (200, 130))
menu_bg = pygame.image.load("rps.jpg").convert()
menu_bg = pygame.transform.scale(menu_bg, (800, 600))

# Function to display the player's score
def player1_score(score1):
    value1 = score_font.render("Your Score: " + str(score1), True, black)
    dis.blit(value1, [37, 4])

# Function to display the system's score
def player2_score(score2):
    value1 = score_font.render("System Score: " + str(score2), True, black)
    dis.blit(value1, [530, 4])

# Function to display a changeable message
def changeable_message(msg, v1, v2, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [v1, v2])

# Function to display an error message
def error_message(msg):
    mesg = error_font.render(msg, True, red)
    dis.blit(mesg, [75, 150])

# Function to create buttons
def button():
    mixer.music.load("Musices\menu.mp3")
    mixer.music.set_volume(0.1)
    pygame.mixer.music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 334 <= mouse[0] <= 474 and 317 <= mouse[1] <= 357:
                    mouse_sound.play()
                    time.sleep(1)
                    gameLoop()

                if 334 <= mouse[0] <= 474 and 257 <= mouse[1] <= 297:
                    mouse_sound.play()
                    time.sleep(1)
                    pygame.quit()

        dis.blit(menu_bg, (0, 0))
        mouse = pygame.mouse.get_pos()

        # Start button
        if 334 <= mouse[0] <= 474 and 317 <= mouse[1] <= 357 :
            pygame.draw.rect(dis, white2, [334, 317, 140, 40])
        else:
            pygame.draw.rect(dis, black, [334, 317, 140, 40])

        # Quit button
        if 334 <= mouse[0] <= 474 and 257 <= mouse[1] <= 297:
            pygame.draw.rect(dis, white2, [334, 257, 140, 40])
        else:
            pygame.draw.rect(dis, black, [334, 257, 140, 40])

        dis.blit(Start, (370, 320))
        dis.blit(Quit, (370, 262))
        pygame.display.update()

# The main game loop
def gameLoop():
    mixer.music.load("Musices\ingame.mp3")
    mixer.music.set_volume(0.1)
    pygame.mixer.music.play()

    game_over = False  # Flag to indicate if the game is over
    s1 = 0  # Player's score
    s2 = 0  # System's score

    while not game_over:
        while s1 == 10 or s2 == 10:
            if s1 == 10:
                dis.fill(white)
                changeable_message("You Won! Press Quit Or Play Again Button", 125, 150, green2)
                pygame.mixer.music.stop()
                wingame_sound.play()

            if s2 == 10:
                dis.fill(black)
                changeable_message("You Lose! Press Quit Or Play Again Button", 125, 150, red)
                pygame.mixer.music.stop()
                gameover_sound.play()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 334 <= mouse[0] <= 474 and 317 <= mouse[1] <= 357:
                        wingame_sound.stop() or gameover_sound.stop()
                        mouse_sound.play()
                        time.sleep(1)
                        gameLoop()

                    if 334 <= mouse[0] <= 474 and 257 <= mouse[1] <= 297:
                        wingame_sound.stop() or gameover_sound.stop()
                        mouse_sound.play()
                        time.sleep(1)
                        pygame.quit()

            mouse = pygame.mouse.get_pos()

            # Start button
            if 334 <= mouse[0] <= 474 and 317 <= mouse[1] <= 357:  # If the mouse is within the specified range
                pygame.draw.rect(dis, white2, [334, 317, 140, 40])  # Draw a white rectangle
            else:
                pygame.draw.rect(dis, green2, [334, 317, 140, 40])  # Draw a green rectangle

            if 334 <= mouse[0] <= 474 and 257 <= mouse[1] <= 297:  # If the mouse is within the specified range
                pygame.draw.rect(dis, white2, [334, 257, 140, 40])  # Draw a white rectangle
            else:
                pygame.draw.rect(dis, green2, [334, 257, 140, 40])  # Draw a green rectangle

            dis.blit(Start, (370, 320))  # Display the "Start" image at coordinate (370, 320)
            dis.blit(Quit, (370, 262))  # Display the "Quit" image at coordinate (370, 262)
            pygame.display.update()

        r = random.randint(1, 9)  # Generate a random number between 1 and 9

        for event in pygame.event.get():  # Check each event in the event queue
            if event.type == pygame.QUIT:  # If the event is quitting the game
                game_over = True  # Set the game_over flag to True

            if event.type == pygame.KEYDOWN:  # If a key is pressed
                if event.key == pygame.K_ESCAPE:  # If the pressed key is Escape
                    pygame.quit()  # Quit the Pygame module
                    quit()  # Quit the game

                if event.key == pygame.K_r:  # If the pressed key is R
                    changeable_message("Rock", 100, 280, black)
                    pygame.draw.rect(dis, black, [175, 415, 450, 40])
                    changeable_message("Lotfan Chand Lahze Sabr Konid...", 180, 420, green)
                    dis.blit(rock_img, (57, 170))
                    print("Player chose : Rock")
                    x = 1
                    card_sound.play()

                elif event.key == pygame.K_p:  # If the pressed key is P
                    changeable_message("Paper", 90, 280, black)
                    pygame.draw.rect(dis, black, [175, 415, 450, 40])
                    changeable_message("Lotfan Chand Lahze Sabr Konid...", 180, 420, green)
                    dis.blit(paper_img, (57, 160))
                    print("Player chose : Paper")
                    x = 2
                    card_sound.play()

                elif event.key == pygame.K_s:  # If the pressed key is S
                    changeable_message("Scissor", 90, 280, black)
                    pygame.draw.rect(dis, black, [175, 415, 450, 40])
                    changeable_message("Lotfan Chand Lahze Sabr Konid...", 180, 420, green)
                    dis.blit(scissor_img, (40, 120))
                    print("Player chose: Scissor")
                    x = 3
                    card_sound.play()

                else:
                    error_message("Lotfan Yeki Az Dokme Haye R, P, S Ra Entekhab Konid")
                    error_sound.play()
                    print("Player chose: Invalid Key")

                pygame.display.update()
                time.sleep(5)

                if event.key == pygame.K_r or event.key == pygame.K_p or event.key == pygame.K_s:  # If the pressed key is R, P, or S
                    if r == 1 or r == 5 or r == 8:  # If the system randomly chose Rock
                        changeable_message("Rock", 600, 280, black)
                        print("System chose : Rock")
                        dis.blit(rock_img, (557, 170))
                        y = 1
                        card_sound.play()
                        
                    elif r == 2 or r == 4 or r == 7:  # If the system randomly chose Paper
                        changeable_message("Paper", 600, 280, black)
                        print("System chose : Paper")
                        dis.blit(paper_img, (557, 160))
                        y = 2
                        card_sound.play()
                        
                    elif r == 3 or r == 6 or r == 9:  # If the system randomly chose Scissor
                        changeable_message("Scissor", 610, 280, black)
                        print("System chose : Scissor")
                        dis.blit(scissor_img, (540, 120))
                        y = 3
                        card_sound.play()
                        
                    pygame.display.update()

                    if x == y:  # If the player and system chose the same option
                        draw_sound.play()
                        print("Draw")
                        
                    elif x == 1 and y == 2:  # If the player chose Rock and the system chose Paper
                        s2 += 1
                        lose_sound.play()
                        print("System Won")
                        
                    elif x == 1 and y == 3:  # If the player chose Rock and the system chose Scissor
                        s1 += 1
                        winround_sound.play()
                        print("Player Won")
                        
                    elif x == 2 and y == 3:  # If the player chose Paper and the system chose Scissor
                        s2 += 1
                        lose_sound.play()
                        print("System Won")
                        
                    elif y == 1 and x == 2:  # If the player chose Paper and the system chose Rock
                        s1 += 1
                        winround_sound.play()
                        print("Player Won")
                        
                    elif y == 1 and x == 3:  # If the player chose Scissor and the system chose Rock
                        s2 += 1
                        lose_sound.play()
                        print("System Won")
                        
                    elif y == 2 and x == 3:  # If the player chose Scissor and the system chose Paper
                        s1 += 1
                        winround_sound.play()
                        print("Player Won")
                                
                    time.sleep(5)

        dis.fill(white)  # Clear the display with white color

        pygame.draw.rect(dis, blue, [15, 10, 250, 40])  # Draw a blue rectangle for player 1
        pygame.draw.rect(dis, red, [515, 10, 270, 40])  # Draw a red rectangle for player 2
        player1_score(s1)  # Display the score of player 1
        player2_score(s2)  # Display the score of player 2
        pygame.display.update()

if __name__ == '__main__':
    button()  # Call the button function when the script is directly run, not imported