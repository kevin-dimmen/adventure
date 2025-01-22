"""
Base class for any firearms.
"""

from adventure.projectiles.projectile import Projectile


class Firearm:
    """A firearm usable by characters."""

    BULLET_DAMAGE = 100
    BULLET_RANGE = 100
    FIRING_SPEED = 0.3

    def __init__(self, wielder):
        self.wielder = wielder
        self.bullet_damage = self.BULLET_DAMAGE
        self.bullet_range = self.BULLET_RANGE
        self.firing_speed = self.FIRING_SPEED
        self.cooldown = 0

    def use(self) -> None:
        self.shoot()

    def shoot(self) -> None:
        if self.cooldown > 0:
            return
        Projectile(self.wielder.position.x, self.wielder.position.y, self.wielder.rotation, self.wielder)
        self.cooldown = self.firing_speed

    def update_cooldown(self, dt: int):
        self.cooldown -= dt


class Pistol(Firearm):

    BULLET_DAMAGE = 75
    BULLET_RANGE = 200
    FIRING_SPEED = 0.5


class SMG(Firearm):

    BULLET_DAMAGE = 85
    BULLET_RANGE = 400
    FIRING_SPEED = 0.075
