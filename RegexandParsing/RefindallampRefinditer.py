'''
Title     : Re.findall() &amp; Re.finditer()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Yash Chudasama
Created   : 15 July 2022

Problem   : https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
'''
import re
s = input()
result = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',s)
if result:
    for i in result:
        print(i)
else:
    print(-1)
