import os
import random
import time
import colorama
from colorama import *
from pystyle import *


banner1 = r"""
         __                              ___   __        .ama     ,
      ,d888a                          ,d88888888888ba.  ,88"I)   d
     a88']8i                         a88".8"8)   `"8888:88  " _a8'
   .d8P' PP                        .d8P'.8  d)      "8:88:baad8P'
  ,d8P' ,ama,   .aa,  .ama.g ,mmm  d8P' 8  .8'        88):888P'
 ,d88' d8[ "8..a8"88 ,8I"88[ I88' d88   ]IaI"        d8[
 a88' ]P "bm8mP8'(8'.8I  8[      d88'    `"         .88
,88I ]P[  .I'.8     88' ,8' I[  ,88P ,ama    ,ama,  d8[  .ama.g
[88' I8, .I' ]8,  ,88B ,d8 aI   (88',88"8)  d8[ "8. 88 ,8I"88[
]88  `8888"  '8888" "88P"8m"    I88 88[ 8[ ]P "bm8m88[.8I  8[
]88,          _,,aaaaaa,_       I88 8"  8 ]P[  .I' 88 88' ,8' I[
`888a,.  ,aadd88888888888bma.   )88,  ,]I I8, .I' )88a8B ,d8 aI
  "888888PP"'        `8""""""8   "888PP'  `8888"  `88P"88P"8m"

             Normand                        Veilleux
"""
Anime.Fade(Center.Center(banner1), Colors.blue_to_cyan, Colorate.Vertical, interval=0.01, enter=True)

banner = """ 
    
         ██████╗ ██╗   ██╗███████╗███████╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
        ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
        ██║  ███╗██║   ██║█████╗  ███████╗███████╗    ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
        ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
        ╚██████╔╝╚██████╔╝███████╗███████║███████║    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
         ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ V1
                                                                                                    
                                         ENTER YOU DIFFICULTY :                                                                                         
                         ╔═══════════════════════════════════════════════════════════╗
                         [1] EASY
                         [2] MEDIUM
                         [3] HARD
                         ╚═══════════════════════════════════════════════════════════╝



"""

banner = Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(banner))

print(banner)
price = random.randint(1, 300)
essai = 0

level = Write.Input("[.] your choice : ", Colors.blue_to_cyan, interval=0.0001)


if level == "1":
    time.sleep(1)
    choix = Write.Print("[.] you have 50 try", Colors.blue_to_cyan, interval=0.0001)
    essai = 50

if level == "2":
    time.sleep(1)
    choix = Write.Print("[.] you have 20 try", Colors.blue_to_cyan, interval=0.0001)
    essai = 20

if level == "3":
    time.sleep(1)
    choix = Write.Print("[.] you have 10 try", Colors.blue_to_cyan, interval=0.0001)
    essai = 10

#banner2 ="""

#[.]collecting data :
#[.]acces to proxy :
#[.][----------------------------]
#[.]redirecting to the game :
#[.]redirecting to the game :
#[.] press enter to start :
#"""
#print(banner2)
#time.sleep(3)
#data = Write.Print("        [.]collecting data :", Colors.blue_to_cyan, interval=0.0001)
#data = Write.Print("        [.]acces to proxy : ", Colors.blue_to_cyan, interval=0.0001)
#choice = Write.Print("      [.][----------------------------]", Colors.blue_to_cyan, interval=0.0001)
#red = Write.Print("         [.]redirecting to the game :", Colors.blue_to_cyan, interval=0.0001)
#sd = Write.Input("          [.] press enter to start : ", Colors.blue_to_cyan, interval=0.0001)

banner3 = """
[.] collecting data :
[.] acces to proxy : "
[.][----------------------------]
[.] redirecting to the game :
[.] press enter to start :
"""
#banner = Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)),(banner))
banner3 = Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)),(banner3))

#banner3= Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(banner3))

print(banner3)
time.sleep(2)
sd = Write.Input("[.] press enter to start : ", Colors.blue_to_cyan, interval=0.0001)
#data = Write.Print("                                                                                                                                                                                                                             [.]collecting data :", Colors.blue_to_cyan, interval=0.0001)
#data = Write.Print("                                                                                                                                                                                                                            [.]acces to proxy : ", Colors.blue_to_cyan, interval=0.0001)
#choice = Write.Print("                                                                                                                                                                                                                            [.][----------------------------]", Colors.blue_to_cyan, interval=0.0001)
#red = Write.Print("                                                                                                                                                                                                               [.]redirecting to the game :", Colors.blue_to_cyan, interval=0.0001)
#sd = Write.Input("                                                                                                                                                                                                                     [.] press enter to start : ", Colors.blue_to_cyan, interval=0.0001)

os.system('cls||clear')

for i in range(int(essai)):
    answer = int(input("[.] guess the price : "))

    if answer == price:

        essai = essai - 1
        print("[.] you gess right ! ")
        print("[.] you did it with ", essai, " try remain" )
        time.sleep(3)
        os.system('cls||clear')

    if answer < price:

        essai = essai - 1
        print("[.] higher")
        print("[.] try remain :", essai)

    elif answer > price:

        essai = essai - 1
        print("[.] lower")
        print("[.] try remain :", essai )
