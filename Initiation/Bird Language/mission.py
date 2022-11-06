def translate(text: str) -> str:
    new_word = ""
    counter = 0
    for x in text:
        if counter == 0:
            if x == " ":
                new_word += x
                continue
            if x not in "aeiouy":
                new_word += x
                counter = 1
                continue
            else:
                new_word += x
                counter = 2
                continue
        counter -= 1
    return new_word


print("Example:")
print(translate("hieeelalaooo"))

assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
