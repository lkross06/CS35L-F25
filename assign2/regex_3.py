matches = ["0", "1613", "ABC", "2F0B1A"]
not_matches = ["0.99", "-12", "abc", "pi", "zero", "ABCDEFEG"]

import re

#can start with every hexadecimal char EXCEPT 0, followed by any hexadecimal char
pattern = r"^[1-9A-F]?[0-9A-F]*$"

# quick unit testing script that prints whether or not the string passed
#   test based on expected behavior (ie should match or should not match)
def test_regex(s, pattern, should_match = 1, buffer = 30):
    result = re.fullmatch(pattern, s) is not None #returns a Match object if found
    print(f"{s:<{buffer}}\t{result == should_match}")

for match in matches:
    test_regex(match, pattern)

for not_match in not_matches:
    test_regex(not_match, pattern, 0)