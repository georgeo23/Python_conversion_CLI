# this function is called and the user is prompted for the desired conversion
def get_user_input():
    # prompts the user for their desired conversion
    string = input('conversion in format "x unitA in unitB" \n')
    return string
# once the user string is inputted, this function then splits it up to find the number, units etc to perform the conversion and output it.
def convert(string):
    #splits the users input into 4 parts if they follow the displayed format, if it isn't in the correct format then they are told so.
    split_string = string.split()
    # existing magnitudes for centi = c, milli = m, kilo = k, all working with 10^magnitude to help calculate.
    magnitudes = {
        "c": -2,
        "k": 3,
        "m": -3
    }
    #each unit is part of a group; length or weight. Units can be added accordingly along with their coefficient to metres for length and grams for weight.
    to_standard = {
        'length': {
            'm': lambda x: x
        },
        'weight': {
            'lb': lambda x: x *0.00220462,
            'g': lambda x: x
        },
        'temperature': {
            'f': lambda x: (x-32)*(5/9),
            'c': lambda x: x
        }
    }
    # this is the reverse coefficient, used to convert the 2nd unit back into the standard unit needed to then provide the correct conversion.
    from_standard = {
        'length': {
            'm': lambda x: x
        },
        'weight': {
            'lb': lambda x: x /0.00220462,
            'g': lambda x: x
        },
        'temperature': {
            'f': lambda x: (x*9/5 + 32),
            'c': lambda x: x
        }
    }
    #the original magnitude coefficients are started at 0 to give a 10^0 (1) multiplier if one are the original unit.
    y = 0
    p = 0
    newdict = None
    unitA = ""
    funcA = ""
    typeA = ""
    unitB = ""
    funcB = ""
    typeB = ""
    number = None
    # checks to see if a number is inputted first, otherwise the user is told to do so.
    try:
        number = float(split_string[0])
    except:
        print('please enter a number to convert')
    # checks if the 2nd word of the user input exists, if it does then it begins checking to see if it is a centi, milli or kilo of its unit.
    if len(split_string[1]) > 0:
        for m in magnitudes.keys():
            # gets the 1st unit's multiplier by checking if it has a c, m or k in front.
            if split_string[1].startswith(m) and len(split_string[1]) > 1:
                y = magnitudes[m]
                
            # gets the 2nd or desired unit's multiplier by checking if it has a c, m or k in front.
            if split_string[3].startswith(m) and len(split_string[3]) > 1:
                p = magnitudes[m]
        # loops through the first dictionary to get the unit to change, its type - e.g length, and the appropriate coefficient to be used if converting to a different measurement.        
        for i, j in to_standard.items():
            for unit, func in j.items():
                if split_string[1].endswith(unit):
                    typeA = i
                    unitA = unit
                    funcA = func
                    break
        # another loop to find the measurement, type of measurement and the reverse coefficient.
        for i, j in from_standard.items():
            for unit, func in j.items():
                if split_string[3].endswith(unit):
                    typeB = i
                    unitB = unit
                    funcB = func
                    break
    # checks that the string entered is 4 words long, as expected, otherwise tells the user they need to enter it correctly.
    if len(split_string) != 4:
        print('please enter in the format "x unitA in unitB"')
        return 'incorrect format entered'
    # checks to see if two units are the same type e.g 'x weightA in weightB'. If 'temperature to length' is typed then it tells the user that it isn't possible.
    elif typeA != typeB:
        print('the units are not both of the same type, please try again')
        return 'units are not of the same type'
    # this checks to see if the units are the same type and measurement, if they are then no coefficients are needed, only the magnitude e.g 'centi' or '-2'.
    elif typeA == typeB and unitA == unitB and number is not None:
        multiplier = y - p
        newnumber = number * 10**multiplier
        return f'{newnumber} {split_string[3]}'
    # final check to see if the number is not None then it makes the conversion to the 2nd unit using the coefficient and the magnitude to produce the correct result.
    elif number is not None:
        calcA = funcA(number*10**y)
        calcB = funcB(calcA*10**-p)
        return calcB
    # if this point is reached, one or both of the inputted units are currently not in the dictionary and the user is told to make a suggestion to get it added.
    else:
        print('the units you have entered are currently unable to be calculated, leave a suggestion and they can be added!')
        return 'one or both units do not exist'
# this initiates the function upon starting up the program.
if __name__ == "__main__":
    print(convert(get_user_input()))