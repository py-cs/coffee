# Write your code here
class CM:
    # Immutable data (recipies, names and units of ingredients, prices)
    recipies = [[250, 0, 16, 1], [350, 75, 20, 1], [200, 100, 12, 1]]
    ing_name = ['water', 'milk', 'coffee beans', 'disposable cups']
    units = ['ml of', 'ml of', 'g of', '']
    prices = [4, 7, 6]

    def __init__(self):  # Settings of the machine
        self.ing = [400, 540, 120, 9]
        self.cash = 550
        self.fill_ing = 0
        self.main_prompt()

    def main_prompt(self):
        print("\nWrite action (buy, fill, take, remaining, exit):")
        self.state = "main"

    def buy(self, n):
        for i in range(4):
            if self.ing[i] < self.recipies[n][i]:
                print("Sorry, not enough " + self.ing_name[i])
                self.main_prompt()
                return None
        print("I have enough resources, making you a coffee!")
        for i in range(4):
            self.ing[i] -= self.recipies[n][i]
        self.cash += self.prices[n]
        self.main_prompt()

    def fill(self, i):
        print("Write how many", self.units[i], self.ing_name[i], "do you want to add:")

    def wtf(self, i, val):
        self.ing[i] += val
        if self.fill_ing == 3:
            self.fill_ing = 0
            self.main_prompt()
            return None
        self.fill_ing += 1
        self.fill(self.fill_ing)

    def take(self):
        print("I gave you $" + str(self.cash))
        self.cash = 0
        self.main_prompt()

    def remaining(self):
        print("The coffee machine has:")
        for i in range(4):
            print(self.ing[i], "of", self.ing_name[i])
        print("$" + str(self.cash) + " of money")
        self.main_prompt()

    def process(self, inp):
        if self.state == "main":
            self.state = inp

        if self.state == "remaining":
            self.remaining()

        if self.state == "what_to_buy":
            if inp == "back":
                self.main_prompt()
                return None
            self.buy(int(inp) - 1)

        if self.state == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            self.state = "what_to_buy"

        if self.state == "what_to_fill":
            self.wtf(self.fill_ing, int(inp))

        if self.state == "fill":
            self.fill(self.fill_ing)
            self.state = "what_to_fill"

        if self.state == "take":
            self.take()

        if self.state == "exit":
            self.fill(self.fill_ing)


my_cm = CM()
while my_cm.state != "exit":
    my_cm.process(input())