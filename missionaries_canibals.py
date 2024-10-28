class State:
    def __init__(self, missionaries_left, cannibals_left, boat_position, parent=None):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_position = boat_position
        self.parent = parent

    def is_goal(self):
        return self.missionaries_left == 0 and self.cannibals_left == 0 and self.boat_position == 1

    def is_valid(self, total_missionaries, total_cannibals):
        if (self.missionaries_left < 0 or self.cannibals_left < 0 or
            self.missionaries_left > total_missionaries or self.cannibals_left > total_cannibals):
            return False

        if (self.missionaries_left > 0 and self.missionaries_left < self.cannibals_left) or \
           (total_missionaries - self.missionaries_left > 0 and total_missionaries - self.missionaries_left < total_cannibals - self.cannibals_left):
            return False

        return True

    def get_possible_moves(self, boat_capacity, total_missionaries, total_cannibals):
        moves = []
        for m in range(boat_capacity + 1):
            for c in range(boat_capacity + 1):
                if 1 <= m + c <= boat_capacity:
                    if self.boat_position == 0:  
                        new_state = State(self.missionaries_left - m, self.cannibals_left - c, 1, self)
                    else:  
                        new_state = State(self.missionaries_left + m, self.cannibals_left + c, 0, self)

                    if new_state.is_valid(total_missionaries, total_cannibals):
                        moves.append(new_state)

        return moves

    def __eq__(self, other):
        return (self.missionaries_left == other.missionaries_left and
                self.cannibals_left == other.cannibals_left and
                self.boat_position == other.boat_position)

    def __hash__(self):
        return hash((self.missionaries_left, self.cannibals_left, self.boat_position))

    def __repr__(self):
        return f"State({self.missionaries_left}M, {self.cannibals_left}C, Boat {'Left' if self.boat_position == 0 else 'Right'})"


def print_solution(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    path.reverse()

    step_number = 1
    for i in range(1, len(path)):
        m_moved = abs(path[i].missionaries_left - path[i-1].missionaries_left)
        c_moved = abs(path[i].cannibals_left - path[i-1].cannibals_left)
        move_direction = "Right" if path[i].boat_position == 1 else "Left"

        print(f"Step {step_number}: Moved {m_moved}M and {c_moved}C to the {move_direction} side.")
        left_bank_boat = "1B" if path[i].boat_position == 0 else "0B"
        right_bank_boat = "1B" if path[i].boat_position == 1 else "0B"
        print(f"Left : ({path[i].missionaries_left}M, {path[i].cannibals_left}C, {left_bank_boat})  Right : ({total_missionaries - path[i].missionaries_left}M, {total_cannibals - path[i].cannibals_left}C, {right_bank_boat})")
        print()

        step_number += 1


def bfs_solve(start_state, total_missionaries, total_cannibals, boat_capacity):
    queue = [start_state]
    explored = set()

    while queue:
        current_state = queue.pop(0)
        if current_state.is_goal():
            print("Solution found!")
            print_solution(current_state)
            return True

        explored.add(current_state)

        for next_state in current_state.get_possible_moves(boat_capacity, total_missionaries, total_cannibals):
            if next_state not in explored:
                queue.append(next_state)

    print("No solution found!")
    return False


def is_valid_positive_integer(value):
    try:
        val = int(value)
        if val > 0:
            return val
        else:
            print("Input must be a positive number.")
            return None
    except ValueError:
        print("Input must be a number.")
        return None


def main():
    global total_missionaries, total_cannibals

    while True:
        missionaries_input = input("Enter the number of missionaries: ")
        total_missionaries = is_valid_positive_integer(missionaries_input)
        if total_missionaries is not None:
            break

    while True:
        cannibals_input = input("Enter the number of cannibals: ")
        total_cannibals = is_valid_positive_integer(cannibals_input)
        if total_cannibals is not None:
            if total_cannibals >= total_missionaries:
                break
            else:
                print("Enter a proper input such that the number of cannibals is greater than or equal to the number of missionaries.")
   
    while True:
        boat_capacity_input = input("Enter the boat capacity : ")
        boat_capacity = is_valid_positive_integer(boat_capacity_input)
        if boat_capacity is not None and boat_capacity <= total_missionaries:
            break
        else:
            print(f"Boat capacity must be a valid number less than or equal to the number of missionaries ({total_missionaries}).")

    start = State(total_missionaries, total_cannibals, 0)
    solution_found = bfs_solve(start, total_missionaries, total_cannibals, boat_capacity)
   
    if solution_found:
        print("All missionaries and cannibals crossed the river successfully! Goal state is reached.")
    else:
        print("All missionaries and cannibals do not reach the goal state.")


if __name__ == "__main__":
    main()

