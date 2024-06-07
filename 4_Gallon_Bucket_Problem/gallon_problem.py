# Code by : Trinadhreddy Seelam
from collections import deque

def fill(bucket, capacity):
    return capacity

def empty(bucket):
    return 0

def pour(bucket_from, bucket_to, bucket_to_capacity):
    transfer_amount = min(bucket_from, bucket_to_capacity - bucket_to)
    return bucket_from - transfer_amount, bucket_to + transfer_amount

def get_next_states(bucket1, bucket2, bucket1_capacity, bucket2_capacity):
    return [
        (fill(bucket1, bucket1_capacity), bucket2),  # Fill bucket1
        (bucket1, fill(bucket2, bucket2_capacity)),  # Fill bucket2
        (empty(bucket1), bucket2),                   # Empty bucket1
        (bucket1, empty(bucket2)),                   # Empty bucket2
        pour(bucket1, bucket2, bucket2_capacity),    # Pour bucket1 into bucket2
        pour(bucket2, bucket1, bucket1_capacity)[::-1]  # Pour bucket2 into bucket1
    ]

def gallon_problem(bucket1_capacity, bucket2_capacity, target, max_steps):
    visited = set()
    queue = deque([((0, 0), [], 0)])

    while queue:
        (bucket1, bucket2), path, steps = queue.popleft()

        if (bucket1 == target or bucket2 == target) and steps <= max_steps:
            return path + [(bucket1, bucket2)]

        if (bucket1, bucket2) in visited or steps >= max_steps:
            continue

        visited.add((bucket1, bucket2))

        next_states = get_next_states(bucket1, bucket2, bucket1_capacity, bucket2_capacity)

        for state in next_states:
            if state not in visited:
                queue.append((state, path + [(bucket1, bucket2)], steps + 1))

    return None

bucket1_capacity = 3
bucket2_capacity = 5
target = 4
max_steps = 15

solution = gallon_problem(bucket1_capacity, bucket2_capacity, target, max_steps)

if solution:
    for step_num, cap in enumerate(solution, start=1):
        print(f"Step {step_num}: {cap}")
else:
    print("No solution found within the step limit.")
