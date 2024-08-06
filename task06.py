def greedy_algorithm(items, budget):
    # Sort items by descending calories-to-cost ratio
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[name]["cost"] for name in item_names]
    calories = [items[name]["calories"] for name in item_names]

    # DP table to store max calories for each budget from 0 to budget
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Recover the selected items
    selected_items = []
    w = budget
    total_calories = dp[n][budget]

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]

    return selected_items[::-1], total_calories, budget - w


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = 100

    # Using the greedy algorithm
    greedy_result = greedy_algorithm(items, budget)
    print(f"Greedy Algorithm:\n"
          f"Selected items: {', '.join(greedy_result[0])}\n"
          f"Total calories: {greedy_result[1]}\n"
          f"Total cost: {greedy_result[2]}\n")

    # Using dynamic programming
    dp_result = dynamic_programming(items, budget)
    print(f"Dynamic Programming:\n"
          f"Selected items: {', '.join(dp_result[0])}\n"
          f"Total calories: {dp_result[1]}\n"
          f"Total cost: {dp_result[2]}\n")