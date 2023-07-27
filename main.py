import os
import keyboard
import random
#os.system('mode con: cols=150 lines=100')
os.system('cls')
import time
gameover = """
xxxxxxxxxxxxxxxxxxxxxxxxxxxxkkxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkxxkkkkkkkxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxkkxxxxxxxxxxxxxxxxxxkkxxxkxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkkkkkkxxkkkkxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxddoooooddxxxxxkxxxxxxxxxxxxxxxkxxxxxxxxxkkxxxxxxxxxddolllllodxxkkk
xxxxxxxdol:;,,,;:codxxkkkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdl:;''.',;codxxk
xxxxxxxol;'......':ldxxxxxkkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdo:,..   ..,coxxx
xxxxxxdl:'.      .':oxxxxxxkkkxxxxxxxxxxxxxxxxxxxxkxxxxxxddo:..     ..:ldxx
xxxxxxdo:'.      ..:odxxkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdoc,..   ..,:odxx         GAME OVER
xxxxxxxdl;'..  ..';coxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdoc;,'.',;codxxx
xxxxxxxxdoc;,'',;cldxxxxddddddddddddddddddddddddddddddddddxxddolccllddxxxxx
xxxxxxxxxddollloodxxxxdolc::::::::::::::::::::::::::::::cclddddddddxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxdoc:,'''......................'''''',:lddxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxdolc;,,,',,,,,,,,,,,,,,,,,,,,,,,,,,,;codxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxddooolllllllllllooooooooollllllloooddxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkxxxxxxxxxx

"""
potato = """
                      WNXXNW                      
              WNNW  WKd,'';xN  WNW                
             WO:cOXKd,..  .c0X0oo0W               
             Wk. ..'..:o:....''.'xW               
             WO,  .:ox0KOdo;,,,..xW               
              Xd,.,xKX0O0KKKk;..;OW               
              WNd.,xOxc,cdkKO:.oKW                
               Wx..:c;''',;oo'.dN                 
               WO;..,ll:ldo;..:OW                      WELCOME TO THE POTATO'S KING HEADS OR TAILS GAME :
              WXkc. .,:c:;,..;oxON                	    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _			
            WNOl,'....'''''..',';lON              
            Xd:,,codddddxxxxxxddl;;o0N    XOxkkxxx						
          NOl;;codxxxxxxxxxxxkkxxdl';OW Xko::lc,. 
        Nkl,,codxxkkxxxxxxxxkkkkkkd:;lkXO;,oOK0d, 
        0;.;loddxxkkxxxxxxxxkkkOOOOko;;cooccoxo::c
       W0,.:oodxxxxxxxkxkkkxxkkOOOOkxo;.;Ok'....lX
      Nkc,,coddxxxxxxxxxkkkxxkkkkkkkxd:.;0Kd,..lOW				 
      K;.,loddxxl:cdxxxxxxxxkkdc:lxkkxc.,0 Nd.:K  					PRESS ANY BUTTON TO START
      0;.;lodxxxoccdxxxxxxxxxxdccoxxkxc.,0 Wd.:K  				 	_ _ _ _ _ _ _ _ _ _ _ _▒
    NOc..;oodxxxxxl;','''''''';lxkxxkxc.,OWNd.:K  
   WK:. .;llodxxxxoc::::::::::coxxxxkxc..,d0o.:K  			
  Nx;.  .;llcloxxxxxkkkxkkkxxkkxxxxxkxc.  .'..:K  
  K:.:l'.;oolloxxxxxxxxxxxxxxxxxxxxxkxl.'lc.  :K  
  Xc,x0:.;lolcldxxxxxxxxxxxxxxxxxxxxkxc.;0k'  :X  
  WK0NKc.,clc:coxxxxxxxxxxxxxxxxxxxxxd:':0NOc.:K  
      WKkc;:ccldxddxxxxxxxdoodxxxxkxl,,dKW Wd.:K  
        WXkc;;coooodxxkxxxdoodxkxxdl:':0   Wd.:K  
          WXx,.,;:clooooodooooollc;,:kXW   Wd.:K  
            0:. .',;;::::c::;;,...:xXW     Wd.:K  
            WXo.,kXXXXXXXXXXXXk,.oKW       Wd.:K  
             Wk';0            K;.xW        Nd.:K  
             W0coX            XocOW        WkcdX  
              WNNW            WWNW          WNW   
"""
potato_game ="""

                                                        .xXXKkOXNXx:.
                                                        .dOko;;d0Xx:.
                                                        .cc'.'''cko,.
                                                          'oo;;dc..
                                                          .;ldoc.
                                                       ......''.........
                                                      .clooodddddddddoo:.
                                                   ..:lddxxxxxxxxkxxxxxdl;.
                                                 .'clodxxkxxxxxkxxkkkkkkkl'.
                                                .;looxxxkkxxxxxkkkkkkOOOOkd;.
                                                .coodxxxxxxxxxxkkkkkkkOOOOkoc,
                                                .loddxxxxxxxxxkxxkkxkkOOOOkxd:.
                                              .'coddxxdooxkxxxxxxkxxxxodxkxxxc.
                                              .:oodxxxc.,oxxkkxxxxxxxl.'lxxxxl.
                                              .:oodxxxdllooooooooooooolodxxxkl.
                                              .:oodxxxxxo;''''''''''':dkxxxxxl.
                           .''.....           .:lcodxxxxxdddddddddddddxxxxxxkl.         .. ....
                     ..,odxOKXKOOOkxd:.       .:lccloxxxxxxxxxxxxxxxxxxxxxxxxl.    .,lloddxkOOxolc'.
               .,clooxkOK0OKXNXK0KNNNXOo,     .:oooodxxxxxxxxxxxxxxxxxxxxxxxxl. .;okKNNNKKXNNNXKKKOxolc:;'..
              .;odolcc::cld▒▒000O▒▒NNNX0o.    .:llccldxxxxxxxxxxxxxxxxxxxxxxxl. :OXNN▒▒▒▒▒▒▒▒0Oxoollodddxdo:.
               .....    .lx▒▒00OO▒▒0XXKOl.    .;clc;coxxxxxxxxxxxxxxxxxxxxxxd:. :kKXNXK0▒▒k000Oxl'.  .....'.
                       .;x0▒▒▒▒▒▒▒▒OKKOo'      .,cccldxddxxxxxxxdlodxxxxxxxc..  'oO0K0Ok▒▒d0KK0Od;.
                      .;k0K▒▒0xdd▒▒XX0o'.        .';coolodxxxxxxdlodxxxxxdl'     'lOKXKO▒▒kO0KXX0k:.
                    .;dOOxO▒▒KOO0▒▒kkx;            ..,:cloddddddddddddooc,.       'okO0O▒▒xk0KX0kOOd:.
                 .,lx0KOoo0NX0k0Kx:'',.               .......''''........         .;;;:lOKOk0KX0doOXKxl,.
                'd0KOdc:o0KOxkddd;.                  ..               ...           ....lxddkO0K0ocldk00x:.
                'odc,;cx0Oo;.'....                   ..               .'.              ..,.';,:d0Oxl:;cxOo.
                 ..  .cdc'.                          ..               ...                      .;okkc.....
                                                                       .                          ...                                                                                                                                                  
"""
parols = ["Wouldn't reccomend :')","That's a virgin's choice","That's why you have no bitches","Know That if you can't pay you will become a potato"]
class player:
    def __init__(self,name,balance=1000):
        self.name = name
        self.balance = balance
        self.bets = 0
        self.wins = 0
    def bet(self,amount, choice):
        if self.balance>=amount:
            self.bets+=1
            bet = random.choice(['Heads','Tails'])
            print(f"You are betting {amount} on {choice}!")
            time.sleep(0.7)
            print(random.choice(parols))

            time.sleep(1)
            print("Here are the results")
            time.sleep(0.6)
            print(3)
            time.sleep(0.6)
            print(2)
            time.sleep(0.6)
            print(1)
            time.sleep(1)
            if choice[0].lower()==bet[0].lower():

                print("You won! The Potato King Is proud of you")
                self.balance += amount
                self.wins += 1
            else :
                print("You lost! The Potato King Is not proud of you")
                self.balance -= amount

            time.sleep(1)

        print(f"""{self.name}:
Your balance is {self.balance} lalatina points
Your winrate is at {self.wins/self.bets*100}%""")
        time.sleep(2)

