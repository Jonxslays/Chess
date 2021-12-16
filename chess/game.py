from __future__ import annotations

import pygame  # type: ignore

from chess.moves import Move  # type: ignore
from chess.players import Player
from chess.state import State


class Game:
    """Represents the actual chess game."""

    def __init__(self) -> None:
        self.white = Player("W")
        self.black = Player("B")
        self.state = State()

    def start(self) -> None:
        pass
