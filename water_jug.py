def pour_water_dfs(j1, j2, target, x=0, y=0, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if (x, y) in visited:
        return False

    visited.add((x, y))


    if x == target or y == target:
        print("\nSolution Found:")
        for step, state in path:
            print(f"{step:<10} -> {state}")
        print(f"Final State -> ({x}, {y})")
        return True

    if pour_water_dfs(j1, j2, target, j1, y, visited, path+[("Fill J1", (j1, y))]):
        return True

    if pour_water_dfs(j1, j2, target, x, j2, visited, path+[("Fill J2", (x, j2))]):
        return True

    if pour_water_dfs(j1, j2, target, 0, y, visited, path+[("Empty J1", (0, y))]):
        return True

    if pour_water_dfs(j1, j2, target, x, 0, visited, path+[("Empty J2", (x, 0))]):
        return True

    pour_to_2 = min(x, j2 - y)
    if pour_water_dfs(j1, j2, target, x - pour_to_2, y + pour_to_2, visited, path+[("Pour 1→2", (x - pour_to_2, y + pour_to_2))]):
        return True

    pour_to_1 = min(y, j1 - x)
    if pour_water_dfs(j1, j2, target, x + pour_to_1, y - pour_to_1, visited, path+[("Pour 2→1", (x + pour_to_1, y - pour_to_1))]):
        return True

    return False

if __name__ == "__main__":
    print("--- Water Jug Problem Solver ---")
    try:
        j1 = int(input("Enter the capacity of Jug 1: "))
        j2 = int(input("Enter the capacity of Jug 2: "))
        target = int(input("Enter the target amount: "))
        
        if not pour_water_dfs(j1, j2, target):
            print("\nNo solution exists for these capacities and target.")
            
    except ValueError:
        print("Invalid input! Please enter whole numbers only.")