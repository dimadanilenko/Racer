from random import randint
import pygame
from pygame.constants import K_LEFT, K_RIGHT, K_SPACE, K_UP, K_DOWN
pygame.init()

w = 500
h = 500

pygame.display.set_caption('Racer')
sc = pygame.display.set_mode((w, h))
sc.fill((100, 150, 200))


clock = pygame.time.Clock()
fps = 60

fone = pygame.image.load('fone.png')
plfone = fone.get_rect(center=(w//2, h//2))


playerCar = pygame.image.load('myCar.png')
playerCarPlace = playerCar.get_rect(center=(50, 450))

trafikCar = pygame.image.load('trafikCar.png')
trafikCarPlace = trafikCar.get_rect(center=(150, h - 450))

twotrafikCar = pygame.image.load('trafickCar1.png')
twotrafikCarPlace = twotrafikCar.get_rect(center=(200, 0))

threetrafikCar = pygame.image.load('trafikCar2.png')
threetrafikCarPlace = threetrafikCar.get_rect(center=(300, 0))

fourtrafikCar = pygame.image.load('bus.png')
fourtrafikCarPlace = fourtrafikCar.get_rect(center=(350, 0))

score = 0

f = pygame.font.Font(None, 24)
sc_text = f.render(str(score), 1, (255, 0, 0), (255, 255, 255))
pos = sc_text.get_rect(center=(w//2, 40))

game = pygame.font.Font(None, 96)
gameText = game.render('Game Over', 1, (255, 0, 0), (255, 255, 255))
gamePos = gameText.get_rect(center=(w//2, h//2))

sms = pygame.font.Font(None, 24)
smsText = sms.render('Для рестарта удерживайте 2 сек. и отпустите пробел', 1, (255, 0, 0), (255, 255, 255))
smsPos = smsText.get_rect(center=(w//2, 200))

priewy = True

speed = 8
trafikSpeed = 4
lose = 0
scoreSpeed = 1
over = False
 
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    
    key = pygame.key.get_pressed()
        
    if key[K_LEFT]:
        if playerCarPlace.x > 50 :    
            playerCarPlace.x -= speed
        
        

    if key[K_RIGHT]:
        if  playerCarPlace.x < 420:
            playerCarPlace.x += speed    
    
    if True:
        trafikCarPlace.y += trafikSpeed
        if trafikCarPlace.y > 500:
            trafikCarPlace.y = 0
            trafikCarPlace.x = randint(50, 130)   
    
    if True:    
        twotrafikCarPlace.y += trafikSpeed
        if twotrafikCarPlace.y > 500:
            twotrafikCarPlace.y = -10
            twotrafikCarPlace.x = randint(150,200)

    if True:
        threetrafikCarPlace.y += trafikSpeed                 
        if threetrafikCarPlace.y > 500:
            threetrafikCarPlace.y = -10
            threetrafikCarPlace.x = randint(260,315)

    if True:
        fourtrafikCarPlace.y += trafikSpeed
        if fourtrafikCarPlace.y > 500:
            fourtrafikCarPlace.y = -10
            fourtrafikCarPlace.x = randint(360, 410)
                    

    if True:
        if scoreSpeed == 0:
            score += 1
            sc_text = f.render(str(score), 1, (255, 0, 0), (255, 255, 255))
        elif scoreSpeed == 1:
            score += 2
            sc_text = f.render(str(score), 1, (255, 0, 0), (255, 255, 255))

        elif scoreSpeed == 2:
            score -= 1
            sc_text = f.render(str(score), 1, (255, 0, 0), (255, 255, 255)) 

        if score == 0:
            gameText = game.render('Game Over', 1, (255, 0, 0), (255, 255, 255))
            smsText = sms.render('Для рестарта удерживайте 2 сек. и отпустите пробел', 1, (255, 0, 0), (255, 255, 255))
    
        if key[K_UP]:
            trafikSpeed = 8
            scoreSpeed = 1
        elif key[K_DOWN]:
            trafikSpeed = 2
            scoreSpeed = 2 

        else:
            trafikSpeed = 4
            scoreSpeed = 0

        if trafikCarPlace.collidepoint(playerCarPlace.center):
            priewy = False


        if twotrafikCarPlace.collidepoint(playerCarPlace.center):   
            priewy = False

        if threetrafikCarPlace.collidepoint(playerCarPlace.center):
            priewy = False

        if fourtrafikCarPlace.collidepoint(playerCarPlace.center):
            priewy = False

    if score < 0:
        priewy = False

    keyy = pygame.key.get_pressed()
    if priewy == False:
        score = 0
        gameText = game.render('Game Over', 1, (255, 0, 0), (255, 255, 255))
        smsText = sms.render('Для рестарта удерживайте 2 сек. и отпустите пробел', 1, (255, 0, 0), (255, 255, 255))
    
    if keyy[K_SPACE]:
        priewy = True
    
    if priewy == True:
        sc.blit(fone, plfone)
        sc.blit(playerCar, playerCarPlace)
        sc.blit(trafikCar, trafikCarPlace)
        sc.blit(twotrafikCar, twotrafikCarPlace)
        sc.blit(sc_text, pos)
        sc.blit(threetrafikCar, threetrafikCarPlace)
        sc.blit(fourtrafikCar, fourtrafikCarPlace)
    if priewy == False:
        sc.blit(gameText, gamePos)
        sc.blit(smsText, smsPos)
    pygame.display.update()
    clock.tick(fps)        