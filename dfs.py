from collections import defaultdict

def dfs(tree, current_node, goal_node, visited, path):
    if current_node == goal_node:
        return path
    visited.add(current_node)
    for child in tree[current_node]:
        if child not in visited:
            new_path = dfs(tree, child, goal_node, visited, path + [child])
            if new_path:
                return new_path
    return None

# Tree printer function to print the tree in a structured format
def tree_printer(tree_list, num_levels):
    current_level = 0
    index = 0
    max_width = 2 ** num_levels  # Maximum width of the tree
    while current_level <= num_levels:
        nodes_at_level = 2 ** current_level
        space_between_nodes = max_width // nodes_at_level
        leading_spaces = space_between_nodes // 2
        line = " " * leading_spaces

        for i in range(nodes_at_level):
            if index < len(tree_list):
                line += tree_list[index]
                index += 1
                if i < nodes_at_level - 1:
                    line += " " * space_between_nodes

        print(line.center(max_width))
        current_level += 1

# Function to handle input validation for number of nodes
def get_num_nodes():
    while True:
        try:
            num_nodes = int(input("Enter the number of nodes: ").strip())
            if num_nodes > 0:
                return num_nodes
            else:
                print("Number of nodes must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Input tree nodes & the children
tree = defaultdict(list)
num_nodes = get_num_nodes()

print("Enter the node value and the child nodes, separated by spaces. If a node has no children, enter only the node value:")
for _ in range(num_nodes):
    node_info = input().strip().split()
    if node_info:
        node = node_info[0]
        children = node_info[1:]  # All elements after the first one are considered children
        tree[node].extend(children)  # Add children to the node
        for child in children:
            if child not in tree:
                tree[child] = []  # Initialize the child node with an empty list

nodes = list(tree.keys())
print("Available nodes: ", nodes)
start_node = nodes[0]
goal_node = input("Enter the node to search for: ").strip()

# Check for invalid node inputs
if start_node not in nodes or goal_node not in nodes:
    print("node entered NOT FOUND ")
else:
    # Perform DFS to find the path
    path = dfs(tree, start_node, goal_node, set(), [start_node])

    if path:
        print("Path from", start_node, "to", goal_node, ":", " -> ".join(path))
    else:
        print("No path found from", start_node, "to", goal_node)

    print("\nTree structure:")

    # Function to convert the tree into a list representation for easier printing
    def convert_tree_to_list(tree, root):
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            result.append(node)
            queue.extend(tree[node])
        return result

    # Function to determine the number of levels in the tree
    def get_tree_levels(tree, root):
        levels = 0
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            levels = max(levels, level)
            queue.extend([(child, level + 1) for child in tree[node]])
        return levels

    # Generate tree list and print it
    num_levels = get_tree_levels(tree, start_node)
    tree_list = convert_tree_to_list(tree, start_node)
    tree_printer(tree_list, num_levels)
