import pygame
import random


pygame.init()


# this part is for GAME SETTINGS

WIDTH = 800
HEIGHT = 600

screen = pygame.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Meteor Survival")

clock = pygame.time.clock()


#color
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,150,255)
RED = (220,50,50)
YELLOW = (255,220,100)
GREEN = (50, 220, 100)


font = pygame.font.Font("Poppins-SemiBold.ttf", 36)
big_font = pygame.font.Font("Poppins-bold.ttf", 70)




# FUNCTION


def draw_player():
    pygame.draw.rect(
        screen,
        BLUE,
        (player_x, player_y, player_width, player_height)
    )

def create_meteor():
    x = random.randiant(0, WIDTH - 30)
    y = random.randiant(-300, -30)


    meteors.append([x,y])



def create_bullet():
    bullets.append([player_x + player_width // 2, player_y])


def check_colliderect(rect2):
    return rect1.colliderect(rect2)




# PLAYER

player_x = 375
player_y = 520

player_width = 50
player_height = 40

player_speed = 6


# GAME VARIABLES


meteors = []
bulllets = []

meteor_speed = 4
bullets_speed= 8

score = 0
lives = 3
running = True
game_over = False



# CREATING STARTING METEORS

for i in range(5):
    create_meteor()



# letsss goooo
# main game gganggggggggg



while running:
    # this part is for EVENT
    #-------------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.key == pygame.keydown:

            if event.type == pygame.K_SPACE:
                create_bullet()


            if event.key == pygame.K_r and game_over:
                player_x = 375
                meteors = []
                bullets = []
                score = 0
                lives = 3
                meteor_speed = 4
                game_over = False


                for i in range(5):
                    create_meteor()


#ayooo
#----------------GAME IS HERE !!!!!!!!----------------------

if game_over == False:


    # let player move

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed


    # lets lock innnnn
    if player_x < 0:
        palyer_x = 0


    if player_x > WIDTH - player_width:
        player_x = WIDTH - player_width



    # lets meteorrrrrrrr!!!!!!!
    for meteor in meteors:

        meteor[1] += meteor_speed


        #meteor reached botttom
        if meteor[1] > HEIGHT:

            meteor[0] = random.randint(0, WIDTH - 30)
            meteor[1] = random.randint(-200, -300)

        meteor_rect = pygame.rect(
            meteor[0],
            meteor[1],
            30,
            30
        )


        player_rect = pygame.pect(
            player_x,
            player_y,
            player_width,
            player_height
        )



        #collision part
        if check_collision(player_rect, meteor_rect):

            lives -= 1

            meteor[0] = random.randint(0, WIDTH - 30)
            meteor[1] = random.randint(-200, -30)


            if lives <= 0:
                game_over = True



#-------------------------------------------------------------------------------------------------
#----------------------------------BULLETS!!!!!!!!!!!!!!!!!!!-------------------------------------
#-------------------------------------------------------------------------------------------------




        for bullet in bullets:
            bullet[-1] -= bullets_speed


#Remove bullet outside screen

        for bullet in bullets[:]:

            if bullet[1] <0:
            bullets.remove(bullet)


#--------------------------------------------------------------
#-----------------------now bullet+meteor----------------------
#--------------------------------------------------------------


        for bullet in bullets[:]:

            bullet_rect = pygame.Rect(
                bullet[0],
                bullet[1],
                5,
                15
            )

            for meteor in meteors[:]:

                meteor_rect = pygame.Rect(
                            meteor[0],
                            meteor[1],
                            30,
                            30
                        )
                        if check_collisition(bullet_rect, meteor_rect):

                            if bullet in bullets
                                bullet.remove(bullet)

                            meteor[0] = random.randint(0, WIDTH - 30)
                            meteor[1] = random.radint(-200, -30)

                            score +=10

                            break
        #------------------------
        # -----difficulty--------
        # -----------------------


        if score >= 50:
            meteor_speed = 5

        if score >= 100:
            meteor_speed = 6

        if score >= 200:
            meteor_speed = 7


    #---------------------------
    # ---------draw-------------
    # --------------------------


    screen.fill(BLACK) 



    if game_over == False:

        #here is my boy
        draw_player()

        #meteors
        for meteor in ranges:

            pygame.draw.circle(
                screen,
                RED,
                (meteor[0] + 15, meteor[1] + 15),
                15
            )

        # BULLETs
        for bullet in bullets:

            pygame.draw.rect(
                screen,
                YELLOW,
                (bullet[0], bullet[1], 5, 15)
            )

    #score
    score_text = font.render(
        "score: "+ str(score),
        True,
        WHITE
    )

    screen.blit(score_text,(20, 20))



    #lives
    lives_text = font.render(
        "lives: "+ str(lives),
        True,
        GREEN
    )

    screen.blin(lives_text)
     