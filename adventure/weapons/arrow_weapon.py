"""
Base class for any firearms.
"""

from __future__ import annotations

from adventure.projectiles.projectile import Arrow
from adventure.weapons.projectile_weapon import ProjectileWeapon


class ArrowWeapon(ProjectileWeapon):

    FIRE_RATE = 1
    MAGAZINE_CAPACITY = 1
    PROJECTILE_TYPE = Arrow
    TOTAL_LENGTH = 15
