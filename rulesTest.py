import pandas as pd
import os

#expecting input as lower case string, with tokens separated by single spaces and variables specified by [x]
def tokenListFromString(input):
    currentTokenList = input.split(" ")
    newTokenList = []
    for curToken in currentTokenList:
        if "[" in curToken:

def prompt_for_csv():
    while True:
        # Prompt the user for the CSV file name 
        testInput = input("Put smth in").lower

if __name__ == "__main__":
    prompt_for_csv()


Threshhold ex:

#New Rule format
#T 0 - 14 R s < 3 AND s > MEAN - STDDEV  AND s < MEAN + STDDEV OR s < s-1 OR S > s+1 OR S = 3
#T indicates expecting time in exact format to follow, R indicates rules following, s-1 indicates sample before s, s+1 indicates sample after s, s+n equas sample n samples after s, STDDEV is average stddev on time bound set, mean is mean, should also process mean, and mode(as =)]
#Would likes = s in 20% of __ means 0.8__ < s < 1.2__ , s in 1 of __ means __ - 1 < s < __  + 1, ability to save rules(necesitates ability to load rules) some SAVELAST [name]
#need : parentheses for logic, e.g (_ and _) OR __ means true if and is fufilled or if other,  while i0 and (i1 OR i2) means true if i0 true and either i1 or 2 is true
 