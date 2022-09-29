from typing import List
from trueskill import rate, Rating

from src.match import Match
from src.player import Player


class RatingCalculator:
    
    def calculate_new_player_ratings(self, match: Match) -> List[Player]:
        ranks = self.__scores_to_ranks(match.team_a_score, match.team_b_score)
        ratings_a = [player.rating for player in match.team_a]
        ratings_b = [player.rating for player in match.team_b]
        new_ratings_a, new_ratings_b = rate([ratings_a, ratings_b], ranks=ranks)
        
        updated_players_a = self.__update_players(match.team_a, new_ratings_a)
        updated_players_b = self.__update_players(match.team_b, new_ratings_b)
        return updated_players_a + updated_players_b
    
    def __scores_to_ranks(self, team_a_score: int, team_b_score: int) -> List[int]:
        if team_a_score == 1 and team_b_score == 0:
            return [0, 1]
        elif team_a_score == 0 and team_b_score == 1:
            return [1, 0]
        elif team_a_score == 0 and team_b_score == 0:
            return [0, 0]
        
        raise ValueError(f"Match contains illegal values for team scores. team_a_score: {team_a_score}, team_b_score: {team_b_score}")
    
    def __update_players(self, players: List[Player], new_ratings: List[Rating]) -> List[Player]:
        updated_players = []
        for i, player in enumerate(players):
            updated_player = Player(player.uuid, new_ratings[i])
            updated_players.append(updated_player)
        return updated_players