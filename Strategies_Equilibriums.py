n_players = int(input("Enter the number of players: "))


Strategies = [] # List at index i represents the possible strategies for player i+1
Strongly_DS_Equilibria = []
Weakly_DS_Equilibria_set = []
Weakly_DS_Equilibria = []
VeryWeakly_DS_Equilibria = []
VeryWeakly_DS_Equilibria_set = []
PSNE_list = []
maxMin_strats = []
minMax_strats = []
maxMin_utility = []
minMax_utility = []

for player in range(n_players):

    # Obtain a list of strategies for each player
    player_num = player + 1
    strat_set_player = input(f"Please give the strategies of player-{player_num} seperated by space: ")

    strategy_Player = strat_set_player.split()
    Strategies.append(strategy_Player)     # Strategies is a list of lists, where each list contains the strategies of the players 


# Now that we have the strategies, lets get the utility for each of them.

# The function strat_product finds cartesian product S1xS2x...Sn from {S1, S2, ..., Sn}
# Each element is a tuple in the list returned by strat_product()

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

# all_strat_comb is a list of tuples, where each tuple is a possible set of strategies. This list covers all strategy profiles.

# We store utilities as a dictionary with keys as the strategy profiles (tuples) and values as lists containing the utility for each player.

Utilities = {}

for strat_comb in all_strat_comb:
    strat_comb_join = ', '.join(strat_comb)
    utility = input(f"Please enter the payoff for each player, seperated by space (in order) when strategies are {strat_comb_join}: ")
    Utilities[strat_comb] = list(map(int, utility.split()))


# We will precompute the utilities for a player in a strategy profile and store player wise to prevent computing later in the loop.

Utility_Comb = {} # Dictionary of dicitonaries, where each player has a dictionary of utilites corresponding to strategy set 

for player in range(n_players):

    player_dict = {}

    for strat_set in all_strat_comb:
        player_dict[strat_set] =  Utilities[strat_set][player]

    Utility_Comb[player] = player_dict

# To find Dominant Strategies for each player, we will look at the strategies of each player and compare with all other strategies

for player in range(n_players):

    player_weakly_dominant_set = []
    player_very_weakly_dominant_set = []

    # MaxMin strategies
    maxMin_strats_player = []
    min_utilities_player = []
    min_utilities_combs_player = []

    # MinMax strategies
    minMax_strats_player = []
    max_utilities_player = []
    max_utilities_combs_player = []
    
    player_num = player + 1
    strategy_set = Strategies[player] # Get all possible stratigies of player

    # Now we need to look at all strategy combinations without that player
    sub_Strategies = Strategies[:player] + Strategies[player+1:]
    
    # Now we need to look at all combinations
    sub_Strategies_Combinations = strat_product(sub_Strategies) # Essentially S1xS2x...S(i-1)xS(i+1)x...xSn

    # To see if a strategy is dominant:
    for strategy in strategy_set:

        # Initalise booleans, assuming the strategy is strongly dominant

        strongly_dominant = True
        very_weakly_dominant = True

        # For Weakly Dominant, we need very weakly + atleast one strictly greater than
        weakly_dominant = False

        # MaxMin
        min_utility = float('inf')
        min_utility_comb = []

        # MinMax
        max_utility = float('-inf')
        max_utility_comb = []

        for strategy_comp in strategy_set:
            if strategy == strategy_comp:
                # Don't do self comparisons
                continue
            
            # Compare the two strategies across all possible strategy profiles which rest of the players play

            for combination_set in sub_Strategies_Combinations:

                # Converting the profiles into lists to inset the strategy of the player

                profile_1 = list(combination_set)
                profile_1.insert(player, strategy)

                profile_2 = list(combination_set)
                profile_2.insert(player, strategy_comp)

                # Using precomputed dictionary to find the utilities of the players

                utility_1 = Utility_Comb[player][tuple(profile_1)]
                utility_2 = Utility_Comb[player][tuple(profile_2)]

                # Condition to check Strongly Dominant Strategy and Very Weakly Dominant Strategy
                if utility_1 == utility_2:
                    strongly_dominant = False
                elif utility_1 < utility_2:
                    strongly_dominant = False
                    very_weakly_dominant = False
                    break
                
                if utility_1 > utility_2:
                    weakly_dominant = True

                # For weakly dominant, we will check very_weakly_dominant and below check
            
        
        for combination_set in sub_Strategies_Combinations:

            profile = list(combination_set)
            profile.insert(player, strategy)
            utility = Utility_Comb[player][tuple(profile)]

            if utility < min_utility:
                min_utility = utility
                min_utility_comb = []
                min_utility_comb.append(tuple(profile))
            elif utility == min_utility:
                min_utility_comb.append(tuple(profile))

            if utility > max_utility:
                max_utility = utility
                max_utility_comb = []
                max_utility_comb.append(tuple(profile))
            elif utility == max_utility:
                max_utility_comb.append(tuple(profile))
        
        min_utilities_player.append(min_utility)
        min_utilities_combs_player.append(min_utility_comb)

        max_utilities_player.append(max_utility)
        max_utilities_combs_player.append(max_utility_comb)



        if strongly_dominant:
            Strongly_DS_Equilibria.append(strategy)
            player_weakly_dominant_set.append(strategy)
            player_very_weakly_dominant_set.append(strategy)
        elif very_weakly_dominant and weakly_dominant:
            player_weakly_dominant_set.append(strategy)
            player_very_weakly_dominant_set.append(strategy)
        elif very_weakly_dominant:
            player_very_weakly_dominant_set.append(strategy)


    if player_weakly_dominant_set == []:
        Weakly_DS_Equilibria.append("Does not exist")
    else:
        Weakly_DS_Equilibria.append(player_weakly_dominant_set)

    if player_very_weakly_dominant_set == []:
        VeryWeakly_DS_Equilibria.append("Does not exist")
    else:
        VeryWeakly_DS_Equilibria.append(player_very_weakly_dominant_set)

    
    maxMin_utility_player = max(min_utilities_player)
    minMax_utility_player = min(max_utilities_player)

    for index, val in enumerate(min_utilities_player):
        if val == maxMin_utility_player:
            strat_maxMin = min_utilities_combs_player[index][0][player]
            maxMin_strats_player.append(strat_maxMin)
    
    maxMin_strats.append(maxMin_strats_player)
    maxMin_utility.append(maxMin_utility_player)


    for index, val in enumerate(max_utilities_player):
        if val == minMax_utility_player:
            strat_minMax = max_utilities_combs_player[index][0][player]
            minMax_strats_player.append(strat_minMax)

    minMax_strats.append(minMax_strats_player)
    minMax_utility.append(minMax_utility_player)


    if len(Strongly_DS_Equilibria) < (player+1):
        Strongly_DS_Equilibria.append("Does not exist")

    print(f"Strongly Dominant strategies for player-{player_num}: {Strongly_DS_Equilibria[player]}")
    print(f"Weakly Dominant strategies for player-{player_num}: {Weakly_DS_Equilibria[player]}")
    print(f"Very Weakly Dominant strategies for player-{player_num}: {VeryWeakly_DS_Equilibria[player]}")


