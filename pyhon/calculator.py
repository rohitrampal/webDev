nme=input("Enter you name: ")
wel_co=print(f"Hi {nme} you are using a calculator\n ")
opt=input("Enter any operator : * ,+ ,- ,/ ,** ,// ,% \n")
n1=eval(input("Enter 1st no.: "))
n2=eval(input("Enter 2nd no.: "))

if opt=="*":
    print("Multiplication of ",n1,"and",n2," = ",n1*n2)
elif opt=="/":
    print("Division of ",n1,"and",n2," = ",n1/n2)
elif opt=="+":
    print("Addition of ",n1,"and",n2," = ",n1+n2)
elif opt=="-":
    print("Substraction of ",n1,"and",n2," = ",n1-n2)
elif opt=="**":
    print("Square  of ",n1,"and",n2," = ",n1**n2)
elif opt=="//":
    print("Floor division of ",n1,"and",n2," = ",n1//n2)
elif opt=="%":
    print("Modulus of ",n1,"and",n2," = ",n1%n2)
else:
    print("invalid operator")