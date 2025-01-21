"""Exceptions to be encountered."""


class AdventureError(Exception):
    """Base Exception class."""


class GameExit(AdventureError):
    """Raised to exit the game."""
