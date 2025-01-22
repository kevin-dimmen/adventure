"""Main game."""

import pygame
from constants import COLOR_BLACK
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from constants import TARGET_FPS
from exceptions import GameExit

from adventure.characters.player import Player
from adventure.projectiles.projectile import Projectile


class Game:
    """Main game."""

    def __init__(self) -> None:
        self.screen = None
        self.clock = None
        self.dt = 0
        self.update_objects = None
        self.drawn_objects = None
        self.projectile_objects = None
        self.player = None

    def setup(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.setup_screen()
        self.setup_groups()
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def setup_screen(self) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Adventure!")

    def setup_groups(self) -> None:
        self.update_objects = pygame.sprite.Group()
        self.drawn_objects = pygame.sprite.Group()
        self.projectile_objects = pygame.sprite.Group()
        Player.containers = (self.update_objects, self.drawn_objects)
        Projectile.containers = (self.update_objects, self.drawn_objects, self.projectile_objects)

    def tick(self) -> None:
        self.dt = self.clock.tick(TARGET_FPS) / 1000

    def update(self) -> None:
        for x in self.update_objects:
            x.update(self.dt)
        for x in self.projectile_objects:
            x.check_range()

    def draw_screen(self) -> None:
        self.screen.fill(COLOR_BLACK)
        for x in self.drawn_objects:
            x.draw(self.screen)
        pygame.display.flip()

    def run(self) -> None:
        """Run the game and exit when we need to."""
        while True:
            self.update()
            self.draw_screen()
            self.tick()
            self.check_for_exit()

    def start(self) -> None:
        self.setup()
        try:
            self.run()
        except GameExit:
            print("Game shutting down")
        self.clean_up()

    def clean_up(self) -> None:
        self.player.kill()
        pygame.quit()

    def check_for_exit(self) -> None:
        """Check if we need to quit the game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise GameExit()


def main() -> None:
    """Run the game."""
    Game().start()


if __name__ == "__main__":
    main()
