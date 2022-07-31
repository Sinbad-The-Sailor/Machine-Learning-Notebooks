import numpy as np
from scipy import stats


def ecdf_normal(data, title, ax):
    observations = data
    n_observations = len(observations)
    observations = np.asarray(observations)
    observations.sort()
    observations = [(x-sum(observations)/n_observations) /
                    observations.std() for x in observations]
    probabilities = []

    for i in range(n_observations):
        probability = (i + 1) / n_observations
        probabilities.append(probability)

    normal_observations = np.linspace(observations[0], observations[-1])
    normal_cdf = stats.norm.cdf(normal_observations)

    plot = ax.step(observations, probabilities)
    plot = ax.plot(normal_observations, normal_cdf,
                   linestyle='dashdot', color='red')
    ax.set_title(title)

    return plot
