'''
Title     : Detect HTML Tags, Attributes and Attribute Values
Subdomain : Regex and Parsing
Domain    : Python
Author    : Yash Chudasama
Created   : 15 Jan 2022
Problem   : https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
'''
from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        self.handle_attrs(attrs)
    def handle_startendtag(self,tag,attrs):
        print(tag)
        self.handle_attrs(attrs)
    def handle_attrs(self,attrs):
        for attrs_pair in attrs:
            print('->',attrs_pair[0].strip(),'>',attrs_pair[1].strip())        

n = int(input())
html_string = ''
for i in range(n):
    html_string += input()
    
customHTMLParser = CustomHTMLParser()
customHTMLParser.feed(html_string)
customHTMLParser.close()
