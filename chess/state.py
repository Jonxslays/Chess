from __future__ import annotations

from dataclasses import dataclass

from chess.pieces import Piece

@dataclass
class Square:
    """Represents a square on the chess board."""

    rank: int
    file: int
    piece: Piece | None = None

    @property
    def occupied(self) -> bool:
        """Whether or not there is a piece on this square."""
        return self.piece is not None

    def __str__(self) -> str:
        return ""


@dataclass
class State:
    """Represents a snapshot of the game state."""
