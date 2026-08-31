import pygame

from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x:float, y:float, radius: float):

        super().__init__(x,y,PLAYER_RADIUS) 
        #calling super to call the constructor of CircleShape with x,y as x,y and PLAYER_RADIUS as radius

        self.rotation: int|float = 0
        # introducing new property `rotation` to probably determine direction/heading

        self.shoot_cooldown = 0

        
        
            
    def triangle(self) -> list[pygame.Vector2]: #provided code
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    """
    To draw the player, override the draw method of CircleShape. It should take the screen object as a parameter, and call pygame.draw.polygon(). It takes as inputs:
    The screen object
    A color (use "white")
    A list of points (use the list returned by a call to the self.triangle() function)
    A line width (use the one in your constants.py file)
    """
    def draw(self, screen: pygame.Surface) -> None: 

    # drawing player polygon call
        pygame.draw.polygon(screen, "white", self.triangle(),LINE_WIDTH)

        #return super().draw(screen)

    def rotate(self,dt):

        self.rotation += (PLAYER_TURN_SPEED * dt)


    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
    #MOVEMENT keys
        if keys[pygame.K_a]: #turning left

            self.rotate(-dt)

            # To go left instead of right when `a`` is pressed, you'll need to reverse dt

        if keys[pygame.K_d]: #turning right

            self.rotate(dt)

            # To go right when `d` keypress is pressed, you'll need to use dt
        
        if keys[pygame.K_w]: # forward/up

            self.move(dt)

        if keys[pygame.K_s]: # backwards/down

            self.move(-dt) # negate `dt`` for the S key, so the player moves backward.

    #SHOOT

        if keys[pygame.K_SPACE]: # shoot bullet button

            if self.shoot_cooldown > 0:
                pass
            else:
                self.shoot()
                self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS


    def shoot(self) -> None: # initializes a shot/bullet from player 

        self.x = self.position[0] # needs to get update position cordinates [0] so needs to take from updating self.postion
        self.y = self.position[1] # needs to get update position cordinates [1] so needs to take from updating self.postion

        shot = Shot(self.x, self.y, SHOT_RADIUS) # need to spawn a new `Shot` at the player's current position

        unit_vector = pygame.Vector2(0,1) # starting with a unit vector

        rotated_vector = unit_vector.rotate(self.rotation) # rotating unit vector to align to player heading, and storing in a new vector

        rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED #Scaling the properly headed vector (multiplied by PLAYER_SHOOT_SPEED) to make it move faster

        shot.velocity += rotated_with_speed_vector # setting the shot.velocity attribute to the scaled and allgned vector



    def move(self,dt): # provided vector code

        #Start with a unit vector pointing straight down from (0, 0) to (0, 1).

        unit_vector = pygame.Vector2(0, 1) 

        #Rotate that vector by the player's rotation, so it's pointing in the same direction as the player.

        rotated_vector = unit_vector.rotate(self.rotation) 

        #import the PLAYER_SPEED constant and multiply the vector by PLAYER_SPEED * dt so that the vector is the length the player should move during this frame.
        
        rotated_with_speed_vector = (rotated_vector * PLAYER_SPEED * dt)

        # Add the vector to the player's position to move them.
        
        self.position += rotated_with_speed_vector

    


