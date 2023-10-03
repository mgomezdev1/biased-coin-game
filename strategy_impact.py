from matplotlib import pyplot as plt
from matplotlib.axes import Axes
import numpy as np

from data_generator import get_data

fig, axes = plt.subplots(2)

for different_wins in [True, False]:
    impact = get_data('optimal', different_wins) - get_data('worst', different_wins)
    ax: Axes = axes[0 if different_wins else 1]
    img = ax.imshow(impact, vmin = 0, vmax = 1, origin='lower')
    ax.set_title(f"Wins if {'different' if different_wins else 'equal'}")
    plt.colorbar(img)

plt.suptitle("Impact (difference in expected outcome) in each case")
plt.show()