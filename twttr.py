def main():
    text = input("input:")
    print("Output:",end="")
    sounds = ['a','e','i','o','u']
    for char in text:

        if not char.lower() in sounds:

            print(char,end="")

main()
