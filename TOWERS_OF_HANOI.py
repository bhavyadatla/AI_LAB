def print_rods(rods):
    height = max(len(rods['A']), len(rods['B']), len(rods['C']))
    
    for level in range(height - 1, -1, -1):
        for rod in 'ABC':
            if len(rods[rod]) > level:
                print(f"  {rods[rod][level]}  ", end=" ")
            else:
                print("  |  ", end=" ")
        print()
    print("------ ------ ------")
    print("  A      B      C  ")
    print("\n")


def TowerOfHanoi(n, from_rod, to_rod, aux_rod, rods, step_count):
    if n == 0:
        return step_count

    step_count = TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod, rods, step_count)

    disk = rods[from_rod].pop()
    rods[to_rod].append(disk)

    step_count += 1

    print(f"Step {step_count}: Move disk {disk} from rod {from_rod} to rod {to_rod}")
    print_rods(rods)

    return TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod, rods, step_count)


def main():
    try:
        N = int(input("Enter the number of disks: "))
        if N <= 0:
            print("Please enter a positive integer for the number of disks.")
            return
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    rods = {
        'A': list(range(N, 0, -1)),
        'B': [],
        'C': []
    }

    print("Initial state:")
    print_rods(rods)

    step_count = 0

    step_count = TowerOfHanoi(N, 'A', 'C', 'B', rods, step_count)

    print("Goal State Reached!")


if __name__ == "__main__":
    main()