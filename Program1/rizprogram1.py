def cardShuffles(numOfCards):
    results = {}

    sumi = 0
    for i in range(1, numOfCards+1):
        sumi += 1
    sumsq = 0
    for i in range(1, numOfCards+1):
        sumsq += i*i