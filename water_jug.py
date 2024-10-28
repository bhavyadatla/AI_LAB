from collections import defaultdict

visited = defaultdict(lambda: False)

J1, J2, L = 0, 0, 0

rules = []

def initialize_rules():
    global rules
    rules = [
        ("Fill Jug 1", lambda X, Y: (J1, Y)),
        ("Empty Jug 1", lambda X, Y: (0, Y) if X > 0 else (X, Y)),
        ("Fill Jug 2", lambda X, Y: (X, J2) if Y < J2 else (X, Y)),
        ("Empty Jug 2", lambda X, Y: (X, 0) if Y > 0 else (X, Y)),
        ("Empty Jug 2 into Jug 1", lambda X, Y: (X + Y, 0) if X + Y <= J1 and Y > 0 else (X, Y)),
        ("Empty Jug 1 into Jug 2", lambda X, Y: (0, X + Y) if X + Y <= J2 and X > 0 else (X, Y)),
        ("Pour water from Jug 2 into Jug 1 until Jug 1 is full", lambda X, Y: (J1, Y - (J1 - X)) if X + Y >= J1 and Y > 0 else (X, Y)),
        ("Pour water from Jug 1 into Jug 2 until Jug 2 is full", lambda X, Y: (X - (J2 - Y), J2) if X + Y >= J2 and X > 0 else (X, Y))
    ]

solution_path = []

def Water_Jug_problem(X, Y):
    global J1, J2, L
    if X == L or Y == L:
        solution_path.append((X, Y, "Target achieved", (X, Y)))
        return True
    if not visited[(X, Y)]:
        visited[(X, Y)] = True
        for rule_name, rule in rules:
            new_X, new_Y = rule(X, Y)
            if not visited[(new_X, new_Y)]:
                solution_path.append((X, Y, rule_name, (new_X, new_Y)))
                if Water_Jug_problem(new_X, new_Y):
                    return True
                solution_path.pop()
    return False

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

# User inputs for Jug capacities and the target volume
J1 = get_integer_input("Enter the capacity of Jug 1: ")
J2 = get_integer_input("Enter the capacity of Jug 2: ")
L = get_integer_input("Enter the target volume: ")

initialize_rules()

if Water_Jug_problem(0, 0):
    print("\nStarting the Water Jug Problem...\n")
    step_count = 1
    print("Steps to reach the solution:")
    print(f"Step {step_count}: Start: (0, 0)")
    for step in solution_path:
        step_count += 1
        X, Y, action, result = step
        print(f"Step {step_count}: {action}: {result}")
    print(f"Solution found: One of the jugs contains {L} liters.")
else:
    print("No solution found.")
