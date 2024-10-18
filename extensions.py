file = input("enter file name: ").lower().strip()
letters=[]
for letter in file:
    letters.append(letter)
# print(letters[-3:])
if letters[-3:] == ['j', 'p', 'g']:
    print("image/jpeg")
elif letters[-3:] == ['p','d','f']:
    print("application/pdf")
elif letters[-3:] == ['t','x','t']:
    print("text/plain")
elif letters[-3:] == ['z','i','p']:
    print("application/zip")
elif letters[-3:] == ['p','n','g']:
    print("image/png")
elif letters[-3:] == ['g','i','f']:
    print("image/gif")
elif letters[-4:] == ['j','p','e','g']:
    print("image/jpeg")



else:
    print("application/octet-stream")
