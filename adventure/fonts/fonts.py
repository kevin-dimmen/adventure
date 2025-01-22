from typing import Optional

import pygame


def get_main_font(size: Optional[int] = 30) -> pygame.font.Font:
    return pygame.font.SysFont("Arial", size, bold=True)
