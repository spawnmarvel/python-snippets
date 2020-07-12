# https://www.w3schools.com/python/python_regex.asp
# https://realpython.com/regex-python/
import re

txt = "TT-80-2000"
for match in re.finditer('[^a-zA-Z]+\d\d', txt):
    print(match.span(), match.group())
