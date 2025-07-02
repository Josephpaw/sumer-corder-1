
import random

players = ["Joseph", "semaj", "rich",
            "tay", "max", "braylen",
            "Ollie", "xavier", "avery"
            "carl", "walter", "darren",
            "EJ", "nahum", "joaquin",
            "marshawn", "ja'den", "Isaiah",
            "kelon", "nishad", "kauri",
            "kriss","kamari", "Jeffrey"]

def PickTeams(players):
    random.shuffle(players)
    team1 = players[:len(players) // 2]
    teamCaptain1 = team1[random.randrange(0, 12)]

    print("TEAM 1:")
    print("Team captain: " + teamCaptain1)
    for player in team1:
        print(player)

team2 = players[len(players) // 2:]
teamcaptain2 = team2[random.randrange(0,12)]
print("TEAM 2")
print("Team 2 captain: " + teamcaptain2)
for player in team2:
    print(player)

PickTeams(players)