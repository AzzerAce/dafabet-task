from dataclasses import dataclass
from typing import List
from datetime import datetime

from src.player import Player


@dataclass
class Match:
    
    uuid: int
    team_a: List[Player]
    team_b: List[Player]
    team_a_score: int
    team_b_score: int
    ts: datetime
