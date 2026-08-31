import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite): 
    containers: tuple[pygame.sprite.Group, ...] #provided code

    def __init__(self, x: float, y: float, radius: float) -> None: #provided code
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y) 
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None: #provided code
        # must override
        pass

    def update(self, dt: float) -> None: #provided code
        # must override
        pass

    def collides_with(self, other) -> bool:

        distance = self.position.distance_to(other.position) #Calculating the distance between the center of the two circles: "distance"

        if distance <= (self.radius + other.radius): # If distance is less than or equal to r1 + r2, the circles are colliding. If not, they aren't!
            return True
        else:
            return False

"""
In Pygame, there's a base Sprite class that represents visual objects.

 CircleShape class that inherits from Sprite to represent objects in our game that are treated as circles (even if they aren't, like the player's ship).

CircleShape extends the Sprite class to store 3 additional attributes specific to our game:

position (x and y coordinates)
velocity
radius.

Later we'll write subclasses of CircleShape and override the draw and update methods with the logic for each particular game object.
"""
