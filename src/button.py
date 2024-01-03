import pygame
import button
import math

class Button():
    def __init__(self, x, y, image, scale, selected_frame_index=0):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.selected_frame_index = selected_frame_index

        self.outline_color = (255, 0, 0) #Select an outline color
        self.outline_width = 5 #Choose how thicc the hitbox will be

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        if self.clicked:
            # Draw the outline when the button is selected
            pygame.draw.rect(surface, self.outline_color, self.rect, self.outline_width)

        return action

