"""
Title     : Set .add()
Subdomain : Sets
Domain    : Python
Author    : Yash Chudasama
Updated   : 19 June 2022
problem   : https://www.hackerrank.com/challenges/py-set-add/problem
"""
n = int(input())
country_set = set()
for i in range(n):
    country_name = input()
    country_set.add(country_name)
print(len(country_set))
