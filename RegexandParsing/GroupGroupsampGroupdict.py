'''
Title     : Group(), Groups() &amp; Groupdict()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Yash Chudasama
Created   : 15 Jan 2022
Problem   : https://www.hackerrank.com/challenges/re-group-groups/problem
'''
import re
s = input()
res = re.search(r'([A-Za-z0-9])\1',s)
if res == None:
    print(-1)
else:
    print(res.group(1))
