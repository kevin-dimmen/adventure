"""Main entry point for the game. Runs the main menu to start everything."""

from typing import Optional

import pygame
from loguru import logger

from adventure.constants import COLOR_DARK_SLATE_GRAY
from adventure.constants import COLOR_LIGHT_SLATE_GRAY
from adventure.engine import Engine
from adventure.exceptions import GameExit
from adventure.exceptions import PlayerDied
from adventure.fonts.fonts import get_main_font
from adventure.main_adventure import MainAdventure
from adventure.menus.button import Button


class Game(Engine):
    """Main game menu."""

    BACKGROUND_COLOR = COLOR_DARK_SLATE_GRAY
    TARGET_FPS = 15

    def __init__(self, screen: Optional[pygame.surface.Surface] = None) -> None:
        super().__init__(screen)
        self.main_menu_text = None
        self.main_menu_rectangle = None
        self.play_button = None
        self.quit_button = None
        self.clickable_objects = None

    def engine_setup(self) -> None:
        width, _ = pygame.display.get_window_size()
        center_width = width // 2
        self.main_menu_text = get_main_font(100).render("Adventure!", True, COLOR_LIGHT_SLATE_GRAY)
        self.main_menu_rectangle = self.main_menu_text.get_rect(center=(640, 100))
        self.play_button = Button(
            x=center_width,
            y=200,
            text="PLAY",
            color="Black",
            hover_color="White",
            font=get_main_font(50),
        )
        self.quit_button = Button(
            x=center_width,
            y=300,
            text="QUIT",
            color="Black",
            hover_color="White",
            font=get_main_font(50),
        )
        self.setup_groups()

    def setup_groups(self) -> None:
        self.clickable_objects = pygame.sprite.Group()
        Button.containers = (self.clickable_objects,)

    def engine_draw(self) -> None: ...

    def engine_logic(self) -> None:
        """Display the main menu and allow the user to select what to do."""
        self.screen.blit(self.main_menu_text, self.main_menu_rectangle)

        # for button in self.clickable_objects:
        for button in [self.play_button, self.quit_button]:
            button.change_color_on_hover()
            button.update(self.screen)

        if self.play_button.is_clicked():
            self.adventure()
        if self.quit_button.is_clicked():
            pygame.quit()
            raise GameExit()

    def adventure(self) -> None:
        try:
            MainAdventure().start()
        except PlayerDied:
            logger.info("Returning to main menu")

    def start(self) -> None:
        self.setup()
        try:
            self.run()
        except GameExit:
            logger.info("Game shutting down")
        self.clean_up()

    def clean_up(self) -> None:
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
