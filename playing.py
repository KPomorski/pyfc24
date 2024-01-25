import json
import time
from pprint import pprint
import requests
import os
from players import Player, PlayerStats
import random
from prettytable import PrettyTable


def get_players():
    players_list = []
    # Check if the given lim/off file exists
    if not os.path.exists("players/all_players.json"):
        return print(f"The file for all players does not exist.")
    f = open("players/all_players.json")
    d = json.load(f)
    for p in d:
        players_list.append(PlayerStats(p))
    return players_list


def get_random_player(players):
    ran = players[random.randint(0, len(players))]
    print(f"Player {ran.playerRank} is {ran}, of {ran.team} in {ran.leagueName}")
    ran.print_stats()


def compare_team_rosters(data: list[PlayerStats], team1: str, team1gender: int, team2: str, team2gender: int):
    # default to Men's if no gender given (sorry)
    if team1gender is None:
        team1gender = 0
    if team2gender is None:
        team2gender = 0
    roster1 = [player for player in players if player.team == team1 and player.gender == team1gender]
    roster2 = [player for player in players if player.team == team2 and player.gender == team2gender]

    for p1 in roster1:
        print(f"{p1}")
    for p2 in roster2:
        print(f"{p2}")


if __name__ == '__main__':
    players = get_players()

    get_random_player(players)

    leagues = set()
    for x in players:
        leagues.add(x.team)
    for l in leagues:

    # teams = []
    # for x in players:
        # leagues.add(x.team)
    # for l in leagues:

