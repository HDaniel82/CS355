def cardShuffles(numOfCards, numOfShuffles, shuffleType):
    results = {}
    #get values needed
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
    
    #inititalize deck
    deck = []
    for i in range(1, numOfCards+1):
        deck.append(i)
    originalDeck = []
    for i in range(numOfCards):
        originalDeck.append(deck[i])

    #start with r values
    rVals = [1.0]
    for i in range(numOfShuffles):
        firstHalf=[]
        for j in range(numOfCards//2):
            firstHalf.append(deck[j])
        secondHalf=[]
        for j in range(numOfCards//2, numOfCards):
            secondHalf.append(deck[j])
        newDeck=[]
        #different shuffles
        if shuffleType == 1:
            for j in range(numOfCards//2):
                newDeck.append(firstHalf[j])
                newDeck.append(secondHalf[j])
        else:
            for j in range(numOfCards//2):
                newDeck.append(secondHalf[j])
                newDeck.append(firstHalf[j])

        deck =[]
        for card in newDeck:
            deck.append(card)
        r= rCalculator(deck)
        rVals.append(r)

        isSameFlag = True
        for j in range(numOfCards):
            if deck[j] != originalDeck[j]:
                isSameFlag = False
                break
        if isSameFlag:
            print(f"Run {shuffleType} (n+{numOfCards}): deck backl to riginal after {i+1} shuffles")
            break
    results['rVals'] = rVals
    results['finalDeck'] = deck

    isSameFlag = True
    for j in range(numOfCards):
        if deck[j] != originalDeck[j]:
            isSameFlag = False
            break
    results['backToSame'] = isSameFlag

    if  results['backToSame']:
        for i in range(1, len(rVals)):
            tempDeck=[]
            for j in range(1, numOfCards+1):
                tempDeck.append(j)
            for k in range(i):
                tempFirstHalf=[]
                for j in range(numOfCards//2):
                    tempFirstHalf.append(tempDeck[j])
                tempSecondHalf=[]
                for j in range(numOfCards//2, numOfCards):
                    tempSecondHalf.append(tempDeck[j])
                tempNewDeck=[]
                if shuffleType==1:
                    for j in range(numOfCards//2):
                        tempNewDeck.append(tempFirstHalf[j])
                        tempNewDeck.append(tempSecondHalf[j])
                else:
                    for j in range(numOfCards//2):
                        tempNewDeck.append(tempSecondHalf[j])
                        tempNewDeck.append(tempFirstHalf[j])
                tempDeck=[]
                for card in tempNewDeck:
                    tempDeck.append(card)

                