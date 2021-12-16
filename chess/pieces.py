from __future__ import annotations

import typing
from abc import ABC
from dataclasses import dataclass

if typing.TYPE_CHECKING:
    from chess.state import Square


@dataclass
class Piece(ABC):
    """Represents a chess piece."""

    name: str
    color: str
    has_moved: bool
    loc: tuple[int, int]

    def move(self) -> None: ...
    def notation(self) -> str: ...
    def is_valid_move(self, sq: Square) -> bool: ...
