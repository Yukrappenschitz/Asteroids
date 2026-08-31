import sys
import pygame
from constants import * #SCREEN_WIDTH, SCREEN_HEIGHT, LINE_WIDTH, PLAYER_RADIUS
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    asteroids = pygame.sprite.Group() # will hold asteroids

    shots = pygame.sprite.Group() # will hold the shots/bullets

    # ADDING CLASSES TO GROUPS:

    Player.containers = (updatable, drawable) # Add the Player class to the updatable and drawable groups before the player object instance is created.
    Asteroid.containers = (asteroids, updatable, drawable) # Asteroid needs to be in updatable and drawable

    AsteroidField.containers = (updatable) # the AsteroidField class and set its static containers field to only the updatable group (it's not drawable, and it's not an asteroid itself)

    Shot.containers = (shots,updatable,drawable) # the Shot class needs to be in its own shot group BUT also in updatable, drawable

# !!!! NEEDS TO BE INITIALIZED AFTER `GROUPS` and `CONTAINERS` INITIALIZATION

# INITIALIZING ASTEROID FIELD OBJECT

    asteroidfield = AsteroidField()

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

        # descreasing shoot timer by dt

        player.shoot_cooldown -= dt

        # GROUPS DRAW CALL

        for drawables in drawable:
            drawables.draw(screen)

        
                # PLAYER UPDATE CALL (switched over to GROUPS)
                #player.update(dt)
        
                #PLAYER DRAW CALL (switched over to GROUPS)
                #player.draw(screen)

        # !!! CHECKING FOR COLLISON (!!! MUST BE AFTER THE "UPDATED" FRAME to properly check collision BUT before next refresh)

        for asteroid in asteroids: # iterate over all the objects in your asteroids group to check collision with player

            if player.collides_with(asteroid): # Checking if any of them collide with the player
                log_event("player_hit") # log event
                print("Game over!")
                sys.exit() # exiting game since game over
            else: 
                pass

        for asteroid in asteroids: # iterate over all the objects in your asteroids group to check collision with shots

            for shot in shots: # iterate over all the objects in the shots to check every shot and if they collide with an asteroid

                if asteroid.collides_with(shot): # checking collision with shot and asteroid
                    log_event("asteroid_shot") # log event

                    # asteroid.kill() # calling built in pygame .kill() method on asteroid [replaced with new splitting method]
                    
                #ASTEROID SPLIITING

                    asteroid.split() # calling new split method to see if asteroid needs to be split/ killed
                    
                    shot.kill() # calling built in pygame .kill() method on shot

                    #The kill() method is a built-in feature of Pygame sprites. It removes the "killed" object from all its groups so that the engine stops updating and drawing it.
                
                else:
                    pass
                 
        #REFRESHING SCREEN (flipping screen)
        # method to refresh the screen. Be sure to call this last!
        pygame.display.flip()

        """At the end of each iteration of the game loop, call the .tick() method on the clock object, 
        pass it 60, and save the return value divided by 1000 into dt. 
        The .tick() method returns the amount of time that has passed since the last time it was called: the delta time.
        """
        dt = Clock.tick(60) / 1000

#push example

if __name__ == "__main__":
    main()
