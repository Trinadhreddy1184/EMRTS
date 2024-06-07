# 4-Gallon Bucket Problem

## Problem Description

Two kids need to fetch exactly 4 gallons of water from a stream using only an unmarked 3-gallon bucket and an unmarked 5-gallon bucket. They need to accomplish this task in no more than 15 steps. 

## Objective

The objective of this project is to develop a program that simulates solving the 4-gallon bucket problem. The program should use the capacities of the two buckets and find a sequence of operations (fill, empty, pour) that results in exactly 4 gallons of water in either bucket within a specified number of steps.

## Solution Approach

The solution employs a breadth-first search (BFS) algorithm to explore all possible states of the buckets and find the shortest path to measure exactly 4 gallons. The BFS ensures that we find the solution with the minimum number of steps.

### Steps:

1. **Initialization**:
   - Start with both buckets empty (`(0, 0)`).
   - Use a queue to store states, paths taken, and the number of steps.
   - Use a set to track visited states to avoid repetitions.

2. **State Generation**:
   - From each state, generate all possible next states by performing the allowed operations:
     - Fill the bucket to its capacity.
     - Empty the bucket.
     - Pour water from one bucket to the other without exceeding the capacity of the receiving bucket.

3. **BFS Algorithm**:
   - Dequeue the current state.
   - Check if the target amount (4 gallons) is reached in either bucket.
   - If the target is reached and within the step limit, return the path.
   - If the state hasn't been visited and the step limit hasn't been exceeded, mark the state as visited and enqueue all possible next states.

4. **Output**:
   - If a solution is found within the step limit, print the sequence of steps.
   - If no solution is found within the step limit, indicate that no solution exists within the given constraints.
