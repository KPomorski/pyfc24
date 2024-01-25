import json
import requests
import os
from players import Player, PlayerStats


# Function to write players into a file
def write_to_file(data, lim, off):
    fname = f"players/players_{off}_to_{off+lim}.json"
    if os.path.exists(fname):
        os.remove(fname)
    else:
        print("The file does not exist")
    f = open(fname, "a")
    f.write(json.dumps(data))
    f.close()



def fetch_players(lim=100, off=0, tot=17326, fetch=0):
    # When fetch = 1, fetch new data, otherwise, see if we have an existing file
    # for the given limit/offset.
    if not fetch:
        # Check if the given lim/off file exists
        fname = f"players/players_{off}_to_{off+lim}.json"
        if os.path.exists(fname):
            print("Reading from json file.")
            f = open(fname, "r")
            return json.load(f)
        else:
            print("The file does not exist")
            # Fetch players from the drop-api.ea.com api
            while lim < tot:
                x = requests.get(f'https://drop-api.ea.com/rating/fc-24?locale=en&offset={off}&limit={lim}').text
                write_to_file(json.loads(x), lim=limit, off=offset)
                return json.loads(x)


# Print out the players' attributes to the console. Just for debugging.
def print_attributes(player):
    print(f'{player["firstName"]} {player["lastName"]} has an overall rating of {player["overallRating"]}.')
    print(f'{player["firstName"]} {player["lastName"]}\'s stats are:')
    for stat in player["stats"]:
        print(f'{stat}: {player["stats"][str(stat)]["value"]}')


if __name__ == '__main__':
    limit = 100
    offset = 0
    total = 101
    while offset < total:
        y = fetch_players(lim=limit, off=offset, fetch=0)
        for item in y["items"]:
            player = PlayerStats(item)
            # print(f'{player.firstName} {player.lastName}, {player.overallRating}')
        print(f"Loading players {offset} to {offset + limit}")
        offset += 100
