import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH, PLAYER_RADIUS
from logger import log_state
from player import Player

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
    Clock = pygame.time.Clock()

# DELTA TIME initialization (must be BEFORE GameLoop while loop)
    dt: float = 0.0


# INITIALIZING GROUPS

    updatable = pygame.sprite.Group() # will hold all the objects that can be updated
    drawable = pygame.sprite.Group() # will hold all the objects that can be drawn

    # ADDING CLASSES TO GROUPS:

    Player.containers = (updatable, drawable) # Add the Player class to the updatable and drawable groups before the player object instance is created.

# !!!! DO AFTER `GROUPS` INITIALIZATION

# INITIALIZING PLAYER OBJECT (!!!! MUST BEFORE GAMELOOP OTHERWISE WILL SPAWN ALWAYS IN GIVEN COORDINATES and NOT UPDATE PROPERLY)
    # For drawing player in center of screen
    playerX = SCREEN_WIDTH / 2  
    playerY = SCREEN_HEIGHT / 2

    player = Player(playerX, playerY, PLAYER_RADIUS)

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
        
    # FILLING SCREEN black, can literally just pass the string "black" to the method    
        screen.fill("black")

    # THINGS THAT NEED TO BE DRAWN/Updated BEFORE REFRESH

        # GROUPS UPDATE CALL

        updatable.update(dt)

        # GROUPS DRAW CALL

        for drawables in drawable:
            drawables.draw(screen)

        
        # PLAYER UPDATE CALL (switched over to GROUPS)
        #player.update(dt)
        
        #PLAYER DRAW CALL (switched over to GROUPS)
        #player.draw(screen)

        
        #REFRESHING SCREEN (flipping screen)
        # method to refresh the screen. Be sure to call this last!
        pygame.display.flip()

        """At the end of each iteration of the game loop, call the .tick() method on the clock object, 
        pass it 60, and save the return value divided by 1000 into dt. 
        The .tick() method returns the amount of time that has passed since the last time it was called: the delta time.
        """
        dt = Clock.tick(60) / 1000

        




if __name__ == "__main__":
    main()
