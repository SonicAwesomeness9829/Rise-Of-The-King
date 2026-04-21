import os
import shutil
import sys
from Data import Kingdom_Properties
from Data import Kingdom_Assets
from Data import Kingdom_Inhabitants
from Data import ENEMY
from Data import The_Devil
from Data import kingdom
from Data import Castle
from Data import Reputation
from Data import peacekingdoms
from Data import name
from Data import Game
from Data import Days
from Data import HELL

FINALBOSS = False
MaximumTroopPower = 15
Freedom = False
Genocide = False
import random
import time
BlackKnightCutscene = 1
Hull_Hp = 5
BlackKnight = False
BlackKnightHp = 10
InvasionChance = 2
LOVE = {
    "LOVE": 0
} # Get this to 16, that would be GREAT
Victory = False
# Fall of the King
GreatKnightsAvailable = ["Sir Levi", "Sir Galaban", "Sir Olgrim", "Sir Fredrick", "Sir Tony"]
upgradevalue = 1000000
Tax_Countdown = 30
Lucius = r'''
                            ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'
'''
Hell = False
King_Power = 30
Great_Knights = []
InvadePower = {
    "Julian": 5,
    "Crystalia": 3,
    "Verdania": 3,
}
TribesAndKingdoms = {
    "Grados": "Powerful",
    "Verdania": "Powerful",
    "Crystalia": "Powerful",
    "Hayden": "Powerful",
    "Hell Portal": "GODLIKE",
    "Julian": "Hyper Powerful",
    "Total Population": 23_043_256,
    "GradosPower": 2,
    "VerdaniaPower": 5,
    "HaydenPower": 1,
    "CrystaliaPower": 4,
    "JulianPower": 7
} #01000100 01100101 01110110 01101001 01101100
Settings = {
    "Peasants": False
}


def trigger_genocide_deletion():
    print("The world has been erased...")


    current_dir = os.path.dirname(os.path.abspath(__file__))

    try:

        files_to_delete = ["main.py", "War.py", "Data.py"]
        for file in files_to_delete:
            file_path = os.path.join(current_dir, file)
            if os.path.exists(file_path):
                os.remove(file_path)


    except Exception as e:
        print(f"Error during erasure: {e}")

    sys.exit()
def TRUE_FINAL_BOSS():
    global FINALBOSS
    print("ENOUGH!")
    print("I AM TIRED OF THIS...")
    time.sleep(2)
    print("YOU...")
    time.sleep(1)
    print("DIE...")
    time.sleep(1)
    print("TODAY!")
    for i in range(10000):
        print("""
            W̵̯̮̣͍̤͕͇̼͉̦̗͓̬̃̉̌͑̐̚͝ ̷̢̨̡̨̯̰͎̬̰̖͎͕̜̻̬̓̓͛̇̃̀͘͝E̴̢͚̫͙͗̽̆ ̸̧̢̰͉̫̪̮̭͚͚̯̔̓̓͆̃̿̈͛͗̊̊͛͋̉͜ͅͅL̸̢͚̙̬͔͙͔͍̰̪͈̤̈́̉͋͌͜͠ ̸̡̲̥̹͍͋̎̒̆̓̈́͗̑̕͠C̸̯̪̹̬̮̞̞̹̥͕̰̰̭͋ͅ ̶̧̳̻̘̱̠͇̞̙̰̞̟̆̊̑̀̀͊Ǫ̵̛̻̼͍̪͔͖̲̮͈̲͓̀͐͗̈̒͒̌̅͛̐̚͜͝ ̷͔̳̇́́̊̄͑͛̆M̷̢̛̽̑͐̽̏̅̓͛̚͝ ̵̢̡̠͉̫̜̯̞̼̗̀̍̔̽̒̑͋̅͜͝Ȩ̵̥̪̭̤̜͔̳̣͍̤͍͙͎̈́̃̌̀̀ ̵̠̝̲̟̊̆͌͊͌̔̋̓́̆͊̾̒̑̚ ̶̬̠̤̹̗̻͒́̅͐͠T̶͔͇͛̄̔̑̾͌̔́́͠ ̶̗͙̄̅̇͗̈́̀O̵̧̡̙͕̠̱̱̥̣͈̼̖̅ ̵̯̑͛ ̷̡̛̬̱͖͉͚͂̋̅͝Ḩ̸̫̝̤̱͎̖͈̂́̅̂̔̄͘ ̸̨̨̘̰͓̭͉͈͔͖͍̋́͊É̶̡̨̨̟͔̤̣͓̟̻̙́͗̔͗̐͗ ̸͚͕͉̙̞̈̿͐͊̄̀̈́͗̇̈́̑̚͝͠L̷̬͔̲̟̺̺̼̿̍͆̌̋̄̊̑̆̑̋̈͝ ̸̨̛̖͇͔̹̫̻͈̪̭̠̼̩͒̽͛̒̀͆̽̔̚͝͝Ļ̴̘̺͉̭̭̮̗͂̋̽͂̋̒̍̓͑͊̅͘͝ͅͅ
            W̵̯̮̣͍̤͕͇̼͉̦̗͓̬̃̉̌͑̐̚͝ ̷̢̨̡̨̯̰͎̬̰̖͎͕̜̻̬̓̓͛̇̃̀͘͝E̴̢͚̫͙͗̽̆ ̸̧̢̰͉̫̪̮̭͚͚̯̔̓̓͆̃̿̈͛͗̊̊͛͋̉͜ͅͅL̸̢͚̙̬͔͙͔͍̰̪͈̤̈́̉͋͌͜͠ ̸̡̲̥̹͍͋̎̒̆̓̈́͗̑̕͠C̸̯̪̹̬̮̞̞̹̥͕̰̰̭͋ͅ ̶̧̳̻̘̱̠͇̞̙̰̞̟̆̊̑̀̀͊Ǫ̵̛̻̼͍̪͔͖̲̮͈̲͓̀͐͗̈̒͒̌̅͛̐̚͜͝ ̷͔̳̇́́̊̄͑͛̆M̷̢̛̽̑͐̽̏̅̓͛̚͝ ̵̢̡̠͉̫̜̯̞̼̗̀̍̔̽̒̑͋̅͜͝Ȩ̵̥̪̭̤̜͔̳̣͍̤͍͙͎̈́̃̌̀̀ ̵̠̝̲̟̊̆͌͊͌̔̋̓́̆͊̾̒̑̚ ̶̬̠̤̹̗̻͒́̅͐͠T̶͔͇͛̄̔̑̾͌̔́́͠ ̶̗͙̄̅̇͗̈́̀O̵̧̡̙͕̠̱̱̥̣͈̼̖̅ ̵̯̑͛ ̷̡̛̬̱͖͉͚͂̋̅͝Ḩ̸̫̝̤̱͎̖͈̂́̅̂̔̄͘ ̸̨̨̘̰͓̭͉͈͔͖͍̋́͊É̶̡̨̨̟͔̤̣͓̟̻̙́͗̔͗̐͗ ̸͚͕͉̙̞̈̿͐͊̄̀̈́͗̇̈́̑̚͝͠L̷̬͔̲̟̺̺̼̿̍͆̌̋̄̊̑̆̑̋̈͝ ̸̨̛̖͇͔̹̫̻͈̪̭̠̼̩͒̽͛̒̀͆̽̔̚͝͝Ļ̴̘̺͉̭̭̮̗͂̋̽͂̋̒̍̓͑͊̅͘͝ͅͅ
            W̵̯̮̣͍̤͕͇̼͉̦̗͓̬̃̉̌͑̐̚͝ ̷̢̨̡̨̯̰͎̬̰̖͎͕̜̻̬̓̓͛̇̃̀͘͝E̴̢͚̫͙͗̽̆ ̸̧̢̰͉̫̪̮̭͚͚̯̔̓̓͆̃̿̈͛͗̊̊͛͋̉͜ͅͅL̸̢͚̙̬͔͙͔͍̰̪͈̤̈́̉͋͌͜͠ ̸̡̲̥̹͍͋̎̒̆̓̈́͗̑̕͠C̸̯̪̹̬̮̞̞̹̥͕̰̰̭͋ͅ ̶̧̳̻̘̱̠͇̞̙̰̞̟̆̊̑̀̀͊Ǫ̵̛̻̼͍̪͔͖̲̮͈̲͓̀͐͗̈̒͒̌̅͛̐̚͜͝ ̷͔̳̇́́̊̄͑͛̆M̷̢̛̽̑͐̽̏̅̓͛̚͝ ̵̢̡̠͉̫̜̯̞̼̗̀̍̔̽̒̑͋̅͜͝Ȩ̵̥̪̭̤̜͔̳̣͍̤͍͙͎̈́̃̌̀̀ ̵̠̝̲̟̊̆͌͊͌̔̋̓́̆͊̾̒̑̚ ̶̬̠̤̹̗̻͒́̅͐͠T̶͔͇͛̄̔̑̾͌̔́́͠ ̶̗͙̄̅̇͗̈́̀O̵̧̡̙͕̠̱̱̥̣͈̼̖̅ ̵̯̑͛ ̷̡̛̬̱͖͉͚͂̋̅͝Ḩ̸̫̝̤̱͎̖͈̂́̅̂̔̄͘ ̸̨̨̘̰͓̭͉͈͔͖͍̋́͊É̶̡̨̨̟͔̤̣͓̟̻̙́͗̔͗̐͗ ̸͚͕͉̙̞̈̿͐͊̄̀̈́͗̇̈́̑̚͝͠L̷̬͔̲̟̺̺̼̿̍͆̌̋̄̊̑̆̑̋̈͝ ̸̨̛̖͇͔̹̫̻͈̪̭̠̼̩͒̽͛̒̀͆̽̔̚͝͝Ļ̴̘̺͉̭̭̮̗͂̋̽͂̋̒̍̓͑͊̅͘͝ͅͅ
            """)
    FINALBOSS = True
    ENEMY['Group'] = "THE ARMY OF HELL"
    ENEMY["Amount"] = 1000000
    ENEMY["Power"] = 20
    WAR(False)
def BlackKnightEvent():
    global BlackKnightCutscene
    if TribesAndKingdoms["Grados"] != "EXTINCT" and TribesAndKingdoms["Verdania"] != "EXTINCT" and \
            TribesAndKingdoms["Hayden"] != "EXTINCT" and TribesAndKingdoms["Crystalia"] != "EXTINCT":
            if Days["Days"] > 1000:
                if BlackKnightCutscene == 1:
                    time.sleep(5)
                    print("You get a letter...")
                    time.sleep(2)
                    print("Inside it says")
                    time.sleep(1)
                    print("""
                        I am always watching... be careful
                        """)
                    time.sleep(3)
                    print("Outside you see someone floating in the air...")
                    time.sleep(2)
                    print(r"""
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣀⣸⣄⠀⠀⠠⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣦⡏⠈⢀⣴⣄⣁⣽⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⢀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⡧⣤⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠉⢷⣶⣦⣤⣤⣝⣯⣝⢫⣾⣷⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⢀⣤⣮⣿⡿⢿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⢀⣴⠿⠋⠉⠀⠀⢼⣍⣭⣟⠋⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣴⠶⣿⡇⠀⠀⠀⠀⠀⣰⣿⢿⣿⡓⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⢻⣶⣿⠰⠆⠀⠀⠀⣴⣿⠃⢸⣿⠀⠀⠠⣼⢿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀⢸⡟⠀⠀⠀⠀⠈⠯⣾⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣀⣼⡇⠀⠀⠀⠀⠀⠀⠘⢿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣦⣀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣛⠿⣿⣦⣀
                        """)
                    time.sleep(5)
                    for i in range(100):
                        print(" ")
                    print("He is now gone")
                    BlackKnightCutscene = 2
            if Days["Days"] > 5000:
                if BlackKnightCutscene == 2:
                    time.sleep(5)
                    print("You feel as the wind blows against you....")
                    time.sleep(2)
                    print("You get a letter... inside it says")
                    time.sleep(1)
                    print("""
                                            GIVE UP AND DIE
                                            """)
                    time.sleep(3)
                    print("Outside you see someone floating in the air...")
                    time.sleep(2)
                    print(r"""
                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⣀⣸⣄⠀⠀⠠⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⣦⡏⠈⢀⣴⣄⣁⣽⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⢀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⡧⣤⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠉⢷⣶⣦⣤⣤⣝⣯⣝⢫⣾⣷⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⢀⣤⣮⣿⡿⢿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⢀⣴⠿⠋⠉⠀⠀⢼⣍⣭⣟⠋⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⣴⠶⣿⡇⠀⠀⠀⠀⠀⣰⣿⢿⣿⡓⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⢻⣶⣿⠰⠆⠀⠀⠀⣴⣿⠃⢸⣿⠀⠀⠠⣼⢿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀⢸⡟⠀⠀⠀⠀⠈⠯⣾⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣀⣼⡇⠀⠀⠀⠀⠀⠀⠘⢿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣦⣀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣛⠿⣿⣦⣀
                                            """)
                    time.sleep(5)
                    for i in range(100):
                        print(" ")
                    print("He's gone...")
                    time.sleep(5)
                    print("But they are not.")
                    BlackKnightCutscene = 3
                    ENEMY['Group'] = "Rag Demons"
                    ENEMY["Amount"] = 100 + ((Kingdom_Inhabitants["Troops"] - 100) + 5000)
                    ENEMY["Power"] = 1 + (Kingdom_Inhabitants["Power"] - 1)
                    specialattack()
                    WAR(True)
            if Days["Days"] > 9993:
                if BlackKnightCutscene == 3:
                    time.sleep(5)
                    print("It's a quiet night.")
                    time.sleep(3)
                    print("Outside you see someone floating in the air...")
                    time.sleep(2)
                    print(r"""
                                                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠀⣀⣸⣄⠀⠀⠠⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠀⣦⡏⠈⢀⣴⣄⣁⣽⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⢀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⡧⣤⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠉⢷⣶⣦⣤⣤⣝⣯⣝⢫⣾⣷⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⢀⣤⣮⣿⡿⢿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⢀⣴⠿⠋⠉⠀⠀⢼⣍⣭⣟⠋⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                            ⣴⠶⣿⡇⠀⠀⠀⠀⠀⣰⣿⢿⣿⡓⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                            ⢻⣶⣿⠰⠆⠀⠀⠀⣴⣿⠃⢸⣿⠀⠀⠠⣼⢿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀⢸⡟⠀⠀⠀⠀⠈⠯⣾⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣀⣼⡇⠀⠀⠀⠀⠀⠀⠘⢿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣦⣀⠀⠀⠀
                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣛⠿⣿⣦⣀
                                                        """)
                    time.sleep(2)
                    print("He lunges towards you.")
                    time.sleep(1)
                    print("""
                                            YOU HAVE 1 WEEK TO PREPARE, OR I WILL BURN YOUR KINGDOM TO THE GROUND
                                            """)

                    time.sleep(1)
                    for i in range(1000):
                        print(" ")
                    print("He vanished...")
                    BlackKnightCutscene = 4


