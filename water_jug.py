def pour_water_dfs(j1, j2, target, x=0, y=0, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
        
    if (x, y) in visited:
        return False
        
    visited.add((x, y))
    print("Visiting:", (x, y)) 
    
    if x == target or y == target:
        print("\nSolution Found:")
        for step, state in path:
            print(step, state)
        return True
        
    if pour_water_dfs(j1, j2, target, j1, y, visited, path+[("Fill J1", (j1,y))]):
        return True
        
    if pour_water_dfs(j1, j2, target, x, j2, visited, path+[("Fill J2", (x,j2))]):
        return True
        
    if pour_water_dfs(j1, j2, target, 0, y, visited, path+[("Empty J1", (0,y))]):
        return True
        
    if pour_water_dfs(j1, j2, target, x, 0, visited, path+[("Empty J2", (x,0))]):
        return True
        
    pour = min(x, j2 - y)
    if pour_water_dfs(j1, j2, target, x - pour, y + pour, visited, path+[("Pour 1->2", (x-pour, y+pour))]):
        return True
        
    pour = min(y, j1 - x)
    if pour_water_dfs(j1, j2, target, x + pour, y - pour, visited, path+[("Pour 2->1", (x+pour, y-pour))]):
        return True
        
    return False

if __name__ == "__main__":
    j1 = 5
    j2 = 3
    target = 2
    
    print(f"Starting search for Jug1={j1}, Jug2={j2}, Target={target}...\n")
    
    if not pour_water_dfs(j1, j2, target):
        print("No solution")