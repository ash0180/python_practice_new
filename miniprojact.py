class expance :
    def __init__(self , itembought , cost , catagory):
        self.itembought = itembought
        self.cost = cost
        self.catagoty = catagory

    def display_budget(self):
        print(f"Expance : {self.itembought}, Cost : {self.cost}, catagory : {self.catagoty}")

class bgttracker:
        def __init__(self , monthlybudget):
            self.monthlybudget = monthlybudget
            monthlybudget = float(input("what is your monthly budget : "))
            self.expance = []

        def add_expance(self , spent):
            self.expance.append(spent)
            print("your expance is added ")

        def get_amountspant(self):
            total = 0
            for item in self.expance :
                total += item.cost
            return total

        def check_budget(self):
            amount_spnt = self.get_amountspant()
            if amount_spnt >= self.monthlybudget :
                print(amount_spnt - self.monthlybudget , "you are overbudget")
            else :
                print(self.monthlybudget - amount_spnt , "is your Remaning budget")

tracker = bgttracker(monthlybudget=5000)
e1 = expance("milk",2880,"food")
e2 = expance("groceries",700,"food")
e3 = expance("food order", 840, "food")

tracker.add_expance(e1)
tracker.add_expance(e2)
tracker.add_expance(e3)

tracker.check_budget()


