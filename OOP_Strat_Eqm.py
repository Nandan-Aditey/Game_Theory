# Class representing a player in the game
class Player:

    def __init__(self, id, strategies):
        self.id = id
        self.strategies = strategies


# Class representing the game
class Game:
    def __init__(self, Players):
        self.players = Players  # List of Player objects
        self.utilities = {} # Stores utilities for each strategy profile
        self.utility_players = {}   # Stores utilities from each player's perspective
        self.strategy_profiles = [player.strategies for player in Players]  # All players' strategy sets
        self.Strongly_DS_Equilibria = []    # Strongly dominant strategies
        self.Weakly_DS_Equilibria = []  # Weakly dominant strategies
        self.VeryWeakly_DS_Equilibria = []  # Very weakly dominant strategies
        self.PSNE_list = [] # Pure Strategy Nash Equilibria
        self.MinMax_Strategies = [] # MinMax strategies
        self.MaxMin_Strategies = [] # MaxMin strategies


    # Generate Cartesian product of all strategies
    def strategy_product(self, strategy_profiles):
        """
        Generate the Cartesian product of strategy sets for all players.

        Args: strategy_profiles (list): List of strategy lists for each player.
        Returns: list: List of tuples representing all possible strategy profiles.
        """
        
        Strategy_set = list(strategy_profiles)

        if Strategy_set == []:
            return [()]

        rest_product = self.strategy_product(Strategy_set[1:])
        result = []
        for strat in Strategy_set[0]:
            for prod in rest_product:
                result.append((strat,) + prod)
        
        return result
    

    # Take input of payoffs for all strategy profiles
    def utility_finder(self, all_strat_profiles):
        """
        Collect utility values from user input for all possible strategy profiles.

        Args: all_strat_profiles (list): List of all possible strategy profiles.
        """
        
        for profile in all_strat_profiles:
            strat_profile_join = ', '.join(profile)
            utility = input(f"Please enter the payoff for each player, seperated by space (in order) when strategies are {strat_profile_join}: ")
            self.utilities[profile] = list(map(int, utility.split()))


    # Build utility view for each individual player
    def Utility_player_creator(self, n_players, all_strat_profiles):
        """
        Construct utility mappings for each player from all strategy profiles.

        Args: n_players (int): Number of players in the game.
              all_strat_profiles (list): List of all possible strategy profiles.
        """

        for player in range(n_players):

            player_dict = {}

            for strat_set in all_strat_profiles:
                player_dict[strat_set] =  self.utilities[strat_set][player]

            self.utility_players[player] = player_dict


    # Find strongly dominant strategies for each player
    def Strongly_Dominant(self, n_players):
        """
        Determine strongly dominant strategies for each player.

        Args: n_players (int): Number of players.
        Returns: list: Strongly dominant strategy for each player or 'Does not exist'.
        """

        for player in range(n_players):

            strategy_set = self.strategy_profiles[player] # Get all possible stratigies of player

            # Now we need to look at all strategy combinations without that player
            sub_Strategies = self.strategy_profiles[:player] + self.strategy_profiles[player+1:]
            
            # Now we need to look at all combinations
            sub_strat_profile = self.strategy_product(sub_Strategies)

            # To see if a strategy is strongly dominant:
            for strategy in strategy_set:

                best = True

                for strategy_comp in strategy_set:
                    if strategy == strategy_comp:
                        continue
                    
                    for profile in sub_strat_profile:

                        profile_1 = list(profile)
                        profile_1.insert(player, strategy)

                        profile_2 = list(profile)
                        profile_2.insert(player, strategy_comp)

                        utility_1 = self.utility_players[player][tuple(profile_1)]
                        utility_2 = self.utility_players[player][tuple(profile_2)]

                        if utility_1 <= utility_2:
                            best = False
                            break
                if best:
                    self.Strongly_DS_Equilibria.append(strategy)
                    break

            if len(self.Strongly_DS_Equilibria) < (player+1):
                self.Strongly_DS_Equilibria.append("Does not exist")
        
        return self.Strongly_DS_Equilibria
    

    # Find weakly dominant strategies for each player
    def Weakly_Dominant(self, n_players):
        """
        Determine weakly dominant strategies for each player.

        Args: n_players (int): Number of players.

        Returns: list: List of weakly dominant strategies for each player.
        """

        for player in range(n_players):

            weakly_strats = []

            strategy_set = self.strategy_profiles[player] # Get all possible strategies of player

            # Now we need to look at all strategy combinations without that player
            sub_Strategies = self.strategy_profiles[:player] + self.strategy_profiles[player+1:]
            
            # Now we need to look at all combinations
            sub_strat_profile = self.strategy_product(sub_Strategies)

            # To see if a strategy is weakly dominant:
            for strategy in strategy_set:

                not_worse = True
                strictly_greater = False

                for strategy_comp in strategy_set:
                    if strategy == strategy_comp:
                        continue
                    
                    for profile in sub_strat_profile:

                        profile_1 = list(profile)
                        profile_1.insert(player, strategy)

                        profile_2 = list(profile)
                        profile_2.insert(player, strategy_comp)

                        utility_1 = self.utility_players[player][tuple(profile_1)]
                        utility_2 = self.utility_players[player][tuple(profile_2)]

                        if utility_1 < utility_2:
                            not_worse = False
                            break
                        if utility_1 > utility_2:
                            strictly_greater = True

                if not_worse and strictly_greater:
                    weakly_strats.append(strategy)

            self.Weakly_DS_Equilibria.append(weakly_strats)

        return self.Weakly_DS_Equilibria
    

    # Find very weakly dominant strategies for each player
    def VWeakly_Dominant(self, n_players):
        """
        Determine very weakly dominant strategies for each player.

        Args: n_players (int): Number of players.
        Returns: list: List of very weakly dominant strategies for each player.
        """

        for player in range(n_players):

            vweakly_strats = []

            strategy_set = self.strategy_profiles[player] # Get all possible stratigies of player

            # Now we need to look at all strategy combinations without that player
            sub_Strategies = self.strategy_profiles[:player] + self.strategy_profiles[player+1:]
            
            # Now we need to look at all combinations
            sub_strat_profile = self.strategy_product(sub_Strategies)

            # To see if a strategy is very weakly dominant:
            for strategy in strategy_set:

                not_worse = True

                for strategy_comp in strategy_set:
                    if strategy == strategy_comp:
                        continue
                    
                    for profile in sub_strat_profile:

                        profile_1 = list(profile)
                        profile_1.insert(player, strategy)

                        profile_2 = list(profile)
                        profile_2.insert(player, strategy_comp)

                        utility_1 = self.utility_players[player][tuple(profile_1)]
                        utility_2 = self.utility_players[player][tuple(profile_2)]

                        if utility_1 < utility_2:
                            not_worse = False
                            break
                if not_worse:
                    vweakly_strats.append(strategy)

            self.VeryWeakly_DS_Equilibria.append(vweakly_strats)
        
        return self.VeryWeakly_DS_Equilibria
    

    # Find Pure Strategy Nash Equilibria
    def PSNE(self, n_players, all_strat_profiles):
        """
        Compute all Pure Strategy Nash Equilibria (PSNE) for the game.

        Args: n_players (int): Number of players.
              all_strat_profiles (list): All possible strategy profiles.
        Returns: list: List of strategy profiles that are Nash equilibria.
        """

        for profile in all_strat_profiles:

            can_Deviate = True

            # To check if the profile is a Nash equilibrium, we need to check that for each player deviation leads to a worse outcome.
            Utilities_List = self.utilities[profile]

            for player in range(n_players):

                utility = Utilities_List[player]

                # We also need the strategy currently adopted by the player
                curr_strat = ''.join(profile[player:player+1])

                for strat_player in self.strategy_profiles[player]:
                    if strat_player == curr_strat:
                        continue
                    outcome_test = profile[:player] + (strat_player,) + profile[player+1:]
                    utility_strat_player = self.utilities[outcome_test][player]
                    if utility < utility_strat_player:
                        can_Deviate = False
                        break
                        
                if not can_Deviate:
                    break
            
            if can_Deviate:
                self.PSNE_list.append(profile)

        return(self.PSNE_list)
    

    # Compute MinMax strategies for each player
    def MinMax(self, n_players):
        """
        Compute MinMax strategies for each player (maximizing their minimum payoff).

        Args: n_players (int): Number of players.
        Returns: tuple: (max_min_utility, list of MinMax strategies per player)
        """

        for player in range(n_players):
            player_strategies = self.strategy_profiles[player]
            min_utilities = []
            min_utilities_strats = []

            for strat in player_strategies:
                utilities_for_strat = []

                # Form all profiles for opponents
                sub_Strategies = self.strategy_profiles[:player] + self.strategy_profiles[player+1:]
                sub_profile_set = self.strategy_product(sub_Strategies)

                for sub_profile in sub_profile_set:
                    profile = list(sub_profile)
                    profile.insert(player, strat)
                    utility = self.utility_players[player][tuple(profile)]
                    utilities_for_strat.append(utility)

                min_utility = min(utilities_for_strat)
                min_utilities.append(min_utility)
                min_utilities_strats.append(strat)

            max_min_utility = max(min_utilities)

            # collect all strategies with that max_min_utility
            best_strats = [strategy for index, strategy in enumerate(min_utilities_strats) if min_utilities[index] == max_min_utility]
            self.MinMax_Strategies.append(best_strats)

        return max_min_utility, self.MinMax_Strategies

    

    # Compute MaxMin strategies for each player
    def MaxMin(self, n_players):
        """
        Compute MaxMin strategies for each player (selecting strategies with the best worst-case utility).

        Args: n_players (int): Number of players.

        Returns: tuple: (max_min_utility, list of MaxMin strategies per player)
        """

        for player in range(n_players):

            player_strategies = self.strategy_profiles[player]
            maxMin_strats = []

            sub_Strategies = self.strategy_profiles[:player] + self.strategy_profiles[player+1:]
            sub_profile_set = self.strategy_product(sub_Strategies)

            min_utilities = []
            min_utilities_strats = []

            for strat in player_strategies:

                min_utility = float('inf')
                min_utility_profile = []

                for sub_profile in sub_profile_set:
                    profile = list(sub_profile)
                    profile.insert(player, strat)

                    utility = self.utility_players[player][tuple(profile)]

                    if utility < min_utility:
                        min_utility = utility
                        min_utility_profile = [strat]
                    elif utility == min_utility:
                        min_utility_profile.append(strat)

                min_utilities.append(min_utility)
                min_utilities_strats.append(min_utility_profile)

            maxMin_utility = max(min_utilities)
            for index, val in enumerate(min_utilities):
                if val == maxMin_utility:
                    strat_maxMin = min_utilities_strats[index]
                    maxMin_strats.extend(strat_maxMin)

            self.MaxMin_Strategies.append(maxMin_strats)

        return maxMin_utility, self.MaxMin_Strategies



