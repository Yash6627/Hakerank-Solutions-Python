'''
Title     : Regex Substitution
Subdomain : Regex and Parsing
Domain    : Python
Author    : Yash Chudasama
Created   : 15 July 2019
Problem   : https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
'''
import re, sys
n = int(input())
for line in sys.stdin:
    remove_and = re.sub(r'(?<= )(&&)(?= )',"and",line)
    remove_or = re.sub(r'(?<= )(\|\|)(?= )',"or",remove_and)
    print(remove_or,end='')