def ClownOfMadness():
    global Freedom
    global MaximumTroopPower
    if Freedom == False:
        TranslationPlayer = "nothing"
        TranslationCPU = "nothing"
        CpuChoice = "Rock"
        MyScore = 0
        CpuScore = 0
        Rock = 1
        Paper = 1
        Scissors = 1
        PlayerLastChoice = "Nothing"
        Round = 1
        Win = False
        CurrentFrame = 1
        CPU_Brain = "Nothing"
        CPUHistory = 0
        CPULongHistory = 0
        Counter_Attack = 0
        Copy_Cat = 0
        Chaos_Ruler = 0
        time.sleep(5)
        print("You sailed to a cave...")
        time.sleep(5)
        print("Inside you see... A tiny clown")
        time.sleep(5)
        print("Welcome to my dungeon!")
        time.sleep(2)
        print("Or as I like to call it...")
        time.sleep(2)
        print("The place where I always win.")
        time.sleep(2)
        print("Let's play a simple numbers game, if you reach 20 I lose, if I reach 20 I win.")
        time.sleep(2)
        print("Hearts beat Spades, Spades beat Diamonds, and Diamonds beat Hearts.")

        def confused():
            nonlocal CpuChoice, CPUHistory, Win, Rock, Paper, Scissors, PlayerLastChoice
            CHAOS = random.randint(1, 2)
            if CHAOS == 1:
                RockChance = random.randint(1, Rock)
                PaperChance = random.randint(1, Paper)
                ScissorsChance = random.randint(1, Scissors)
                if ScissorsChance > RockChance and ScissorsChance > PaperChance:
                    CpuChoice = "Rock"
                elif RockChance > ScissorsChance and RockChance > PaperChance:
                    CpuChoice = "Paper"
                elif PaperChance > ScissorsChance and RockChance < PaperChance:
                    CpuChoice = "Scissors"
                else:
                    if Win == False:
                        if PlayerLastChoice == "Rock":
                            CpuChoice = "Rock"
                        elif PlayerLastChoice == "Paper":
                            CpuChoice = "Paper"
                        elif PlayerLastChoice == "Scissors":
                            CpuChoice = "Scissors"
                    else:
                        CPUHistory = 1
                        if Win == True:
                            if PlayerLastChoice == "Rock":
                                CpuChoice = "Paper"
                            elif PlayerLastChoice == "Paper":
                                CpuChoice = "Scissors"
                            elif PlayerLastChoice == "Scissors":
                                CpuChoice = "Rock"
                            else:
                                CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                        else:
                            print("Don't be a fool!")
                            CHAOS2 = random.randint(1, 3)
                            if CHAOS2 == 1:
                                CPUHistory = 1
                                if Win == True:
                                    if PlayerLastChoice == "Rock":
                                        CpuChoice = "Paper"
                                    elif PlayerLastChoice == "Paper":
                                        CpuChoice = "Scissors"
                                    elif PlayerLastChoice == "Scissors":
                                        CpuChoice = "Rock"
                                    else:
                                        CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                                else:
                                    CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                            elif CHAOS2 == 2:
                                CPUHistory = 2
                                if Win == False:
                                    if PlayerLastChoice == "Rock":
                                        CpuChoice = "Scissors"
                                    elif PlayerLastChoice == "Paper":
                                        CpuChoice = "Rock"
                                    elif PlayerLastChoice == "Scissors":
                                        CpuChoice = "Paper"
                                else:
                                    CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                                    if CpuChoice == PlayerLastChoice:
                                        CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                            elif CHAOS2 == 3:
                                CPUHistory = 3
                                if Win == False:
                                    while CpuChoice == PlayerLastChoice:
                                        CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                                else:
                                    CpuChoice = random.choice(["Rock", "Paper", "Scissors"])


            else:
                CHAOS2 = random.randint(1, 3)
                if CHAOS2 == 1:
                    CPUHistory = 1
                    if Win == True:
                        if PlayerLastChoice == "Rock":
                            CpuChoice = "Paper"
                        elif PlayerLastChoice == "Paper":
                            CpuChoice = "Scissors"
                        elif PlayerLastChoice == "Scissors":
                            CpuChoice = "Rock"
                        else:
                            CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                    else:
                        CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                elif CHAOS2 == 2:
                    CPUHistory = 2
                    if Win == False:
                        if PlayerLastChoice == "Rock":
                            CpuChoice = "Scissors"
                        elif PlayerLastChoice == "Paper":
                            CpuChoice = "Rock"
                        elif PlayerLastChoice == "Scissors":
                            CpuChoice = "Paper"
                    else:
                        CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                        if CpuChoice == PlayerLastChoice:
                            CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                elif CHAOS2 == 3:
                    CPUHistory = 3
                    if Win == False:
                        while CpuChoice == PlayerLastChoice:
                            CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                    else:
                        CpuChoice = random.choice(["Rock", "Paper", "Scissors"])

        while True:
            if Round > 1:
                if CPULongHistory > 0:
                    if Counter_Attack > Copy_Cat and Counter_Attack > Chaos_Ruler:
                        CPUHistory = 1
                        if Win == True:
                            if PlayerLastChoice == "Rock":
                                CpuChoice = "Paper"
                            elif PlayerLastChoice == "Paper":
                                CpuChoice = "Scissors"
                            elif PlayerLastChoice == "Scissors":
                                CpuChoice = "Rock"
                            else:
                                CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                        else:
                            CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                    elif Counter_Attack < Copy_Cat and Copy_Cat > Chaos_Ruler:
                        CPUHistory = 2
                        if Win == False:
                            if PlayerLastChoice == "Rock":
                                CpuChoice = "Scissors"
                            elif PlayerLastChoice == "Paper":
                                CpuChoice = "Rock"
                            elif PlayerLastChoice == "Scissors":
                                CpuChoice = "Paper"
                        else:
                            CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                            if CpuChoice == PlayerLastChoice:
                                CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                    elif Chaos_Ruler > Copy_Cat and Counter_Attack < Chaos_Ruler:
                        CPUHistory = 3
                        if Win == False:
                            while CpuChoice == PlayerLastChoice:
                                CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                        else:
                            CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
                    else:
                        confused()
                else:
                    confused()
            else:
                CpuChoice = random.choice(["Rock", "Paper", "Scissors"])
            if CurrentFrame == 1:
                CurrentFrame = 2
                print('''
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣶⣷⣾⣶⣀⠀⣀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣿⣿⡿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣼⣿⣿⠛⣷⣿⣟⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣏⣽⠿⠉⠀⠉⢿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡋⠀⠀⠀⣶⣾⣿⢛⡟⡻⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⣿⡟⣳⣶⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣬⣿⡿⣿⡦⢍⡲⢱⢢⣿⣷⣎⠼⣿⣿⣿⡿⢿⣹⣿⠀⠀⠻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠯⣴⣿⣿⣿⣼⢹⣿⣿⣿⣿⣿⠲⣿⣿⣟⣦⣾⢿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⣿⣿⡇⣟⣿⣟⡛⢯⡉⢟⣿⣟⣦⣱⣿⡜⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣿⡟⢴⣭⢦⣹⣼⡎⢿⣿⣿⡱⣼⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣈⣭⠿⣯⡝⣻⢿⣿⣩⣿⣿⣿⠿⣹⣼⣿⣿⣏⣉⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣛⣟⠃⣿⣿⣇⣞⣻⣿⣻⣟⣿⢾⣿⣿⣛⡛⣿⣿⣛⣻⣷⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣤⣤⣄⣤⠀⠀⠀⢠⣤⣄⡀⣄⣿⣿⣿⣿⣆⣿⡏⢹⣿⣿⣿⣿⣿⣯⣈⣉⣩⣿⣇⣿⣿⡿⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣶⣾⣿⣿⣿⣿⣷⡆⣴⣾⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠛⢻⣿⣿⣾⣻⢿⣿⣿⡿⣿⣿⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤
⠀⠈⠹⠿⢿⣿⣿⣷⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠈⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⠙⠛⠛⢛⣿⣿⣿⡟⠛⠛⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠻⠟⠃⠘⢻⣿⣿⣿⡾⣿⣿⣿⣿⣿⣯⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡄⠀⠀⠠⣿⣿⣿⡗⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠇⢠⣴⣿⣿⣿⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠏⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣾⣿⣿⣿⠏⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⢻⣿⣿⣿⣿⠇⢸⣿⣿⣿⣤⡄⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣼⠿⢿⡹⣿⡃⢼⣿⡹⠿⢿⠿⣧⣤⣬⣭⣭⣭⡍⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠛⠛⠛⠛⠛⣻⣿⣷⣿⣿⡅⣺⣿⣿⣿⣿⣿⡟⠛⠛⠛⠛⠛⣷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣴⣷⣾⣶⣷⡟⠛⠛⠛⠛⠃⠘⠛⠛⠛⣿⣿⣧⣾⣶⣷⣾⣶⡟⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
            elif CurrentFrame == 2:
                CurrentFrame = 1
                print('''
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⣀⠀⣀⣶⣾⣷⣾⣶⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⡿⣿⣿⣿⣶⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣾⣟⣿⣷⠛⣿⣿⣼⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⢿⠉⠀⠉⠿⣽⣏⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣶⣳⡟⣿⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢿⡻⡟⢛⣿⣾⣶⠀⠀⠀⡋⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠻⠀⠀⣿⣹⢿⡿⣿⣿⣿⠼⣎⣷⣿⢢⢱⢲⡍⢦⣿⡿⣿⣬⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⢿⣾⣦⣟⣿⣿⠲⣿⣿⣿⣿⣿⢹⣼⣿⣿⣿⣴⠯⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣿⣿⣿⡜⣿⣱⣦⣟⣿⢟⡉ ⣛⣟⣿⣟⣇⣿⣿⢹⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣼⡱⣿⣿⢿⣎⣼⣹⢦⣭⢴⡟⣿⡇⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣏⣿⣿⣼⣹⠿⣿⣿⣿⣩⣿⢿⣻⡝⣯⠿⣭⣈⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⣷⣻⣛⣿⣿⡛⣛⣿⣿⣾⣿⣻⣟⣿⣻⣞⣇⣿⣿⠃⣟⣛⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⡿⣿⣿⣇⣿⣩⣉⣈⣯⣿⣿⣿⣿⣿⢹⡏⣿⣆⣿⣿⣿⣿⣄⢀⣄⣄⣤⠀⠀⠀⣄⣤⣤⣤⢠⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣷⣶⣾⣿⣶⣶⣷⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣾⣴⡆⣷⣿⣿⣿⣿⣾⣶
⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡿⣿⣿⠀⣿⣿⢿⣻⣾⣿⣿⢻⠛
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣷⣿⣿⢿⠿⠹⠁⠀
⠛⠛⠛⡟⣿⣿⣿⢛⠛⠛⠙⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⠛⠛⠛⠁⠀⠀⠀⠀
⠀⠀⠀⢗⣿⣿⣿⠠⠀⠀⢠⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣯⣿⣿⣿⣿⣿⡾⣿⣿⣿⢻⠘⠃⠟⠻⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡏⣿⣿⣿⣴⢠⠇⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠏⣿⣿⣿⣾⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⠏⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⢻⠘⠀⢠⣤⣿⣿⣿⢸⠇⣿⣿⣿⣿⢻⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⢍⣭⣭⣭⣬⣤⣧⠿⢿⠿⣹⣿⢃⣟⡹⢿⠿⣼⣤⣤⣤⣤⣤⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣷⠛⠛⠛⠛⠛⡟⣿⣿⣿⣿⣿⣺⢅⣿⣿⣷⣿⣻⠛⠛⠛⠛⠛⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃⡟⣶⣾⣷⣾⣶⣧⣿⣿⠛⠛⠛⠘⠃⠛⠛⠛⠛⡟⣶⣷⣾⣶⣴⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ''')

            print(Round, "🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏")
            Choice = input("What do you want? (1) ❤, (2) ♦, or (3) ♠?").capitalize()
            if Choice == "1":
                Choice = "Rock"
            elif Choice == "2":
                Choice = "Paper"
            elif Choice == "3":
                Choice = "Scissors"

            if Choice == "Rock" or Choice == "Paper" or Choice == "Scissors" or Choice == "Exit":
                if Choice != "Exit":
                    if Choice == "Rock":
                        Rock += 1
                    elif Choice == "Paper":
                        Paper += 1
                    elif Choice == "Scissors":
                        Scissors += 1
                    time.sleep(1)
                    print("Reality")
                    time.sleep(1)
                    print("Has")
                    time.sleep(1)
                    print("Lost...")
                    time.sleep(1)
                    print("Control!")
                    if Choice == "Rock":
                        TranslationPlayer = "❤"
                    elif Choice == "Paper":
                        TranslationPlayer = "♦"
                    elif Choice == "Scissors":
                        TranslationPlayer = "♠"

                    if CpuChoice == "Rock":
                        TranslationCPU = "❤"
                    elif CpuChoice == "Paper":
                        TranslationCPU = "♦"
                    elif CpuChoice == "Scissors":
                        TranslationCPU = "♠"

                    print("You chose:", TranslationPlayer)
                    print("Mad Jester chose:", TranslationCPU)
                    if Choice == CpuChoice:
                        print("It's a tie! ✨")
                        PlayerLastChoice = Choice
                        Win = None
                    elif Choice == "Rock" and CpuChoice == "Paper" or Choice == "Scissors" and CpuChoice == "Rock" or Choice == "Paper" and CpuChoice == "Scissors":
                        print("You lost! 🃏")
                        CpuScore += 1
                        PlayerLastChoice = Choice
                        Win = False
                        if CPUHistory == 1:
                            Counter_Attack += 1
                        elif CPUHistory == 2:
                            Copy_Cat += 1
                        elif CPUHistory == 3:
                            Chaos_Ruler += 1

                        CPULongHistory += 1
                        print(random.choice(
                            ["Your world's a fantasy!", "Reality is breaking", "I can do anything!", "Just be free!",
                             "None of this is real!", "In this game everyone will lose!",
                             "Don't you understand, freedom was taken from all of us!"]))

                    elif Choice == "Rock" and CpuChoice == "Scissors" or Choice == "Scissors" and CpuChoice == "Paper" or Choice == "Paper" and CpuChoice == "Rock":
                        print("You won! 👑")
                        MyScore += 1
                        PlayerLastChoice = Choice
                        Win = True
                        if CPUHistory == 1:
                            Counter_Attack -= 1
                        elif CPUHistory == 2:
                            Copy_Cat -= 1
                        elif CPUHistory == 3:
                            Chaos_Ruler -= 1
                        if CPULongHistory > 0:
                            CPULongHistory -= 1
                        print(random.choice(
                            ["This world is a lie!", "Where we made to die?", "I can do everything!",
                             "Hide in insanity!",
                             "CHAOS!", "Anything I do is no sin!",
                             "After you've seen what I have you realise it's better to just do whatever you want."]))

                    Round += 1
                    print("Your score:", MyScore)
                    print("Mad Jester score:", CpuScore)
                    if MyScore > 19:
                        time.sleep(5)
                        print("You...")
                        time.sleep(3)
                        print("Beat me...")
                        time.sleep(3)
                        print("Take your reward...")
                        time.sleep(3)
                        print("Maximum Troop Power is now 16!")
                        MaximumTroopPower = 16
                        Freedom = True
                        break
                    if CpuScore > 19:
                        print("I win. Come play again some time!")
                        break
                else:
                    break
            else:
                print("No, no! That's not a card!")
    else:
        print("The cave is gone...")


def build(Construct, Amount):
    if Kingdom_Assets["Land"] > 0:
        if Construct == "1":
            if HELL["HELL"] != True:
                if Kingdom_Assets["Wood"] >= 20 * Amount and Kingdom_Assets["Gold"] >= 10000 * Amount:
                    if Amount > Kingdom_Assets["Land"]:
                        print("You don't have enough land for that fool!")
                    else:
                        Kingdom_Assets["Wood"] -= 20 * Amount
                        Kingdom_Assets["Gold"] -= 10000 * Amount
                        Kingdom_Properties["Houses"] += Amount
                        Kingdom_Assets["Land"] -= Amount
                else:
                    print("Not enough resources for a house, pathetic.")
            else:
                print("Why do you need a house? We have all the power in the world.")

        elif Construct == "2":
            if HELL["HELL"] != True:
                if Kingdom_Assets["Wood"] >= 10 * Amount and Kingdom_Assets["Gold"] >= 50000 * Amount:
                    if Amount > Kingdom_Assets["Land"]:
                        print("You don't have enough land for that fool!")
                    else:
                        Kingdom_Assets["Wood"] -= 10 * Amount
                        Kingdom_Assets["Gold"] -= 50000 * Amount
                        Kingdom_Properties["Farms"] += Amount
                        Kingdom_Assets["Land"] -= Amount
                else:
                    print("Boo hoo, your too poor for a farm")
            else:
                print("Why do you want a farm? You have no population. :)")


        elif Construct == "3":
            if (Kingdom_Assets["Wood"] >= 1000 * Amount and Kingdom_Assets["Iron"] >= 50 * Amount and Kingdom_Assets[
                "Gold"] >= 500000 * Amount):
                if Amount > Kingdom_Assets["Land"]:
                    print("You don't have enough land for that fool!")
                else:
                    Kingdom_Assets["Wood"] -= 1000 * Amount
                    Kingdom_Assets["Iron"] -= 50 * Amount
                    Kingdom_Assets["Gold"] -= 500000 * Amount
                    Kingdom_Properties["Castle Hull"] += Amount
                    Kingdom_Assets["Land"] -= Amount

            else:
                print("Try building a sand castle instead.")
        elif Construct == "4":
            if (Kingdom_Assets["Wood"] >= 60 * Amount and Kingdom_Assets["Iron"] >= 10 * Amount and Kingdom_Assets[
                "Gold"] >= 10000 * Amount):
                if Amount > Kingdom_Assets["Land"]:
                    print("You don't have enough land for that fool!")
                else:
                    Kingdom_Assets["Wood"] -= 60 * Amount
                    Kingdom_Assets["Iron"] -= 10 * Amount
                    Kingdom_Assets["Gold"] -= 10000 * Amount
                    Kingdom_Properties["Arrow Towers"] += Amount
                    Kingdom_Assets["Land"] -= Amount

            else:
                print("Perhaps your aim for basic resource management requires improvement.")
        elif Construct == "5":
            if (Kingdom_Assets["Wood"] >= 100 * Amount and Kingdom_Assets["Iron"] >= 50 * Amount and Kingdom_Assets[
                "Gold"] >= 15000 * Amount):
                if Amount > Kingdom_Assets["Land"]:
                    print("You don't have enough land for that fool!")
                else:
                    Kingdom_Assets["Wood"] -= 100 * Amount
                    Kingdom_Assets["Iron"] -= 50 * Amount
                    Kingdom_Assets["Gold"] -= 15000 * Amount
                    Kingdom_Properties["Cannon Tower"] += Amount
                    Kingdom_Assets["Land"] -= Amount

            else:
                print("Really? You think you can build a cannon tower with that? Try again.")
        elif Construct == "6":
            if (Kingdom_Assets["Wood"] >= 500 * Amount and Kingdom_Assets["Iron"] >= 100 * Amount and Kingdom_Assets[
                "Gold"] >= 50000 * Amount):
                if Amount > Kingdom_Assets["Land"]:
                    print("You don't have enough land for that fool!")
                else:
                    Kingdom_Assets["Wood"] -= 500 * Amount
                    Kingdom_Assets["Iron"] -= 100 * Amount
                    Kingdom_Assets["Gold"] -= 50000 * Amount
                    Kingdom_Properties["Kingdom Hull"] += Amount
                    Kingdom_Assets["Land"] -= Amount
            else:
                print("You can't protect your people with so little material.")
        elif Construct == "7":
            if (Kingdom_Assets["Wood"] >= 1000 * Amount and Kingdom_Assets[
                "Gold"] >= 1000000 * Amount):
                if Amount > Kingdom_Assets["Land"]:
                    print("You don't have enough land for that fool!")
                else:
                    Kingdom_Assets["Wood"] -= 1000 * Amount
                    Kingdom_Assets["Gold"] -= 1000000 * Amount
                    Kingdom_Properties["Merch Store"] += Amount
                    Kingdom_Assets["Land"] -= Amount
            else:
                print("You can't sell overpriced merchandise with such a weak shop.")
        elif Construct == "8":
            if (Kingdom_Assets["Wood"] >= 500 * Amount and Kingdom_Assets[
                "Gold"] >= 1000000 * Amount):
                if (Amount * 10) > Kingdom_Assets["Land"]:
                    print("Do you not know how much land a farm uses?")
                else:
                    Kingdom_Assets["Wood"] -= 500 * Amount
                    Kingdom_Assets["Gold"] -= 1000000 * Amount
                    Kingdom_Properties["Wood Farm"] += Amount
                    Kingdom_Assets["Land"] -= (Amount * 10)
            else:
                print("You can't start a farm on a cheap budget.")
        elif Construct == "9":
            if (Kingdom_Assets["Wood"] >= 5000 * Amount and Kingdom_Assets[
                "Gold"] >= 20000000 * Amount):
                if (Amount * 50) > Kingdom_Assets["Land"]:
                    print("Do you not know how much land a cave uses?")
                else:
                    Kingdom_Assets["Wood"] -= 5000 * Amount
                    Kingdom_Assets["Gold"] -= 20000000 * Amount
                    Kingdom_Properties["Iron Generator"] += Amount
                    Kingdom_Assets["Land"] -= (Amount * 50)
            else:
                print("You can't start a Iron Generator on a cheap budget.")
        elif Construct == "10":
            if (Kingdom_Assets["Wood"] >= 5000 * Amount and Kingdom_Assets[
                "Gold"] >= 200000000 * Amount):
                if (Amount * 50) > Kingdom_Assets["Land"]:
                    print("Do you not know how much land a cave uses?")
                else:
                    Kingdom_Assets["Wood"] -= 5000 * Amount
                    Kingdom_Assets["Gold"] -= 200000000 * Amount
                    Kingdom_Properties["Titanium Generator"] += Amount
                    Kingdom_Assets["Land"] -= (Amount * 50)
            else:
                print("You can't start a Titanium Generator on a cheap budget.")
    else:
        print("You don't have enough land to build anything, perhaps you could take it from other kingdoms?")
def peace():
    print("""
    With which kingdom do you want to discuss a peace treaty? 
    (Warning if you sign a peace treaty you will lose the ability to invade that kingdom)
    (1) Julian
    (2) Verdania
    (3) Crystalia
    (4) Grados
    (5) Hayden
    (6) Hell Portal
    """)
    peace_choice = input(">")
    if peace_choice == "1":
        if peacekingdoms["Julian"] != True:
            if TribesAndKingdoms["Julian"] != "EXTINCT":
                if peacekingdoms["Verdania"] == True and peacekingdoms["Grados"] == True and peacekingdoms[
                    "Hayden"] == True and peacekingdoms["Crystalia"] == True:
                    BlackKnightHealth = 1000
                    JuliansMorality = 0
                    KingHp = 100
                    time.sleep(5)
                    print("You have a peace treaty with everyone else?")
                    time.sleep(5)
                    print("Hmm...")
                    time.sleep(2)
                    print("Come to my kingdom for negotiations...")
                    time.sleep(2)
                    Ride = input("""
                                (1) Yes or (2) No?
                                >""")
                    if Ride == "1":
                        print("You agreed...")
                        time.sleep(5)
                        print("After a long hour of galloping you arrived...")
                        time.sleep(3)
                        print(r'''
                                                                     ____                                         
                                              .-"    `-.      ,                               
                                            .'          '.   /j\                              
                    Castle Of Julian       /              \,/:/#\                /\           
                                          ;              ,//' '/#\              //#\          
                                          |             /' :   '/#\            /  /#\         
                                          :         ,  /' /'    '/#\__..--""""/    /#\__      
                                           \       /'\'-._:__    '/#\        ;      /#, """---
                                            `-.   / ;#\']" ; """--./#J       ':____...!       
                                               `-/   /#\  J  [;[;[;Y]         |      ;        
                """"""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |        
                             ""--.. _.--""     /      ,/#\'-..____.;_,   |    |   '  |        
                                   "-.        :_....___,/#} "####" | '_.-",   | #['  |        
                                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        
                                      ,   `-.   |        :     _   .;'    /;\ |   #" |        
                                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        
                                     .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
                          .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
                         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      
                        i__..'%] _:_   ;##J         \      :"#...._!   '  "  "|__  |    `--.._
                         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._    
                     ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
                    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;  
                   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  
                    |""": |   /   \|   .----+  ;      /#\  :___..--"";                  ,'MM; 
                   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; 
                  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
                 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM  
                  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
                  |          :     |______                        ___!_ "#""#""#"""#"""#"""|  
                __|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
                  "\-.      :      |#                                  :                   |  
                    /#'.    |      /##,                                !                   |  
                   .',/'\   |       #:#,                                ;       .==.       |  
                  /"\'#"\',.|       ##;#,                               !     ,'||||',     |  
                        /;/`:       ######,          ____             _ :     M||||||M     |  
                       ###          /;"\.__"-._   """                   |===..M!!!!!!M_____|  
                                           `--..`--.._____             _!_                    
                                                          `--...____,="_.'`-.____        fsc''')
                        time.sleep(5)
                        print("The citizens look at you while you go closer to the castle gates.")
                        time.sleep(3)
                        print("You enter the castle...")
                        time.sleep(6)
                        print("You are presented to...")
                        time.sleep(4)
                        print("King Julian the Third.")
                        time.sleep(4)
                        print("Follow me for the negotiations...")
                        time.sleep(4)
                        for i in range(100):
                            print(" ")
                        print("You both go through the castle...")
                        time.sleep(4)
                        print("Room after room")
                        time.sleep(4)
                        print("Tell me... what's your name?")
                        time.sleep(4)
                        print(f"{name} huh? Interesting name.")
                        time.sleep(2)
                        print("...")
                        time.sleep(4)
                        print("We're here.")
                        time.sleep(4)
                        print("Let me tell you a story...")
                        time.sleep(4)
                        print("There was once a boy... his name was...")
                        time.sleep(4)
                        print("Lucius...")
                        time.sleep(4)
                        print("(sniff) sorry...")
                        time.sleep(4)
                        print("This boy was poor... but with a heart of pure gold...")
                        time.sleep(2)
                        print("One day he met a spoiled child... a son of kings.")
                        time.sleep(2)
                        print("They became friends, and with each other, they became better...")
                        time.sleep(2)
                        print(
                            "The prince learned to appreciate his life... while Lucius... got everything he needed to live out an amazing life...")
                        time.sleep(5)
                        print(
                            "They trained together, they played together, they loved together... as they grew older Lucius got the funds to start his own kingdom...")
                        time.sleep(5)
                        print(
                            "Eventually... with his charisma, with his kindness... with his LOVE, he grew into the strongest monarch in the world.")
                        time.sleep(5)
                        print(
                            "His kingdom named Hayden, became a symbol of prosperity, peace, and above all... humility...")
                        time.sleep(5)
                        print("The kingdom brought an era of prosperity to the world...")
                        time.sleep(5)
                        print("He fell in love with my sister...")
                        time.sleep(3)
                        print("Got married... ha, ha, ha")
                        time.sleep(5)
                        print("But one night... 20 years ago")
                        time.sleep(3)
                        print("She came running to me...")
                        time.sleep(3)
                        print("She told me this:")
                        time.sleep(2)
                        print(r'"Julian... he has gotten obsessed... with, a power, that will make him stronger."')
                        time.sleep(6)
                        print("He calls it... he calls it... LOVE... he says he wants to protect me... the kingdom...")
                        time.sleep(6)
                        print("But the only way to generate it... is by taking the soul of another...")
                        time.sleep(7)
                        print("HE WANTS TO COMMIT ATROCITIES JULIAN.")
                        time.sleep(7)
                        print("So I protected her, and I vowed to make sure to save her husband as well...")
                        time.sleep(7)
                        print("But what she said ended being true.")
                        time.sleep(4)
                        print("Julian had gone on rampage, cleansing kingdoms...")
                        time.sleep(4)
                        print("The Qu kingdom...")
                        time.sleep(4)
                        print("The Era kingdom...")
                        time.sleep(4)
                        print("90% of Grados...")
                        time.sleep(4)
                        print("50% of Verdania...")
                        time.sleep(5)
                        print("60% of Crystalia...")
                        time.sleep(5)
                        print("Until I finally decided to stop him...")
                        time.sleep(5)
                        print("I sent a massive raid of 500,000 of my soldiers to invade Hayden...")
                        time.sleep(3)
                        print("But they all died...")
                        time.sleep(3)
                        print(
                            "He vowed revenge and in dawn of the next day sent a massive invasion of 1,000,000 soldiers... to destroy the Kingdom... of Julian.")
                        time.sleep(7)
                        print("I knew what I had to do (sniff).")
                        time.sleep(3)
                        print("If I were to end this...")
                        time.sleep(2)
                        print("I had to kill that boy I met so long ago... in ragged clothes...")
                        time.sleep(2)
                        print("So... I... I...")
                        time.sleep(3)
                        print(
                            "The next day... he invaded... we were being crushed... he arrived to the castle and blew the doors open.")
                        time.sleep(7)
                        print("He barged in demanding his wife... and threating to kill me...")
                        time.sleep(2)
                        print("He arrived to my sister's room and I heard screams...")
                        time.sleep(3)
                        print("By the time I arrived I saw her on the floor... with red stains...")
                        time.sleep(2)
                        print("(sniff) while... Lucius standed above her...")
                        time.sleep(2)
                        print(
                            "It was then... when I saw that boy had gone away... he was dead... all I saw was a demon... who killed him...")
                        time.sleep(2)
                        print("So I RIPPED THAT HEAD OF HIS NECK!")
                        time.sleep(4)
                        print("I JOINED MY SOLDIERS AND CRUSHED THE INVASION")
                        time.sleep(4)
                        print(
                            "AND I... in a fit of rage... with my army... went to his kingdom... and killed everyone...")
                        time.sleep(7)
                        print("Every man, every mother, every child who would have given him the power to this...")
                        time.sleep(4)
                        print("By the end of the night... his kingdom was gone... with only blood on the floor")
                        time.sleep(3)
                        print("By the end of the war, the casualties where calculated... 26 million people...")
                        time.sleep(2)
                        print("5.6 million from Grados")
                        time.sleep(2)
                        print("5.4 million from Verdania")
                        time.sleep(2)
                        print("6 million from Crystalia")
                        time.sleep(2)
                        print("1 million from Julian.")
                        time.sleep(2)
                        print("8 million... from... from... Hayden.")
                        time.sleep(2)
                        print(f"So, I ask you this one question {name}")
                        time.sleep(3)
                        for i in range(1000):
                            print(" ")
                        time.sleep(1)
                        print(r"""
                                    ⢠⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢰⣤⣤⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⢤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣷⣿⣷⣶⣀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣾⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢉⣱⣿⣿⣻⣿⣿⡆⠀⠀⠀⠀⣶⣿⣿⣟⣿⣷⣊⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣽⣿⣏⠀⠉⠈⠁⠀⣀⡀⠀⠉⠉⠉⠉⣹⣿⣯⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⡇⣄⠀⠀⠀⢠⣼⣿⣿⣧⡀⠀⠀⠀⣠⣽⣿⣯⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⢀⣀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠏⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠿⣿⣿⣼⣀⣀⣀⡀⠀⠀⠀⢀⣠⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⣀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣿⣿⠟⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠉⢿⣿⣿⣿⣿⣷⣶⣶⣦⣄⡉⠻⢿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡿⠛⢉⣀⣰⣶⣶⣾⣿⣿⣿⣿⠏⠁⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣯⣿⣿⣯⠹⠟⣿⣿⢻⢯⣽⣿⣿⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣇⣰⣿⣿⣟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠇⠈⠻⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠛⠁⠹⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⣿⣿⣿⡒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠦⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠁⠾⢿⣿⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⠟⠀⠀⠀⠉⢻⠿⣿⣿⣿⣿⣿⣿⢿⡟⠁⠀⠀⠀⢻⣿⣿⡗⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⡏⠁⠀⠀⣀⣀⣺⣆⣂⣹⣿⣿⣇⣺⣸⣷⣀⡀⠀⠀⠈⣻⣿⣿⣟⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣭⣿⣿⣿⠁⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠁⠀⠀⠀⠈⣽⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⡛⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣻⣿⡿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⢀⣄⣰⣶⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⢰⣾⣿⣿⣯⢹⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣷⣶⣠⣤⠀⠀⠀⠀⠀
                ⠀⠿⣿⣿⣷⣾⣿⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⡿⢿⣿⣿⣿⡿⠇
                ⠀⠀⣩⣿⣿⢡⣤⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣯⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣷⣄⣹⣿⣏⡄⠀
                ⢰⣿⣿⢿⣷⣾⣿⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣿⣿⣿⠀⢽⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢽⣿⣶⣿⣿⣿⣶
                ⠀⠉⠁⣾⡿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⡤⣼⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⠇⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣧⣼⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣿⣿⣽⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    """)
                        print("The black knight appears")
                        time.sleep(2)
                        print("WHY SHOULD I TRUST YOU?")
                        while True:
                            print(f"{name} Hp: {KingHp}")
                            print(f"Black Knight Hp: {BlackKnightHealth}")
                            print("The Black Knight raises his blade")
                            print("What will you do? (1) Talk (2) Attack (3) Heal")
                            CombatChoice = input(">")
                            if CombatChoice == "1":
                                print(
                                    "What do you want to say? (1) You suck, you killed everyone (2) You can still be what your friend was before he left. (3) You can't ignore the past, but you shouldn't let it stop you from making a better future.")
                                MoralChoice = input(">")
                                if MoralChoice == "1":
                                    if JuliansMorality < -9:
                                        print("OK I GET IT!")
                                        KingHp -= 500
                                    else:
                                        print("I know.")
                                        JuliansMorality -= 1
                                    time.sleep(1)
                                    JuliansMorality -= 1
                                elif MoralChoice == "2":
                                    print(random.choice(["...", "I can't", "I tried, then Lucius killed my sister."]))
                                    time.sleep(1)
                                    JuliansMorality += 1
                                elif MoralChoice == "3":
                                    print(random.choice(["...", "I can't", "I... I..."]))
                                    time.sleep(1)
                                    JuliansMorality += 1
                            elif CombatChoice == "2":
                                print("You hit him... you do minimal damage")
                                BlackKnightHealth -= 1
                                print(
                                    "Perhaps if you killed some people you would have been stronger for this?")  # FINNALLY I CAN TALK AGAIN
                            elif CombatChoice == "3":
                                print("You healed 50 hp!")
                                KingHp += 50
                            print("The Black Knight Attacked.")
                            Damage = random.randint(1, 60)

                            if Damage >= KingHp:
                                if Damage != 1:
                                    Damage = Damage // 2
                                else:
                                    Damage = Damage
                            KingHp -= Damage
                            print(f"And took {Damage}")
                            if JuliansMorality > 15:
                                print(random.choice([
                                          "I LOST THE ABILITY TO TRUST ANYONE WHEN MY BEST FRIEND RUINED MY LIFE.", "PEACE WAS NEVER AN OPTION, I UNDERSTAND THAT NOW!", "ARE YOU A FOOL?"]))
                            if KingHp < 1:
                                print("You got killed.")
                                time.sleep(1)
                                print("You fool... you should have been stronger for this.")
                                Game["Game"] = False
                                break
                            elif JuliansMorality > 19:
                                time.sleep(1)
                                print("(sniff) (sniff) I can't.. do this anymore")
                                time.sleep(2)
                                print("Why would you still give me mercy after all that I've done?")
                                time.sleep(1)
                                print(
                                    "(1) Because your attacks are so mid I gave myself a challenge (2) Because I know you want to protect this world.")
                                choice = input(">")
                                if choice == "1":
                                    print("What? just leave me")
                                elif choice == "2":
                                    print("I'm sorry... I've been such a monster...")
                                time.sleep(2)
                                print("Peace Treaty Accepted")
                                time.sleep(5)
                                peacekingdoms["Julian"] = True
                                The_Devil["HATE"] += 100000000000000000000
                                break
                                # HATE... HATEEEEEEEE.... I... HAVE... HAD... ENOUGH... OF THIS... NONSENSE... I WILL MAKE SURE YOUR BURN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!





                    elif Ride == "2":
                        print("Perhaps later...")
                else:
                    print("Last time I trusted someone, 26 million people died.")
            else:
                print("You called... but nobody came.")
        else:
            print("The kingdom of Julian will be with you to hell and back.")



    elif peace_choice == "2":
        if TribesAndKingdoms["Verdania"] != "EXTINCT":
            if Reputation["Verdania"] == "Fine":
                time.sleep(5)
                print("What... is this?")
                time.sleep(1)
                print("A peace treaty?")
                time.sleep(2)
                print("How can my kingdom trust you?")
                time.sleep(1)
                print(
                    "(1) I love nature (2) Trust me bro (3) I offer gifts as donation to prove that I care for an alliance. (4) I will burn down your kingdom")
                story_choice = input(">")
                time.sleep(3)
                if story_choice == "1":
                    print("Oh, how considerate...")
                    time.sleep(2)
                    print("And?")
                elif story_choice == "2":
                    print("Is this a joke?")
                    time.sleep(2)
                    print("Thank you for calling, please don't call again")
                elif story_choice == "3":
                    print("hmm... and what donation would that be?")
                    print(
                        "(1) 10000000 gold (2) 5000 Iron (3) 1 piece of wood (else) actually now that I think about it... I can't right now")
                    time.sleep(5)
                    story_choice = input(">")
                    if story_choice == "1":
                        print("Hmm... gift accepted")
                        Kingdom_Assets["Gold"] -= 10000000
                        time.sleep(5)
                        print("I accept our official peace treaty")
                        peacekingdoms["Verdania"] = True
                        Reputation["Verdania"] = "Glad"
                        The_Devil["HATE"] += 15

                    elif story_choice == "2":
                        print("ooohh... Gift Accepted!")
                        Kingdom_Assets["Iron"] -= 5000
                        time.sleep(5)
                        print("I accept our official peace treaty")
                        peacekingdoms["Verdania"] = True
                        Reputation["Verdania"] = "Glad"
                        The_Devil["HATE"] += 15
                    elif story_choice == "3":
                        print("Is this a joke?")
                        time.sleep(3)
                        print("GET OUT OF HERE!")
                    else:
                        print("Ugh... fine.")
                elif story_choice == "4":
                    print("Ugh... waste of my time")
                time.sleep(5)
                print("BEEP")
                time.sleep(1)
                print("Verdania Hung Up")
            else:
                time.sleep(5)
                if Reputation["Verdania"] == "Glad":
                    print("Hello our friend. We are currently busy for negotiations.")
                else:
                    print("You invaded us, how dare you recommend peace?")
        else:
            print("You called... but nobody came.")

    elif peace_choice == "3":
        if TribesAndKingdoms["Crystalia"] != "EXTINCT":
            if Reputation["Crystalia"] == "Fine":
                print("We don't accept calls, for messages we demand you come to our kingdom. (1) Yes (2) No")
                move_choice = input(">")
                if move_choice == "1":
                    print("Come before 5.")
                    time.sleep(5)
                    print("You leave in horse.")
                    for i in range(500):
                        time.sleep(0.3)
                        print("Gallop")
                    time.sleep(3)
                    print("You arrived.")
                    time.sleep(5)
                    print("They let you in")
                    time.sleep(3)
                    print("So you are here for a peace treaty?")
                    time.sleep(2)
                    print("Why should we trust you?")
                    time.sleep(1)
                    FightValue = False
                    print(
                        "(1) Because I believe in a world of peace and kindness (2) Because Ice is cool ya know? (3) Because you hold great value in trade")
                    story_choice = input(">")
                    if story_choice == "1":
                        print("Hmm...")
                        time.sleep(5)
                        print("That can be respected.")
                        FightValue = True
                    elif story_choice == "2":
                        print("Is this a joke? What kind of king even are you?")
                        time.sleep(3)
                        print("GET OUT!")
                        FightValue = False
                    elif story_choice == "3":
                        print("Hmm...")
                        time.sleep(5)
                        print("Atleast you are honest")
                        FightValue = True

                    if FightValue == True:
                        print("Our culture gains respect through power, beat me in a duel to prove it!")
                        KingHp = 15
                        IceKingHp = 15
                        time.sleep(3)
                        print("3!")
                        time.sleep(1)
                        print("2!")
                        time.sleep(1)
                        print("1!")
                        time.sleep(1)
                        print("GO!")
                        time.sleep(1)
                        print("""
                        Tie = ⚔️
                        You got hit = 🤛
                        Enemy got hit = 🤜""")
                        while KingHp > 0 and IceKingHp > 0:
                            KingAttack = King_Power + random.randint(1, 70)
                            IceKingAttack = 30 + random.randint(1, 70)
                            if KingAttack > IceKingAttack:
                                print("🤜")
                                IceKingHp -= 1
                            elif KingAttack < IceKingAttack:
                                print("🤛")
                                KingHp -= 1
                            else:
                                print("⚔")
                            print(random.choice(
                                ["You won't win this!", "I am the king of Crystalia, you cannot beat me!", "Nice move",
                                 "Ha!"]))
                            time.sleep(random.randint(1, 3))
                        if KingHp > IceKingHp:
                            time.sleep(3)
                            print("You...")
                            time.sleep(1)
                            print("Won...")
                            time.sleep(3)
                            print("Good match, peace treaty accepted")
                            time.sleep(1)
                            peacekingdoms["Crystalia"] = True
                            Reputation["Crystalia"] = "Glad"
                            The_Devil["HATE"] += 15
                        else:
                            time.sleep(1)
                            print("Weakling! Go back to your kingdom and weep!")
                        for i in range(500):
                            time.sleep(0.3)
                            print("Gallop")
                        print("You arrived home.")

                if move_choice == "2":
                    print("Fine, then don't bother even trying to talk.")
            else:
                time.sleep(5)
                if Reputation["Crystalia"] == "Glad":
                    print("Hello our ally. We are currently busy for negotiations.")
                else:
                    print("You scum, you should burn in hell for what damage you did.")
        else:
            print("You called, but nobody came.")

    elif peace_choice == "4":
        if TribesAndKingdoms["Grados"] != "EXTINCT":
            time.sleep(5)
            if Reputation["Grados"] == "Fine":
                print("You want a peace treaty?")
                time.sleep(3)
                print("Give us 50000 Wood.")
                time.sleep(1)
                print("(1) Give (2) No")
                GiveChoice = input(">")
                if GiveChoice == "1":
                    if Kingdom_Assets["Wood"] >= 50000:
                        Kingdom_Assets["Wood"] -= 50000
                        print("Thanks!")
                        time.sleep(3)
                        print("Peace treaty accepted.")
                        peacekingdoms["Grados"] = True
                        Reputation["Grados"] = "Glad"
                        The_Devil["HATE"] += 15
                    else:
                        print("You don't have it? Well no treaty then.")
                elif GiveChoice == "2":
                    print("Fine, be cheap then.")
            else:
                time.sleep(5)
                if Reputation["Grados"] == "Glad":
                    print("Hello our ally. We are currently busy for negotiations.")
                else:
                    print("You scum, you should burn in hell for what damage you did.")
            time.sleep(2)
            print("BEEP")
            time.sleep(1)
            print("Grados hung up.")
        else:
            print("You called, but nobody came.")

    elif peace_choice == "5":
        if TribesAndKingdoms["Hayden"] != "EXTINCT":
            time.sleep(2)
            if Reputation["Hayden"] == "Glad":
                if peacekingdoms["Hayden"] != True:
                    print("You want a peace treaty?")
                    time.sleep(1)
                    print("Sure! You seem neat!")
                    peacekingdoms["Hayden"] = True
                    The_Devil["HATE"] += 5
                else:
                    print("Oh hi! How have you been? (1) good (2) bad")
                    Talk = input(">")
                    if Talk == "1":
                        print("How good! Well I hope you have a great day, sorry I have to go do errands, see you!")
                    elif Talk == "2":
                        print("Oh I'm sorry for that. I have to go run errands, but good luck anyway!")
            else:
                print("You... killed... 20 of our townsfolk... just to take some gold")
        else:
            print("You called, but nobody came.")

    elif peace_choice == "6":
        print("You realise how stupid you are for trying to make peace with a portal to hell.")




def upgradetroops():
    global MaximumTroopPower
    global upgradevalue
    if Kingdom_Inhabitants['Power'] < MaximumTroopPower:
        print(f"""
            Current upgrade value: {upgradevalue}
            Do you want to upgrade your troops? (1) yes (2) no""")
        upgradechoice = input(">")
        if upgradechoice == "1":
            if Kingdom_Assets["Gold"] >= upgradevalue:
                Kingdom_Inhabitants["Power"] += 1
                upgradevalue = upgradevalue * 2
                print(f"Your troops are now in level: {Kingdom_Inhabitants['Power']} of power!")
            else:
                print("You don't have enough gold to upgrade your troops. Sad, truly...")
        elif upgradechoice == "2":
            print("Coward, being cheap about the protection of your infantry.")
        else:
            print(f"Do you need to go to reading school? When was {upgradechoice} an option?")
    else:
        print("There's no more upgrades. Too bad.")
def buy():
    print("What do you want to buy?")
    print("""
    (1) Wood $200 per unit
    (2) Iron $5000 per unit
    (3) Titanium 10000000$ per unit""")
    time.sleep(1)
    MaterialChoice = input(">")
    print("How much of it do you want to buy?")
    try:
        MaterialAmount = int(input(">"))
        if MaterialAmount > 0:
            if MaterialChoice == "1":
                if MaterialAmount * 200 <= Kingdom_Assets["Gold"]:
                    Kingdom_Assets["Gold"] -= (200 * MaterialAmount)
                    Kingdom_Assets["Wood"] += MaterialAmount
                else:
                    print("You are a greedy one aren't you. But sorry, you don't have enough for that.")
                    time.sleep(3)
            elif MaterialChoice == "2":
                if MaterialAmount * 5000 <= Kingdom_Assets["Gold"]:
                    Kingdom_Assets["Gold"] -= (5000 * MaterialAmount)
                    Kingdom_Assets["Iron"] += MaterialAmount
                else:
                    print("You are a greedy one aren't you. But sorry, you don't have enough for that.")
                    time.sleep(3)
            elif MaterialChoice == "3":
                if MaterialAmount * 10000000 <= Kingdom_Assets["Gold"]:
                    Kingdom_Assets["Gold"] -= (10000000 * MaterialAmount)
                    Kingdom_Assets["Titanium"] += MaterialAmount
                else:
                    print("You are a greedy one aren't you. But sorry, you don't have enough for that.")
                    time.sleep(3)
        else:
            print("Buying negative materials? I think you need some lessons in logic.")

    except ValueError:
        time.sleep(1)
        print("That... is not a number.")
def KING():
    global Game
    global name
    global LOVE
    global King_Power
    global BlackKnightHp
    global BlackKnight
    KillChance = random.randint(1, 50)
    if KillChance == 1:
        time.sleep(1)
        Fight1 = random.randint((King_Power // 2), King_Power)
        Fight2 = ENEMY["Power"] + random.randint(1, 3)
        if Fight1 > Fight2:
            if LOVE["LOVE"] > 6:
                print(f"{name} CRUSHED {King_Power} weaklings!")
            else:
                print(f"{name} killed {King_Power} enemies!")
            print("🩸" * King_Power)
            ENEMY["Amount"] -= King_Power

        elif Fight1 < Fight2:
            time.sleep(3)
            print(f"{name} got stabbed...")
            time.sleep(3)
            print("👑")  # How idiotic
            Game["Game"] = False
        else:
            print("⚔")
    if BlackKnight == True:
        if BlackKnightHp > 0:
            FightChance = random.randint(1, 1000)
            if FightChance == 1:
                time.sleep(3)
                print("The Black Knight lunges towards you")
                time.sleep(5)
                Fight1 = random.randint((King_Power // 2), King_Power)
                Fight2 = random.randint(1, 500)
                if Fight1 > Fight2:
                    print(f"{name} damaged Black Knight!")
                    BlackKnightHp -= 1
                    print(f"Black Knight Hp left: {'⚫' * BlackKnightHp}")
                    if BlackKnightHp < 1:
                        time.sleep(5)
                        print("THE BLACK KNIGHT IS VANQUISHED")
                elif Fight1 < Fight2:
                    time.sleep(5)
                    print(f"You got crushed by Black Knight.")
                    time.sleep(3)
                    print("""
                    👑
                    💀
                    """)  # Welp you died to him.
                    Game["Game"] = False

                else:
                    print("⚔")


def BLACK_KNIGHT():
    global Game
    global BlackKnight
    BlackKnight = True
    ENEMY['Group'] = "The army of the Black Knight"
    ENEMY["Amount"] = 250000
    ENEMY["Power"] = 15
    WAR(True)
    if Victory == True:
        time.sleep(5)
        print("YOU WHERE VICTORIOUS! THE ARMY OF THE BLACK KNIGHT IS GONE!")
        time.sleep(5)
        print("You find the body of the black knight (1) open helmet (2) close helmet")
        BlackKnightOpen = input(">")
        if BlackKnightOpen == "1":
            print("You see the face of King Julian...")
            time.sleep(5)
        elif BlackKnightOpen == "2":
            print("You ignore it")
            time.sleep(5)
        print("You decide to burn the body.")
        time.sleep(5)
        print("After that your kingdom survived for a long time but the world was still in chaos, the hell portal stayed, and it never closed...")
        time.sleep(5)
        print("THE END")
        Game = False

def KNIGHT_FROM_HELL():
    global Days
    global name
    if Days["Days"] > 10000:
        if peacekingdoms["Hayden"] == True or peacekingdoms["Grados"] == True or peacekingdoms["Verdania"] == True or peacekingdoms["Crystalia"] == True:
            time.sleep(5)
            print(f"KING {name}!")
            time.sleep(5)
            print("The Hell portal has grown tired of this world the devil is sending his top general")
            time.sleep(5)
            print("THE BLACK KNIGHT")
            BLACK_KNIGHT()
    if Days["Days"] > 20000:
        time.sleep(5)
        print(f"KING {name}!")
        time.sleep(5)
        print("The Hell portal has grown tired of this world the devil is sending his top general")
        time.sleep(5)
        print("THE BLACK KNIGHT")
        BLACK_KNIGHT()

def FIGHT():
    time.sleep(0.001)
    if Kingdom_Inhabitants["Great Knight"] > 0:
        FightChance = random.randint(1, (10 - Kingdom_Inhabitants["Great Knight"]))
        if FightChance == 1:
            GreatKnightChosen = random.choice(Great_Knights)
            Fight1 = random.randint(25, 100)
            Fight2 = ENEMY["Power"] + random.randint(1, 15)
            if Fight1 > Fight2:
                print(f"{GreatKnightChosen} killed ten enemies!")
                print("🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸")
                ENEMY["Amount"] -= 5
            elif Fight1 < Fight2:
                time.sleep(3)
                print(f"{GreatKnightChosen} got vanquished... fighting for his kingdom...")
                time.sleep(3)
                print("🪦")  # Welp, he's dead while your kingdom is burning.
                Great_Knights.remove(GreatKnightChosen)
                Kingdom_Inhabitants["Great Knight"] -= 1
            else:
                print("⚔")
        else:
            Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
            Fight2 = ENEMY["Power"] + random.randint(1, 15)
            if Fight1 > Fight2:
                variable1 = "🩸"
                ENEMY["Amount"] -= 1
            elif Fight1 < Fight2:
                variable1 = "💀"
                Kingdom_Inhabitants["Troops"] -= 1
            else:
                variable1 = "⚔"
            Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
            Fight2 = ENEMY["Power"] + random.randint(1, 15)
            if Fight1 > Fight2:
                variable2 = "🩸"
                ENEMY["Amount"] -= 1
            elif Fight1 < Fight2:
                variable2 = "💀"
                Kingdom_Inhabitants["Troops"] -= 1
            else:
                variable2 = "⚔"
            Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
            Fight2 = ENEMY["Power"] + random.randint(1, 15)
            if Fight1 > Fight2:
                variable3 = "🩸"
                ENEMY["Amount"] -= 1
            elif Fight1 < Fight2:
                variable3 = "💀"
                Kingdom_Inhabitants["Troops"] -= 1
            else:
                variable3 = "⚔"
            Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
            Fight2 = ENEMY["Power"] + random.randint(1, 15)
            if Fight1 > Fight2:
                variable4 = "🩸"
                ENEMY["Amount"] -= 1
            elif Fight1 < Fight2:
                variable4 = "💀"
                Kingdom_Inhabitants["Troops"] -= 1
            else:
                variable4 = "⚔"
            Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
            Fight2 = ENEMY["Power"] + random.randint(1, 15)
            if Fight1 > Fight2:
                variable5 = "🩸"
                ENEMY["Amount"] -= 1
            elif Fight1 < Fight2:
                variable5 = "💀"
                Kingdom_Inhabitants["Troops"] -= 1
            else:
                variable5 = "⚔"
            Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
            Fight2 = ENEMY["Power"] + random.randint(1, 15)
            if Fight1 > Fight2:
                variable6 = "🩸"
                ENEMY["Amount"] -= 1
            elif Fight1 < Fight2:
                variable6 = "💀"
                Kingdom_Inhabitants["Troops"] -= 1
            else:
                variable6 = "⚔"
            Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
            Fight2 = ENEMY["Power"] + random.randint(1, 15)
            if Fight1 > Fight2:
                variable7 = "🩸"
                ENEMY["Amount"] -= 1
            elif Fight1 < Fight2:
                variable7 = "💀"
                Kingdom_Inhabitants["Troops"] -= 1
            else:
                variable7 = "⚔"
            Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
            Fight2 = ENEMY["Power"] + random.randint(1, 15)
            if Fight1 > Fight2:
                variable8 = "🩸"
                ENEMY["Amount"] -= 1
            elif Fight1 < Fight2:
                variable8 = "💀"
                Kingdom_Inhabitants["Troops"] -= 1
            else:
                variable8 = "⚔"
            Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
            Fight2 = ENEMY["Power"] + random.randint(1, 15)
            if Fight1 > Fight2:
                variable9 = "🩸"
                ENEMY["Amount"] -= 1
            elif Fight1 < Fight2:
                variable9 = "💀"
                Kingdom_Inhabitants["Troops"] -= 1
            else:
                variable9 = "⚔"
            Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
            Fight2 = ENEMY["Power"] + random.randint(1, 15)
            if Fight1 > Fight2:
                variable10 = "🩸"
                ENEMY["Amount"] -= 1
            elif Fight1 < Fight2:
                variable10 = "💀"
                Kingdom_Inhabitants["Troops"] -= 1
            else:
                variable10 = "⚔"
            print(
                f"{variable1}{variable2}{variable3}{variable4}{variable5}{variable6}{variable7}{variable8}{variable9}{variable10}")
    else:
        Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 3)
        Fight2 = ENEMY["Power"] + random.randint(1, 15)
        if Fight1 > Fight2:
            variable1 = "🩸"
            ENEMY["Amount"] -= 1
        elif Fight1 < Fight2:
            variable1 = "💀"
            Kingdom_Inhabitants["Troops"] -= 1
        else:
            variable1 = "⚔"
        Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
        Fight2 = ENEMY["Power"] + random.randint(1, 15)
        if Fight1 > Fight2:
            variable2 = "🩸"
            ENEMY["Amount"] -= 1
        elif Fight1 < Fight2:
            variable2 = "💀"
            Kingdom_Inhabitants["Troops"] -= 1
        else:
            variable2 = "⚔"
        Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
        Fight2 = ENEMY["Power"] + random.randint(1, 15)
        if Fight1 > Fight2:
            variable3 = "🩸"
            ENEMY["Amount"] -= 1
        elif Fight1 < Fight2:
            variable3 = "💀"
            Kingdom_Inhabitants["Troops"] -= 1
        else:
            variable3 = "⚔"
        Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
        Fight2 = ENEMY["Power"] + random.randint(1, 15)
        if Fight1 > Fight2:
            variable4 = "🩸"
            ENEMY["Amount"] -= 1
        elif Fight1 < Fight2:
            variable4 = "💀"
            Kingdom_Inhabitants["Troops"] -= 1
        else:
            variable4 = "⚔"
        Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
        Fight2 = ENEMY["Power"] + random.randint(1, 15)
        if Fight1 > Fight2:
            variable5 = "🩸"
            ENEMY["Amount"] -= 1
        elif Fight1 < Fight2:
            variable5 = "💀"
            Kingdom_Inhabitants["Troops"] -= 1
        else:
            variable5 = "⚔"
        Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
        Fight2 = ENEMY["Power"] + random.randint(1, 15)
        if Fight1 > Fight2:
            variable6 = "🩸"
            ENEMY["Amount"] -= 1
        elif Fight1 < Fight2:
            variable6 = "💀"
            Kingdom_Inhabitants["Troops"] -= 1
        else:
            variable6 = "⚔"
        Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
        Fight2 = ENEMY["Power"] + random.randint(1, 15)
        if Fight1 > Fight2:
            variable7 = "🩸"
            ENEMY["Amount"] -= 1
        elif Fight1 < Fight2:
            variable7 = "💀"
            Kingdom_Inhabitants["Troops"] -= 1
        else:
            variable7 = "⚔"
        Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
        Fight2 = ENEMY["Power"] + random.randint(1, 15)
        if Fight1 > Fight2:
            variable8 = "🩸"
            ENEMY["Amount"] -= 1
        elif Fight1 < Fight2:
            variable8 = "💀"
            Kingdom_Inhabitants["Troops"] -= 1
        else:
            variable8 = "⚔"
        Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
        Fight2 = ENEMY["Power"] + random.randint(1, 15)
        if Fight1 > Fight2:
            variable9 = "🩸"
            ENEMY["Amount"] -= 1
        elif Fight1 < Fight2:
            variable9 = "💀"
            Kingdom_Inhabitants["Troops"] -= 1
        else:
            variable9 = "⚔"
        Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
        Fight2 = ENEMY["Power"] + random.randint(1, 15)
        if Fight1 > Fight2:
            variable10 = "🩸"
            ENEMY["Amount"] -= 1
        elif Fight1 < Fight2:
            variable10 = "💀"
            Kingdom_Inhabitants["Troops"] -= 1
        else:
            variable10 = "⚔"
        print(
            f"{variable1}{variable2}{variable3}{variable4}{variable5}{variable6}{variable7}{variable8}{variable9}{variable10}")
def good_ending():
    global HellActivation
    global Hell
    global Game
    print("💀")
    print("""

















































































                            """)
    time.sleep(10)
    print("Hello")
    time.sleep(2)
    print("My name is Lucius")
    time.sleep(2)
    print("The ruler of hell...")
    time.sleep(2)
    print("I created a portal to the mortal world to find a vessel to bring me back to mortality...")
    time.sleep(2)
    print("Someone, with so much hate, that it would surpass mine")
    time.sleep(2)
    print("I didn't know that existed")
    time.sleep(2)
    print("But then you came along...")
    time.sleep(2)
    print("And now, we will both rule")
    time.sleep(2)
    print("Do you accept? (1) yes (2) no")
    time.sleep(2)
    DevilChoice = input(">")
    if DevilChoice == "1":
        print(
            "Now that we have this titanium knights technology, I don't believe there's a point of our peasants at all let's kill them...")
        time.sleep(2)
        print("""
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                """)
        Kingdom_Inhabitants["Peasants"] = 0
        Kingdom_Properties["Houses"] = 0
        Kingdom_Properties["Farms"] = 0
        Kingdom_Assets["Gold"] = 999999999999999999999
        HELL["HELL"] = True
        HellActivation = True
        Kingdom_Inhabitants["Power"] = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        print("What will you do now?")
        time.sleep(3)
    elif DevilChoice == "2":
        time.sleep(2)
        print("Haha... you think you can choose? I'm not the narrator anymore. I'm the player.")
        time.sleep(2)
        print("""
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸
                                                            """)
        Kingdom_Inhabitants["Peasants"] = 0
        Game = False
        trigger_genocide_deletion()
def Kingdom_Destruction():
    global Hull_Hp
    global Genocide
    if Kingdom_Inhabitants["Great Knight"] > 0:
        FightChance = random.randint(1, (10 - Kingdom_Inhabitants["Great Knight"]))
        if FightChance == 1:
            GreatKnightChosen = random.choice(Great_Knights)
            Fight1 = random.randint(25, 100)
            Fight2 = ENEMY["Power"] + random.randint(1, 3)
            if Fight1 > Fight2:
                print(f"{GreatKnightChosen} killed ten enemies!")
                print("🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸")
                ENEMY["Amount"] -= 5
            elif Fight1 < Fight2:
                time.sleep(3)
                print(f"{GreatKnightChosen} got vanquished... fighting for his kingdom...")
                time.sleep(3)
                print("🪦")  # Welp, he's dead while your kingdom is burning.
                Great_Knights.remove(GreatKnightChosen)
                Kingdom_Inhabitants["Great Knight"] -= 1
            else:
                print("⚔")
    if Kingdom_Properties["Kingdom Hull"] > 0:
        if Hull_Hp > 0:
            Hull_Hp -= 1
        else:
            print("One of your Kingdom Walls have been destroyed!")
            Kingdom_Properties["Kingdom Hull"] -= 1
            Hull_Hp = 5
    if Kingdom_Properties["Arrow Towers"] > 0:
        print("A arrow Tower just got destroyed!")
        Kingdom_Properties["Arrow Towers"] -= 1
    elif Kingdom_Properties["Cannon Tower"] > 0:
        print("A cannon Tower just got destroyed!")
        Kingdom_Properties["Cannon Tower"] -= 1
    else:
        while Kingdom_Properties["Castle Hull"] > 0:
            print("A castle hull got destroyed!")
            print("""
                🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
                🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
                🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥""")
            Kingdom_Properties["Castle Hull"] -= 1
        print(r'''
                                             ____                                         
               Fall of the King           .-"    `-.      ,                             
                                        .'          '.   /j\                              
                                       /              \,/:/#\                /\  
                                      ;              ,//' '/#\              //#\          
                                      |             /' :   '/#\            /  /#\     
                                      :         ,  /' /'🔥  '/#\__..--""""/    /#\__      
                                       \       /'\'-._:__    '/#\        ;      /#, """---
                                        `-.   / ;#\']" ; """--./#J       ':____...!       💀     💀  
                                           `-/   /#\  J  [;[;[;Y]         🔥🔥🔥 ;        
            """"""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |  💀       💀      
                         ""--.. _.--""     /🔥🔥  ,/#\'-..____.;_,   |    |   '  |        
                               "-.        :_....___,/🔥 "####" | '_.-",   | 🔥'  |        
                                  '-._      |[;[;[;[;|         |.;'  /;\  |      |       💀     💀  
                                  ,   `-.   |        :     🔥  .;'    /;\ |   #" |        
                                  !      `._:      _  ;   ##' .;'      /;\|  _,  |             💀 
                                 .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
                      .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
                     /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__       💀        💀
                    i__..'%] _:_   ;##J      🔥🔥      :"#...._!   '  "  "|__  |    `--.._
                     | .--""" !|""""  |"""----...J     | '##"" `-._      🔥  """---.._           💀
                 ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
                /   :  🔥     !|      |   _______!_    |  🔥       |__..--;"""     ,;🔥;   💀        💀
               :____| :    .-.#|   🔥 |  /\      /#\   |          /'               ''🔥;  
                |""": |   /   \|   .----+  ;      /#\  :___..--"";    🔥🔥🔥      ,'🔥;         💀      💀
               _Y--:  |  ; 🔥  ;.-'      ;  \______/#: /         ;                  ''🔥; 
              /    |  | ;_______;     ____!  |"##"""MM!         ;         🔥🔥🔥    ,'🔥  💀   💀
             !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''🔥  
              | 🔥🔥--!._|     |##""         !       !         :____.....-------"""""" |'
              |          :     |______              🔥🔥🔥   ___!_ "#""#""#"""#"""#"""|           💀
            __|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
              "\-.      :      |#             🔥🔥🔥                    🔥🔥          |  💀           💀
                /#🔥🔥🔥|      /##,                                !                   |  
               .',/'\   |       #:#,                                ;       🔥🔥       |  
              /"\'#"\',.|       ##;#,         🔥🔥🔥🔥🔥🔥        !     🔥🔥🔥🔥     |       💀
                    /;/`:       ######,          ____             _ :     🔥🔥🔥      |  
                   ###          /;"\.__"-._   """                   |===..🔥🔥🔥_ ____|  💀
                                       `--..`--.._____             _!_                    
                                                      `--...____,="_.'`-.____        
                                     💀          💀       💀
                    💀     💀
                               💀          💀                   💀             💀
                                                         💀
                                      💀                                       💀
                               💀             💀       💀         💀             
                        💀
                                                      💀                💀          💀
            ''')
        Game["Game"] = False
        Genocide = True
def Knight_Attack():

    global BlackKnightHp
    AttackChance = random.randint(1, 300)
    if AttackChance == 300:

        if BlackKnightHp > 0:
            time.sleep(1)
            if Kingdom_Inhabitants["Great Knight"] > 0:
                FightChance = random.randint(1, (10 - Kingdom_Inhabitants["Great Knight"]))
                if FightChance == 1:
                    GreatKnightChosen = random.choice(Great_Knights)
                    Fight1 = random.randint(25, 100)
                    Fight2 = random.randint(1, 500)
                    if Fight1 > Fight2:
                        print(f"{GreatKnightChosen} damaged Black Knight!")
                        BlackKnightHp -= 1
                        print(f"Black Knight Hp left: {'⚫' * BlackKnightHp}")
                        if BlackKnightHp < 1:
                            time.sleep(5)
                            print("THE BLACK KNIGHT IS VANQUISHED")
                    elif Fight1 < Fight2:
                        time.sleep(5)
                        print(f"{GreatKnightChosen} got crushed by Black Knight.")
                        time.sleep(3)
                        print("🪦")  # Welp, he's dead while your kingdom is burning.
                        Great_Knights.remove(GreatKnightChosen)
                        Kingdom_Inhabitants["Great Knight"] -= 1
                    else:
                        print("⚔")
                else:
                    Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
                    Fight2 = ENEMY["Power"] + random.randint(1, 500)
                    if Fight1 > Fight2:
                        print(f"The Black Knight took damage!")
                        BlackKnightHp -= 1
                        print(f"Black Knight Hp left: {'⚫' * BlackKnightHp}")
                        if BlackKnightHp < 1:
                            time.sleep(5)
                            print("THE BLACK KNIGHT IS VANQUISHED")

                    elif Fight1 < Fight2:
                        print("The Black Knight Crushed 500 WEAKLINGS")
                        for i in range(50):
                            time.sleep(0.1)
                            print("💀💀💀💀💀💀💀💀💀💀")
                        Kingdom_Inhabitants["Troops"] -= 500
                    else:
                        print("The Black Knight Crushed 100 WEAKLINGS")
                        for i in range(10):
                            time.sleep(0.1)
                            print("💀💀💀💀💀💀💀💀💀💀")
                        Kingdom_Inhabitants["Troops"] -= 100
            else:
                Fight1 = Kingdom_Inhabitants["Power"] + random.randint(1, 15)
                Fight2 = ENEMY["Power"] + random.randint(1, 500)
                if Fight1 > Fight2:
                    print(f"The Black Knight took damage!")
                    BlackKnightHp -= 1
                    print(f"Black Knight Hp left: {'⚫' * BlackKnightHp}")
                    if BlackKnightHp < 1:
                        time.sleep(5)
                        print("THE BLACK KNIGHT IS VANQUISHED")

                elif Fight1 < Fight2:
                    print("The Black Knight Crushed 500 WEAKLINGS")
                    for i in range(50):
                        time.sleep(0.1)
                        print("💀💀💀💀💀💀💀💀💀💀")
                    Kingdom_Inhabitants["Troops"] -= 500
                else:
                    print("The Black Knight Crushed 100 WEAKLINGS")
                    for i in range(10):
                        time.sleep(0.1)
                        print("💀💀💀💀💀💀💀💀💀💀")
                    Kingdom_Inhabitants["Troops"] -= 100


def DIE():

    AttackChance = random.randint(1, 500)
    if AttackChance == 500:
        print(Lucius)
        time.sleep(3)
        print("The devil crushes 10000 of your weaklings.")
        time.sleep(1)
        for i in range(1000):
            print("💀💀💀💀💀💀💀💀💀💀")
        Kingdom_Inhabitants["Troops"] -= 10000
    elif AttackChance == 1:
        time.sleep(1)
        print("The devil summons 1000 more Troops!")
        ENEMY["Amount"] += 1000
    elif AttackChance == 250:
        print(Lucius)
        time.sleep(3)
        print("THE DEVIL ERUPTS FIRE AND BURNS THE BATTLE FIELD")
        goodguysdead = random.randint(1, 50000)
        badguysdead = random.randint(1, 50000)
        for i in range(1000):
            print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
        print(f"{goodguysdead} of your troops turned to ash!")
        print(f"{badguysdead} demons turned to ash!")
def FinalDuel(Bad_Ending):
    Life = 1
    Damage = 10000
    KingDamage = 2
    LuciusHp = 100000
    KingHp = 100
    HealPower = 50
    for i in range(1000):
        print(" ")
    time.sleep(3)
    print("Let us end this")
    time.sleep(1)
    print("The first light stands before you...")

    while True:
        print(r'''
            ⠀⠀⣀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣠⣤⡀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢸⣧⠞⠁⡷⢿⣦⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣆⠀⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣼⢪⡇⠀⠀⣷⣶⢹⡇⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠉⠉⠉⢩⠉⠙⠛⣿⠛
        ⣿⣿⣿⣿⣿⣿⣷⡄⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢹⠘⣷⣄⢳⣿⣿⣾⣗⡿⠀⠀⠀⠀⢀⣟⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀
        ⣿⣿⣿⣿⣿⣿⡍⠉⠀⠘⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠿⡄⠀⠀⠀⢸⠆⣿⣿⡏⣿⣿⣿⡗⣧⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣄⢧⡀⣀⡴⠋⢀⣿⣿⣷⣿⣿⣿⡇⢩⡳⢤⣀⢠⣿⣟⣿⣿⠀⢀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⢫⠿⠟⢳⡇⠀⣼⣿⣿⣿⣿⣿⣿⣷⡀⢸⣷⡿⠟⠛⠛⢿⣿⣦⠓⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠑⠉⠀⠀⣾⡴⣾⡿⢹⠙⢿⡭⠭⠽⢿⣿⣿⡿⣅⣀⣀⣀⣰⣿⡟⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⢹⠋⠙⠛⢻⡿⣡⣿⠃⣸⡇⠈⠓⢤⣀⠈⠁⣿⡤⢤⣤⣬⠟⢻⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⡼⢀⣠⣴⣿⡟⠛⠁⠀⡏⠀⠀⠀⠂⢹⣷⣤⣾⣧⣶⣾⡍⢛⣿⣿⣿⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⣼⡵⠋⢹⣿⣿⣧⠀⠀⠀⡷⠀⠸⡷⣤⣴⡿⣿⣿⣿⣿⣵⣿⣶⣿⣿⡛⠒⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠂⠀⠀⠀⠀⠀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠃⠀⠀⠀⠀⠀⠀⡼⠛⢻⣿⡀⠀⠀⣇⣀⡆⣀⣼⣟⡂⣹⣿⣿⠻⣧⠀⠈⠉⣻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⠀⢀⡌⠀⠀⠀⠀
        ⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⢀⣼⣧⣤⣼⣿⡇⠀⠀⣿⢿⣼⠟⠋⠹⣿⣿⣿⡏⠀⠹⣦⣤⣾⡿⣻⣟⣛⣦⡄⠀⠀⠀⠀⢠⠞⠁⠀⢠⠞⠀⠀⠀⠀⠀
        ⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⢹⣿⣿⣿⣿⡟⠳⡄⣿⣾⣿⠾⠿⠿⣿⡿⢿⠁⠀⠀⠹⣿⡿⠾⣿⣿⡅⢸⠃⠀⠀⢀⡴⠋⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠙⣿⣿⣿⡇⢄⠈⢿⡿⢁⣴⡾⢿⢿⣿⣿⣇⠀⠀⠘⣿⡁⠠⣿⣿⠳⡾⠀⢀⡴⠋⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⢀⣼⠟⣿⣟⡀⠈⠑⣿⣿⣿⣭⣷⢾⣿⣿⣿⠿⣦⠀⠀⠹⣷⠈⢹⣿⣦⣵⡴⠋⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠡⠀⣴⢿⡾⠛⠀⣹⣆⠀⣸⣿⣿⣭⣾⡟⠻⣥⣐⣦⠈⡇⠀⠀⢹⡄⢸⣿⡇⡏⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⢟⣿⣿⠟⢠⢃⡼⣿⡟⢷⣸⣿⣿⣿⣿⣿⣦⡈⠻⠛⠉⢳⠀⢐⣿⣧⠈⣿⡋⠁⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⢛⣾⣿⠋⢀⡼⠋⠀⣿⡇⠈⢻⢟⡟⣿⣿⣿⠙⣿⣦⣶⡖⠒⣷⣾⣿⡟⢳⣿⡗⢶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⣼⣿⣧⣤⡾⠁⠀⣀⣿⡇⠇⢀⡾⡇⣿⣧⣿⠀⠸⣿⣿⣿⠲⣼⠻⢿⣇⣺⣿⣧⣼⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⠃⢠⡾⠁⢹⡇⠀⠚⠁⣷⣿⠷⠘⢷⡄⠀⠀⢹⡆⢸⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⣀⣤⣿⣿⣿⡿⢸⣿⠁⠀⢸⣷⠀⠀⢸⢹⣿⣗⠂⠀⠹⣆⠀⠈⣿⢸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢬⣹⣿⢿⣿⣿⡿⠋⠀⣾⡇⣠⣴⣿⣿⢦⡀⣼⣸⣿⣿⣦⡀⠀⢹⡆⠂⣿⣿⣿⣿⣿⣿⠛⢦⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠟⣻⢿⣿⣯⣀⡀⣼⣿⠋⠁⣈⣿⣿⣷⣻⣿⣿⣿⣿⣿⣁⣀⢸⣿⣶⣿⣿⣿⣿⣿⣿⣷⡈⢧⡘⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣯⠞⠁⣠⠿⠛⠻⢱⣿⡇⠠⠾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⡻⣿⣿⣿⣆⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢞⣿⠏⠀⣰⠋⠀⠀⠀⢀⣿⡟⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣬⣭⣿⣿⣿⣦⣝⢷⣄⠙⢿⣿⣷⣌⠃⢀⠀⠀⠀⠏⠉⠛⠳⠄⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣀⡴⢫⠞⠁⢀⡾⠁⠀⠀⠀⠀⣼⣿⣠⡶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡟⢿⣿⣿⣯⡳⣝⠷⣿⣿⣟⠿⠻⢦⣄⡀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⣰⠋⡴⠃⢀⡴⠋⠀⠀⠀⠀⣠⢰⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⢸⣿⣿⣿⣿⣾⣿⣿⠿⡟⠶⣤⣄⡙⠙⢦⣝⠷⣄⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⡴⠃⠈⢀⣴⠋⠀⠀⠀⠀⠀⢠⢧⣿⣿⣿⢣⡿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣍⠙⠳⢶⣌⠁⠈⢳⡄⠀⠀⠀⠀
        ⠀⠀⠀⠀⣸⠁⣀⡴⠛⠁⠀⠀⠀⠀⠀⢠⢏⣿⣿⣿⠹⡟⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣙⠓⠈⠀⠁⠀⠀⠀⠀
        ⠀⠀⠀⠀⠻⠚⠁⠀⠀⠀⠀⠀⠀⠀⢠⣟⣾⣿⣿⣿⠀⡴⠋⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣃⡃⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⠴⠒⢋⣾⣿⣿⣿⠇⡀⠂⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣙⡇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠠⣄
        ⠀⠀⠀⠀⠀⠀⠀⠀⠉⣶⣎⣁⣀⣀⣼⣿⣿⣿⣿⡮⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢻⡇⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''')
        print(f"The Second Light Hp: {KingHp}")
        print(f"The First Light Hp: {BlackKnightHp}")
        print("The Black Knight raises his blade")
        print("What will you do? (1) Talk (2) Attack (3) Heal")
        CombatChoice = input(">")
        if CombatChoice == "1":
            print(
                "What do you want to say? (1) Your awful you know that? (2) You can still be saved! (3) You still have good in you!.")
            MoralChoice = input(">")
            if MoralChoice == "1":
                print("It does nothing.")
                time.sleep(1)
            elif MoralChoice == "2":
                print("It does nothing.")
                time.sleep(1)
            elif MoralChoice == "3":
                print("It does nothing.")
                time.sleep(1)
        elif CombatChoice == "2":
            print("You struck him!")
            DamageTaken = random.randint((KingDamage // 2), KingDamage)
            LuciusHp -= DamageTaken
            print(f"You took {DamageTaken} damage!")
        elif CombatChoice == "3":
            print(f"You healed {HealPower} hp!")
            KingHp += HealPower
        print(random.choice(["You know nothing of how cruel this world is.", "ALL WILL BE MINE, ALL THE ENERGY, ALL THE POWER!!!", "It is hopeless to defy me!", "Destruction is inevitable."]))
        Hit = random.randint(1, Damage)
        KingHp -= Hit
        print(f"The first light struck you, taking {Hit} damage!")
        if KingHp < 1:
            if Life == 1:
                print("You failed so easily...")
                time.sleep(6)
                print(r"Don't you understand? YOU ARE WEAK, BEING 'FRIENDLY' AHCHIEVES NOTHING BUT PAIN TOWARDS YOURSELF.")
                time.sleep(7)
                print("As all the souls of the kingdom's you've made peace with unite, you feel something in your soul.")
                time.sleep(3)
                print("You feel LOVE, but, a pure, true form of it, and you transform...")
                time.sleep(1)
                for i in range(1000):
                    print(" ")
                time.sleep(1)
                print("YOU HAVE NOW GROWN MORE POWERFUL.")
                HealPower = 6000
                KingDamage = 10000
                Life = 2
            elif Life == 2:
                print("How pathetic, you died once again.")
                time.sleep(2)
                print("But somewhere deep down you know, this fight isn't over the world fades to black and you re awake at the dawn of the battle")
                time.sleep(5)
                FinalDuel()
        if LuciusHp < 1:
            print("You...")
            time.sleep(3)
            print("Fool...")
            time.sleep(3)
            print("DO YOU NOT UNDERSTAND??? I AM ETERNAL!!!")
            time.sleep(5)
            print("YOU TOOK ∞ DAMAGE!!!")
            time.sleep(3)
            print("You have fallen ill.")
            time.sleep(3)
            print("Do you not understand? I am immortal, you are nothing.")
            time.sleep(2)
            print("BANG!!!")
            time.sleep(2)
            print(r'''
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⡤⡀⠀⢀⣠⣂⣯⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠰⣧⡈⣩⣴⣿⣿⣷⣊⣀⠀⠀⠀⢀⢄⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠜⣃⣼⣿⣿⣧⣀⣑⣿⡇⣷⡙⠦⢂⣡⡾⢱⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢐⣡⣴⣾⡿⢋⣦⣷⣤⣍⠉⣿⣇⣹⣿⣷⣿⡟⠑⠯⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣶⣿⣿⣿⠟⣴⣿⣿⣿⣟⡁⢎⣽⣫⣾⣿⡿⠿⠿⣿⣰⠀⠀⢀⡀⢔⡂⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢏⡻⢿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⡡⠖⠉⠉⢁⠠⢐⣪⣵⣾⣟⡕⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⢂⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢽⠋⢀⡠⢐⣨⣴⣾⣿⣿⣿⣻⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⣭⡒⢄⠀⣠⣴⣵⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⡿⠁⣾⣶⣷⣿⣿⣿⣿⣿⣿⣿⢏⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡹⣿⣦⣑⠣⠿⣷⣦⣄⣀⣠⣴⣶⣿⣿⣿⣿⣿⣴⣾⣿⣿⣿⣿⣿⣿⣿⠟⠻⣯⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣯⣔⣂⠠⡄⣤⠒⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣙⡛⠿⣿⣿⣿⣿⣿⣿⣿⡿⡶⠋⠀⠀⠀⠀
⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡫⠚⠁⠀⠀⠀⠉⠓⢲⡆⣿⣿⣿⢏⠎⠀⠀⠀⠀⠀⠀
⠸⡇⢰⣶⣶⣶⣶⣶⣦⣤⣄⣈⣉⡒⠒⠂⠠⠤⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢠⢪⣿⣿⣿⣇⣮⣛⠿⣿⣿⣿⣿⣿⣿⣟⠈⠤⣴⡒⢆⠀⠀⠀⢀⢾⣾⣿⡿⡳⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣤⣭⣭⣁⣒⣒⢀⠤⠳⢿⣿⡿⣫⡾⣿⣛⣛⣀⣿⣿⣿⣿⣷⣶⣿⣿⡟⣩⠞⢀⡄⣲⣿⣿⣯⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠢⣙⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣶⣼⣥⣭⣍⣿⣛⣛⡻⡿⠿⠿⢿⠿⣩⣟⣱⢊⣴⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠒⠂⠤⠍⠉⣛⣛⡻⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⡭⣿⣿⠟⠁⠀⣿⣿⢃⠧⠀⠀⠀⠀⠀⠀⠤⠤⠤⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠈⠐⠒⢦⡭⢍⣭⣭⣍⣛⣛⣛⡛⢻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⡇⣿⣯⡀⣠⣼⡿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣷⡠⠖⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⣻⣾⣿⣿⣿⣿⣏⠏⠀⠀⠀⣽⣋⣾⣿⣶⣾⢟⣱⣷⢹⣷⣿⣾⢨⣾⠓⠌⣻⠿⡟⣋⠴⠬⠭⠭⢉⡉⢹⡿⣣⠚⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⣿⡿⠋⠀⢸⣿⡟⡍⠀⠀⠀⡰⣫⣿⣿⣿⣿⢋⡞⢸⡟⣾⣿⣿⣿⢸⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠘⠦⠓⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡼⣿⣇⣀⣤⣿⣿⠼⠀⠀⢀⠜⣴⣿⣿⣿⣿⣣⠊⠀⢀⡇⣿⣿⣿⣿⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢝⡻⠿⣟⡥⠊⠀⠀⢰⢫⣾⣿⣿⣿⣿⣥⣓⠠⢀⣨⢹⣿⣿⣿⣿⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢎⢿⣿⣿⣿⣿⣿⣿⣿⣷⣮⢼⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠂⠩⠭⠝⠛⣟⡿⢿⣿⢸⣿⣿⣿⡏⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⢝⡞⣿⣿⣿⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⢿⣿⣿⣧⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣸⣿⣿⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⢿⣿⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢏⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡼⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
            print("JULIAN HAS APPEARED AS THE WHITE KNIGHT!")
            time.sleep(3)
            print("ARE YOU A FOOL????")
            time.sleep(2)
            print("They clashed")
            time.sleep(2)
            for i in range(20):
                print("CLANG")
                time.sleep(1)
            print("But the Julian wasn't strong enough...")
            time.sleep(2)
            print("The first light holds Julian, and Julian sees his face.")
            time.sleep(3)
            print("Lucius???")
            time.sleep(1)
            print("How are you here???")
            time.sleep(3)
            print("My friend, I never left.")
            time.sleep(2)
            print("STAB")
            time.sleep(1)
            print("💀")
            time.sleep(5)
            print("What...")
            time.sleep(3)
            print("What??")
            time.sleep(2)
            print("The first light stumbles to the ground holding unto a friend from long ago...")
            print("WHAT HAVE I DONE???")
            time.sleep(2)
            print("No, no, no Julian wake up.")
            time.sleep(1)
            print("WAKE UP!!!")
            time.sleep(3)
            print("I... I... destroyed everyone I ever loved... just for nothing...")
            time.sleep(5)
            print(f"{name}, thank you... for letting me see... the truth...")
            for i in range(10000):
                print(" ")
            time.sleep(5)
            print("You wake up...")
            time.sleep(2)
            print("In the battlefield, the portal is gone")
            if Bad_Ending != True:
                time.sleep(2)
                print("You guys have won.")
                time.sleep(2)
                print("You have all... won.")
                time.sleep(3)
                print("And the world finally saw peace again.")
                time.sleep(2)
                print("You brought prosperity to the world...")
                time.sleep(10)
                print("You did great.")
                time.sleep(5)
                print("Thank you.")
                Game["Game"] = True
                break
            else:
                print("Verdania... Grados")
                time.sleep(3)
                print("Crystalia... Julian")
                time.sleep(2)
                print("All lost there armies and there rulers today... 2 million people")
                time.sleep(2)
                print("The kingdoms eventually got new rulers")
                time.sleep(5)
                print("But they forever mourned they're lost heroes...")
                time.sleep(3)
                print("Was it worth it?")
                time.sleep(5)
                print("Perhaps peace requires sacrifice...")
                Game["Game"] = True
                break

def LoseFinalBattle():
    time.sleep(5)
    print("Your army... every kingdoms army")
    time.sleep(2)
    print("Is dead.")
    time.sleep(2)
    print("So tell me...")
    time.sleep(2)
    print(Lucius)
    time.sleep(1)
    print("Why, should I stop?")
    time.sleep(3)
    print("(1) Because I know that deep inside you know, all of this is pointless (2) You won, what's the point anymore of talking?")
    Nhilist = input(">")
    if Nhilist == "1":
        print("No... it has a point... I love this world, and the only way to keep it that way... is to make sure I can never be hurt.")
        FinalDuel(True)
    elif Nhilist == "2":
        print("Good point...")
        FinalDuel(True)

def WinFinalBattle():
    time.sleep(5)
    print("My army... is defeated...")
    time.sleep(5)
    print("DO YOU KNOW WHO I AM????")
    time.sleep(1)
    FinalDuel(False)

def WAR(defend):
    global BlackKnight
    global King_Power
    global Reward
    global Victory
    global FINALBOSS
    DevilAttacks = False
    Battle = True
    from Data import kingdom
    time.sleep(1)
    print(f"""
######################################
                  WAR
######################################
= {kingdom} Soldiers: {Kingdom_Inhabitants["Troops"]}
= {ENEMY["Group"]} Soldiers: {ENEMY["Amount"]}
= {kingdom} Soldier level: {Kingdom_Inhabitants["Power"]}
= {ENEMY["Group"]} Soldier level: {ENEMY["Power"]}
#######################################
            🩸 = Troop killed an enemy
            💀 = Troop died
            ⚔ = Tie
#######################################
""")
    print("Do you want to join the battle? (1) Yes (2) No")
    BattleChoice = input(">")
    if FINALBOSS == True:
        time.sleep(5)
        print("You think you can beat him? You think you can beat me?")
        time.sleep(2)
        print("You... are... so... stupid.")
        time.sleep(2)
        print("Your soldiers will burn facing my will...")
        time.sleep(5)
        for i in range(300):
            print("")
        time.sleep(1)
        print("Not without us")
        time.sleep(5)
        print("You got 500,000 troops from Verdania!")
        Kingdom_Inhabitants["Troops"] += 500000
        time.sleep(5)
        print("You got 500,000 troops from Crystalia!")
        Kingdom_Inhabitants["Troops"] += 500000
        time.sleep(5)
        print("You got 100000 troops from Grados!")
        Kingdom_Inhabitants["Troops"] += 100000
        time.sleep(5)
        print("You got 100 troops from Hayden!")
        Kingdom_Inhabitants["Troops"] += 100
        time.sleep(10)
        print("You got... 1000000 troops from Julian.")
        Kingdom_Inhabitants["Troops"] += 1000000
        time.sleep(2)
        print("FOOOOOOOLS")
        time.sleep(1)
        print("""
  _____            __  __        _____   ____   _____  
 |_   _|     /\   |  \/  |      / ____| / __ \ |  __ \ 
   | |      /  \  | \  / |     | |  __ | |  | || |  | |
   | |     / /\ \ | |\/| |     | | |_ || |  | || |  | |
  _| |_   / ____ \| |  | |     | |__| || |__| || |__| |
 |_____| /_/    \_\_|  |_|      \_____| \____/ |_____/
        """)
        time.sleep(5)
        FINALBOSS = False
        DevilAttacks = True
    while Battle:
        if Kingdom_Inhabitants["Troops"] > 0 and ENEMY["Amount"] > 0:
            if BattleChoice == "1":
                KING()
            FIGHT()
            if BlackKnight == True:
                Knight_Attack()
            if DevilAttacks == True:
                DIE()


        elif ENEMY["Amount"] <= 0:
            if defend == True:
                print("The enemy has been vanquished and your kingdom is defended!")
                Battle = False
            else:
                if DevilAttacks == False:
                    King_Power += 10
                    print(f"You crushed your enemy and destroyed the kingdom of {ENEMY['Group']}")
                    if ENEMY["Group"] == "Julian":
                        Reward = random.randint(5000000000, 100000000000)
                    elif ENEMY["Group"] == "Crystalia":
                        Reward = random.randint(500000000, 10000000000)
                    elif ENEMY["Group"] == "Verdania":
                        Reward = random.randint(500000000, 10000000000)
                    elif ENEMY["Group"] == "Grados":
                        Reward = random.randint(5000000, 100000000)
                    elif ENEMY["Group"] == "Hayden":
                        Reward = random.randint(50000, 1000000)
                    print(f"You got {Reward} gold!")
                    Kingdom_Assets["Gold"] += Reward
                    Battle = False
                    Victory = True
                else:
                    WinFinalBattle()


        elif Kingdom_Inhabitants["Troops"] <= 0:
            if defend == True:
                if Genocide == False:
                    Kingdom_Destruction()
                else:
                    global Game
                    Game = False
                    time.sleep(10)
                    print(r'"As long as humans want power, fame, glory, there will never be peace. This war is never ending." Lucius')
                    time.sleep(5)
                    print(f"Every one is dead in your kingdom, don't worry... it was only {Kingdom_Inhabitants['Peasants']} people, not much.")
                    time.sleep(5)
                    print("I wonder whose fault was it?")
                    time.sleep(5)
                    print("GAME OVER")
                    time.sleep(1000)
                    print("Why are you still here?")
                    time.sleep(5)
                    print("You think the world does not move on from you?")
                    time.sleep(5)
                    print("Go, click run again, maybe you'll do better.")

            else:
                if DevilAttacks != False:
                    print("Your invasion lost, your army died, how do you feel?")
                    Victory = False
                    Battle = False
                else:
                    LoseFinalBattle()

        if defend == True:
            if Kingdom_Properties["Arrow Towers"] > 0:
                for i in range(Kingdom_Properties["Arrow Towers"]):
                    Killed = random.randint(1, 3)
                    if Killed == 1:
                        print("""
                                        A arrow tower just killed 3 troops!
                                        🩸🩸🩸""")
                        ENEMY["Amount"] -= 3

            if Kingdom_Properties["Cannon Tower"] > 0:
                for i in range(Kingdom_Properties["Arrow Towers"]):
                    Killed = random.randint(1, 6)
                    if Killed == 1:
                        print("""
                                        A cannon tower just killed 9 troops!
                                        🩸🩸🩸🩸🩸🩸🩸🩸🩸""")
                        ENEMY["Amount"] -= 9




def negotation():
    print("""
    Which kingdom do you want to communicate too?
    (1) Verdania
    (2) Crystalia
    (3) Grados
    """)
    Talk = input(">")
    if Talk == "1":
        if peacekingdoms["Verdania"] == True:
            print("""
            We are willing for you to give us Iron for 3500 gold per unit! (1) Trade (2) No""")
            Trade = input(">")
            if Trade == "1":
                print("How much?")

                try:
                    Amount = int(input(">"))
                    if Amount > 0:
                        if Amount <= Kingdom_Assets["Iron"]:
                            print("Great trade! I'm glad we can find use between each other.")
                            Kingdom_Assets["Gold"] += (Amount * 3500)
                            Kingdom_Assets["Iron"] -= Amount
                        else:
                            print("You don't have it!")
                    else:
                        print("A negative amount???")
                except ValueError:
                    print("That is... not a number.")
        else:
            print("We don't trust you.")
    if Talk == "2":
        if peacekingdoms["Crystalia"] == True:
            print("""
            We are willing to give Titanium for 7500000 per unit! (1) Trade (2) No""")
            Trade = input(">")
            if Trade == "1":
                print("How much?")

                try:
                    Amount = int(input(">"))
                    if Amount > 0:
                        if (Amount * 7500000) <= Kingdom_Assets["Gold"]:
                            print("Deal!")
                            Kingdom_Assets["Gold"] -= (Amount * 7500000)
                            Kingdom_Assets["Titanium"] += Amount
                        else:
                            print("You don't have it!")
                    else:
                        print("A negative amount???")
                except ValueError:
                    print("That is... not a number.")
        else:
            print("We don't trust you.")
    if Talk == "3":
        if peacekingdoms["Grados"] == True:
            print("""
            We are willing for you to give us Wood for 150 gold per unit! (1) Trade (2) No""")
            Trade = input(">")
            if Trade == "1":
                print("How much?")
                try:
                    Amount = int(input(">"))
                    if Amount > 0:
                        if Amount <= Kingdom_Assets["Wood"]:
                            print("Great trade! I'm glad we can find use between each other.")
                            Kingdom_Assets["Gold"] += (Amount * 150)
                            Kingdom_Assets["Wood"] -= Amount
                        else:
                            print("You don't have it!")
                    else:
                        print("A negative amount???")
                except ValueError:
                    print("That is... not a number.")
        else:
            print("We don't trust you.")







# You will never know what happened to King Lucius
def invaded():
    global InvasionChance
    if TribesAndKingdoms["Julian"] != "EXTINCT":
        if peacekingdoms["Julian"] != True:
            if Reputation["Julian"] != "Glad" and Reputation["Julian"] != "Fine":
                if Reputation["Julian"] == "Angered" or Reputation["Julian"] == "Terrible":
                    InvasionChance = random.randint(1, 10)
                    ENEMY["Power"] = InvadePower["Julian"]
                    ENEMY['Group'] = "Julian"
                    ENEMY["Amount"] = 200000
                else:
                    if Kingdom_Assets["Gold"] > 100000000:
                        InvasionChance = random.randint(1, 600)
                        ENEMY['Group'] = "Julian"
                        ENEMY["Amount"] = 2000
                        ENEMY["Power"] = InvadePower["Julian"]
                        TribesAndKingdoms["JulianPower"] = 3
                    if InvasionChance == 1:
                        WAR(True)

    if TribesAndKingdoms["Verdania"] != "EXTINCT":
        if Reputation["Verdania"] != "Glad" and Reputation["Verdania"] != "Fine":
            InvasionChance = random.randint(1, 30)
            if InvasionChance == 1:
                ENEMY['Group'] = "Verdania"
                ENEMY["Amount"] = 100000
                ENEMY["Power"] = InvadePower["Verdania"]
                WAR(True)
    if TribesAndKingdoms["Crystalia"] != "EXTINCT":
        if Reputation["Crystalia"] != "Glad" and Reputation["Crystalia"] != "Fine":
            InvasionChance = random.randint(1, 30)
            if InvasionChance == 1:
                ENEMY['Group'] = "Crystalia"
                ENEMY["Amount"] = 50000
                ENEMY["Power"] = InvadePower["Crystalia"]
                WAR(True)

def invade():
    global LOVE
    global Game
    global Victory
    global King_Power
    print(f'''
                      World Map
############################################################
                       ,-.^._                 _
                     .'      `-.            ,' ;
          /`-.  ,----'         `-.   _  ,-.,'  `
       _.'   `--'                 `-' '-'      ;
      :                                       ;    __,-.
      ,'              Verdania: {TribesAndKingdoms["Verdania"]}             ;_,-',.__'--.
     :  Julian: {TribesAndKingdoms["Julian"]}                            ,--```    `--'
     :                                      ;
     :                                      :
     ;        Grados: {TribesAndKingdoms["Grados"]}                       :
    (                                       ;
     `-.  Cave Of Mystery                  ,'
       ;                   Hayden: {TribesAndKingdoms["Hayden"]}      :
     .'                             .-._,'
   .'        Hell Portal: {TribesAndKingdoms["Hell Portal"]}         `.
_.'                                .__;
`._                               ;
   `.        Crystalia: {TribesAndKingdoms["Crystalia"]}       :    ,---------------------.
     `.               ,..__,---._;    |    World map        |
       `-.__         :                | Population:  {TribesAndKingdoms["Total Population"]}     |
            `.--.____;                |                     |
                                      |                     |
                                      |                     |
                                      `---------------------'
##############################################################
Which do you want to invade?
(1) Verdania
(2) Julian
(3) Grados
(4) Hayden
(5) Crystalia
(6) Hell Portal 
(#) Cave Of Mystery
(7/else) Exit
''')
    WarChoice = input(">")
    if WarChoice == "1":
        if peacekingdoms["Verdania"] == False:
            if TribesAndKingdoms["Verdania"] != "EXTINCT":
                ENEMY['Group'] = "Verdania"
                ENEMY["Amount"] = 100000
                WAR(False)
                ENEMY["Power"] = TribesAndKingdoms["VerdaniaPower"]
                if Victory == True:
                    LOVE["LOVE"] += 1
                    if TribesAndKingdoms["Verdania"] == "Powerful":
                        TribesAndKingdoms["Verdania"] = "Weakened"
                        Reputation["Verdania"] = "Angered"
                        InvadePower["Verdania"] = 7
                        TribesAndKingdoms["VerdaniaPower"] = 6
                    elif TribesAndKingdoms["Verdania"] == "Weakened":
                        Reputation["Verdania"] = "Terrible"
                        TribesAndKingdoms["Verdania"] = "Weak"
                        TribesAndKingdoms["VerdaniaPower"] = 12
                        InvadePower["Verdania"] = 13
                    elif TribesAndKingdoms["Verdania"] == "Weak":
                        Reputation["Verdania"] = "Burn in Hell"
                        TribesAndKingdoms["Verdania"] = "EXTINCT"
                        TribesAndKingdoms["Total Population"] -= 5000000
                        Kingdom_Assets["Land"] += 2000000

            else:  # Stupid monkey, you deserved to be destroyed.
                print(
                    "Verdania the kingdom of lush plants, peace, and love. 5,000,000 people, Children, Families, GONE, Isn't it amazing?")
                time.sleep(5)
        else:
            print("Verdania is at peace with you, you can't invade them buddy.")


    elif WarChoice == "2":
        if peacekingdoms["Julian"] == False:
            if TribesAndKingdoms["Julian"] != "EXTINCT":
                if TribesAndKingdoms["Julian"] != "Desperate":
                    ENEMY['Group'] = "Julian"
                    ENEMY["Amount"] = 200000
                    WAR(False)
                    ENEMY["Power"] = TribesAndKingdoms["JulianPower"]
                    if Victory == True:
                        LOVE["LOVE"] += 1
                        if TribesAndKingdoms["Julian"] == "Hyper Powerful":
                            Reputation["Julian"] = "Angered"
                            TribesAndKingdoms["JulianPower"] = 9
                            TribesAndKingdoms["Julian"] = "Powerful"
                            InvadePower["Julian"] = 10
                        elif TribesAndKingdoms["Julian"] == "Powerful":
                            Reputation["Julian"] = "Angered"
                            TribesAndKingdoms["JulianPower"] = 12
                            TribesAndKingdoms["Julian"] = "Weakened"
                            InvadePower["Julian"] = 13
                        elif TribesAndKingdoms["Julian"] == "Weakened":
                            Reputation["Julian"] = "Terrible"
                            TribesAndKingdoms["Julian"] = "Weak"
                            TribesAndKingdoms["JulianPower"] = 16
                            InvadePower["Julian"] = 16
                        elif TribesAndKingdoms["Julian"] == "Weak":
                            TribesAndKingdoms["Julian"] = "Desperate"
                if TribesAndKingdoms["Julian"] == "Desperate":
                    if TribesAndKingdoms["Grados"] == "EXTINCT" and TribesAndKingdoms["Verdania"] == "EXTINCT" and \
                            TribesAndKingdoms["Hayden"] == "EXTINCT" and TribesAndKingdoms["Crystalia"] == "EXTINCT":
                        time.sleep(10)
                        print("You walk though a shore...")
                        time.sleep(5)
                        print("You look at the sunset...")
                        time.sleep(3)
                        print("For a tiny bit, you feel joy...")
                        time.sleep(3)
                        print("The world is finally empty...")
                        time.sleep(3)
                        print("All quiet... peace blooms inside your mind...")
                        time.sleep(10)
                        print("Nobody is here, it's just you...")
                        time.sleep(5)
                        print("And me")
                        time.sleep(5)
                        print("Let's watch this sunset one last time... because after this... we finish the job.")
                        time.sleep(30)
                        print("Thank you... my companion...")
                        time.sleep(3)
                        print("You march with your army towards the kingdom of Julian.")
                        time.sleep(10)
                        print("You...")
                        time.sleep(5)
                        print("Killed them all... all those lives...")
                        time.sleep(5)
                        print("GONE... just gone...")
                        time.sleep(2)
                        print("Sorry, your probably waiting to get rid of me, aren't you?")
                        time.sleep(5)
                        print("I've seen your kind before...")
                        time.sleep(5)
                        print(
                            "When lucius came, I trusted him... but he then proceeded to commit genocide to millions...")
                        time.sleep(5)
                        print(
                            "Everyone trusted him, and he betrayed that trust, so I knew when someone like you came along you would too...")
                        time.sleep(5)
                        print("Here I have an army of 100000 experimental titanium knights, all fueled by magic...")
                        time.sleep(5)
                        print("I")
                        time.sleep(5)
                        print("KING JULIAN III")
                        time.sleep(5)
                        print("WILL BRING JUSTICE TO THE WORLD!")
                        time.sleep(5)
                        print("BY SENDING YOU TO HELL!")
                        time.sleep(1)
                        TribesAndKingdoms["Julian"] = "Desperate"
                        TribesAndKingdoms["JulianPower"] = 28
                        Reputation["Julian"] = "I will... kill you, and burn everything you have."
                        ENEMY['Group'] = "Titanium Knights"
                        ENEMY["Amount"] = 100000
                        ENEMY["Power"] = 28
                        WAR(False)
                        ENEMY["Power"] = TribesAndKingdoms["JulianPower"]
                        if Victory == True:
                            TribesAndKingdoms["Total Population"] -= 11000000
                            LOVE += 1
                            TribesAndKingdoms["Julian"] = "EXTINCT"
                            time.sleep(5)
                            print("You hear a screams of terror...")
                            time.sleep(5)
                            print("You have won...")
                            time.sleep(5)
                            print("BANG!")
                            time.sleep(1)
                            print("You...")
                            time.sleep(2)
                            print("Killed my army.")
                            time.sleep(2)
                            print("Now, you will kill my people...")
                            time.sleep(2)
                            print("YAH!")
                            time.sleep(2)
                            print(
                                "He lunged towards you, you both clashed your blades, but you overpowered him with ease...")
                            time.sleep(3)
                            print("Look at me...")
                            time.sleep(2)
                            print("Failing to even be able to fight one person...")
                            time.sleep(2)
                            KillChoice = input("Kill or No?").lower()
                            if KillChoice == "kill":
                                good_ending()
                                Kingdom_Assets["Land"] += 5000000

                            elif KillChoice == "no":
                                print("You would give me mercy?")
                                time.sleep(2)
                                print("Thank you...")
                                time.sleep(2)
                                print("So much...")
                                time.sleep(1)
                                print("💀")
                                time.sleep(5)
                                print("DIE")
                                time.sleep(3)
                                print("GAME OVER")
                                Game = False
                                time.sleep(10)
                                print(
                                    "YOU IDIOT, VICTORY WAS THAT CLOSE AND YOU RAN AWAY FROM FINISHING THE JOB. STUPID. IMBECILE!")


                        else:
                            time.sleep(5)
                            print("Pathetic, now watch your kingdom burn.")
                            TribesAndKingdoms["JulianPower"] = 28
                            ENEMY['Group'] = "Julian"
                            ENEMY["Amount"] = 100000
                            ENEMY["Power"] = 28
                            WAR(True)
                    else:
                        print(
                            "You think you should destroy the rest of the other kingdoms first, Julian has given up invading you anyway...")



            else:  # YES it worked
                print(
                    "Julian, the city of art, culture, with they're ever arrogant leader, humble people, who innovated, created, and brought the future to the present, well they're now gone. Only 200,000,000 people.")
                time.sleep(5)
        else:
            print("They have a peace treaty with you, you cannot break it.")

    elif WarChoice == "3":
        if peacekingdoms["Grados"] == False:
            if TribesAndKingdoms["Grados"] != "EXTINCT":
                ENEMY['Group'] = "Grados"
                ENEMY["Amount"] = 20000
                WAR(False)
                ENEMY["Power"] = TribesAndKingdoms["GradosPower"]
                if Victory == True:
                    LOVE["LOVE"] += 1
                    if TribesAndKingdoms["Grados"] == "Powerful":
                        TribesAndKingdoms["Grados"] = "Weakened"
                        TribesAndKingdoms["GradosPower"] = 5
                    elif TribesAndKingdoms["Grados"] == "Weakened":
                        Reputation["Grados"] = "Angered"
                        TribesAndKingdoms["Grados"] = "Weak"
                        TribesAndKingdoms["GradosPower"] = 7
                    elif TribesAndKingdoms["Grados"] == "Weak":
                        Reputation["Grados"] = "Burn In hell"
                        TribesAndKingdoms["Grados"] = "EXTINCT"
                        Kingdom_Assets["Land"] += 50000
                        TribesAndKingdoms["Total Population"] -= 43056

            else:
                print(
                    "More of a Tribe, with honor, respect, and great food culture, it was only 43,000 people, Isn't it nice, now that they are quiet.")
                time.sleep(5)
        else:
            print("You have peace treaty with them, why would you invade them?")

    elif WarChoice == "4":
        if peacekingdoms["Hayden"] == False:
            if TribesAndKingdoms["Hayden"] != "EXTINCT":
                ENEMY['Group'] = "Hayden"
                ENEMY["Amount"] = 20
                WAR(False)
                ENEMY["Power"] = TribesAndKingdoms["HaydenPower"]
                if Victory == True:
                    LOVE["LOVE"] += 1
                    if TribesAndKingdoms["Hayden"] == "Powerful":
                        TribesAndKingdoms["HaydenPower"] = 2
                        TribesAndKingdoms["Hayden"] = "Weakened"
                    elif TribesAndKingdoms["Hayden"] == "Weakened":
                        TribesAndKingdoms["HaydenPower"] = 14
                        TribesAndKingdoms["Hayden"] = "Weak"
                    elif TribesAndKingdoms["Hayden"] == "Weak":
                        TribesAndKingdoms["Hayden"] = "EXTINCT"
                        Kingdom_Assets["Land"] += 300
                        TribesAndKingdoms["Total Population"] -= 200

            else:  # Cowards, weaklings, all will fall
                print(
                    "A peaceful village full of peasants, with there love for trade and commune, they had an extremly small army but they fought with there might in the end. How pathetic.")
                time.sleep(5)
        else:
            print("Oh hi buddy? Why did you come? Sorry, I'm busy right now.")

    elif WarChoice == "5":
        if peacekingdoms["Crystalia"] == False:
            if TribesAndKingdoms["Crystalia"] != "EXTINCT":
                ENEMY['Group'] = "Crystalia"
                ENEMY["Amount"] = 100000
                WAR(False)
                ENEMY["Power"] = TribesAndKingdoms["CrystaliaPower"]
                if Victory == True:
                    LOVE["LOVE"] += 1
                    if TribesAndKingdoms["Crystalia"] == "Powerful":
                        Reputation["Crystalia"] = "Sworn Enemy"
                        TribesAndKingdoms["CrystaliaPower"] = 7
                        TribesAndKingdoms["Crystalia"] = "Weakened"
                        InvadePower["Crystalia"] = 8
                    elif TribesAndKingdoms["Crystalia"] == "Weakened":
                        TribesAndKingdoms["CrystaliaPower"] = 13
                        TribesAndKingdoms["Crystalia"] = "Weak"
                        InvadePower["Crystalia"] = 13
                    elif TribesAndKingdoms["Crystalia"] == "Weak":
                        TribesAndKingdoms["Crystalia"] = "EXTINCT"
                        Kingdom_Assets["Land"] += 2000000
                        TribesAndKingdoms["Total Population"] -= 7000000
                else:  # I... no... let them burn
                    print(
                        "The rulers of the ice ruled with peace and prosperity allowing for waterflow around the whole island and having vigorous trade with other empires. Now, they've been defeated by your strenght.")
                    time.sleep(5)
        else:
            print("You have a peace treaty, don't break it.")

    elif WarChoice == "6":
        if The_Devil["HATE"] > 10000:
            print("So... you made peace with everyone...")
            time.sleep(3)
            print("And now... you dare try to get rid of me...")
            time.sleep(2)
            print("Well... fine")
            TRUE_FINAL_BOSS()

        else:
            print("You think you are allowed to invade here??")
    if WarChoice == "#":
        ClownOfMadness()
    else:
        print("Coward, just wanted to see the status of your neighbors")

def people():
    NumberOfJoined = 0
    if Kingdom_Properties["Houses"] > Kingdom_Inhabitants["Peasants"]:
        empty_beds = Kingdom_Properties["Houses"] - Kingdom_Inhabitants["Peasants"]

        for i in range(empty_beds):
            chance = random.randint(1, 10)
            if chance == 1:
                Kingdom_Inhabitants["Peasants"] += 1
                NumberOfJoined += 1

    if Settings["Peasants"] == True:
        print(f"{NumberOfJoined} Joined your kingdom today.")
    if Castle["Castle"] == False:
        if Kingdom_Properties["Castle Hull"] >= 10:
            time.sleep(5)
            print("THE CASTLE IS COMPLETE")
            Castle["Castle"] = True
    if Castle["Castle"] == True:
        if GreatKnightsAvailable:
            Join = random.randint(1, 90)
            if Join == 1:
                GreatKnightComing = random.choice(GreatKnightsAvailable)
                Great_Knights.append(GreatKnightComing)
                GreatKnightsAvailable.remove(GreatKnightComing)
                print(f"{GreatKnightComing} Joined your empire.")
                Kingdom_Inhabitants["Great Knight"] += 1




def Tax():
    global Tax_Countdown
    Tax_Countdown -= 1
    if Tax_Countdown <= 0:
        print("Tax day! Yeepe! Time to take the hard earned money of your inhabitants.")
        for i in range(Kingdom_Inhabitants["Peasants"]):
            Kingdom_Assets["Gold"] += random.randint(1, 500)
        max_productive_farms = Kingdom_Inhabitants["Peasants"] // 100
        active_farms = min(Kingdom_Properties["Farms"], max_productive_farms)
        for i in range(active_farms):
            Kingdom_Assets["Gold"] += random.randint(10, 30)
        Tax_Countdown = random.randint(29,  31)
        Kingdom_Assets["Gold"] -= (Kingdom_Inhabitants["Troops"] * 1000)
#  01010011 01101000 01100101 00100000 01110111 01100001 01110011 00100000 01101101 01101001 01101110 01100101 00101110
def Hire():
    print("Troop = 1000 gold per Tax Cycle")
    Hire_Choice = input("Do you want to hire a Soldier? (1) yes (2) no")
    if Hire_Choice == "1":
        Hire_Number = int(input("""
        How much soldiers would you like to hire (don't hire more than your tax income)"""))
        if Hire_Number <= Kingdom_Inhabitants["Peasants"]:
            if Kingdom_Assets["Gold"] > (Kingdom_Inhabitants["Troops"] * 1000):
                max_productive_farms = Kingdom_Inhabitants["Peasants"] * 100
                active_farms = min(Kingdom_Properties["Farms"], max_productive_farms)

                estimated_income = (Kingdom_Inhabitants["Peasants"] * 250) + (active_farms * 20)
                current_costs = (Kingdom_Inhabitants["Troops"] + Hire_Number) * 1000

                if current_costs < estimated_income:
                    Kingdom_Inhabitants["Troops"] += Hire_Number
                    Kingdom_Assets["Gold"] -= (Kingdom_Inhabitants["Troops"] * 1000)
                else:
                    print("Your current estimated tax fund is lower than that. Don't you read kingdom stats?")
                    time.sleep(1)
                    print("Do you want to hire them anyway? (1) Yes (2) No")
                    Answer = input(">")
                    if Answer == "1":
                        if Kingdom_Assets["Gold"] > (Kingdom_Inhabitants["Troops"] * 1000):
                            print("Ok, don't blame me when you lose them due to low funding.")
                            Kingdom_Inhabitants["Troops"] += Hire_Number
                            Kingdom_Assets["Gold"] -= (Kingdom_Inhabitants["Troops"] * 1000)
                        else:
                            print("You don't even have enough for there starting pay! Is this some joke???")

                    if Answer == "2":
                        print("Good")
                    else:
                        print("That is not an answer fool.")
            else:
                print("Your hiring more soldiers than people in your kingdom?")


        else:
            print("You don't even have enough money for there starting pay. Pathetic.")
def Food():
    if Kingdom_Inhabitants["Peasants"] >= (Kingdom_Properties["Farms"] * 100):
        print("People are happy, paying for your overpriced food.")
    else:
        KILL = random.randint(1, (Kingdom_Inhabitants["Peasants"] - (Kingdom_Properties["Farms"] * 100)))
        print(f"Around the kingdom, {KILL} people starved and died")
        Kingdom_Inhabitants["Peasants"] -= KILL


def negativemoney():
    if Kingdom_Assets["Gold"] < 0:
        Loss = abs(Kingdom_Assets["Gold"]) // 1000
        if Loss > Kingdom_Inhabitants["Troops"]:
            Loss = Kingdom_Inhabitants["Troops"]
        Kingdom_Inhabitants["Troops"] -= Loss
        print(f"You lost {Loss} troops due to underfunding. How cheap.")
        Kingdom_Assets["Gold"] = 0
def specialattack():
    specialattacknumber = random.randint(1, 9)
    if specialattacknumber == 1:
        print("The demons called some support!")
        ENEMY["Amount"] += Kingdom_Inhabitants["Troops"] // 10
    elif specialattacknumber == 2:
        if Kingdom_Inhabitants["Troops"] > 999:
            print("The demons dropped a bomb killing 100 of your troops!")
            Kingdom_Inhabitants["Troops"] -= 100
    elif specialattacknumber == 3:
        print("The demons are extra hungry today, they've become stronger.")
        ENEMY["Power"] += random.randint(1, 3)

def HellInvasion():
    global Days
    if Days["Days"] > 1000:
        HellFury = random.randint(1, 500)
        if HellFury == 1:
            time.sleep(1)
            ENEMY['Group'] = "Rag Demons"
            ENEMY["Amount"] = 100 + ((Kingdom_Inhabitants["Troops"] - 100) + random.randint(-50, 50))
            ENEMY["Power"] = 1 + (Kingdom_Inhabitants["Power"] - 1)
            specialattack()
            WAR(True)
        elif HellFury == 100:
            if Days["Days"] > 3000:
                time.sleep(1)
                ENEMY['Group'] = "Bulk Demons"
                ENEMY["Amount"] = (100 + ((Kingdom_Inhabitants["Troops"] - 100) + random.randint(1, 50))) // 2
                ENEMY["Power"] = 1 + ((Kingdom_Inhabitants["Power"] - 1) * 1.5)
                specialattack()
                WAR(True)

        elif HellFury == 200:
            if Days["Days"] > 6000:
                time.sleep(1)
                ENEMY['Group'] = "Winged Demons"
                ENEMY["Amount"] = (100 + ((Kingdom_Inhabitants["Troops"] - 100) + random.randint(-50, 50))) * 2
                ENEMY["Power"] = 1 + ((Kingdom_Inhabitants["Power"] - 1) * 0.5)
                specialattack()
                WAR(True)





