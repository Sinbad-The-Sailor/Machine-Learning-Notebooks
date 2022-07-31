import numpy as np
from scipy import stats


def qq_plot_normal(data, title, ax):
    observations = data
    observations.sort()
    n_observations = len(observations)

    empirical_quantiles = observations
    theoretical_quantiles = [stats.norm.ppf(
        (i - 0.5)/n_observations) for i in range(1, n_observations + 1)]

    # qq-line (y = mx + b) based on the 25th and 75th quantile of each distribtuion.
    (x1, x2) = stats.norm.ppf((0.25, 0.75))
    (y1, y2) = np.quantile(observations, (0.25, 0.75))

    slope = (y2 - y1)/(x2 - x1)
    intercept = y2 - (slope * x2)
    qqrange = np.linspace(theoretical_quantiles[0], theoretical_quantiles[-1])
    qqline = [slope * x + intercept for x in qqrange]

    plot = ax.plot(qqrange, qqline, linestyle='dashdot', color='red')
    plot = ax.scatter(theoretical_quantiles, empirical_quantiles,
                      marker='+', zorder=2, color='blue')
    ax.set_title(title)

    return plot
