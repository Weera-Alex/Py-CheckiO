def checkio(words: str) -> bool:
    # add your code here
    counter = 0
    words = words.split()
    for x in range(len(words)):
        if not words[x].isdigit():
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 0
    return False


print("Example:")
print(checkio("Hello World hello"))

assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
