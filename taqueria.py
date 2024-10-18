total = 0
menu = {
"Baja Taco": 4.25,
"Burrito": 7.50,
"Bowl": 8.50,
"Nachos": 11.00,
"Quesadilla": 8.50,
"Super Burrito": 8.50,
"Super Quesadilla": 9.50,
"Taco": 3.00,
"Tortilla Salad": 8.00
}
try:
    while True:
        food = input("Enter your Foods line by line: ").title()
        if food in menu:
            price = menu[food]
            total += price
            print("Total:$",end="")
            print(f"{total:.2f}")
except EOFError:
    exit

