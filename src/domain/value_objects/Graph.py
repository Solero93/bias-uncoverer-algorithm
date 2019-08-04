from __future__ import annotations

from dataclasses import dataclass
from typing import List

from src.domain.value_objects.GraphPoint import GraphPoint


@dataclass
class Graph:
    points: List[GraphPoint]
