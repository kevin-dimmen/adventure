"""Exceptions to be encountered."""


class AdventureError(Exception):
    """Base Exception class."""


class GameExit(AdventureError):
    """Raised to exit the game."""


class PlayerDied(AdventureError):
    """Raised when the player dies."""
