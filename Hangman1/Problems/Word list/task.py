#  Posted from EduTools plugin
text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
check = int(input())
res = [word for sentence in text for word in sentence if len(word) <= check]
print(res)