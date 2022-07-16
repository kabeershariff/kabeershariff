from random import  randint

money = 1000
ticket = 0
winning_number = int(f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}")

while money >= 50 or ticket!=0:
    print("\t\t\t========$$$=============$$$=  Welcome to Lottery Sim ======= $$$ 1000000 =========$$$=======$$$========")
    ##buying
    if money >= 50:
        buy = int(input(f"\tEnter number of Tickets you will like to buy ? Your balance is {money} $. One Ticket costs 50$ ."))
        if buy*50 <= money:
            money = money - buy*50
            ticket = ticket + buy
            print(f"\t\t\tyou have {ticket} tickets and balance {money} $")
        else:
            print("\t\t\tno cheaters allowed")

    ##Lottery
    if ticket > 0:
        while ticket > 0:
            print("\t\t\tTime to see your luck !!!")
            spin = input("\t\t\t\t Enter to spin !!!!!")
            result = int(f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}")
            print(f"\t\t\tYour ticket number is {result} and the winning number is {winning_number}")
            ticket = ticket - 1
            if winning_number == result:
                print("\t\t\t\t=====>>>$$$===>>>You have won the jackpot<<<=======$$$<<<=====")
                money = money + 1000000
            else: 
                print("\t\t\t\t=====>>better luck next time<<=======")

print("You Lost all your money")
