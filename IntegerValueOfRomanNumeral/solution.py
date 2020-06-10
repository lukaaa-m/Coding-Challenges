from test_cases import *

val = {'I': 1,
       'V': 5,
       'X': 10,
       'L': 50,
       'C': 100,
       'D': 500,
       'M': 1000}

trip_repeatable = [1,10,100]

def splitIntoParts(s):
    #Replaces letters with numbers
    s = list(s)
    s = [val[letter] for letter in s]
    print(s)

    parts = []

    #Remove digits as they are added to a part
    #Make temporary copy of list?

    for i, num in enumerate(s):
        part = []
        #if next digit is same
        if s[i+1] == num:
            #if it is possible for number to be repeated thrice
            if num in trip_repeatable:
                #if the next two numbers are same
                if s[i+2] == num:
                    #add to part
                    part.append(s[i:i+2])
            #if there are two consecutive, add to part
            part.append(s[i:i+1])
        print(part)

        parts.append(part)

    return parts

def evaluateParts(parts):
    #If smaller value is before larger in part, subtract
    #If larger value is before smaller in part, add
    for part in parts:
        pass

    pass

def integerValueOfRomanNumeral(s):
    output = evaluateParts(splitIntoParts(s))

    return output
    
    

'''Testing'''
for i, case in enumerate(tests):
    print(f'Input: {case}')
    print(f'My Output: {integerValueOfRomanNumeral(case)}')
    print(f'Solution: {answers[i]}\n')

#Ideas:
#Use logic to split the numeral into pairs / triples, evaluate the pairs / triples and add

#Rules:
#I, X and C can be repeated up to three times
#Lower value digits to the right are added to larger digit
#Lower value digits to the left are subtracted