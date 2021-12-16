from __future__ import annotations

from dataclasses import dataclass

from chess.pieces import Piece
from chess.state import Square


@dataclass(eq=True)
class Move:
    """Represents a chess move."""

    piece: Piece
    start: Square
    end: Square

    @property
    def is_capture(self) -> bool:
        return self.end.occupied

    @property
    def is_valid(self) -> bool:
        return self.piece.is_valid_move(self.end)
