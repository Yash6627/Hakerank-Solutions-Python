'''
Title     : Hex Color Code
Subdomain : Regex and Parsing
Domain    : Python
Author    : Yash Chudasama
Created   : 15 July 2022
Problem   : https://www.hackerrank.com/challenges/hex-color-code/problem
'''
import re
n = int(input())
for t in range(n):
    s = input()
    match_result = re.findall(r'(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})',s)
    for i in match_result:
        if i != '':
            print(i)
