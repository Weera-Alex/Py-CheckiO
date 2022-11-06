import time
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def f(num):
    return FIRST_TEN[num - 1]


def s(num):
    return SECOND_TEN[num - 10]


def o(num):
    if num % 10 == 0:
        return OTHER_TENS[num // 10 - 2]
    else:
        return OTHER_TENS[num // 10 - 2] + " " + FIRST_TEN[num % 10 - 1]


def checkio(number):
    # replace this for solution
    if number in range(1, 10):
        return f(number)
    if number in range(10, 20):
        return s(number)
    if number in range(20, 100):
        return o(number)
    else:
        num = []
        for x in str(number):
            num.append(x)
        if number % 100 == 0:
                return FIRST_TEN[number // 100 - 1] + " " + HUNDRED
        if num[1] == "0":
            return f(int(num[0])) + " " + HUNDRED + " " + f(int(num[2]))
        elif (a := int(str(num[1] + num[2]))) in range(10, 20):
            return f(int(num[0])) + " " + HUNDRED + " " + s(a)
        else:
            return f(int(num[0])) + " " + HUNDRED + " " + o(int(str(num[1] + num[2])))


for x in range(1, 1000):
    print(checkio(x), x)
    time.sleep(0.1)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
