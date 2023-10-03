# Biased Coin Game
An analysis on the two-player known environment version of the biased coin game.

## The Game
The game requires two players and two biased coins with known biases. The first player picks one of the coins to flip, then flips it. The second player goes next, they can pick the same coin or the other one.

The goal of one of the players is to obtain two tails or two heads, whereas the other player wants to get one head and one tail.

## Analysis

Depending on the biases of each coin (0-100% chance of rolling heads), these are the probabilities that player 1 wins with various strategies.

![Figure 1](https://github.com/mgomezdev1/biased-coin-game/blob/main/figures/Figure_1.png)

Interestingly, if we take the difference in outcome between each strategy, we obtain this graph:

![Figure 2](https://github.com/mgomezdev1/biased-coin-game/blob/main/figures/Figure_2.png)

Which is the same for either goal!
