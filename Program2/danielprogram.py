from numpy import random 

def generate_flight_times(u, sigma): 
    min_time = u - 3 * sigma 
    max_time = u + 3 * sigma 
    return max(min(random.normal(u, sigma), max_time), min_time)

def airline_one(trials=10000):
    stranded = 0 
    on_time = 0 
    total_time = 0 
    success = 0 

    for i in range(trials): 
        time = 0 

        #a -> b 
        t1 = generate_flight_times(240, 24)
        time += t1 
        if time < 750 - 1: 
            dep2 = 750
        elif time < 780-1: 
            dep2 = 780 
        else: 
            stranded += 1 
            continue 
        time = dep2 

        #b -> c 
        t2 = generate_flight_times(240, 24)
        time += t2
        if time < 1020 - 1: 
            dep3 = 1020 
        elif time < 1050 - 1: 
            dep3 = 1050 
        else: 
            stranded += 1
            continue 
        time = dep3 

        #c -> d 
        t3 = generate_flight_times(210, 24)
        time += t3 
        total_time += time 
        success += 1 
        if time <= 780: 
            on_time += 1 
        
    return{ 
        "avg_time": total_time / success if success else None,
        "time_prob": on_time / success if success else 0,
        "stranded_prob": stranded / trials
    }

def airline_two(trials = 10000):
    stranded = 0 
    on_time = 0 
    total_time = 0 
    success = 0

    for i in range (trials):
        time = 0 

        t1 = generate_flight_times(210, 48)
        time += t1 
        if time < 720 - 1: 
            dep2 = 720 
        elif time < 750 - 1: 
            dep2 = 750 
        else: 
            stranded += 1 
            continue 
        time = dep2 

        #e -> f 
        t2 = generate_flight_times(240, 48)
        time += t2 
        if time < 990 - 1: 
            dep3 = 990 
        elif time < 1020 - 1: 
            dep3 = 1020 
        else: 
            stranded += 1 
            continue 
        time = dep3 

        #f -> d 
        t3 = generate_flight_times(210, 48)
        time += t3
        total_time += time 
        success += 1 
        if time <= 750: 
            on_time += 1 
        
    return{ 
        "avg_time": total_time / success if success else None,
        "time_prob": on_time / success if success else 0,
        "stranded_prob": stranded / trials
    }

def mins_to_hours(min):
    hours = min // 60 
    minutes = min % 60 
    return hours, minutes

def main(): 
    one = airline_one()
    two = airline_two()
    avg_hours, avg_minutes = mins_to_hours(one['avg_time'])
    avg_hours2, avg_minutes2 = mins_to_hours(two['avg_time'])


    print(f"Average Arrival Time: {avg_hours} hours and {avg_minutes:.2f} minutes")
    print(f"Probability of On-Time Arrival: {one['time_prob']:.4f}")
    print(f"Probability of being Stranded: {one['stranded_prob']:.4f}")

    print(f"\nAverage Arrival Time: {avg_hours2} hours and {avg_minutes2:.2f} minutes")
    print(f"Probability of On-Time Arrival: {two['time_prob']:.4f}")
    print(f"Probability of being Stranded: {two['stranded_prob']:.4f}")

main()