'''
Title     : Validating phone numbers
Subdomain : Regex and Parsing
Domain    : Python
Author    : Yash Chudasama
Updated   : 3 April 2021
Problem   : https://www.hackerrank.com/challenges/validating-the-phone-number/problem
'''

from re import compile, match

n = int(input())
for _ in range(n):
    phone_number = input()
    condition = compile(r'^[7-9]\d{9}$')
    if bool(match(condition, phone_number)):
        print("YES")
    else:
        print("NO")
