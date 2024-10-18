import validators
import sys
def main():
    try:
        if validators.email(input("Email?")):
            print("Valid")
        else:
            print("Invalid")
    except:
        pass

if __name__ == "__main__":
    main()
