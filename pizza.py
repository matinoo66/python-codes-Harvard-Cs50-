import sys
import csv
from tabulate import tabulate

def main():
    check_cmd_arg()
    table = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
            print(tabulate(table[1:],headers=table[0],tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

def check_cmd_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a python file")

if __name__ == "__main__":
    main()
