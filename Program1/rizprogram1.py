def cardShuffles(numOfCards):
    results = {}

    sumi = 0
    for i in range(1, numOfCards+1):
        sumi += 1
    sumsq = 0
    for i in range(1, numOfCards+1):
        sumsq += i*i
    sqsum = sumi*sumi

    def rCalculator(deck):
        sumIyi = 0
        for i in range(numOfCards):
            sumIyi += (i+1)*deck[i]
        r= (numOfCards*sumIyi - sqsum)/(numOfCards*sumsq - sqsum)
        return r