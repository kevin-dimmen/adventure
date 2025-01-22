"""Base class for engine runners."""

from typing import Optional

import pygame
from constants import COLOR_BLACK
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from constants import TARGET_FPS
from exceptions import GameExit
from loguru import logger


class Engine:
    """Main game engine."""

    BACKGROUND_COLOR = COLOR_BLACK
    TARGET_FPS = TARGET_FPS

    def __init__(self, screen: Optional[pygame.surface.Surface] = None) -> None:
        self.screen = screen
        self.clock = None
        self.dt = 0
        self.events = []

    def setup(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.setup_screen()
        self.engine_setup()

    def setup_screen(self) -> None:
        if self.screen is None:
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Adventure!")

    def engine_setup(self) -> None:
        raise NotImplementedError()

    def run(self):
        """Display the main menu and allow the user to select what to do."""
        while True:
            self.check_for_exit()
            self.draw_background()
            self.engine_logic()
            self.draw_elements()
            self.tick()

    def tick(self) -> None:
        self.dt = self.clock.tick(self.TARGET_FPS) / 1000

    def draw_background(self) -> None:
        self.screen.fill(self.BACKGROUND_COLOR)

    def draw_elements(self) -> None:
        self.engine_draw()
        pygame.display.flip()

    def engine_draw(self) -> None:
        raise NotImplementedError()

    def engine_logic(self) -> None:
        raise NotImplementedError()

    def start(self) -> None:
        self.setup()
        self.run()
        self.clean_up()

    def clean_up(self) -> None:
        pygame.quit()

    def check_for_exit(self) -> None:
        """Check if we need to quit the game."""
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                raise GameExit()


def main() -> None:
    """Run the game."""
    Engine().start()


if __name__ == "__main__":
    main()
