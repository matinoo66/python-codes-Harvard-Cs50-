
# def main():
#     sentence = input("Type your sentence: ")
#     convert(sentence)
# def convert(sentence):
#     for key in sentence:
#         newsentence = sentence.replace(":)","🙂").replace(":(","🙁")
#     print(newsentence)
# main()
def main():

    x = input("what's x: ")

    print(convert(x))





def convert(str):

    return str.replace(":)" , "🙂").replace(":(" , "🙁")



main()

