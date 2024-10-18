import re
def main():
    id = input("input ipv4: ").strip()
    print(validate(id))
def validate(id):
    if match := re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",id):
        list_of_nums = id.split(".")
        for number in list_of_nums:
            if int(number) < 0 or int(number)>255:
                return False
        return True
    else:
        return False
if __name__ == "__main__":
    main()


