"""Handles base entities in the game."""

from __future__ import annotations

from typing import Optional

import pygame

from adventure.constants import COLOR_WHITE


class Entity(pygame.sprite.Sprite):
    """Base class for any entity in the game."""

    COLOR = COLOR_WHITE
    TURN_SPEED = 20
    MOVEMENT_SPEED = 50

    def __init__(self, x: Optional[int] = 0, y: Optional[int] = 0, radius: Optional[int] = 5):

        # handle containers for this entity, TODO: fix later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.movement_speed = self.MOVEMENT_SPEED
        self.radius = radius
        self.rotation = 0
        self.color = self.COLOR
        self.turn_speed = self.TURN_SPEED
        self.width = 2

    def draw(self, screen) -> None:
        """Draw this entity on the screen."""
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def rotate(self, dt: int) -> None:
        self.rotation += self.turn_speed * dt

    def rotate_towards(self, dt: int, vector: pygame.Vector2) -> None:
        """Rotate towards a given angle, but don't get there unless we have enough time to get there."""
        max_rotation = self.turn_speed * dt
        target_angle = self.get_angle_to_vector(vector)
        self.rotation %= 360
        difference = (self.rotation - target_angle) % 360
        if difference < 0.5:
            # skip any overcorrection and just set our angle appropriately
            self.rotation = target_angle
        else:
            direction = 1 if difference > 180 else -1
            self.rotation += max_rotation * direction

    def update(self, dt) -> None: ...

    def get_angle_to_vector(self, vector: pygame.Vector2) -> float:
        """Return the polar angle from the current entity to a given vector."""
        self_to_vector = (vector - self.position).normalize()
        polar_angle = self_to_vector.as_polar()[1] - 90
        return polar_angle % 360

    def get_angle_to_mouse(self) -> float:
        """Return the polar angle from the current entity to the mouse cursor."""
        return self.get_angle_to_vector(pygame.Vector2(*pygame.mouse.get_pos()))

    @staticmethod
    def get_mouse_position() -> pygame.Vector2:
        return pygame.Vector2(*pygame.mouse.get_pos())

    def check_collision(self, other: Entity) -> bool:
        """Check if this is colliding with another entity."""
        collision_distance = self.radius + other.radius
        actual_distance = self.position.distance_to(other.position)
        return actual_distance <= collision_distance
