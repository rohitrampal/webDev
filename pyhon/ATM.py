us=input("\t\t\t\t\t\t\tEnter your name:  ")
# print("\n")
# user=us.upper()
# print(f"\t\t\t\t\tNAMASKAARM  {user}:  ASMAAKAM  DIGITAL  ATM  MADHYE  SAWAGATAM\n\n")


bal=223344
chance=3
pin=9988
while chance>0:
    user_in=int(input("\t\t\t\tEnter your four digit PIN: "))
    if user_in==pin:

        print("\n")
        print("\t\t\t\t\t\t\tCHOOSE \tYOUR \tOPTION\n")
        user_inp=int(input('''\t\tFor Statement Press 1:  \n
        \tFor  Withdrwal  Press 2:  \n
        \tFor  Add Amount  Press 3:  \n
        \tFor  Quit  Press 4:  \n\t\t\t\t\t'''))

        if user_inp==1:
            print('''\n\n\t\t\tYour Current Balance is :  ''',bal) 
            print("\t\t\tThanks for using our bank, Have a good day\n")
            


        elif user_inp==2:
            print('''\n\n''')
            us3er=int(input('''\t\tEnter Withdrwal Amount:   '''))
            a=bal-us3er
            print(f'''\n\t\t{us3er} Rs has been depted from your account 
            \t Remaining balance is {a}
            \t If not done by you call help line no.
            \t 99009900999\n''')
            print("\t\t\tThanks for using our bank, Have a good day\n")
            
        
        elif user_inp==3:
            print('''\n\n''')
            us4er=int(input('''\t\tEnter Amount:  '''))

            print("\t\t\tYour updated Amount is :  ",bal+us4er)
            print("\t\t\tThanks for using our bank, Have a good day\n")
        
        else:
            break

    else:
        if chance>1:
            print(f"Invalid pin  {chance-1}  chances left")
        else:
            print("Try after 24 hr ,Your card is blocked temp.\n")
        chance-=1