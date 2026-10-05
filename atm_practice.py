account = {
    "pin":"4321",
    "balance" : 1000,
    "daily_limit":500
}
attempts_left = 3

while attempts_left > 0:
    pin = input("what is your pin : ")
    if account['pin'] == pin :
        print(" Access Granted ")
        withdraw_amount = int(input("what is your withdraw amount : "))
        if withdraw_amount > account["balance"]:
            print("insufficient balance ")
        elif withdraw_amount > account["daily_limit"]:
            print("daily limit exceeded ")
        else :
            account["balance"] -= withdraw_amount
            print(f"withdrawal successful ! Rimaning balance : {account['balance']}")
        break

    else :
        attempts_left -= 1
        if attempts_left > 0 :
                print(f"incorrect pin only {attempts_left} attempts left ")
        else :
                print ("card is blocked please contect your bank ")
    
    