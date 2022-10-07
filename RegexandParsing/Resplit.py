'''
Title     : Re.split()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Yash Chudasama
Updated   : 3 April 2021
Problem   : https://www.hackerrank.com/challenges/re-split/problem
'''

import re
regex_pattern = r'[.,]+'

print("\n".join(re.split(regex_pattern, input())))
