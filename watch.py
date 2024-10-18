# import sys
import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
         match = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-Z0-9]+)\"",s)
         if match:
            corelink = match.group(4)
            return (f"https://youtu.be/{corelink}")




if __name__ == "__main__":
  main()

