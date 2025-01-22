"""Classes for enemy characters."""

import random
from typing import Optional

import pygame

from adventure.characters.character import Character
from adventure.constants import COLOR_RED
from adventure.weapons.arrow_weapon import ArrowWeapon
from adventure.weapons.firearms import AR15
from adventure.weapons.firearms import SMG
from adventure.weapons.firearms import Cannon
from adventure.weapons.firearms import Colt1911
from adventure.weapons.firearms import Glock19


class Enemy(Character):
    """Base class for any enemy in the game."""

    COLOR = COLOR_RED
    TURN_SPEED = 80
    MOVEMENT_SPEED = 90
    COMBAT_RANGE = 500
    AVAILABLE_FIREARMS = [Glock19, Colt1911, AR15, SMG, ArrowWeapon, Cannon]

    def __init__(
        self, x: Optional[int] = 0, y: Optional[int] = 0, radius: Optional[int] = None, rotation: Optional[int] = 0
    ):
        super().__init__(x, y, radius, rotation)
        self.combat_range = self.COMBAT_RANGE
        self.engage_combat = False
        self.weapon = random.choice(self.AVAILABLE_FIREARMS)(self)

    def check_player(self, player: Character, dt: float) -> None:
        """Check our current status against the player."""
        if self.check_combat_range(player):
            self.engage_combat = True
            self.move_forwards(dt)
            if self.is_facing_character(player):
                if self.check_weapon_range(player):
                    self.use_weapon(dt)
        if self.engage_combat:
            # so far enemies remain in combat until death
            self.target_character(player, dt)

    def check_combat_range(self, player: Character) -> bool:
        """Check is we are within combat range of the player."""
        distance_to_player = self.position.distance_to(player.position)
        return distance_to_player <= self.combat_range

    def check_weapon_range(self, player: Character) -> bool:
        """Check is we are within combat range of the player."""
        distance_to_player = self.position.distance_to(player.position)
        return distance_to_player <= self.weapon.get_max_range()


class EnemySpawner(pygame.sprite.Sprite):

    SPAWN_RATE = 1.5

    def __init__(self, screen_width: int, screen_height: int) -> None:
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_rate = self.SPAWN_RATE
        self.spawn_timer = 0
        self.screen_width = screen_width
        self.screen_height = screen_height

    def spawn(self):
        Enemy(random.randrange(self.screen_width), random.randrange(self.screen_height), rotation=random.randrange(360))

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > self.spawn_rate:
            self.spawn_timer = 0
            self.spawn()
