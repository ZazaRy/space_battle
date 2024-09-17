import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



def main():
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    while True:
        screen.fill("BLACK")
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return





if __name__ == "__main__":
    main()

