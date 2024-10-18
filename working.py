import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    nah = ""
    nch = ""
    cm = "00"
    am = "00"

    if match := re.search(r"((([0-9])+)(:)?([0-9]+)?) ([AM|PM]+) to (([0-9]+)(:)?([0-9]+)?) ([AM|PM]+)",s):

        if match.group(5):
            am = match.group(5)
        if match.group(10):
            cm = match.group(10)
        ah = match.group(2)

        b = match.group(6)
        ch = match.group(8)

        d = match.group(11)


        if  0 < int(ah) <= 12 and  0 < int(ch) <= 12 and int(am) < 60  and int(cm) < 60 :

            if "AM" in b:
                if int(ah) == 12:
                    ah = int(ah)-12
                else:
                    ah = int(ah)
                nah = f"{ah:02}"

            if "AM" in d:
                if int(ch) == 12:
                    ch = int(ch)-12
                else:
                    ch = int(ch)
                nch = f"{ch:02}"

            if "PM" in b:
                    if int(ah) != 12:
                        ah = int(ah)+12
                    elif int(ah) == 12:
                        ah = int(ah)
                    nah = f"{ah:02}"


            if "PM" in d:
                    if int(ch) != 12:
                        ch = int(ch)+12
                    elif int(ah) == 12:
                        ch = int(ch)
                    nch = f"{ch:02}"

            return f"{nah}:{am} to {nch}:{cm}"
        else:
            raise ValueError
    else:
        raise ValueError




if __name__ == "__main__":
    main()
