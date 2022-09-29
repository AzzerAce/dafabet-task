from typing import Optional
from trueskill import Rating


class Player:
    
    def __init__(self, uuid: int, rating: Optional[Rating] = None) -> None:
        self.uuid = uuid
        if rating:
            self.rating = rating
        else:
            self.rating = Rating()
            
    @property
    def rating_number(self) -> float:
        return self.rating.mu - (3 * self.rating.sigma)
