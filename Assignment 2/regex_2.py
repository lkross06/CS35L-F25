matches = ["This task is easy!", "FddsfU*ÜA"]
not_matches = ["A.B.C1", "2?Fddsa3fU*ÜA", "2.2?Fddsa3fU*ÜA"]

import re

#every character must be part of the set that excludes 0-9
pattern = r"[^0-9]*"

# quick unit testing script that prints whether or not the string passed
#   test based on expected behavior (ie should match or should not match)
def test_regex(s, pattern, should_match = 1, buffer = 30):
    result = re.fullmatch(pattern, s) is not None #returns a Match object if found
    print(f"{s:<{buffer}}\t{result == should_match}")

for match in matches:
    test_regex(match, pattern)

for not_match in not_matches:
    test_regex(not_match, pattern, 0)