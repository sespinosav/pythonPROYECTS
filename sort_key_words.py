"""
This script sort key words for documents
"""

keys = input("Give me the keywords: ")

keys = keys.split(",")

keys = [word.replace(".","").strip().lower() for word in keys]

keys.sort()

result = ""

for word in keys:
    if keys.index(word) == 0:
        result += word.capitalize() + ","
    elif keys.index(word) == len(keys) - 1:
        result += " " + word + "."
    else:
        result += " " + word + ","
    
print(result)