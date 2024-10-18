def coke_machine():
    accepted_coins = [25, 10, 5]
    amount_due = 50

    while amount_due > 0:
        print("Amount Due:",amount_due)
        coin = int(input("insert Coin: "))

        if coin in accepted_coins:

            amount_due -= coin

    change_owed = abs(amount_due)

    print("Change Owed:",change_owed)

coke_machine()

