matches = ["Is this task easy?", "12?", "a?b?c?", "2?Fddsa3fU*ÜA?"]
not_matches = ["Is this task easy", "12", "a?b?c", "2?Fddsa3fU*ÜA"]

import re

#any number of any characters allowed, follow by single ? character
pattern = r".*\?"

# quick unit testing script that prints whether or not the string passed
#   test based on expected behavior (ie should match or should not match)
def test_regex(s, pattern, should_match = 1, buffer = 30):
    result = re.fullmatch(pattern, s) is not None #returns a Match object if found
    print(f"{s:<{buffer}}\t{result == should_match}")

for match in matches:
    test_regex(match, pattern)

for not_match in not_matches:
    test_regex(not_match, pattern, 0)