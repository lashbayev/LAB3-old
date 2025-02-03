def solve():
    heads = 35
    legs = 94

    
    for x in range(heads + 1):  
        y = heads - x  
        if 2 * x + 4 * y == legs:  
            return x, y  

    return "No solution found"

chickens, rabbits = solve_puzzle()
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
