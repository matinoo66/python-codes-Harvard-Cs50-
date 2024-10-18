def main():
    time = input("enter the time: ")
    convert(time)
    converted_time = convert(time)

    if  7 <= converted_time <= 8:
        print("breakfast time")
    if 12 <= converted_time <= 13:
        print("lunch time")
    if 18 <= converted_time <= 19:
        print("dinner time")

def convert(time):
    hour , minute = map(int,time.split(':'))
    converted_time = hour + (minute/60)
    return converted_time

if __name__ == "__main__":
    main()