# Execution

n_players = int(input("Enter the number of players: "))

Players_list = []

for player in range(n_players):

    # Obtain a list of strategies for each player
    player_num = player + 1
    strat_set_player = input(f"Please give the strategies of player-{player_num} seperated by space: ")

    # Convert the input into a list
    strategy_Player = strat_set_player.split()

    Players_list.append(Player(player_num, strategy_Player))


# Create Game instance and compute outcomes
game1 = Game(Players_list)
all_strat_profiles = game1.strategy_product(game1.strategy_profiles)
game1.utility_finder(all_strat_profiles)
game1.Utility_player_creator(n_players, all_strat_profiles)
strongly_dominant = game1.Strongly_Dominant(n_players)
weakly_dominant = game1.Weakly_Dominant(n_players)
vweakly_dominant = game1.VWeakly_Dominant(n_players)
PSNE_list = game1.PSNE(n_players, all_strat_profiles)
minMax_utility, minMax_strats = game1.MinMax(n_players)
maxMin_utility, maxMin_strats = game1.MaxMin(n_players)


print("--------------------------------------------------------------------------")
print()


for player, strategy in enumerate(strongly_dominant):

    player_num = player + 1

    print(f"Strongly Dominant strategy for {player_num}: {strategy}")

if "Does not exist" not in strongly_dominant:
    print("\nStrongly Dominant Strategy Equilibrium: ", strongly_dominant)


