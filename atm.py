#1.ATM Simulation

balance=0
while True:
    choice=int(input(' 1.Check balance \n 2.Deposit money \n 3.withdraw money \n 4.exit \n Enter the choice =' ))
    if(choice == 1):
        print(f'balance is {balance}')
    elif(choice == 2):
        n=int(input('enter money to deposite ='))
        balance+=n
        print("money deposited successfully")
    elif(choice == 3):
        n=int(input('Money to with draw ='))
        if(balance < n):
            print(f'Insufficient balance,available balance is only {balance}')
        else:
            balance-=n
            print('payment successfull')
    else:
        break