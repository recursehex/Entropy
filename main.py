import numpy as np
import matplotlib.pyplot as plt
import math

def normal_pdf(x, mu, sigma):
    """Return the value of the normal distribution PDF 
    with mean mu and standard deviation sigma at x."""
    return (1.0 / (sigma * math.sqrt(2.0 * math.pi))) * \
           math.exp(-0.5 * ((x - mu) / sigma)**2)

class Dist:
    def __init__(self, start, end, num_points, mu, sigma):
        self.start = start              # start of range
        self.end = end                  # end of range
        self.num_points = num_points    # how many points you want in [a, b]
        self.mu = mu                    # mean of the normal distribution
        self.sigma = sigma              # standard deviation
        self.x_values = np.linspace(start, end, num_points)
        self.y_values = [normal_pdf(x, mu, sigma) for x in self.x_values]
        self.xy_pairs = list(zip(self.x_values, self.y_values))

dists = []
# Dist(start, end, num_points, mu, sigma)
dists.append(Dist(-5.0, -3.0, 100, -4.0, 0.25))
dists.append(Dist(-4.0, -2.0, 100, -3.0, 0.15))
dists.append(Dist(-3.0, -1.0, 100, -2.0, 0.05))

for dist in dists:
    plt.plot(dist.x_values, dist.y_values, label=f"N({dist.mu}, {dist.sigma}^2)")
    plt.title("Normal Distribution")
    plt.xlabel("x")
    plt.ylabel("PDF")
    plt.legend()
    plt.grid(True)
    plt.show()