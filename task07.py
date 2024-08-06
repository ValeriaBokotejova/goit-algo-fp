import random
import matplotlib.pyplot as plt
from tabulate import tabulate

def simulate_dice_rolls(n):
    # Simulate n rolls of two dice and count occurrences of each sum
    results = {i: 0 for i in range(2, 13)}

    for _ in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        result = dice1 + dice2
        results[result] += 1

    return results

def calculate_probabilities(results, n):
    # Calculate probabilities of each sum based on simulation results
    probabilities = {k: (v / n) * 100 for k, v in results.items()}
    return probabilities

def plot_probabilities(probabilities):
    # Plot a bar chart of probabilities for each sum
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color='blue')
    plt.xlabel('Sum')
    plt.ylabel('Probability (%)')
    plt.title('Probability of Sums from Two Dice Rolls (Monte Carlo)')
    plt.xticks(sums)
    plt.show()

if __name__ == "__main__":
    n_rolls = 1000000  # Number of simulations
    results = simulate_dice_rolls(n_rolls)
    probabilities = calculate_probabilities(results, n_rolls)

    analytical_probabilities = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78,
    }

    # Create a table to compare the results
    table = []
    for sum_ in range(2, 13):
        sim_prob = probabilities.get(sum_, 0)
        ana_prob = analytical_probabilities.get(sum_, 0)
        table.append([sum_, f"{sim_prob:.2f}%", f"{ana_prob:.2f}%"])

    # Print the table
    headers = ["Sum", "Simulated Probability", "Analytical Probability"]
    print(tabulate(table, headers, tablefmt="pretty"))

    # Plot the simulated probabilities
    plot_probabilities(probabilities)