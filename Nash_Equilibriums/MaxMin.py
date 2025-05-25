# Let us try to find all strongly dominant strategies in a strategic form game.

# We need to first input the number for players

n_players = int(input("Enter the number of players: "))

# For each player, we need to know their possible strategies. We create a list for that.

Strategies = [] # List at index i represents the possible strategies for player i+1
Strategy_equilibria = []

for player in range(n_players):

    # Obtain a list of strategies for each player

    player_ = player + 1
    strat_line = input(f"Please give the strategies of player-{player_} seperated by space: ")

    strategy = strat_line.split()
    Strategies.append(strategy)

# Now that we have the strategies, lets get the utility for each of them.

def strat_product(Strategies):
    
    if Strategies == []:
        return [()]

    rest_product = strat_product(Strategies[1:])
    result = []
    for strat in Strategies[0]:
        for prod in rest_product:
            result.append((strat,) + prod)
    
    return result

all_strat_comb = strat_product(Strategies)

Utilities = {}

for strat_comb in all_strat_comb:
    strat_comb_join = ', '.join(strat_comb)
    utility = input(f"Please enter the payoff for each player, seperated by space (in order) when strategies are {strat_comb_join}: ")
    Utilities[strat_comb] = utility


for player in range(n_players):

    player_ = player + 1
    player_strategies = Strategies[player]


    sub_Strategies = Strategies[:player] + Strategies[player+1:]
    comb_sub = strat_product(sub_Strategies)

    maxMin_strats = []
    min_utilities = []
    min_utilities_combs = []

    for strat in player_strategies:
        
        min_utility = float('inf')

        min_utility_comb = []

        for comb in comb_sub:

            profile = list(comb)
            profile.insert(player, strat)
            utility = Utilities[tuple(profile)]
            utility = int(utility.split()[player])

            if utility < min_utility:
                min_utility = utility
                min_utility_comb = []
                min_utility_comb.append(tuple(profile))
            elif utility == min_utility:
                min_utility_comb.append(tuple(profile))
        
        min_utilities.append(min_utility)
        min_utilities_combs.append(min_utility_comb)
    
    maxMin_utility = max(min_utilities)

    for index, val in enumerate(min_utilities):
        if val == maxMin_utility:
            strat_maxMin = min_utilities_combs[index][0][player]
            maxMin_strats.extend(strat_maxMin)

    print(f"\nMaxMin utility for player-{player_}: {maxMin_utility}")
    print(f"MaxMin strategies for player-{player_}: ", ", ".join(maxMin_strats))
    print()