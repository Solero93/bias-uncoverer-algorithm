from dataclasses import dataclass
from typing import Dict


@dataclass
class GraphPoint:
    x: float
    y: float

    def serialize(self) -> Dict[str, float]:
        return {
            'x': self.x,
            'y': self.y
        }
