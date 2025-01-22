"""Handles base HUD elements in the game."""

from __future__ import annotations

from typing import Optional

import pygame

from adventure.characters.player import Player
from adventure.constants import COLOR_RED
from adventure.entities.entity import Entity
from adventure.fonts.fonts import get_main_font


class HeadsUpDisplayElement(Entity):
    """Base class for any HUD element in the game."""

    COLOR = COLOR_RED

    def __init__(
        self,
        x: Optional[int] = 0,
        y: Optional[int] = 0,
    ):
        super().__init__(x=x, y=y)


class HealthBar(HeadsUpDisplayElement):

    COLOR = COLOR_RED

    def __init__(
        self,
        x: Optional[int] = 10,
        y: Optional[int] = 10,
        player: Optional[Player] = None,
    ):
        super().__init__(x=x, y=y)
        self.player = player if player else Player
        self.image = None
        self.rect = None

    def draw(self, screen: pygame.surface.Surface) -> None:
        self.image = get_main_font(20).render(f"Health: {self.player.health}", 1, "red")
        self.rect = self.image.get_rect(topleft=self.position.xy)
        screen.blit(self.image, self.rect)
