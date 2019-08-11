from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict

from src.domain.value_objects.GraphPoint import GraphPoint


@dataclass
class Graph:
    points: List[GraphPoint]

    def serialize(self) -> List[Dict]:
        return [g.serialize() for g in self.points]
