class BankAccount:
    def __init__(self,acountholder, balance):
        self.acountholder = acountholder
        self.balance = balance

    def deposit_amount(self):
        self.deposit_amount = int(input("what is ur deposite amount : "))
        totlamt = self.balance + self.deposit_amount
        print(f"your total amount is {totlamt}")

    def withdraw_amount(self):
        self.withdraw_amount = int(input("what is ur withdraw amount : "))
        updtblnc = self.balance - self.withdraw_amount
        if updtblnc :
            updtblnc >=0
            print(f" remaning balance = {updtblnc}")
        else :
            print(" insufficiant balance ")

ah1 = BankAccount("vedansh" , 500000)
ah1.deposit_amount()
ah1.withdraw_amount()
        
        

    

        