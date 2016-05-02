player1=input("Enter the name of Player 1 : ")
player2=input("Enter the name of Player 2 : ")
a=range(1,10)
def draw():
    print ("\n\t",a[0],"|",a[1],"|",a[2])
    print ("\t", "_________")
    print ("\n\t",a[3],"|",a[4],"|",a[5])
    print ("\t", "_________")
    print ("\n\t",a[6],"|",a[7],"|",a[8], "\n")
draw()	#Function Call
i=0
b=1
while i<9:
	if (a[0]=="O" and a[1]=="O" and a[2]=="O") or (a[3]=="O" and a[4]=="O" and a[5]=="O") or (a[6]=="O" and a[7]=="O" and a[8]=="O") or (a[0]=="O" and a[3]=="O" and a[6]=="O") or (a[1]=="O" and a[4]=="O" and a[7]=="O") or (a[2]=="O" and a[5]=="O" and a[8]=="O") or (a[0]=="O" and a[4]=="O" and a[8]=="O") or (a[2]=="O" and a[4]=="O" and a[6]=="O"):	#Condition Check for Player 1 Win
		import sys
		sys.exit ("Congratulations " + player1 + "! You won.") #For Exiting the Program
	else:
		if (a[0]=="X" and a[1]=="X" and a[2]=="X") or (a[3]=="X" and a[4]=="X" and a[5]=="X") or (a[6]=="X" and a[7]=="X" and a[8]=="X") or (a[0]=="X" and a[3]=="X" and a[6]=="X") or (a[1]=="X" and a[4]=="X" and a[7]=="X") or (a[2]=="X" and a[5]=="X" and a[8]=="X") or (a[0]=="X" and a[4]=="X" and a[8]=="X") or (a[2]=="X" and a[4]=="X" and a[6]=="X"):	#Condition Check for Player 2 Win
			import sys			
			sys.exit ("Congratulations " + player1 + "! You won.")
    		else:
                    if b==1:
                        print (player1 + "!")
                        x=input("It's your turn. Choose the box (1-9) : ")
                        if (a[x-1] != "O" and a[x-1] != "X"):	#Check if box isn't already filled
                            a[x-1]="O"
                            draw()
                            b=2
                            i+=1
                        else:
                            if b==2:
                                print (player2 + "!")
                                x=input("It's your turn. Choose the box (1-9) : ")
                                if (a[x-1] != "O" and a[x-1] != "X"):
                                    a[x-1]="X"
                                    draw()
                                    b=1
                                    i+=1
if i==9:		
	print ("It was a draw.")

