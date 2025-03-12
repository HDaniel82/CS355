import numpy as np 
import matploblib.pyplot as plt
#computation for first run of [1-26] then [27-52] [daniel huynh]
def shuffle(deck);
    #shuffle deck from 1-26 and 27-52 
    half1 =deck[:26]
    half2 = deck[26:]
    #iterating through the paired elements then we extract each card from each pair alternating from h1 and h2  
    shuffled = [card for pair in zip(half1, half2) for card in pair]
    return shuffled

#main computation for the given formula: [daniel huynh]
def compuation(deck); 
n = 52; 
compute_sum = sum((i+1) * deck[i] for i in range(n)) #sum of i * yi
numer = (n* compute_sum) - 13782
denom =  2507960 - 13782 
return numer / denom

def main()