from typing import Literal, Tuple
import numpy as np

def optimal_utilities(prob_h1: float, prob_h2: float, different_wins = True) -> Tuple[float,float]:
    prob_t1 = 1 - prob_h1
    prob_t2 = 1 - prob_h2

    utilities = []
    for first in 'H','T':
        minimizer = []
        heads_utility = 0 if different_wins == (first == 'H') else 1
        tails_utility = 1 - heads_utility
        minimizer.append(heads_utility * prob_h1 + tails_utility * prob_t1)
        minimizer.append(heads_utility * prob_h2 + tails_utility * prob_t2)
        
        utilities.append(min(minimizer))
    return tuple(utilities)

def optimal_strategy(prob_h1: float, prob_h2: float, different_wins = True) -> float:
    prob_t1 = 1 - prob_h1
    prob_t2 = 1 - prob_h2
    maximizer = []
    heads_utility, tails_utility = optimal_utilities(prob_h1, prob_h2, different_wins)
    maximizer.append(heads_utility * prob_h1 + tails_utility * prob_t1)
    maximizer.append(heads_utility * prob_h2 + tails_utility * prob_t2)

    return max(maximizer)
    
def random_strategy(prob_h1: float, prob_h2: float, different_wins = True) -> float:
    prob_t1 = 1 - prob_h1
    prob_t2 = 1 - prob_h2
    prob_h = (prob_h1 + prob_h2)/2
    prob_t = (prob_t1 + prob_t2)/2
    same = prob_h * prob_h + prob_t * prob_t
    return (1 - same) if different_wins else same

def worst_strategy(prob_h1: float, prob_h2: float, different_wins = True) -> float:
    prob_t1 = 1 - prob_h1
    prob_t2 = 1 - prob_h2
    maximizer = []
    heads_utility, tails_utility = optimal_utilities(prob_h1, prob_h2, different_wins)
    maximizer.append(heads_utility * prob_h1 + tails_utility * prob_t1)
    maximizer.append(heads_utility * prob_h2 + tails_utility * prob_t2)

    return min(maximizer)

strategies = {
    "optimal": optimal_strategy,
    "random": random_strategy,
    "worst": worst_strategy
}

def get_data(strategy_name: Literal["optimal", "random", "worst"], different_wins = True):
    data = {}
    strategy = strategies[strategy_name]
    heatmap = np.zeros((101, 101))
    for prob_h1 in range(101):
        for prob_h2 in range(101):
            heatmap[prob_h1,prob_h2] = strategy(prob_h1/100, prob_h2/100, different_wins)
    return heatmap