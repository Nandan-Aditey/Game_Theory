# Let us try to find all Very Weakly Dominant strategies in a strategic form game.

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

print("\n--------------------------------------\n")

for player in range(n_players):

    all_strategies = []
    player_ = player + 1
    max_payoff = 0
    strategy_set = Strategies[player] # Get all possible stratigies of player

    # Now we need to look at all strategy combinations without that player

    sub_Strategies = Strategies[:player] + Strategies[player+1:]
    
    # Now we need to look at all combinations

    comb_sub = strat_product(sub_Strategies)

    # To see if a strategy is Very Weakly Dominant:

    for strategy in strategy_set:

        possible = True

        for strategy_comp in strategy_set:
            if strategy == strategy_comp:
                continue
            
            for comb in comb_sub:

                profile_1 = list(comb)
                profile_1.insert(player, strategy)

                profile_2 = list(comb)
                profile_2.insert(player, strategy_comp)

                utility_1_str = Utilities[tuple(profile_1)]
                utility_2_str = Utilities[tuple(profile_2)]

                utility_1 = int(utility_1_str.split()[player])
                utility_2 = int(utility_2_str.split()[player])

                if utility_1 < utility_2:
                    possible = False
                    break
        if possible:
            all_strategies.append(strategy)

    Strategy_equilibria.append(all_strategies)

    print(f"Very Weakly Dominant strategies for player-{player_}: {Strategy_equilibria[player]}")



def equilibria_product(Strategies):
    if not Strategies:
        return [()]
    rest_product = equilibria_product(Strategies[1:])
    result = []
    for strat in Strategies[0]:
        for prod in rest_product:
            result.append((strat,) + prod)
    return result


if [] not in Strategy_equilibria:
    print("\n\nVery Weakly Dominant Strategy Equilibriums:")
    all_equilibria = equilibria_product(Strategy_equilibria)
    for i, strategies in enumerate(all_equilibria, 1):
        print(f"Equilibrium-{i}: {strategies}")
