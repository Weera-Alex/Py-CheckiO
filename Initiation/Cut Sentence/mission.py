def cut_sentence(line: str, length: int) -> str:
    """
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    """
    # your code here
    return line[:length]


print("Example:")
print(cut_sentence("Hi my name is Alex", 4))

assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")
