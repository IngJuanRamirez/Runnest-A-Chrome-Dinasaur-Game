# ========================================================================================================================
# Runnest-A-Chrome-Dinasaur-Game
# Created by Juan. A. Ramirez
# November 2025
# If you wan to see the code, please visit: https://github.com/IngJuanRamirez/Runnest-A-Chrome-Dinasaur-Game.git
# ========================================================================================================================

# player.py

from pygame import sprite, Surface, Rect

class Player(sprite.Sprite):
    def __init__(self, x, y, *groups) -> None:
        super().__init__(*groups)

        # Player image
        self.image = Surface((40, 60))
        self.image.fill((255, 0, 0)) # Red color for player

        # Player Rect
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # == Character Physics ==
        self.gravity = 1
        self.vel_y = 0 # Vertical velocity
        # This variable is negative because is moving up
        self.jump_power = -20 # How high does he jump?
        self.is_on_ground = True # Default

    def jump(self) -> None:
        """Jumps only if the player is on the ground"""
        if self.is_on_ground:
            self.vel_y = self.jump_power
            self.is_on_ground = False

    def update(self, ground_group: sprite.Group) -> None:
        """Update Logic"""
        
        # Apply gravity
        self.vel_y += self.gravity
        # Update pos Y
        self.rect.y += self.vel_y

        hits = sprite.spritecollide(self, ground_group, False)

        # Check for collisions
        if hits:
            # If collides, land"
            self.rect.bottom = hits[0].rect.top
            self.vel_y = 0
            self.is_on_ground = True
        else:
            self.is_on_ground = False