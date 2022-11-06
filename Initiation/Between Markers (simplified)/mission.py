def between_markers(text: str, start: str, end: str) -> str:
    a = False
    your_word = ""
    for x in text:
        if x == end:
            a = False
        if a:
            your_word += x
        if x == start:
            a = True
    return your_word


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")
