from prettytable import PrettyTable


class Player:
    def __init__(self, player: dict):
        self.player = player
        self.id = player["id"]
        self.firstName = player["firstName"]
        self.lastName = player["lastName"]
        self.commonName = player["commonName"]
        self.playerRank = player["rank"]
        self.overallRating = player["overallRating"]
        self.birthdate = player["birthdate"]
        self.height = player["height"]
        self.skillMoves = player["skillMoves"]
        self.weakFootAbility = player["weakFootAbility"]
        self.attackingWorkRate = player["attackingWorkRate"]
        self.defensiveWorkRate = player["defensiveWorkRate"]
        self.preferredFoot = player["preferredFoot"]
        self.leagueName = player["leagueName"]
        self.weight = player["weight"]
        self.avatarUrl = player["avatarUrl"]
        self.shieldUrl = player["shieldUrl"]
        self.primaryPosition = player["position"]["shortLabel"]
        self.alternativePositions = player["alternatePositions"]
        self.playStyles = player["playStyle"]
        self.playStylePlus = player["playStylePlus"]
        self.gender = player["gender"]["id"]
        self.nationality = player["nationality"]["label"]
        self.nationalityUrl = player["nationality"]["imageUrl"]
        self.team = player["team"]["label"]

        self.positions = [self.primaryPosition]
        if self.alternativePositions:
            for altp in self.alternativePositions:
                self.positions.append(altp["shortLabel"])

    def __str__(self):
        if self.commonName:
            return f'{self.commonName}, {self.overallRating}, {self.primaryPosition}'
        else:
            return f'{self.firstName} {self.lastName}, {self.overallRating}, {self.primaryPosition}'


class PlayerStats(Player):
    def __init__(self, player: dict):
        super().__init__(player)
        self.acceleration = player["stats"]["acceleration"]["value"]
        self.aggression = player["stats"]["aggression"]["value"]
        self.agility = player["stats"]["agility"]["value"]
        self.balance = player["stats"]["balance"]["value"]
        self.ballControl = player["stats"]["ballControl"]["value"]
        self.composure = player["stats"]["composure"]["value"]
        self.crossing = player["stats"]["crossing"]["value"]
        self.curve = player["stats"]["curve"]["value"]
        self.defense = player["stats"]["def"]["value"]
        self.defensiveAwareness = player["stats"]["defensiveAwareness"]["value"]
        self.dri = player["stats"]["dri"]["value"]
        self.dribbling = player["stats"]["dribbling"]["value"]
        self.finishing = player["stats"]["finishing"]["value"]
        self.freeKickAccuracy = player["stats"]["freeKickAccuracy"]["value"]
        self.gkDiving = player["stats"]["gkDiving"]["value"]
        self.gkHandling = player["stats"]["gkHandling"]["value"]
        self.gkKicking = player["stats"]["gkKicking"]["value"]
        self.gkPositioning = player["stats"]["gkPositioning"]["value"]
        self.gkReflexes = player["stats"]["gkReflexes"]["value"]
        self.headingAccuracy = player["stats"]["headingAccuracy"]["value"]
        self.interceptions = player["stats"]["interceptions"]["value"]
        self.jumping = player["stats"]["jumping"]["value"]
        self.longPassing = player["stats"]["longPassing"]["value"]
        self.longShots = player["stats"]["longShots"]["value"]
        self.pac = player["stats"]["pac"]["value"]
        self.pas = player["stats"]["pas"]["value"]
        self.penalties = player["stats"]["penalties"]["value"]
        self.phy = player["stats"]["phy"]["value"]
        self.positioning = player["stats"]["positioning"]["value"]
        self.reactions = player["stats"]["reactions"]["value"]
        self.sho = player["stats"]["sho"]["value"]
        self.shortPassing = player["stats"]["shortPassing"]["value"]
        self.shotPower = player["stats"]["shotPower"]["value"]
        self.slidingTackle = player["stats"]["slidingTackle"]["value"]
        self.sprintSpeed = player["stats"]["sprintSpeed"]["value"]
        self.stamina = player["stats"]["stamina"]["value"]
        self.standingTackle = player["stats"]["standingTackle"]["value"]
        self.strength = player["stats"]["strength"]["value"]
        self.vision = player["stats"]["vision"]["value"]
        self.volleys = player["stats"]["volleys"]["value"]
        stats = {}
        for stat in player["stats"]:
            stats[stat] = player["stats"][stat]["value"]
        self.stats = stats

    # Print out the players' attributes to the console. Just for debugging.
    def print_stats(self):
        x = PrettyTable()
        x.field_names = ['dri', 'sho', 'phy', 'pac', 'pas', 'def']
        tops = []
        for k in x.field_names:
            tops.append(self.stats.get(k))
        x.add_row(tops)
        print(x)
        # for s, v in self.stats.items():
        #     print(f"{s}: {v}")

