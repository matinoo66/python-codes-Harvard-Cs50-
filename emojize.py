import emoji
text = input("input: ")
etext = emoji.emojize(text, language='alias')
print("Output: ",etext)
