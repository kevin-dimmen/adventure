"""Main adventure portion of the game."""

from typing import Optional

import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH

from adventure.characters.enemy import Enemy
from adventure.characters.enemy import EnemySpawner
from adventure.characters.player import Player
from adventure.engine import Engine
from adventure.projectiles.projectile import Projectile


class MainAdventure(Engine):
    """Main adventure game."""

    def __init__(self, screen: Optional[pygame.surface.Surface] = None) -> None:
        super().__init__(screen)
        self.update_objects = None
        self.drawn_objects = None
        self.projectile_objects = None
        self.enemy_objects = None
        self.player = None

    def engine_setup(self) -> None:
        self.setup_groups()
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        EnemySpawner(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup_groups(self) -> None:
        self.update_objects = pygame.sprite.Group()
        self.drawn_objects = pygame.sprite.Group()
        self.projectile_objects = pygame.sprite.Group()
        self.enemy_objects = pygame.sprite.Group()
        Player.containers = (self.update_objects, self.drawn_objects)
        Projectile.containers = (self.update_objects, self.drawn_objects, self.projectile_objects)
        Enemy.containers = (self.update_objects, self.drawn_objects, self.enemy_objects)
        EnemySpawner.containers = (self.update_objects,)

    def show_health(self) -> None:
        font = pygame.font.Font(None, 20)
        self.health_bar = pygame.sprite.Sprite()
        self.health_bar.image = font.render(f"Health: {self.player.health}", 1, "red")
        self.health_bar.rect = self.health_bar.image.get_rect(topleft=(10, 10))
        # self.health_bar.draw()

    def engine_draw(self) -> None:
        for x in self.drawn_objects:
            x.draw(self.screen)
        self.show_health()

    def engine_logic(self) -> None:
        self.update()

    def update(self) -> None:
        for updated in self.update_objects:
            updated.update(self.dt)
        for enemy in self.enemy_objects:
            enemy.check_player(self.player, self.dt)
        for projectile in self.projectile_objects:
            projectile.check_range()
            if projectile.check_hit(self.player):
                self.player.kill()
            for enemy in self.enemy_objects:
                if projectile.check_hit(enemy):
                    enemy.kill()

    def clean_up(self) -> None:
        self.player.kill()


def main() -> None:
    """Run the game."""
    MainAdventure().start()


if __name__ == "__main__":
    main()