print()
print()


for player, strategy in enumerate(weakly_dominant):

    player_num = player + 1

    print(f"Weakly Dominant strategies for {player_num}: {strategy}")

if [] not in weakly_dominant:
    print("\nWeakly Dominant Strategy Equilibriums:")
    all_equilibria = game1.strategy_product(weakly_dominant)
    for index, strategies in enumerate(all_equilibria, 1):
        print(f"Equilibrium-{index}: {list(strategies)}")


print()
print()


for player, strategy in enumerate(vweakly_dominant):

    player_num = player + 1

    print(f"Very Weakly Dominant strategies for {player_num}: {strategy}")

if [] not in vweakly_dominant:
    print("\nWeakly Dominant Strategy Equilibriums:")
    all_equilibria = game1.strategy_product(vweakly_dominant)
    for index, strategies in enumerate(all_equilibria, 1):
        print(f"Equilibrium-{index}: {list(strategies)}")


print("\n\nAll Pure Strategy Nash Equilibriums: ")
for index, psne in enumerate(PSNE_list, 1):
    print(f"Equilibrium-{index}: {psne}")

print()
print()

for player in range(1, n_players+1):
    print(f"MinMax utility of player-{player} is {minMax_utility} with strategies: {list(set(minMax_strats[player-1]))}")

print()
print()

for player in range(1, n_players+1):
    print(f"MaxMin utility of player-{player} is {maxMin_utility} with strategies: {list(set(maxMin_strats[player-1]))}")