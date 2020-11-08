import random as rd
import time as  ti 


class Single:
    def __init__(self):
        self.com_score = 0
        self.my = 0
        self.myscore = 0
        #vs 2
        self.player1_name = None
        self.player2_name = None
        self.player1 = 0
        self.player2 = 0
        self.player1_sco = 0
        self.player2_sco = 0

    def start(self):
        print("1.Odd\n2.Even")
        toss = input("> ")
        t = rd.randint(1, 2)
        if (toss == t):
            print("You won the Toss")
            self.myturn()
        else:
            print("Computer Won the Toss")
            self.Comturn()

    def myturn(self):
        self.check()
        print("-"*10)
        print("Your Chance")
        input("Enter a any key to rool: ")
        print("Dice is Rooling...")
        ti.sleep(5)
        self.my = rd.randint(1, 6)
        print("You Got => ",self.my)
        self.myscore += self.my
        print(f'Your score {self.myscore}/30')
        print("-"*10)
        if(self.my == 1 or self.my == 6):
            print("Again for you")
            self.myturn()
        else:
            self.Comturn()

    def Comturn(self):
        self.check()
        print("-"*10)
        print("Computer Chance")
        print("Dice is Rooling...")
        ti.sleep(5)
        self.com = rd.randint(1, 6)
        print("Computer Got => ",self.com)
        self.com_score += self.com
        print(f'Computer score {self.com_score}/30')
        print("-"*10)
        if(self.com == 1 or self.com == 6):
            print("Again for Computer")
            self.Comturn()
        else:
            self.myturn()
    
    def check(self):
        if (self.myscore >= 30):
            print("#"*20)
            print("You Won...")
            print("#"*20)
            self.deall()
            d = Double()
            d.menu()
        elif (self.com_score >= 30):
            print("#"*20)
            print("Computer Won\n Better luck Next Time...")
            print("#"*20)
            self.deall()
            d = Double()
            d.menu()
        
    def deall(self):
        self.com_score = 0
        self.myscore = 0
        self.player1_name = None
        self.player1_sco = 0
        self.player2_name = None
        self.player2_sco = 0

class Double(Single):
    
    def menu(self):
        print("First who get 30 Points Win")
        print("_"*15)
        print("\n1.Vs Computer\n2.vs Player2")
        print("_"*15)
        x = int(input("> "))
        if(x == 1):
            self.start()
        elif (x == 2):
            self.start2()
        else:
            print("Invalid option")
            self.menu()

    def start2(self):
        
        self.player1_name = input("Enter Player1 Name: ")
        self.player2_name = input("Enter Player2 Name: ")
        print(self.player1_name, "Choose your Options")
        print("1.Odd\n2.Even")
        toss = input("> ")
        t = rd.randint(1, 2)
        if (toss == t):
            print(self.player1_name, "won the Toss")
            self.play1()
        else:
            print(self.player2_name, "Won the Toss")
            self.play2()

    def play1(self):
        self.chec2()
        print("-"*10)
        print(self.player1_name, " Chance")
        input("Enter a any key to rool: ")
        print("Dice is Rooling...")
        ti.sleep(5)
        self.my = rd.randint(1, 6)
        print("You Got => ",self.my)
        self.player1_sco += self.my
        print(f'Your score {self.player1_sco}/30')
        print("-"*10)
        if(self.my == 1 or self.my == 6):
            print("Again for you")
            self.play1()
        else:
            self.play2()

    def play2(self):
        self.chec2()
        print("-"*10)
        print(self.player2_name, " Chance")
        input("Enter a any key to rool: ")
        print("Dice is Rooling...")
        ti.sleep(5)
        self.my = rd.randint(1, 6)
        print("You Got => ",self.my)
        self.player2_sco += self.my
        print(f'Your score {self.player2_sco}/30')
        print("-"*10)
        if(self.my == 1 or self.my == 6):
            print("Again for you")
            self.play2()
        else:
            self.play1()

    def chec2(self):
        if (self.player1_sco >= 30):
            print("#"*20)
            print(self.player1_name, " Won...")
            print("#"*20)
            self.deall()
            self.menu()
        elif (self.player2_sco >= 30):
            print("#"*20)
            print(self.player2_name," Won...")
            print("#"*20)
            self.deall()
            self.menu()

        

if __name__ == "__main__":
    d = Double()
    d.menu()
