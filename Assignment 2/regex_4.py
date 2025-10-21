matches = ["1.99", "1234.00", "-5.55", "3.141592", "3.141592" , "58312", "5", "0"]
not_matches = [".99", "pi", "zero", "3.13321937420e-09", "00000.01", "00001.01", "11." , "001", "422CF450", "0001", "01343", "00", ""]

import re

#optional negative sign,
#  at least one number thats not a leading zero,
#  optional decimal point, if true then at least one more number
#  OR just zero. -0 doesn't match but thats okay
pattern = r"^-?([1-9]+([.][0-9]+)?)|0$"

# quick unit testing script that prints whether or not the string passed
#   test based on expected behavior (ie should match or should not match)
def test_regex(s, pattern, should_match = 1, buffer = 30):
    result = re.fullmatch(pattern, s) is not None #returns a Match object if found
    print(f"{s:<{buffer}}\t{result == should_match}")

for match in matches:
    test_regex(match, pattern)

for not_match in not_matches:
    test_regex(not_match, pattern, 0)