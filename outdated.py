months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]
while True:

    date = input("Date: ").strip()
    try:
        if "/" in date:
            mm , dd , yyyy = date.split("/")
            if 1<=int(mm)<=12 and 1<=int(dd)<=31:
                print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
                break

        elif "," in date:
            date = date.replace(",","")
            mm , dd , yyyy = date.split()
            if mm in months:
                mm = months.index(mm)
                mm += 1
                if 1<=int(mm)<=12 and 1<=int(dd)<=31:
                    print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
                    break
    except:
        pass


