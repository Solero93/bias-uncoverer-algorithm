from dataclasses import dataclass
from typing import Dict


@dataclass
class GraphPoint:
    x: int
    y: int

    def serialize(self) -> Dict[str, int]:
        return {
            'x': self.x,
            'y': self.y
        }
