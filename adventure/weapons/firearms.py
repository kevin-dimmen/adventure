"""
Base class for any firearms.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Tuple

import pygame

from adventure.entities.entity import Entity
from adventure.projectiles.projectile import Bullet9mm
from adventure.projectiles.projectile import Bullet45cal
from adventure.projectiles.projectile import Bullet556cal
from adventure.projectiles.projectile import CannonBall
from adventure.weapons.projectile_weapon import ProjectileWeapon

if TYPE_CHECKING:
    from adventure.characters.character import Character


class Firearm(ProjectileWeapon):
    """A firearm usable by characters."""

    FIRE_RATE = 0.3
    MAGAZINE_CAPACITY = 30
    PROJECTILE_TYPE = Bullet9mm


class Glock19(Firearm):

    FIRE_RATE = 0.5
    COLOR = "green"


class Colt1911(Firearm):

    FIRE_RATE = 0.8
    PROJECTILE_TYPE = Bullet45cal
    COLOR = "orange"


class SMG(Firearm):

    FIRE_RATE = 0.075
    COLOR = "white"


class AR15(Firearm):

    FIRE_RATE = 0.11
    PROJECTILE_TYPE = Bullet556cal
    COLOR = "purple"


class Cannon(Firearm):

    FIRE_RATE = 2
    PROJECTILE_TYPE = CannonBall
    COLOR = "purple"
