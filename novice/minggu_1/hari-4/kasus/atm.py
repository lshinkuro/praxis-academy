class ATMMachine:
    
   def checkBalance(self):
      print("\tYour current balance is " + BalanceInquiry.getBalance())
    
   
   def withdrawMoney(self):
    
        if BalanceInquiry.balance==0:
            print("\tYour current balance is zero.");
            print("\tYou cannot withdraw!");
            print("\tYou need to deposit money first.");
        elif BalanceInquiry.balance<=500:
            
            print("\tYou do not have sufficient money to withdraw")
            print("\tChecked your balance to see your money in the bank.")
        
        elif(Withdraw.withdraw > BalanceInquiry.balance):
        
            print("\tThe amount you withdraw is greater than to your balance");
            print("\tPlease check the amount you entered.");
        
        else:
        
            BalanceInquiry.balance = BalanceInquiry.balance - Withdraw.withdraw;
            print("\n\tYou withdraw the amount of Php " + Withdraw.withdraw);
        
    
                   
   def depositMoney(self):
       print("\tYou deposited the amount of " + Deposit.getDeposit())
    
   
   def main(self):
    
        read = int(input())
        select = 0
        choice = 0
       
        print("====================================================")
        print("\tWelcome to this simple ATM machine")
        print("====================================================")
        print()
       
        

        
    
        print("\t Please select ATM Transactions")
        print("\t Press [1] Deposit")
        print("\t Press [2] Withdraw")
        print("\t Press [3] Balance Inquiry")
        print("\t Press [4] Exit")
               
        print("\n\tWhat would you like to do? ")
                   
        select = read.nextInt()
   
        if select > 4:
            print("\n\tPlease select correct transaction.")
                        
        else:
         if select ==1:
                print("\n\tEnter the amount of money to deposit: ");
                Deposit.deposit = read.nextDouble();
                BalanceInquiry.balance = Deposit.deposit + BalanceInquiry.balance;
                depositMoney();
                               
         elif select==2:
                               
                print("\n\tTo withdraw, make sure that you have sufficient balance in your account.");
                print();
                print("\tEnter amount of money to withdraw: ");
                Withdraw.withdraw = read.nextDouble();
                withdrawMoney();
         elif select==3:
                checkBalance();
                
                           
         else:
            print("\n\tTransaction exited.");
           
             
        
                                  
        while select>4 :

                print("\n\tWould you like to try another transaction?");
                print("\n\tPress [1] Yes \n\tPress [2] No");
                print("\tEnter choice: ");
                choice = read.nextInt();
               
                if choice>2:
                    print("\n\tPlease select correct choice.");
                        

                   
                    
                   
                else:
                    
                       print("\tError Input! Please enter a number only.");
                       read = input();
                       print("\tEnter yout choice:");
                       choice = read.nextInt();
                    
        while choice>2 :
                
                   print("\tError Input! Please enter a number only.");
                   read = input();
                   print("\tEnter yout choice:");
                   select = read.nextInt();
                
               
        while choice<=1:
              print("\n\tThank you for using this simple ATM Machine.");


class Deposit(ATMMachine):

    deposit:0
    def setDeposit(d):
        deposit =d
   
    def getDeposit(self):
        return deposit
    


# The Wihtdraw class

# Here is the program source code:

class Withdraw(ATMMachine):
    
    withdraw=0
    def set_withdraw(w):
        withdraw= w

    def get_withdraw(self):
        return withdraw



# The Balance Inquiry class

# Here is the program source code:


class BalanceInquiry(ATMMachine):

    balance = 0;
    def setBalance(b):
        balance =b

    def getBalance(self):
        return balance

mesin_atm=ATMMachine()

print(mesin_atm())
  
