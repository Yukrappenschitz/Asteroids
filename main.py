import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initiliazing pygame
    pygame.init()

    #initial setup for pygame
    #using `display.set_mode` function to get a new instance of GUI window:
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #creating GAMELOOP

    while True:
        # for logging
        
        log_state() 

        #can start processing the pygame event queue
        
        for event in pygame.event.get(): 
            pass

        # can literally just pass the string "black" to the method    
        screen.fill("black")

        # method to refresh the screen. Be sure to call this last!
        pygame.display.flip()


if __name__ == "__main__":
    main()
