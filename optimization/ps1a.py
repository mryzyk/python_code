###########################
# Problem Set 1a: Space Cows


from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.split(',')
            cows[line[0]] = int(line[1])
    file.close()
    return cows

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    sorted_cows = dict(sorted(cows.items(), key=lambda item: item[1], reverse=True))
    trips = []
    '''loop through dictionary of cows and create trips for as long as there still are any cows left'''
    while len(sorted_cows):
        trip = []
        weight_loaded = 0
        too_heavy = []
        for cow, weight in sorted_cows.items():
            if weight > limit:
                print(f"{cow} is to heavy for the ship and will not be taken on any trip")
                too_heavy.append(cow)
        for cow in too_heavy:
            sorted_cows.pop(cow)
        for cow, weight in sorted_cows.items():
            if limit - weight_loaded >= weight:
                trip.append(cow)
                # sorted_cows.pop(cow)
                weight_loaded += weight
        trips.append(trip)
        for cow in trip:
            sorted_cows.pop(cow)

    return trips




# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    too_heavy = []
    for cow, weight in sorted_cows.items():
        if weight > limit:
            print(f"{cow} is to heavy for the ship and will not be taken on any trip")
            too_heavy.append(cow)
    for cow in too_heavy:
        sorted_cows.pop(cow)
    possible_combinations = []
    for combination in get_partitions(cows):
        is_possible = True
        for trip in combination:
            trip_weight = 0
            for cow in trip:
                trip_weight += cows[cow]
            if trip_weight > limit:
                is_possible = False
            # print(trip)
            # print(trip_weight)
            # print(is_possible)
        if is_possible:
            possible_combinations.append(combination)

    best_combination = min(possible_combinations, key=len)

    return best_combination



        
# Problem 4
def compare_cow_transport_algorithms(cows, limit=22):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    start = time.time()
    greedy = greedy_cow_transport(cows,limit)
    end = time.time()
    print(greedy)
    print(f'greedy #trips: {len(greedy)}')
    print(f'greedy time taken: {end - start}')
    start = time.time()
    brute_force = brute_force_cow_transport(cows,limit)
    end = time.time()
    print(brute_force)
    print(f'brute force #trips: {len(brute_force)}')
    print(f'brute force time taken: {end - start}')


if __name__ == '__main__':


    cows = load_cows('ps1_cow_data.txt')
    sorted_cows = dict(sorted(cows.items(), key=lambda item: item[1], reverse=True))
    print(sorted_cows)
    print()
    print()
    compare_cow_transport_algorithms(cows, 27)
