import pygame
from random import randint

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load("music.mp3")  

pygame.mixer.music.play(-1)

pygame.mixer.music.set_volume(0.7)

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock paper scissors ")

mini_rock_img = pygame.transform.scale(pygame.image.load("images/rock.png"), (120, 120))
mini_paper_img = pygame.transform.scale(pygame.image.load("images/paper.png"), (120, 120))
mini_scissors_img = pygame.transform.scale(pygame.image.load("images/scissors.png"), (120, 120))

rock_image = pygame.transform.scale(pygame.image.load("images/rock.png"), (190, 190)) 
paper_image = pygame.transform.scale(pygame.image.load("images/paper.png"), (190, 190))
scissors_image = pygame.transform.scale(pygame.image.load("images/scissors.png"), (190, 190))
screen_image = pygame.transform.scale(pygame.image.load("images/screen_image.png"), (600, 600))
start_btn = pygame.transform.scale(pygame.image.load("images/start_btn.png"), (290, 290))
next_btn = pygame.transform.scale(pygame.image.load("images/next_btn.png"), (290, 290))

start_btn_rect = start_btn.get_rect(topleft=(170, 170))
rock_rect = mini_rock_img.get_rect(topleft=(100, 465))
paper_rect = mini_paper_img.get_rect(topleft=(240, 465))
scissors_rect = mini_scissors_img.get_rect(topleft=(380, 465))
next_btn_rect = next_btn.get_rect(topleft=(400, 170))

my_item = "none"
enemy_item = "none"

start = False
draw_mini_image = True
rock = False
paper = False
scissors = False
fight = False

enemy_item_select = randint(1, 3)

my_score = 0
enemy_score = 0

font = pygame.font.Font(None, 150)

text_win_rect = (text_win := font.render("Win!", True, (100, 100, 100))).get_rect(center=(WIDTH // 2, HEIGHT // 2))
text_lose_rect = (text_lose := font.render("Lose!", True, (100, 100, 100))).get_rect(center=(WIDTH // 2, HEIGHT // 2))
text_draw_rect = (text_draw := font.render("Draw!", True, (100, 100, 100))).get_rect(center=(WIDTH // 2, HEIGHT // 2))


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if start_btn_rect.collidepoint(event.pos):
            start = True

    screen.blit(screen_image, (0, 0))

    text_score_rect = (text_score := font.render(str(my_score) + ":" + str(enemy_score), True, (100, 100, 100))).get_rect(topleft=(10, 200))

    if enemy_item_select == 1:
        enemy_item = "rock"
        enemy_item_image = rock_image
    if enemy_item_select == 2:
        enemy_item = "paper"
        enemy_item_image = paper_image
    if enemy_item_select == 3:
        enemy_item = "scissors"
        enemy_item_image = scissors_image

    if start == False:
        screen.blit(start_btn, (170, 170))

    if start == True and draw_mini_image == True:
        screen.blit(mini_rock_img, (100, 465))
        screen.blit(mini_paper_img, (240, 465))
        screen.blit(mini_scissors_img, (380, 465))

    if event.type == pygame.MOUSEBUTTONDOWN:
        if rock_rect.collidepoint(event.pos):
            draw_mini_image = False
            rock = True

    if rock == True:
        screen.blit(rock_image, (200, 300))
        my_item = "rock"
        fight = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        if paper_rect.collidepoint(event.pos):
            draw_mini_image = False
            paper = True

    if paper == True:
        screen.blit(paper_image, (200, 300))
        my_item = "paper"
        fight = True

    if event.type == pygame.MOUSEBUTTONDOWN:
        if scissors_rect.collidepoint(event.pos):
            draw_mini_image = False
            scissors = True

    if scissors == True:
        screen.blit(scissors_image, (200, 300))
        my_item = "scissors"
        fight = True

    ############
    #str(my_score), str(enemy_score)
    #screen.blit(text_score, text_score_rect)
    #int(my_score), int(enemy_score)
    ############

    if fight == True:
        screen.blit(enemy_item_image, (200, 100))
        screen.blit(next_btn, (400, 170))

        if my_item == "rock" and enemy_item == "rock":
            screen.blit(text_draw, text_draw_rect)
        if my_item == "paper" and enemy_item == "paper":
            screen.blit(text_draw, text_draw_rect)
        if my_item == "scissors" and enemy_item == "scissors":
            screen.blit(text_draw, text_draw_rect)

        if my_item == "rock" and enemy_item == "scissors":
            my_score += 1
            screen.blit(text_win, text_win_rect)
        if my_item == "paper" and enemy_item == "rock":
            my_score += 1
            screen.blit(text_win, text_win_rect)
        if my_item == "scissors" and enemy_item == "paper":
            my_score += 1
            screen.blit(text_win, text_win_rect)

        if my_item == "rock" and enemy_item == "paper":
            enemy_score += 1
            screen.blit(text_lose, text_lose_rect)
        if my_item == "paper" and enemy_item == "scissors":
            enemy_score += 1
            screen.blit(text_lose, text_lose_rect)
        if my_item == "scissors" and enemy_item == "rock":
            enemy_score += 1
            screen.blit(text_lose, text_lose_rect)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if next_btn_rect.collidepoint(event.pos):
                draw_mini_image = True
                rock = False
                paper = False
                scissors = False
                fight = False
                enemy_item_select = randint(1, 3)

    pygame.display.flip()

################ music, seting, fix score