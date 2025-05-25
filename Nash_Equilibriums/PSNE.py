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


PSNE_list = []

for outcome in all_strat_comb:

    can_Deviate = True

    # To check if the outcome is a Nash equilibrium, we need to check that for each player deviation leads to a worse outcome.

    for player in range(n_players):

        Utilities_List = [int(_) for _ in Utilities[outcome].split()]

        utility = Utilities_List[player]

        # We also need the strategy currently adopted by the player
        curr_strat = ''.join(outcome[player:player+1])

        for strat_player in Strategies[player]:
            if strat_player == curr_strat:
                continue
            outcome_test = outcome[:player] + (strat_player,) + outcome[player+1:]
            utility_strat_player = [int(_) for _ in Utilities[outcome_test].split()][player]
            if utility < utility_strat_player:
                can_Deviate = False
                break
                
        if not can_Deviate:
            break
    
    if can_Deviate:
        PSNE_list.append(outcome)


for outcome in PSNE_list:
    print(outcome, "\n")