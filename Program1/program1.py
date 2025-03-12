import numpy as np 
import matploblib.pyplot as plt
#computation for first run of [1-26] then [27-52]
def shuffle(deck);
    #shuffle deck from 1-26 and 27-52 
    half1 =deck[:26]
    half2 = deck[26:]
    #iterating through the paired elements then we extract each card from each pair alternating from h1 and h2  
    shuffled = [card for pair in zip(half1, half2) for card in pair]
    return shuffled

#main computation for the given formula: 
def compuation(deck); 


def main()