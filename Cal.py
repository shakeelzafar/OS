def add(n, n2):
        return n + n2
def sub(n, n2):
        return n - n2
def mul(n, n2):
        return n * n2
def div(n, n2):
        return n / n2

def main():        
        b = True
        while b == True:
                oper = input("What you want to do ? (+,-,*,/): ")
                if(oper != '+' and oper != '-' and oper != '*' and oper != '/'):
                        print("You Entered a wrong operator.\n")
                         
                else:
                        v1 = int(input("Enter Number 1: "))
                        v2 = int(input("Enter Number 2: "))
                        if(oper=='+'):
                                print(add(v1,v2))
                        elif(oper=='-'):
                                print(sub(v1,v2))
                        elif(oper=='*'):
                                print(mul(v1,v2))
                        elif(oper=='/'):
                                print(div(v1,v2))
                check = input("Exit Calculator, Y/y : ")
                if(check=='Y' or check == 'y'):
                        b=False
                
                                

main()
