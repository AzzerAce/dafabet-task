from datetime import datetime
from src.player import Player
from src.match import Match
import pytest
from src.rating_calculator import RatingCalculator

@pytest.mark.parametrize("uuid, team_a, team_b, score_a, score_b, ts",
                         [(1, [Player(1), Player(2), Player(3)], [Player(4), Player(5), Player(6)], 1, 0, datetime.now()),
                          (1, [Player(1), Player(2), Player(3)], [Player(4), Player(5), Player(6)], 0, 1, datetime.now())])
def test_calculate_new_player_ratings_should_increase_when_win(uuid, team_a, team_b, score_a, score_b, ts):
    match = Match(uuid, team_a, team_b, score_a, score_b, ts)
    rc = RatingCalculator()
    
    updated_players = rc.calculate_new_player_ratings(match)
    
    team = []
    players_to_compare = []
    if score_a == 1:
        team = team_a
        players_to_compare = updated_players[:len(team_a)]
    elif score_b == 1:
        team = team_b
        players_to_compare = updated_players[len(team_a):len(team_a)+len(team_b)]
        
    for i, player in enumerate(team):
        assert players_to_compare[i].rating_number > player.rating_number


@pytest.mark.parametrize("uuid, team_a, team_b, score_a, score_b, ts",
                         [(1, [Player(1), Player(2), Player(3)], [Player(4), Player(5), Player(6)], 1, 0, datetime.now()),
                          (1, [Player(1), Player(2), Player(3)], [Player(4), Player(5), Player(6)], 0, 1, datetime.now())])
def test_calculate_new_player_ratings_should_decrease_when_loss(uuid, team_a, team_b, score_a, score_b, ts):
    match = Match(uuid, team_a, team_b, score_a, score_b, ts)
    rc = RatingCalculator()
    
    updated_players = rc.calculate_new_player_ratings(match)
    
    team = []
    players_to_compare = []
    if score_b == 1:
        team = team_a
        players_to_compare = updated_players[:len(team_a)]
    elif score_a == 1:
        team = team_b
        players_to_compare = updated_players[len(team_a):len(team_a)+len(team_b)]
        
    for i, player in enumerate(team):
        assert players_to_compare[i].rating_number < player.rating_number


def test_calculate_new_player_ratings_should_raise_error_when_invalid_team_score():
    match = Match(1, [Player(1), Player(2), Player(3)], [Player(4), Player(5), Player(6)], 2, 0, datetime.now())
    rc = RatingCalculator()
    
    with pytest.raises(ValueError):
        rc.calculate_new_player_ratings(match)
