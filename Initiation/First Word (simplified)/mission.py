def first_word(text: str) -> str:
    # your code here
    text = text.split()
    return text[0]


print("Example:")
print(first_word("Hello world"))

assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
