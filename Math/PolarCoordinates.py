'''
Title     : Polar Coordinates
Subdomain : Math
Domain    : Python
Author    : Yash Chudasama
Created   : 28 July 2021
Problem   : https://www.hackerrank.com/challenges/polar-coordinates/problem
'''
import cmath
z = complex(input())
p = cmath.polar(z)
print(p[0])
print(p[1])
