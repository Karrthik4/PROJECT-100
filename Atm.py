class Atm(object):
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def balanceInquiry(self):
        print("Your balance is: 5000INR")

    def cashWithdrawl(self, amount):
        new_amount = 5000-amount
        print("You withdrawed: " + str(amount) + "INR Your remaining balance is: " + str(new_amount))
    
def main():
    name = input("Hello, Enter your name: ")
    print("Hello, " + name)

    cardNumber = input("Insert your card number: ")
    pin = input("Insert your pin: ")

    new_user = Atm(cardNumber, pin)

    print("Choose your activity:")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawel")
    activity = int(input("Enter activity choice: "))

    if(activity == 1):
        new_user.balanceInquiry()
    elif(activity == 2):
        amount = int(input("Enter the amount: "))
        new_user.cashWithdrawl(amount)
    else:
        print("Enter a valid number choice")

main()