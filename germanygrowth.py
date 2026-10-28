import numpy as np
import matplotlib.pyplot as plt

# Population estimates, in people
population_2023 = 83_287_273
P0 = 83_516_593  # Germany's estimated population in 2024

# Estimate the continuous annual growth rate from 2023 to 2024.
# The logarithm makes this rate match the continuous model dP/dt = alpha * P.
alpha = np.log(P0 / population_2023)

# Return the population's rate of change at a given time.
# Here, t is included to match the model function pattern; alpha is constant.
def growth_func(t, P):
    return alpha * P

# Create 501 time points from 2024 to 2074.
# This gives 500 small intervals, each 0.1 year long.
years = np.linspace(2024, 2074, 501)
dt = years[1] - years[0]

# Make an array to store the simulated population at each time point.
population = np.zeros(len(years))
population[0] = P0  # Start the simulation with the 2024 population

# Use Euler's method to step the model forward through time.
# Each step adds the current growth rate multiplied by the time interval.
for i in range(1, len(years)):
    population[i] = population[i - 1] + growth_func(
        years[i - 1], population[i - 1]
    ) * dt

# Save the final simulated population for 2074.
P_2074 = population[-1]

# Plot the simulated population, converting people to millions for readability.
plt.figure(figsize=(9, 5))
plt.plot(years, population / 1_000_000, label="Simulated population")

# Mark and label the 2074 estimate on the plot.
plt.scatter(
    [2074],
    [P_2074 / 1_000_000],
    color="red",
    zorder=3,
    label=f"2074: {P_2074 / 1_000_000:.1f} million"
)

# Add labels and formatting to the graph.
plt.title("Germany population model (2024–2074)")
plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Print the estimated growth rate and the 2074 population.
print(f"Estimated alpha: {alpha:.6f} per year ({alpha * 100:.3f}%)")
print(f"Simulated population in 2074: {P_2074:,.0f}")
