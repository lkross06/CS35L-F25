matches = ["$4", "4$", "€5.23", "3.00€", "0.30$", "$0.00", "$111111.99"]
not_matches = [".99$", "0$", "4 $", "30", "000005$", "00001.01", "11.1$" , "001", "-40$", "00.00$"]

import re

'''
Write a regex that finds all valid price tags in $ or € in a text and that
names the group of the unit “unitL” in case the unit is left of the number
(e.g, “$4”) and "unitR" in case the unit is right of the number (e.g., “4€”).
Accept prices that include either no decimal places or exactly two decimal places.
There should be no spaces in the matched string. Implicit zeros in the front should not match
(e.g., “00000.01$”) while they should match at the end (e.g., “$3.00”).

Example Matches: “$4”, “4$”, “€5.23”, “3.00€”, “0.30$” , 
Example Non-Matches: “.99$”, “0$”, “4 $”, “30”, “000005$”, “00001.01”, “11.1$” , “001”, “-40$”

'''

#look for unitL unit (one $ or €)
#  look for at least one of 1-9
#  OR
#  "0." followed by two of 0-9
#    look for "." followed by two of 0-9 (optional) //note this will only run of we find at least one of 1-9 above
#OR
#look for at least one of 1-9
#OR "0." followed by two of 0-9
#  look for "." followed by two of 0-9 (optional)
#  look for unitR unit (one of $ or €)
pattern = r"((?P<unitL>[$€])([1-9]+|0.[0-9]{2})([.][0-9]{2})?([^0-9]+)?)|(([^0-9]+)?([1-9]+|0.[0-9]{2})([.][0-9]{2})?(?P<unitR>[$€]))"

# quick unit testing script that prints whether or not the string passed
#   test based on expected behavior (ie should match or should not match)
def test_regex(s, pattern, should_match = 1, buffer = 30):
    result = re.fullmatch(pattern, s) is not None #returns a Match object if found
    print(f"{s:<{buffer}}\t{result == should_match}")

for match in matches:
    test_regex(match, pattern)

for not_match in not_matches:
    test_regex(not_match, pattern, 0)