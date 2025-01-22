"""
Base class for any firearms.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Tuple

import pygame

from adventure.entities.entity import Entity
from adventure.projectiles.projectile import Projectile

if TYPE_CHECKING:
    from adventure.characters.character import Character


class ProjectileWeapon(Entity):
    """A firearm usable by characters."""

    FIRE_RATE = 2
    MAGAZINE_CAPACITY = 1
    PROJECTILE_TYPE = Projectile
    TOTAL_LENGTH = 20

    def __init__(self, wielder: Character):
        super().__init__(wielder.position.x, wielder.position.y, wielder.rotation)
        self.wielder = wielder
        self.fire_rate = self.FIRE_RATE
        self.magazine_capacity = self.MAGAZINE_CAPACITY
        self.magazine_count = self.magazine_capacity  # start fully loaded
        self.projectile_type = self.PROJECTILE_TYPE
        self.total_length = self.TOTAL_LENGTH
        self.shot_cooldown = 0

    def update(self, dt) -> None:
        self.position = self.wielder.hand_position()
        self.rotation = self.wielder.rotation

    def muzzle(self) -> pygame.Vector2:
        return self.position + pygame.Vector2(0, self.total_length).rotate(self.rotation)

    def polygon(self) -> Tuple[int, int, int, int]:
        muzzle = self.muzzle()
        return muzzle, self.wielder.hand_position()
        muzzle = pygame.Vector2(0, self.total_length).rotate(self.rotation)
        butt = pygame.Vector2(0, 1).rotate(self.rotation)
        a = self.position + muzzle * self.radius
        b = self.position + muzzle * self.radius
        c = self.position + butt * self.radius
        d = self.position + butt * self.radius
        return a, c, b, d

    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, self.color, self.polygon(), 2)

    def use(self) -> None:
        self.shoot()

    def shoot(self) -> None:
        if self.shot_cooldown > 0:
            return
        muzzle = self.muzzle()
        self.projectile_type(
            muzzle.x,
            muzzle.y,
            self.rotation,
            self.wielder,
        )
        self.magazine_count -= 1
        self.shot_cooldown = self.fire_rate

    def update_cooldown(self, dt: float):
        self.shot_cooldown -= dt

    def get_max_range(self) -> int:
        return self.projectile_type.MAX_RANGE
