"""
Base class for any firearms.
"""

from adventure.projectiles.projectile import Bullet9mm
from adventure.projectiles.projectile import Bullet45cal
from adventure.projectiles.projectile import Bullet556cal
from adventure.projectiles.projectile import Projectile


class Firearm:
    """A firearm usable by characters."""

    BULLET_DAMAGE = 100
    FIRE_RATE = 0.3
    MAGAZINE_CAPACITY = 30
    BULLET_TYPE = Bullet9mm

    def __init__(self, wielder):
        self.wielder = wielder
        self.fire_rate = self.FIRE_RATE
        self.magazine_capacity = self.MAGAZINE_CAPACITY
        self.magazine_count = self.magazine_capacity  # start fully loaded
        self.bullet_type = self.BULLET_TYPE
        self.shot_cooldown = 0

    def use(self) -> None:
        self.shoot()

    def shoot(self) -> None:
        if self.shot_cooldown > 0:
            return
        self.bullet_type(
            self.wielder.position.x,
            self.wielder.position.y,
            self.wielder.rotation,
            self.wielder,
        )
        self.magazine_count -= 1
        self.shot_cooldown = self.fire_rate

    def update_cooldown(self, dt: int):
        self.shot_cooldown -= dt

    def get_max_range(self) -> int:
        return self.bullet_type.MAX_RANGE


class Glock19(Firearm):

    FIRE_RATE = 0.5


class Colt1911(Firearm):

    FIRE_RATE = 0.8
    BULLET_TYPE = Bullet45cal


class SMG(Firearm):

    FIRE_RATE = 0.075


class AR15(Firearm):

    FIRE_RATE = 0.11
    BULLET_TYPE = Bullet556cal
