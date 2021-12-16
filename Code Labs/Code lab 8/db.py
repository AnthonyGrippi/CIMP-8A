
FILENAME = "A:\\Python Projects\\Code Labs\\Code lab 8\\money.txt"

def read_money():
    with open(FILENAME, "r") as file:
        line = file.readline()
    
    money = float(line)
    return money

def write_money(money):
    with open(FILENAME, "w") as file:
        file.write(str(money))
