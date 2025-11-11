# ========================================================================================================================
# Runnest-A-Chrome-Dinasaur-Game
# Created by Juan. A. Ramirez
# November 2025
# If you wan to see the code, please visit: https://github.com/IngJuanRamirez/Runnest-A-Chrome-Dinasaur-Game.git
# ========================================================================================================================

# player.py

from pygame import sprite, Surface

class Player(sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)

        # Player image
        self.original_image = Surface((40, 60))
        self.original_image.fill((255, 0, 0)) # Red color for player

        # Player image crouched
        self.crouch_image = Surface((40, 30))
        self.original_image.fill((0, 0, 255)) # Red color for player

        # Normal image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

        # == Character Physics ==
        self.gravity = 1
        self.vel_y = 0 # Vertical velocity
        # This variable is negative because is moving up
        self.jump_power = -20 # How high does he jump?
        
        # States
        self.is_on_ground = True # Default
        self.is_crounched = False

    def jump(self) -> None:
        """Jumps only if the player is on the ground"""
        if self.is_on_ground  and not self.is_crounched:
            self.vel_y = self.jump_power
            self.is_on_ground = False

    def bend(self) -> None:
        "The player bend"
        # Only if the player is in the ground.
        if self.is_on_ground and not self.is_crounched:
            self.is_crounched = True
            # Save the old pos
            old_bottomleft = self.rect.bottomleft
            
            # Change the image
            self.image = self.crouch_image
            # Get the new rect
            self.rect = self.image.get_rect()

            # Repos the new rect
            self.rect.bottomleft = old_bottomleft

    def stand_up(self) -> None:
        "Get up the player"
        # Only if the player is crouched
        if self.is_crounched:
            self.is_crounched = False

            # Save the old pos
            old_bottomleft = self.rect.bottomleft

            # Return to the original image
            self.image = self.original_image
            self.rect = self.image.get_rect()

            # Repos
            self.rect.bottomleft = old_bottomleft


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