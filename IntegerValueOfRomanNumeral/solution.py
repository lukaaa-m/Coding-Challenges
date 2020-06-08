from test_cases import *

val = {'I': 1,
       'V': 5,
       'X': 10,
       'L': 50,
       'C': 100,
       'D': 500,
       'M': 1000}

trip_repeatable = ['I','X','C']

def splitIntoParts(s):
    s = list(s)
    for letter in s:
        letter = val[letter]
    print(s)

    for i, num in enumerate(s):

        

def integerValueOfRomanNumeral(s):
    splitIntoParts(s)
    

'''Testing'''
for i,case in tests:
    print(f'Input: {case}')
    print(f'My Output: {integerValueOfRomanNumeral(case)}')
    print(f'Solution: {answers[i]}\n')

#Ideas:
#Use logic to split the numeral into pairs / triples, evaluate the pairs / triples and add

#Rules:
#I, X and C can be repeated up to three times
#Lower value digits to the right are added to larger digit
#Lower value digits to the left are subtracted