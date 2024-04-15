# Bepaal recursief of een getal voldoet aan het luhn-criteria.

def luhn(cardNumber):
    result = 0
    cardNumber = str(cardNumber)
    if len(cardNumber) == 0:
        return result
    if len(cardNumber) % 2 == 0:
        result = int(cardNumber[0]) * 2
        if result > 9:
            result -= 9
    else:
        result = int(cardNumber[0])
    result += luhn(cardNumber[1:])    
    return result
    
    # result = 0
    # for index, number in enumerate(str(cardNumber)):
    #     number = int(number)
    #     if index % 2 == 0:
    #         number *= 2
    #         if number > 9:
    #             number -= 9
    #     result += number
    # return result % 10 == 0
                
print( luhn(4687612962034330) ) # 70 --> geldig
print( luhn(6728003096702784) ) # 70 --> geldig
print( luhn(2727903413621029) ) # 66 --> ongeldig
print( luhn(9727009535679498) ) # 92 --> ongeldig