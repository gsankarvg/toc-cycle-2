import math
import sys

class TSPSolver:
    def __init__(self, cost_matrix):
        self.cost_matrix = cost_matrix
        self.num_cities = len(cost_matrix)
        self.final_res = sys.maxsize  # Infinity value for comparison
        self.final_path = [-1] * (self.num_cities + 1)  # Store the final solution path
        self.visited = [False] * self.num_cities

    # Function to copy temporary solution to the final result
    def copy_to_final(self, curr_path):
        self.final_path[:self.num_cities + 1] = curr_path[:]
        self.final_path[self.num_cities] = curr_path[0]

    # Function to find the minimum edge cost from a city
    def first_min(self, i):
        min_val = sys.maxsize
        for k in range(self.num_cities):
            if self.cost_matrix[i][k] != 0 and self.cost_matrix[i][k] < min_val:
                min_val = self.cost_matrix[i][k]
        return min_val

    # Function to find the second minimum edge cost from a city
    def second_min(self, i):
        first, second = sys.maxsize, sys.maxsize
        for j in range(self.num_cities):
            if i == j or self.cost_matrix[i][j] == 0:
                continue
            if self.cost_matrix[i][j] <= first:
                second = first
                first = self.cost_matrix[i][j]
            elif self.cost_matrix[i][j] < second:
                second = self.cost_matrix[i][j]
        return second

    # Function to calculate the lower bound on the path
    def calculate_bound(self, curr_path, level, curr_bound):
        if level == 1:
            return curr_bound

        # Calculate the reduced cost of the current level
        new_bound = curr_bound
        for i in range(level):
            if curr_path[i] != -1:
                new_bound += (self.first_min(curr_path[i]) + self.second_min(curr_path[i])) / 2
        return new_bound

    # Recursive function to solve the TSP problem using Branch and Bound
    def tsp_recursive(self, curr_bound, curr_weight, level, curr_path):
        # If we have reached the last node
        if level == self.num_cities:
            # Check if there is a path back to the starting city
            if self.cost_matrix[curr_path[level - 1]][curr_path[0]] != 0:
                curr_res = curr_weight + self.cost_matrix[curr_path[level - 1]][curr_path[0]]
                if curr_res < self.final_res:
                    self.copy_to_final(curr_path)
                    self.final_res = curr_res
            return

        # Try all cities as the next node
        for i in range(self.num_cities):
            if (self.cost_matrix[curr_path[level - 1]][i] != 0 and not self.visited[i]):
                temp_bound = curr_bound
                temp_weight = curr_weight + self.cost_matrix[curr_path[level - 1]][i]
                # Calculate the new lower bound
                new_bound = self.calculate_bound(curr_path, level, temp_bound)

                # If promising, proceed to the next level
                if new_bound < self.final_res:
                    curr_path[level] = i
                    self.visited[i] = True
                    self.tsp_recursive(new_bound, temp_weight, level + 1, curr_path)
                # Backtrack
                self.visited[i] = False

    # Function to initialize the solution
    def tsp(self):
        curr_bound = 0
        curr_path = [-1] * (self.num_cities + 1)
        curr_weight = 0

        # Start the path with the first city
        curr_path[0] = 0
        self.visited[0] = True

        # Calculate the initial lower bound
        for i in range(self.num_cities):
            curr_bound += (self.first_min(i) + self.second_min(i)) / 2

        # Start the recursive function to solve the TSP problem
        self.tsp_recursive(curr_bound, curr_weight, 1, curr_path)

        # Print the final result
        print(f"Minimum cost: {self.final_res}")
        print(f"Path taken: {self.final_path}")

# Example usage
# Cost matrix representing the distances between cities
cost_matrix = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

tsp_solver = TSPSolver(cost_matrix)
tsp_solver.tsp()
