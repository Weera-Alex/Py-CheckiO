def end_zeros(a: int) -> int:
    a = str(a)
    count = 0
    for x in a:
        if x == "0":
            count += 1
        else:
            count = 0
    return count


print("Example:")
print(end_zeros(10))

assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
