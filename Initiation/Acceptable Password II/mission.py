# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    # your code here
    return True if len(password) > 6 else False


print("Example:")
print(is_acceptable_password("short"))

assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")


assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
