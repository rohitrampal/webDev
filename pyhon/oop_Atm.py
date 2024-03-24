from typing import Self
class Atm():

    def __init__(Self):
        Self.pin=""
        Self.balance=0
        Self.Main()

    def Main(Self):
       user_input = input("""Welcome to the ATM
        For Create pin press 1
        For Add Amount press 2
        For Withdrawal press 3
        For Current Balance Press 4
        For Exit press 5:   """)
       
       if user_input =='1':
          Self.create_pin()

       elif user_input=='2':
          Self.add()

       elif user_input=='3':
          Self.debit()
          
       elif user_input=='4':
          Self.check_bal()

       else:
          print("Apka din achaa jaye: ")

    def create_pin(self):
        self.pin=input('Enter the pin: ')
        print('Pin create successfully')
        Self.Main()

    def add(self):
       user=int(input("Enter the Pin: "))
       if user==self.pin:
          amount=int(input("Enter the amount: "))
          self.balance=self.balance+amount
          print("Amount add successfully")
          
        
       else:
          print("Pin Bhul gya kya")
       Self.Main()

    def debit(self):
       user=int(input("Enter the Pin: "))
       if user==self.pin:
          debited_amount=int(input("Enter the amount: "))
          if debited_amount<self.balance:
             self.balance=self.balance-debited_amount
             print(f"""{debited_amount} Rs debited from your account 
             remaining balance is {self.balance}""")
             
          else:
             print("Gareeb manush ")   
       else:
          print("Pin yaad nhi hai kya")
       Self.Main()

    def check_bal(self):
       user=int(input("Enter the Pin: "))
       if user==self.pin:
          print("Your current balnce is: ",self.balance)

       else:
          print("Pin yaad kr le")
       Self.Main()

pnb= Atm()

print(pnb.check_bal())