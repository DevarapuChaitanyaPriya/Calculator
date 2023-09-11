from calculation import add,sub,div,mul
import art 
import os
operations={"+":add,"-":sub,"*":mul,"/":div}
def calulator():
    print(art.logo)
    num1=float(input("What's the first number?: "))
    for i in operations:
        print(i)
    flag=True
    while(flag): 
        operation_symbol=input("Pick an operation: ")
        num2=float(input("What's the next number?: "))
        answer=operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_cal=input(f"Type 'y' to continue with {answer}, or type 'n' to start new calculation.: ").rstrip().lower()
        if(continue_cal=="y"):
            num1=answer
        else:
            flag=False
            os.system('clear')
            calulator()

calulator()

