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
    rem_digits = [x for x in s] #copy of solution array

    #Remove digits as they are added to a part
    #Make temporary copy of list?

    for i, num in enumerate(rem_digits):
        part = []
        #if not the last element
        if i != (len(rem_digits)-1):
            #if next digit is same
            if num == rem_digits[i+1]:
                #if number can be repeated twice
                if num in trip_repeatable:
                    #if it is repeated three times
                    if num == rem_digits[i+2]:
                        #add next three digits to part
                        part.append(rem_digits[i:i+2])
                        del rem_digits[i:i+2]
                        continue
                #add next two digits to part
                part.append(rem_digits[i:i+1])
                del rem_digits[i:i+1]
                continue

            #if digit is smaller than next digit
            if num < rem_digits[i+1]:
                #add both digits to new part
                part.append(rem_digits[i:i+1])
                del rem_digits[i:i+1]
                continue
        
        #if digit is standalone (not subtracted)
        if i == (len(rem_digits)-1) and len(rem_digits) == 1:
            part.append(rem_digits[i])
            del rem_digits[i]
            continue
    
        parts.append(part)

    print(parts)
    return(parts)


def evaluateParts(parts):
    #If smaller value is before larger in part, subtract
    #If larger value is before smaller in part, add
    total = 0
    for part in parts:
        if len(part) > 1:
            if part[0] < part[1]:
                total += part[1] - part[0]
        else:
            total += sum(part)

    return total

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