def main():
    print(potato)
    while True:
        k=keyboard.read_key()
        if k!="":
            break
    os.system('cls')
    print("Welcome to the Potato King's Casino!")
    time.sleep(1)
    print("Give me your name foolish human")
    name = input()
    p1 = player(name)
    time.sleep(0.6)
    print('The generous Potato King have bestowed you 1000 Lalatina Points Bet carefully')
    time.sleep(1)
    while p1.balance>0:
        print(potato_game)
        while True:
            print("How much do you want to bet?")
            try:
                amount = int(input())
                if amount<=p1.balance:
                    break
                else:
                    print("You don't have enough money to bet that much!")
                    time.sleep(0.5)
                    print("Sigh use your braincells", end="")
                    time.sleep(0.5)
                    print(".", end="")
                    time.sleep(0.5)
                    print(".", end="")
                    time.sleep(0.5)
                    print(".")
            except:
                print("That's not a number you fool")
                time.sleep(1)
        os.system('cls')
        while True:
            print(potato_game)
            choice = input("Choose Heads Or Tails !\n")
            if choice in ["Heads","Tails","H","T","h","t"]:
                break
            else:
                os.system('cls')
                print("That's not a valid choice you fool type something within 'Heads','Tails','H','T','h','t'")
                time.sleep(1)
        time.sleep(0.1)
        os.system('cls')
        p1.bet(amount,choice)
    time.sleep(0.5)
    print(gameover)
    time.sleep(1)
    exit()
main()