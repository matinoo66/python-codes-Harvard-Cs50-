import sys

def main():
    check_cmd_arg()
    try:
        file = open(sys.argv[1],"r")
        lines = file.readlines()
        count = 0
        for line in lines:
            if check_lines(line) == False:
                count += 1
        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")

def check_lines(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    return False




def check_cmd_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")


if __name__ == "__main__":
    main()
