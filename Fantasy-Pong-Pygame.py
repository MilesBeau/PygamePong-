import pygame

pygame.init()

background_colour = (234, 212, 252)

screen = pygame.display.set_mode((800,600))

screen = pygame.display.set_caption("Medieval Pygame Pong")

pygame.display.flip()

# Main Game Loop
KeepGameRunning = True

while KeepGameRunning:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            KeepGameRunning = False 