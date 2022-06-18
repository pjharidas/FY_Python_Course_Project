import random
import pygame
import math
'''initialise pygame'''
pygame.init()
# -------------------------------------------------
'''making our screen'''
screen = pygame.display.set_mode((800, 600))
# ------------------------------------------------
'''Caption  Decoration'''
pygame.display.set_caption("Space Invader")
# making an icon variable
icon = pygame.image.load("Caption icon.png")
pygame.display.set_icon(icon)
# ------------------------------------------------
global AsteroidX, AsteroidY, Asteroid_SpeedY, Asteroid_SpeedX, Asteroid_Size

'''Spaceship Declaration'''

Spaceship = pygame.image.load('ufo.png')
Spaceship = pygame.transform.scale(Spaceship, (80, 80))
# Spaceship = pygame.transform.rotate(Spaceship, 180)
Spaceship_Speed = 0
SpaceshipX = 370
SpaceshipY = 500

'''Asteroid Declaration'''

num_of_Enemies = 10
# for i in range(num_of_Enemies):
AsteroidImg = pygame.image.load("asteroid.png")
Asteroid_Size = random.randint(20, 70)
AsteroidImg = pygame.transform.scale(
    AsteroidImg, (Asteroid_Size, Asteroid_Size))
AsteroidX = random.randint(0, 500)
AsteroidY = random.randint(0, 200)
Asteriod_SpeedX = random.randint(10, 30) / 100 *-1
Asteroid_SpeedY = Asteriod_SpeedX if Asteriod_SpeedX > 0 else -Asteriod_SpeedX

# This shit does'nt work!
def Reset_Asteroid():
    AsteroidX = random.randint(0, 500)
    AsteroidY = random.randint(0, 200)
    Asteroid_SpeedX = random.randint(20, 50) / 100 * -1
    Asteroid_SpeedY = Asteriod_SpeedX if Asteriod_SpeedX > 0 else -Asteriod_SpeedX
    Asteroid_Size = random.randint(20, 70)

    return [AsteroidX, AsteroidY, Asteroid_SpeedX, Asteroid_SpeedY,Asteroid_Size]


def Respawn_Asteroid(AsteroidX,AsteroidY,):
    screen.blit(AsteroidImg, (AsteroidX, AsteroidY))


'''Background Image Declaration'''
BG_Image = pygame.image.load("BG_IMAGE.jpg")
BG_Image = pygame.transform.scale(BG_Image, (800, 600))
'''Sperm Declaration'''
Bullet = pygame.image.load("bullet.png")
Bullet = pygame.transform.scale(Bullet, (30, 30))
Bullet = pygame.transform.rotate(Bullet, 55)
BulletY = 530
BulletX = 0
Bullet_Speed = 3
# Sperm State == Ready => No-Shoot
# Sperm State == Fire => Shoot
Bullet_state = "Ready"


def fire_Bullet(x, y):
    global Bullet_state
    Bullet_state = "Fire"
    screen.blit(Bullet, (x + 17, y))


def isCollision(Bul_X, Bul_Y, Ast_X, Ast_Y, Ast_size):

    distance = math.sqrt(math.pow(Ast_X - Bul_X, 2) +
                         math.pow(Ast_Y - Bul_Y, 2))

    if Ast_X < Bul_X < (Ast_X + Ast_size) and distance < Asteroid_Size:
        return True
    else:
        return False
    # if  Ast_X < Bul_X < (Ast_X) and Ast_Y < Bul_Y < (Ast_Y) :
    #     print("Asteroid Size : ", Asteroid_size)
    #     print(f"Ast_X : {Ast_X}\n(Ast_X + Asteroid_size) : {(Ast_X + Asteroid_size)} \n(Ast_Y + Asteroid_size) : {(Ast_Y + Asteroid_size)}\nSpermX : {Bul_X}\nSpermY : {Bul_Y}")
    #     return True
    # else:
    #     return False


'''Explosion Declaration'''
Explosion = pygame.image.load('explosion.png')
Explosion = pygame.transform.scale(Explosion, (60, 60))

Score = 0
'''Main game loop'''
running = True
while running:
    # screen colouring
    screen.fill((159, 43, 104))  # PINK

    # making sure we can legitly quit the gaming
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print('left key is pressed')
                Spaceship_Speed = -2
            if event.key == pygame.K_RIGHT:
                # print('Right key is pressed')
                Spaceship_Speed = 2
            if event.key == pygame.K_SPACE:
                if Bullet_state == "Ready":
                    # Get the current X coord of Spaceship
                    BulletX = SpaceshipX
                    fire_Bullet(BulletX, BulletY)

        if event.type == pygame.KEYUP:
            # print('KEYUP')
            Spaceship_Speed = 0
    # Move the Asteroid
    # for i in range(num_of_Enemies):
    if AsteroidX > 750:
        AsteroidX = 749
        Asteriod_SpeedX *= -1
    if AsteroidX < 0:
        AsteroidX = 0
        Asteriod_SpeedX *= -1
    AsteroidX += Asteriod_SpeedX
    AsteroidY += Asteroid_SpeedY
    collision = isCollision(Bul_X=BulletX,
                            Ast_X=AsteroidX,
                            Bul_Y=BulletY,
                            Ast_Y=AsteroidY,
                            Ast_size=Asteroid_Size)
    if collision:

        screen.blit(Explosion, (BulletX, BulletY))
        BulletY = 530
        Score += 1
        print(Score)
        '''Resetting the Asteroid'''
        [AsteroidX, AsteroidY, Asteroid_SpeedX, Asteroid_SpeedY,Asteroid_Size] =Reset_Asteroid()
        '''Resetting the Explosion'''
        Bullet_state = "Ready"
    if AsteroidY > 500:
        BulletY = 530
        Score -= 1
        print(Score)
        '''Resetting the Asteroid'''
        [AsteroidX, AsteroidY, Asteroid_SpeedX, Asteroid_SpeedY,Asteroid_Size] = Reset_Asteroid()
        '''Resetting the Explosion'''
        Bullet_state = "Ready"
    # ============================================
    # Move the Spaceship
    SpaceshipX += Spaceship_Speed
    if SpaceshipX < 00:
        SpaceshipX = 00
    if SpaceshipX > 750:
        SpaceshipX = 750

    # Show BG Image
    screen.blit(BG_Image, (0, 0))
    # Move The Bullet
    if BulletY < 0:
        BulletY = 530
        Bullet_state = "Ready"
    if Bullet_state == "Fire":
        fire_Bullet(BulletX, BulletY)
        BulletY -= Bullet_Speed

    # show Spaceship on screen
    screen.blit(Spaceship, (SpaceshipX, SpaceshipY))
    # # show Asteroid on screen
    screen.blit(AsteroidImg, (AsteroidX, AsteroidY))

    pygame.display.update()
