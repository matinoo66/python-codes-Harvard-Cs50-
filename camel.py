camel_case = input("input your words as camel case: ").strip()
new_word = ''

for c in camel_case:
    if c.isupper():
        new_word += '_' + c
    else:
        new_word += c
print(new_word.lower())
