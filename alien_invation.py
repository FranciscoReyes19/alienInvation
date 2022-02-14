import sys
import pygame
# SDL - Simple Directmedia Layer

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800)) # devuelve Surface
    pygame.display.set_caption("Invación de Alies")

    while True:

        #Interaccion del usuario
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Dibujar
        pygame.display.flip()

run_game()