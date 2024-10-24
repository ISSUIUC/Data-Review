import pandas as pd
import os



precedenceDict = {
    ("MEAN", "STDDEV", "MEDIAN", "MODE"): 0,
    ("+", "-", "*", "/", "^"): 1,
    ("<", "<=", ">=", "=", ">"): 2,
    ("AND", "OR", "NOT"): 3
}
def add_spaces_around_parentheses(s):
    result = []  # To store the final result as a list of characters
    length = len(s)
    
    for i, char in enumerate(s):
        if char == '(':
            # If there's a next character and it's not a space, add space after '('
            result.append('(')
            if i + 1 < length and s[i + 1] != ' ':
                result.append(' ')
        elif char == ')':
            # If there's a previous character and it's not a space, add space before ')'
            if i > 0 and s[i - 1] != ' ':
                result.append(' ')
            result.append(')')
        else:
            # For other characters, just add them to the result
            result.append(char)
    
    # Join the list of characters into a final string
    return ''.join(result)
def tokenizer(function):
    funcImproved = add_spaces_around_parentheses(function)
    return funcImproved.split(" ")

def split_list_around_element(lst, element):
    if element not in lst:
        return None, None, None  # If element is not in the list
    
    index = lst.index(element)  # Find the index of the element
    left = lst[:index]          # All elements to the left
    middle = lst[index]         # The element itself
    right = lst[index + 1:]     # All elements to the right
    
    return left, middle, right

def functionStripper(functionTokens):
    counter = 0
    currentHighestPrecedence = -1
    currentHighestPosition = -1
    while  counter <len(functionTokens):
        currentToken = functionTokens[counter] 
        if currentToken in precedenceDict:
            if precedenceDict[currentToken] > currentHighestPrecedence:
                currentHighestPrecedence = precedenceDict[currentToken]
                currentHighestPositon = counter
                currentHighestOp = currentToken

        counter += 1
    split_list_around_element(functionTokens,   )
    #needs to uodatre split for unary operations
    

# Now we create a dictionary that maps the operations to functions
operation_functions = {
    "+": lambda a,b: a+b,
    "-": lambda a,b:a -b,
    "*": lambda a,b: a * b,
    "/": lambda a,b: a / b,
    "^": lambda a,b: a ** b,
    "<": lambda a,b: a < b,
    "<=": lambda a,b: a <= b,
    ">": lambda a,b: a > b,
    ">=": lambda a,b: a >= b,
    "=": lambda a,b: a==b,
    "AND": lambda a,b: a and b,
    "OR": lambda a,b: a or b,
    "NOT": lambda a: not a
}
#expecting input as lower case string, with tokens separated by single spaces and variables specified by [x]
class tokenTree:
    def __init__(self, function):
        self.children = []
        highestPrec, highestPrecValue, func1, func2 = functionStripper(function)
        self.operation = highestPrec
        if highestPrecValue != 0:
            if func1 != "nonextant":
                self.children.append(func1)
            if func2 != "nonextant":
                self.children.append(func2)
        
            
    #expecting data to be list of all needed datapoints, 
    def eval(self, data):
        if len(self.children) == 0:
            return self.operation
        if len(self.children) == 1:
            return operation_functions[self.operation](self.children[0].eval(data))
        if len(self.children) == 2:
            return operation_functions[self.operation](self.children[0].eval(data),self.children[1].eval(data))
        else:
            raise ValueError(f"Unknown operation: {self.operation}")
        

    

    #children are elements of highest predence 


    #need evaluateor given values of paramters
    #needs wayto get paramtersfrom tree
    #build valuesneeded  from listof overall vals
    

#need to have large list of data, evaluate a given tree, needs to be given a index for sample, and the data features(MEAN, MEDIAN, MODE, STDDEV, etc. ) over desired range
#could also create method to simply slice out needed data (from earliest possible reference to latest), and have    
def stripList(list, index):
    counter = 0
    returnList = []
    for element in list:
        if counter != index:
            returnList.append(element)
            counter += 1
    return returnList

#returns a list of the highest predence tokens from a given list, where numbers are treated as precdence 0, also returns list of remaining tokens



def findHighestPrecedence(tokenList):
    precedenceList = [[],[],[],[],[]]
    for token in tokenList:
        if token[0:1].equals("s"):
            precedenceList[1].append(token)
        else:
            for key in precedenceDict.key:
                if token in key:
                    precedenceList[precedenceDict[key] + 1].append(token)
            else:
                precedenceList[0].append(token)
    counter = 4
    while counter >= 0:
        if len(tokenList[counter]) != 0:
            return [tokenList[counter], stripList(tokenList, counter)]




def prompt_for_csv():
    while True:
        # Prompt the user for the CSV file name sd
        testInput = input("Put smth in").lower

if __name__ == "__main__":
    prompt_for_csv()


#Threshhold ex:

#New Rule format
#T 0 - 14 R s < 3 AND s > MEAN - STDDEV  AND s < MEAN + STDDEV OR s < s-1 OR S > s+1 OR S = 3
#T indicates expecting time in exact format to follow, R indicates rules following, s-1 indicates sample before s, s+1 indicates sample after s, s+n equas sample n samples after s, STDDEV is average stddev on time bound set, mean is mean, should also process mean, and mode(as =)]
#Would likes = s in 20% of __ means 0.8__ < s < 1.2__ , s in 1 of __ means __ - 1 < s < __  + 1, ability to save rules(necesitates ability to load rules) some SAVELAST [name]
#need : parentheses for logic, e.g (_ and _) OR __ means true if and is fufilled or if other,  while i0 and (i1 OR i2) means true if i0 true and either i1 or 2 is true
 


#goal is to create tree
#precdence order lowest first(bottom of tree not including parenthess) variables replaced and numbers, then variables(variables here being MEAN, STDDEV, s, s+n (n is integer) , MODE, MEDIAN), then arithmetic operators, then comparisons(incl equal) , then AND/OR/NOT 
#comparisons will evaluate to 1 being true, 0 being false
