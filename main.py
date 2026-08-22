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

# NEW CLOCK OBJECT from pygame (must be BEFORE GameLoop while loop)
    Clock: Clock = pygame.time.Clock()

# DELTA TIME initialization (must be BEFORE GameLoop while loop)
    dt: float = 0.0

#creating GAMELOOP

    while True:
        # for logging
        
        log_state() 

        #can start processing the pygame event queue
        
        for event in pygame.event.get(): 

            """
            This will check if the user has closed the window, and exit the game loop if they do. 
            It will make the window's close button actually work.
            """
            if event.type == pygame.QUIT:
                return



        # can literally just pass the string "black" to the method    
        screen.fill("black")

        # method to refresh the screen. Be sure to call this last!
        pygame.display.flip()

        """At the end of each iteration of the game loop, call the .tick() method on the clock object, 
        pass it 60, and save the return value divided by 1000 into dt. 
        The .tick() method returns the amount of time that has passed since the last time it was called: the delta time.
        """
        dt = Clock.tick(60) / 1000

        




if __name__ == "__main__":
    main()
