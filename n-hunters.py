import math
import random
import multiprocessing

def shoot_and_survive(n):
    # Simulate one round of the hunting game for 'n' hunters in a 2D space.
    positions = [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(n)]
    # hunters starts all ones as "alive"
    hunters = [1] * n

    for i in range(n):
        closest_distance = float('inf') 
        for j in range(n):
            if i != j:
                # Calculate the Euclidean distance between hunters i and j in 2D space.
                distance = ((positions[i][0] - positions[j][0])**2 + (positions[i][1] - positions[j][1])**2)**0.5
                
                if distance < closest_distance:
                    closest_distance = distance
                    hunter = j
                    
        # Hunter i shoots hunter j.
        hunters[hunter] = 0
    
    return sum(hunters)/n

if __name__ == "__main__":
    num_hunters = 25 
    num_simulations = 600000

    pool = multiprocessing.Pool()
    results = pool.map(shoot_and_survive, [num_hunters] * num_simulations)
    pool.close()
    pool.join()

    # Calculate the average survival rate.
    survival_rate = sum(results) / num_simulations * 100

    print(f"Percentage of hunters that survive: {survival_rate:.10f}%")
    
    expected = 1/math.e
    for i in range(3, 100):
        expected -= 1/math.e**i
    print(f"Expected survival rate: {expected*100:.10f}%")
        
