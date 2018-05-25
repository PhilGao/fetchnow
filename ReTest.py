import re

StringSet = ("/wiki/Wikipedia:Naming_conventions_(technical_restrictions)#Forbidden_characters",
             "/wiki/Naming_conventions_(technical_restrictions)#Forbidden_characters")

for str in StringSet:
    result = re.search("^/wiki/(?!Wikipedia).*$", str)
    print(str)
    if result != None: print(result.group())
