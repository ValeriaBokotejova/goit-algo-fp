# Project: Algorithms and Data Structures in Python

This repository contains solutions to several algorithmic and data structure tasks implemented in Python. Below is a brief description of each task:

## Task 1: Data Structures - Sorting and Singly Linked List
- **Reverse a singly linked list** by changing the links between nodes.
- Implement **sorting algorithms** for a singly linked list, such as insertion sort or merge sort.
- Develop a function to **merge two sorted singly linked lists** into one sorted list.

## Task 2: Recursion - Pythagoras Tree Fractal
- Implement a recursive algorithm to create the **Pythagoras Tree fractal**.
- The program visualizes the fractal, allowing the user to specify the recursion depth.

## Task 3: Trees - Dijkstra's Algorithm
- Develop Dijkstra's algorithm to find the shortest paths in a weighted graph using a binary heap.
- The task includes graph creation, heap usage for vertex selection, and calculation of the shortest paths from the source vertex to all other vertices.

## Task 4: Binary Tree Visualization
- Analyze the provided code that builds binary trees and visualizes them.
- Based on the code, implement a function to visualize a binary heap as a tree.

## Task 5: Binary Tree Traversal Visualization
- Extend the tree visualization code to show **tree traversals**: depth-first and breadth-first.
- The program should visually represent each traversal step, changing node colors based on their visitation order using a gradient from dark to light shades.

## Task 6: Greedy Algorithms and Dynamic Programming
- Implement two approaches to solve the problem of selecting foods with the highest total calories within a limited budget.
  - **Greedy Algorithm:** Selects items by maximizing the calorie-to-cost ratio.
  - **Dynamic Programming:** Finds the optimal set of items to maximize calories within the budget.

## Task 7: Monte Carlo Method - Dice Roll Simulation
- Simulate a large number of dice rolls and calculate the probability of each possible sum (from 2 to 12).
- Compare the simulated probabilities with analytical probabilities.

### Conclusions for Task 7

The simulation results were compared to the analytical probabilities of sums obtained when rolling two six-sided dice. The results are summarized in the table below:

| Sum | Simulated Probability (%) | Analytical Probability (%) |
|-----|----------------------------|----------------------------|
| 2   | 2.76                       | 2.78                       |
| 3   | 5.53                       | 5.56                       |
| 4   | 8.31                       | 8.33                       |
| 5   | 11.08                      | 11.11                      |
| 6   | 13.91                      | 13.89                      |
| 7   | 16.65                      | 16.67                      |
| 8   | 13.90                      | 13.89                      |
| 9   | 11.10                      | 11.11                      |
| 10  | 8.36                       | 8.33                       |
| 11  | 5.58                       | 5.56                       |
| 12  | 2.82                       | 2.78                       |

### Analysis

The Monte Carlo simulation produced results very close to the theoretical (analytical) probabilities. Small discrepancies are due to the randomness inherent in simulation, which decreases as the number of simulations increases.

The table above shows that the simulated probabilities align well with the analytical probabilities, validating the accuracy of the simulation approach.

---

This repository provides practical examples of various algorithms and data structures implemented in Python, including recursive algorithms, tree structures, graph algorithms, and more.
