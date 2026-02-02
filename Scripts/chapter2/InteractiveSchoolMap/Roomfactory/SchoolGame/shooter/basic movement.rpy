default shooterHealth = 20

init python:
    import pygame
    
    shooterSquareX = 45
    shooterSquareY = 250
    shooterSpeed = 10
    #player manager


    def updateSquare():
        global shooterSquareX, shooterSquareY
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            shooterSquareY -= shooterSpeed
        if keys[pygame.K_DOWN]:
            shooterSquareY += shooterSpeed
        if keys[pygame.K_LEFT]:
            shooterSquareX -= shooterSpeed
        if keys[pygame.K_RIGHT]:
            shooterSquareX += shooterSpeed
        
        #Boundaries
        if shooterSquareX > 225:
            shooterSquareX = 225
        elif shooterSquareX < 45:
            shooterSquareX = 45
        if shooterSquareY > 1050:
            shooterSquareY = 1050
        elif shooterSquareY < 40:
            shooterSquareY = 40
        
        renpy.restart_interaction()

label shootingGame:
    call screen ShooterGameScreen
    return