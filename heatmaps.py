from matplotlib import pyplot as plt
from matplotlib.axes import Axes
import numpy as np

from data_generator import get_data, strategies

data: dict[bool,list[np.ndarray]] = {}
fig, axes = plt.subplots(2,3)
fig.set_figwidth(15)
fig.set_figheight(7.5)

for different_wins in [True, False]:
    data[different_wins] = []
    for i,strategy in enumerate(strategies.keys()):
        heatmap = get_data(strategy, different_wins)

        index = (0 if different_wins else 1, i)
        ax: Axes = axes[index]
        img = ax.imshow(heatmap, vmin=0, vmax=1, origin="lower")
        ax.set_title(f"{strategy.capitalize()} strategy, wins if {'different' if different_wins else 'equal'}")
        plt.colorbar(img)

plt.suptitle("Probability that player 1 wins")
plt.show()
