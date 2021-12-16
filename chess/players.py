from __future__ import annotations

from dataclasses import dataclass, field

from chess.moves import Move

@dataclass
class Player:
    """Represents a chess player."""

    color: str
    score: int = 0
    captures: list[Move] = field(default_factory=list)
