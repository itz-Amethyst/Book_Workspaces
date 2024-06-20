infinity = float("inf")

graph = {}
graph["Start"] = {"A": 5, "B": 2}
graph["A"] = {"C": 4}
graph["B"] = {"A": 8, "D": 7}
graph["C"] = {"Finish": 3}
graph["D"] = {"C": 6, "Finish": 1}
graph["E"] = {} 

costs = {
    "A": 5,
    "B": 2,
    "C": infinity,
    "D": infinity,
    "E": infinity,
    "Finish": infinity,
}

parents = {
    "A": "Start",
    "B": "Start",
    "C": None,
    "D": None,
    "E": None,
    "Finish": None,
}

processed = []

def find_the_lowest_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
            
    return lowest_cost_node

def main():
    node = find_the_lowest_node(costs)
    while node is not None:
        cost = costs[node]
        
        if node in graph:
            neighbors = graph[node]
            for n, cost_to_n in neighbors.items():
                new_cost = cost + cost_to_n
                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = node
        
        processed.append(node)
        node = find_the_lowest_node(costs)
    
    print("Costs:", costs)
    print("Parents:", parents)

if __name__ == "__main__":
    main()
