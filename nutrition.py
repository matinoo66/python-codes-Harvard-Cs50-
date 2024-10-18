fruits ={
"strawberries": 50,
"apple": 130,
"avocado": 50,
"banana": 110,
"cantaloupe":50,
"grapefruit":60,
"grapes":90,
"honeydew melon":50,
"kiwifruit":90,
"lemon":15,
"lime":20,
"nectarine":60,
"orange":80,
"peach":60,
"pear":100,
"pineapple":50,
"plums":70,
"sweet cherries":100,
"tangerine":50,
"wetermelone":80
}
fruit_name = input("Enter The Fruit Name: ").lower()
if fruit_name in fruits:
    calories = fruits[fruit_name]
    print("The caolories of the ftuit is:", calories)
else:
    print("")