if "Does not exist" not in Strongly_DS_Equilibria:
    print("\nStrongly Dominant Strategy Equilibrium: ", Strongly_DS_Equilibria)


if "Does not exist" not in Weakly_DS_Equilibria:
    print("\nWeakly Dominant Strategy Equilibriums:")
    all_equilibria = strat_product(Weakly_DS_Equilibria)
    for index, strategies in enumerate(all_equilibria, 1):
        print(f"Equilibrium-{index}: {strategies}")

if "Does not exist" not in VeryWeakly_DS_Equilibria:
    print("\nVery Weakly Dominant Strategy Equilibriums:")
    all_equilibria = strat_product(VeryWeakly_DS_Equilibria)
    for index, strategies in enumerate(all_equilibria, 1):
        print(f"Equilibrium-{index}: {strategies}")


PSNE_list = list(all_equilibria)   # Since VeryWeakly_DS_Equilibria are also equilibriums

# Let us now find all Pure Strategy Nash Equilibriums:


for outcome in all_strat_comb:

    if outcome in PSNE_list:
        # To not look at strategy sets which are already PSNE
        continue

    can_Deviate = True

    # To check if the outcome is a Nash equilibrium, we need to check that for each player deviation leads to a worse outcome.

    for player in range(n_players):

        Utilities_List = Utilities[outcome]

        utility = Utilities_List[player]

        # We also need the strategy currently adopted by the player
        curr_strat = ''.join(outcome[player:player+1])

        for strat_player in Strategies[player]:
            if strat_player == curr_strat:
                continue
            outcome_test = outcome[:player] + (strat_player,) + outcome[player+1:]
            utility_strat_player = Utilities_List[player]
            if utility < utility_strat_player:
                can_Deviate = False
                break
                
        if not can_Deviate:
            break
    
    if can_Deviate:
        PSNE_list.append(outcome)


print("\n\nAll Pure Strategy Nash Equilibriums: ")

for index, psne in enumerate(PSNE_list, 1):
    print(f"Equilibrium-{index}: {psne}")




print("\n\nMaxMin Strategies:")
for i in range(n_players):
    print(f"Player-{i+1}: {maxMin_strats[i]} with MaxMin utility = {maxMin_utility[i]}")

print("\nMinMax Strategies:")
for i in range(n_players):
    print(f"Player-{i+1}: {minMax_strats[i]} with MinMax utility = {minMax_utility[i]}")