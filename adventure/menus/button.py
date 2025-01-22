"""Implements buttons for the menus."""

from typing import Tuple

import pygame


class Button(pygame.sprite.Sprite):

    def __init__(
        self,
        x: int,
        y: int,
        text: str,
        color: str | Tuple[int, int, int],
        hover_color: str | Tuple[int, int, int],
        font: pygame.font.Font,
    ):

        # handle containers for this entity, TODO: fix later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.font = font
        self.render = self.font.render(self.text, True, self.color)
        self.rect = self.render.get_rect(center=(self.x, self.y))
        self.text_rect = self.render.get_rect(center=(self.x, self.y))

    def update(self, screen: pygame.surface.Surface):
        screen.blit(self.render, self.text_rect)

    def is_mouse_on_self(self) -> bool:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return mouse_x in range(self.rect.left, self.rect.right) and mouse_y in range(self.rect.top, self.rect.bottom)

    def is_clicked(self) -> bool:
        """Check if this button is being clicked."""
        return self.is_mouse_on_self() and pygame.mouse.get_pressed()[0]

    def change_color_on_hover(self) -> None:
        """Change the color if this button is being hovered over."""
        if self.is_mouse_on_self():
            self.render = self.font.render(self.text, True, self.hover_color)
        else:
            self.render = self.font.render(self.text, True, self.color)
