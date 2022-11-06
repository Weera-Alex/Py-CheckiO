def max_digit(value: int) -> int:
    # your code here
    value = str(value)
    highest = 0
    for x in value:
        if int(x) > highest:
            highest = int(x)
    return highest


print("Example:")
print(max_digit(10))

assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
