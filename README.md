# Game Theory

This project provides interactive Python scripts to analyze **strategic form games** with multiple players and strategies. In this project, we find the following:

1. Strongly Dominant Strategy  
2. Weakly Dominant Strategies  
3. Very Weakly Dominant Strategies  
4. Dominant Strategy Equilibria  
5. Pure Strategy Nash Equilibria (PSNE)  
6. MaxMin and MinMax Strategies

## Features

- Input based setup of strategic form games.
- Support for any number of players and their strategies.
- Accepts complete payoff profiles for each strategy combination.
- Computes:
  - Strongly Dominant Strategies
  - Weakly Dominant Strategies
  - Very Weakly Dominant Strategies
  - Pure Strategy Nash Equilibria (PSNE)
  - MaxMin and MinMax strategies for each player
- Finds all possible dominant strategy equilibria.

## Definitions

- **Strongly Dominant Strategy**: A strategy that yields a strictly better payoff for a player, no matter what the others play.
- **Weakly Dominant Strategy**: A strategy that yields at least as much payoff as any other strategy, and strictly more in at least one case.
- **Very Weakly Dominant Strategy**: A strategy that is never worse than any other, but not necessarily strictly better in any situation.
- **Strongly Dominant Strategy Equilibrium**: A profile (combination) where each player plays their strongly dominant strategy.
- **Weakly Dominant Strategy Equilibrium**: A profile where each player chooses one of their weakly dominant strategies. There may be multiple such equilibria.
- **Very Weakly Dominant Strategy Equilibrium**: A profile where each player chooses one of their very weakly dominant strategies. There may be multiple such equilibria.
- **Pure Strategy Nash Equilibrium (PSNE)**: A strategy profile where no player can unilaterally deviate and improve their payoff.
- **MaxMin Strategy**: For a player, this is the strategy that maximizes their *minimum* possible payoff, assuming worst-case scenarios.
- **MinMax Strategy**: For a player, this is the strategy that minimizes the *maximum* utility the player could be forced to accept by the others. It is often used in zero-sum or adversarial games.


## Author
Aditey Nandan