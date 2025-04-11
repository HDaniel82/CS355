import random 

def generate_flight_times(u, sigma): 
    min_time = u - 3 * sigma 
    max_time = u + 3 * sigma 
    return max(min(random.guass(u, sigma), max_time), min_time)

def airline_one(trials=10000):
    stranded = 0 