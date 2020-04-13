# You are given a string .
# Your task is to find out whether  is a valid regex or not.
#
# Input Format
#
# The first line contains integer , the number of test cases.
# The next  lines contains the string .
#
# Constraints
# 0 < T < 100
#
# Output Format
#
# Print "True" or "False" for each test case without quotes.
#
# Sample Input
#
# 2
# .*\+
# .*+
# Sample Output
#
# True
# False
# Explanation
#
# .*\+ : Valid regex.
# .*+: Has the error multiple repeat. Hence, it is invalid.

import re

for count in range(int(input())):
    _input = input()
    try:
        print(bool(re.compile(_input)))
    except:
        print(False)
