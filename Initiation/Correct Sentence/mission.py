def correct_sentence(text: str) -> str:
    if text[-1] != ".":
        text = text + "."
    cap = text[0].capitalize()
    return cap + text[1:]


print("Example:")
print(correct_sentence("greetings, friends"))

assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print("The mission is done! Click 'Check Solution' to earn rewards!")
