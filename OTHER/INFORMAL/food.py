class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.amount_sold = 0
        self.total_gained = 0
        foods[name] = self

    def sell(self, amount = 1):
        self.amount_sold += amount
        self.total_gained += self.price * amount

        self.update()

    def update(self):
        foods[self.name] = self

    def __str__(self):
        return f"{self.name}:\n\nPrice: {self.price} kr\nTotal gained: {self.total_gained}\nAmount Sold: {self.amount_sold}"

foods = {}

Food("Brownies", 10)
Food("Muffins", 15)
Food("Sjokoladekake", 15)
Food("Pizzaboller", 15)
Food("Glutenfrie Brownies", 10)
Food("Kanelboller", 15)
Food("Saft", 5)
Food("Sjokoladeboller", 15)
Food("Fruktspyd", 10)
Food("Horn med ost og skinke", 15)
Food("Popcorn", 5)

commands = {
    "list": "Lists all foods",
    "buy <amount> <food>": "Buys <amount> of <food>",
    "price <food> <amount>": "Sets the price of <food> to <amount>",
    "check": "Get information about a certain food",
    "help": "Shows this message",
    "exit": "Exits the program"
}

while True:
    user = input(">> ")

    if user and user[0] == "!":
        user = user[1:].split()

        if user[0] == "list":
            print("\n".join([f"{food.name}: {food.price} kr" for food in foods.values()]))
        elif user[0] == "buy" or user[0] == "sell" or user[0] == "price":
            buy = "buy" if user[0] == "buy" or user[0] == "sell" else ""
            price = "price" if not buy else ""

            try:
                if buy:
                    food = foods[user[2].title()]
                else:
                    food = foods[user[1].title()]
            except Exception as e:
                if type(e) == KeyError:
                    food = user[2].title() if buy else user[1].title()

                    print(f"Food `{food}` does not exist!")
                else:
                    for command in commands:
                        c = command.split()[0]

                        if c in [buy, price]:
                            print(f"Invalid usage of command! Use `!{command}`.")
                            break
                continue

            try:
                if buy:
                    food.sell(int(user[1]))
                else:
                    food.price = int(user[2])
            except Exception:
                for command in commands:
                    c = command.split()[0]

                    if c in [buy, price]:
                        print(f"Invalid usage of command! Use `!{command}`.")
                        break
                continue

            foods[food.name] = food
        elif user[0] == "check":
            try:
                print(str(foods[user[1].title()]))
            except KeyError:
                print(f"Food `{user[1].title()}` does not exist!.")
        elif user[0] == "exit":
            break
        elif user[0] == "help":
            print("\n".join([f"!{command} - {description}" for command, description in commands.items()]))
            continue


        continue

    print(f"Total amount of KR gained: {sum([food.total_gained for food in foods.values()])}")