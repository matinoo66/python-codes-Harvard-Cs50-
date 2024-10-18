def main():
    x = input("what's The Answer? ").lower().strip()
    # print(x)
    check(x)
def check(x):
    if x in ["42","forty-two","forty two"]:
        print("Yes")
    else :
        print("No")
main()
