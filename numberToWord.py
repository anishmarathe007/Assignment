def numberToWord(n, suffix):

    NOTHING = ""

    X = [NOTHING, "One ", "Two ", "Three ", "Four ", "Five ", "Six ",
         "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
         "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
         "Seventeen ", "Eighteen ", "Nineteen "]

    Y = [NOTHING, NOTHING, "Twenty ", "Thirty ", "Forty ", "Fifty ",
         "Sixty ", "Seventy ", "Eighty ", "Ninety "]

    if n < 0:
        raise IndexError(n , " Not Available!")

    if n == 0:
        return NOTHING

    if n > 19:
        return Y[n // 10] + X[n % 10] + suffix
    else:
        return X[n] + suffix

def convert(n):
    if n == 0 :
        return "Zero"

    result = numberToWord(( n // 10000000000000000000) % 100, "Maha Shankh ")

    result += numberToWord(( n // 100000000000000000) % 100, "Shankh ")

    result += numberToWord(( n // 1000000000000000) % 100, "Padma ")

    result += numberToWord(( n // 10000000000000) % 100, "Neel ")

    result += numberToWord(( n // 100000000000) % 100, "Kharab ")

    result += numberToWord((n // 1000000000) % 100, "Arab ")

    result += numberToWord((n // 10000000) % 100, "Crore ")

    result += numberToWord(((n // 100000) % 100), "Lakh ")

    result += numberToWord(((n // 1000) % 100), "Thousand ")

    result += numberToWord(((n // 100) % 10), "Hundred ")

    result += numberToWord((n % 100), "")

    return result
