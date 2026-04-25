# -*- coding: utf-8 -*-
# Rise of the King
import time
import random
from War import buy
from War import build
from War import people
from Data import Kingdom_Properties
from Data import Kingdom_Assets
from Data import Kingdom_Inhabitants
from War import Settings
from War import Tax
from War import Hire
from War import invade
from Data import kingdom
from War import Great_Knights
from Data import Game
from War import upgradetroops
from War import invaded
from War import negativemoney
from War import LOVE
from War import peace
from Data import Days
from War import HellInvasion
from War import KNIGHT_FROM_HELL
from Data import HELL
from War import negotation
from War import BlackKnightEvent
from War import The_Devil
from War import trigger_genocide_deletion
from Data import timeskipvalue
HellActivation = False
cutscene = False
inventory = []
TimeSkip = False
timespeed = {
    "speed": 0
}
Kingdom_Extras = {
    "Power": 1
}
def MerchSale():
    if Kingdom_Inhabitants["Peasants"] > 1000:
        Sale = random.randint(1, 3)
        if Sale == 1:
            for i in range(Kingdom_Inhabitants["Peasants"] // 100):
                Kingdom_Assets["Gold"] += random.randint(0, (Kingdom_Properties["Merch Store"] * random.randint(1, 100)))
        if Sale == 2:
            for i in range(Kingdom_Inhabitants["Peasants"] // 100):
                Kingdom_Assets["Gold"] += random.randint(0, (Kingdom_Properties["Merch Store"] * random.randint(1, 10)))
        if Sale == 3:
            Kingdom_Assets["Gold"] -= (Kingdom_Properties["Merch Store"] * 2)
    WoodGain = (Kingdom_Properties["Wood Farm"] * random.randint(0, 30))
    IronGain = (Kingdom_Properties["Iron Generator"] * random.randint(0, 10))
    TitaniumChance = random.randint(1, 90)
    Kingdom_Assets["Wood"] += WoodGain
    Kingdom_Assets["Iron"] += IronGain
    if Kingdom_Properties["Wood Farm"] > 0:
        print(f"You got {WoodGain} wood today!")
    if Kingdom_Properties["Iron Generator"] > 0:
        print(f"You got {IronGain} iron today!")
    if TitaniumChance == 1:
        TitaniumGain = (Kingdom_Properties["Titanium Generator"] * random.randint(0, 3))
        Kingdom_Assets["Titanium"] += TitaniumGain
        if Kingdom_Properties["Titanium Generator"] > 0:
            print(f"You got {TitaniumGain} titanium today!")
def help():
    print("""
    Book of Knowledge
    Written by Duke Gukesh the VI
    Chapters:
    (0) Introduction
    (1) The prophecy
    (2) Materials
    (3) Managing a kingdom
    (4) War
    (5) Peace
    (6) King Lucius
    (7) Structures
    (8) What happens after Death?
    (9) History
    (10) Conclusion""")
    ChapterRead = input(">")
    if ChapterRead == "0":
        print("""
        ##########################################################################################################
        "As long as humans want power and fame, there shall never be peace." — King Lucius
        
        I decided to write this book for my love of the art of kingdom management and the sorts.
        This book will go through in depth of all required to manage a kingdom in this land,
        through the economic density of thy kingdom and how to keep a population upkeep throughout time and life,
        while surviving the struggle of war and diving deep into the magic of love and violence. 
        This guide will be your definitive handbook throughout your journey and so on.
        
        Good Luck.
        ##########################################################################################################""")
    elif ChapterRead == "1":
        print("""
        ################################################################################################################
        "For all who fall, they all learn the same thing, that it was there utter fault." — King Martin II
                
        Throughout history there has been many king's and lord's, many fell, many grew, but they always feared on thing...
        The prophecy... written by the 5 mages of ark, they wrote it on stone under the floor of the great Lord Geneva VI
        I shall recite thy script to you right now.
        
        The two lights:
        
        "A great light bringer will be brought to this world, this light bringer will be loved and cared for by many
        And it will find joy in it's life, but this light bringer will thy be found to be unpure
        corrupt, though it's purity it will realise that it needs not others, and will try to become the most powerful of all
        this light bringer will die, but it will thy keep attempting to come back to rue the lives of other's who usurped him
        eventually a second light will come to this world this light will be a weaker form, but it alone...
        will have the power to wipe the first light off the planet or help it achieve it's goal as they are one and the same in soul"
        
        This prophecy has been brought down through generations, the kings have feared the coming of both lights
        it is the most sacred text of all and the original scroll is held under the deep protection of the Julian Family
        Don't fear this prophecy, for it was made as a message for milenia by these 5 wise men.
        ################################################################################################################""")
    elif ChapterRead == "2":
        print("""
                ################################################################################################################
                "The build of a structure is composed of 3 extremely important items, the form, the texture, and the material." — King Fredrand VIII 
                You will find it utter most important to build structures in your kingdom for it to grow high and mighty, so in
                this chapter I shall focus on how to get materials and there properties and history.
                
                Wood:
                First used in the 560 DG wood is the most commonly needed material in almost any structure, it is also the easiest 
                to obtain the first option is to gain it through the market where it will cost 200 gold per unit... the prices
                might seem expensive at first hand, but you eventually learn the struggle it is to import materials over
                the sea or throughout the land, the second option is creating a farm, farms generate an average of 15 wood per day,
                but they require a significant amount of gold, land, and wood to get created so it is recommended you buy imports
                other than spend your gold on a farm early on your journey, as soon you have at least 100 residents in your kingdom
                then you can build a wood farm, just beware, they are really expensive.
                Iron:
                This material was originally ignored until 320 AF where soldiers used it for armor, then it quickly spread to
                be used in almost any defensive mechanisms. It costs a measly of 5000 gold to buy it imported, or you can purchase a generator,
                first invented by Sir Draco III, the iron generator will turn a plot of land into a well fueled infinite machine,
                giving an average of 10 iron a day, it is used in almost the entire industry, but as a wood farm, it is remarkably expensive
                it requires a significant amount of land, wood, iron, and gold I would not suggest making one early, for it will be far too expensive.
                Titanium:
                First discovered by King Lucius 5 years ago, Titanium has been found to be the strongest, most powerful substance that,
                our kind has bare witnessed, it can be used to make any structure 10 times more efficient than it was before.
                But creating it has come at such a cost it has become remarkably expensive, due to the current state of the titanium market,
                I further recommend doing your own research on it's costs as this book might become outdated in some years.
                Gold:
                Before the modern economy change to gold in 730 DG, we used common items and craftmanship for trade, but it was soon deemed inefficient and chaotic,
                so the world changed to gold, discovered in 746 DG by Sir Arthur V, gold has been used for the economy.
                It is mined by exclusive miners at the island where it was discovered, rightfully dubbed, "Gold Island" by the world Gold Trade Center
                and equally distributed to the economy via using it to pay for common goods at the trade center all to flow back to the world economy.
                This is your most important assets, it controls your power, your kingdom, and your future, don't lose hold of it.
                ################################################################################################################""")
    elif ChapterRead == "3":
        print("""
        ################################################################################################################
        "A kingdom's heart is in it's people, and people are driven by the sustainability of there life." — King Juan X
        If you want your kingdom to survive, you'll need to understand how to keep it running, people's lives depend on the infrastructure of the kingdom
        so it is your responsibility to make sure the kingdom works, this chapter will focus on how people live, how much taxes they give, and how much food they need.
        For a peasant to move into your kingdom, they will need a place to stay resident.
        The House:
        You need a house, the house first replaced living under caves and trees at 9450 DG or as I call it, the Neolithic Revolution.
        A house needs 1 acre of land 20 wood and 10000 gold to hire someone to do it, I deeply recommend not building it yourself.
        The more houses you have in your kingdom the more people who will move in to the kingdom.
        The Farm:
        People need food to survive in life, so your going to soon need to add farms to your kingdom.
        A farm can feed up to 100 people, and to those 100 people it makes an average of 15 gold per person in revenue of them every month.
        But if you have more food production than needed it won't sell all the food and will just be a waste of resources.
        You need 10 wood, 50000 gold, and 1 acre of land for a farm.
        If you don't have enough farms to feed your people, they will die.
        Revenue:
        Every person in your kingdom will give you an average of 250 gold in taxes per month, people are the secret to 
        having the power to scale in this world, make sure you have a desirable amount.
        Merch Stores:
        As of the time of me writing this book, Merch Stores have just started going into production.
        But what I do know about them is that they generate income at an exorbitant rate.
        They make money every day and multiply profits by the amount you have, but they are extremely expensive to make.
        So it's recommended you get one once you have at least 1000 people living in your land, merch stores get more profit by them too. 
        ################################################################################################################""")
    elif ChapterRead == "4":
        print("""
        ################################################################################################################
        "Humans want power, and the only way of achieving power is taking it from someone else" King Era I
        Now, I am a strict pacifist the only reason this is a chapter is because there will be enemies that will want your land, goal, and most of all, power.
        War is inevitable, so you must know how to defend your kingdom.
        Your soldiers are you first and most important unit in battle, a soldier takes 1000 gold from you per month,
        so to afford a good army I recommend having at least 4 people living in your kingdom per 1 soldier you have, but I recommend doing, 
        a 8 to 1 ratio instead as it's far more economically viable.
        I will not provide the information to start a war, since I highly not recommend doing so.
        So I shall move on the next portion.
        How war works:
        In battle you have two variables of extreme importance, your troop count, and your troop power, if you invest in upgrading
        your troops power each individual troop will be stronger if you have higher troops power you will have a higher win rate than loss in 
        individual battles, but if you have a weaker power, you will lose more.
        The second variable is the amount of troops you have, you can win a war of sheer numbers if you have enough troops.
        But if your enemy has the same amount of troops the war will be decided on power, and if your enemy has more...
        Hope that your troops are strong enough.
        Great Knights:
        Very few people survive multiple battles, even fewer become strong, but the rarest, is to gain a title of a great knight.
        These Knights are elite units that are far stronger than your average troop, and they will certainly not lose in battle.
        But these knights all have one thing in common, for there strength is far higher than any troop, there elitism grows with it.
        They will not even dare work  for a king without a kingdom, and what is the way to show you have one?
        By having a castle, build a castle and these units will come to you in due time and help you in war.
        Yourself:
        You can join your battle and fight along side your troops, I would not recommend this due to it risking your life,
        but that is your choice.
        LV:
        Your LV is your power, what power? Very few men have experimented with this but it turns out you get stronger the more souls you take,
        this power is redirected to the person who started the war, if you invade a nation and win, you'll become stronger in power,
        the few who have done this became monstrous beasts in battle. But, throughout history, they're story never ends well.
        ################################################################################################################""")
    elif ChapterRead == "5":
        print("""
        ################################################################################################################
        "Peace, is a fantasy, but a an amazing fantasy all must strive for" — King Qu II
        I left one part of the prophecy... I will recite it now:
        "There is one way the second light can get rid of the influence of the first... forevermore, but it requires the union
        of all kingdoms, villages, tribes, all together united, they will have the will to vanish the light."
        The 5 mages or Ark knew that peace was the way to unite the world. 
        Making peace with kingdoms will provide many advantages, improved trade and stop of war.
        It's important to make peace with all kingdoms, to do so, you will have to get them to sign a peace treaty.
        I should be easy, kingdoms are really reliable and logical.
        ################################################################################################################""")
    elif ChapterRead == "6":
        print("You flip the page... it has been ripped off.")
    elif ChapterRead == "7":
        print("""
        ################################################################################################################
        "A kingdom needs defense, the less soldiers who die, the more families get to see their father tonight" — King Qu I
        Defenses are a great bonus to battle when you are defending, for they kill off enemies without sacrificing your own.
        Arrow Tower:
        Has a 30% chance to hit every cycle, and when it does, it kills 3 enemies.
        Cannon Tower:
        Has a 1 in 6 chance to hit every cycle, and when it does, it kills 9 enemies.
        ################################################################################################################""")
    elif ChapterRead == "8":
        print("""
        ################################################################################################################
        "Life is a fragile thing, full of regrets and pain, but what happens when it shatters?" Lord #$%@$@%#^% — AKA Gloom King
        And I dared to asked the same question...
        As I dove deep into my research I found the knowledge of a folk legend, 1 mad man, a jester, who claimed to have surpassed death.
        He went to hell and back and when he came back, he turned mad. If what this man says is true, there is chance of punishment.
        In the afterlife, but he carried no evidence except the same looks of a jester who died 5 years ago. 
        Then there was the man who dared defy death by trying to get devine gifts from the god of nightmare, he raised a cult,
        but then they were never seen again.
        ################################################################################################################""")
    elif ChapterRead == "9":
        print("You ignore this page for it's boring information.")
    elif ChapterRead == "10":
        print("""
        ################################################################################################################
        "What is life if it always ends the same, in ruin?" Gukesh Amoth VI
        I set out to write this book to spread my knowledge, but know I realise the futility of it, perhaps the prophecy was a lie
        What happens if the second light never comes? What happens if the world goes on to die?
        Are we pointless to the universe?
        Should we be able to dream?
        To love?
        To give?
        So I end this book here, I hope one day someone will find usefulness in my teachings.
        Farewell.
        Gukesh.
        """)


def stats():
    global Days

    peasant_tax = Kingdom_Inhabitants["Peasants"] * 250

    max_productive_farms = Kingdom_Inhabitants["Peasants"] * 100
    active_farms = min(Kingdom_Properties["Farms"], max_productive_farms)
    farm_profit = active_farms * 20

    troop_costs = Kingdom_Inhabitants["Troops"] * 1000

    total_estimated = peasant_tax + farm_profit - troop_costs
    print(f"""
==============================
     {kingdom} inventory
------------------------------
Gold: {Kingdom_Assets["Gold"]}
Land: {Kingdom_Assets["Land"]}
Wood: {Kingdom_Assets["Wood"]}
Iron: {Kingdom_Assets["Iron"]}
Titanium: {Kingdom_Assets["Titanium"]}
==============================
    {kingdom} architecture
------------------------------
Houses: {Kingdom_Properties["Houses"]}
Arrow Towers: {Kingdom_Properties["Arrow Towers"]}
Water Stations: {Kingdom_Properties["Water Stations"]}
Farms: {Kingdom_Properties["Farms"]}
Castle Hull: {Kingdom_Properties["Castle Hull"]}
Kingdom Hull: {Kingdom_Properties["Kingdom Hull"]}
Cannon Tower: {Kingdom_Properties["Cannon Tower"]}
Multi Spuck Shot Tower: {Kingdom_Properties["Multi Spuck Shot Tower"]}
Merch Store: {Kingdom_Properties["Merch Store"]}
==============================
    {kingdom} inhabitants
------------------------------     
People: {Kingdom_Inhabitants["Peasants"]}
Troops: {Kingdom_Inhabitants["Troops"]}
Great Knights: {Great_Knights}
===============================
 {kingdom} estimated tax fund
-------------------------------
    {total_estimated}
===============================
Day: {Days["Days"]}
""")
def settings():
    print(f"""
    (1) Show every new person moving into your kingdom: {Settings["Peasants"]}""")
    settingchoice = input("Which one do you want to change?")
    if settingchoice == "1":
        peasantchoice = input("What should this be set to? (1) True (2) False")
        if peasantchoice == "1":
            Settings["Peasants"] = True
        elif peasantchoice == "2":
            Settings["Peasants"] = False
        else:  # What happened?
            print("Can't you read?")

def slow_print(text, delay=1):
    print(text)
    time.sleep(delay)


def buildchoice():
    print("What do you want to build?")
    print("""
        (1) Houses (20 Wood, 10000 Gold)
        (2) Farms (10 Wood, 50000 Gold) 
        (3) Castle Hull (Buy this 10 times to get a castle) (1000 Wood 50 Iron 500000)
        (4) Arrow Tower (60 Wood 10 Iron 10000 Gold)
        (5) Cannon Tower (100 Wood 50 Iron 15000 Gold)
        (6) Kingdom Hull (500 Wood 100 Iron 50000 Gold)
        (7) Merch Store (1000 Wood 1000000 Gold)
        (8) Wood Farm (500 Wood 10 Land [Yes not only 1 land like the rest.] 1000000 Gold)
        (9) Iron Generator (5000 Wood 50 Land 20000000 Gold)
        (10) Titanium Generator (5000 Wood 50 Land 200000000 Gold)""")

    BuildChoice = input(">").lower()

    try:
        print("How much of this do you want to build?")
        BuildAmount = int(input(">") or 0)

        if BuildAmount <= 0:
            print("You think you can build 0 (or less) of something? I believe you have a very minor case of serious brain damage.")
            return

        build(BuildChoice, BuildAmount)

    except ValueError:
        print("That is not a number, fool.")






def note():
    slow_print("""It reads:
        Here is the land, it's big, it's legal... ish, don't annoy the rest of the tribes nearby.""")

print("Choose your wanted time speed (1) 0.1 of a day per turn (2) 0.3 of a day per turn (3) 1 day per turn (4) 2 days per turn (5) 7 days per turn")
print("The faster it is the harder it is to prepare, so it is recommended to do option (1) in a first playthrough.")
timespeed["speed"] = 0.2
TimeChoice = input(">")
if TimeChoice == "1":
    timespeed["speed"] = 0.1
elif TimeChoice == "2":
    timespeed["speed"] = 0.3
elif TimeChoice == "3":
    timespeed["speed"] = 1
elif TimeChoice == "4":
    timespeed["speed"] = 2
elif TimeChoice == "5":
    timespeed["speed"] = 7
print(r'''
                                 ____                                         
                              .-"    `-.      ,                               
                            .'          '.   /j\                              
                           /              \,/:/#\                /\           
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
                                          `--...____,="_.'`-.____        fsc
''')
time.sleep(3)
print("""












""")
print("RISE OF THE KING")
time.sleep(5)
print("In the land of $#%$#%@^$#@%@, many great kingdoms flourish. Will you rise to greatness and claim your place in glory alongside the kings of old? But beware: ever since the death of King Lucius, a mysterious portal has stood open. No one knows what lies on the other side, for all who enter meet their end. Since its arrival, the great emperors have grown cruel and malicious, plunging the world into a new age of conflict.")
time.sleep(3)
print("You arrived")
time.sleep(3)
slow_print("You find a note")
Open = input("Do you want to open it? (1) Open and Pack it (2) Pack it (3) Throw it away")
if Open == "1":
    note()
    inventory.insert(0, "Note")
elif Open == "2":
    inventory.insert(0, "Note")
elif Open == "3":
    slow_print("Junk!")
print("Ok... anyway")
time.sleep(3)
TimeSkipValue = 0
while Game["Game"] == True:
    global Days
    global Hell

    if timeskipvalue["TimeSkip"] == False:
        people()
        Tax()
        invaded()
        negativemoney()
        MerchSale()
        KNIGHT_FROM_HELL()
        HellInvasion()
        Days["Days"] += timespeed["speed"]
        BlackKnightEvent()

        if LOVE["LOVE"] == 1:
            print("You feel a little good...")
        if LOVE["LOVE"] == 5:
            print("Your feeling better...")
        if LOVE["LOVE"] == 7:
            print("You feel amazing...")
        if LOVE["LOVE"] == 10:
            print("You whisper in your dreams, Death... what an amazing word")
        if LOVE["LOVE"] == 11:
            print("You whisper in your dreams, Death... what an amazing word")
        if LOVE["LOVE"] > 12:
            if LOVE["LOVE"] < 14:
                print("You've entered a state of megalomania... YOU WANT MORE POWER")
            else:
                print("Let all die... let all who dream, see there death.")
        if LOVE["LOVE"] == 10:
            if cutscene == True:
                cutscene = False
                print("Crescit potestas mea...")
                time.sleep(5)
                print("I WANT TO SEE THE END!!!")

        if The_Devil["HATE"] <= 9999:
            print("What will you do?")
            print(f"""
                    (1) Build
                    (2) Buy
                    (3) Invade (Military strength: {Kingdom_Inhabitants["Power"]})
                    (4) Check Kingdom Stats
                    (5) Hire
                    (6) Settings
                    (7) Upgrade Infantry Power
                    (8) Peace Treaty
                    (9) Book of Knowledge
                    (10) Trade with other kingdoms
                    (11) Do nothing for multiple turns
                    (Else) Do nothing
                    """)
            if HELL["HELL"] == True:
                print("""
                        (12) Destroy this world.""")
            Action = input(">")
            if Action == "1":
                buildchoice()
            elif Action == "2":
                buy()
            elif Action == "3":
                invade()
            elif Action == "4":
                stats()
            elif Action == "5":
                Hire()
            elif Action == "6":
                settings()
            elif Action == "7":
                upgradetroops()
            elif Action == "8":
                peace()
            elif Action == "9":
                help()
            elif Action == "10":
                negotation()
            elif Action == "11":
                try:
                    timeskipvalue["TimeSkipValue"] = int(input("""
                        How much turns do you want to skip ahead to?
                        >"""))
                    timeskipvalue["TimeSkip"] = True
                except ValueError:
                    print("That is not a number.")



            elif Action == "12":
                if HELL["HELL"] == True:
                    print("Good...")
                    time.sleep(5)
                    Game = False
                    for i in range(100000):
                        print("""

                            """)
                    time.sleep(5)
                    print("Love, Hopes, and Dreams")
                    time.sleep(2)
                    print("Are all not reality")
                    time.sleep(3)
                    print("See all those die...")
                    time.sleep(2)
                    print("Let them scream...")
                    time.sleep(2)
                    print("See them run...")
                    time.sleep(2)
                    print("See the children cry...")
                    time.sleep(2)
                    print("See the mothers die...")
                    time.sleep(2)
                    print("See them run...")
                    time.sleep(2)
                    print("Let them scream...")
                    time.sleep(2)
                    print("They all die...")
                    time.sleep(2)
                    print("Let their tears fill the sky...")
                    time.sleep(2)
                    print("Their blood brings more love to our lives...")
                    time.sleep(2)
                    print("Hear them scream, hear them die...")
                    time.sleep(3)
                    print(f"Don't you like this? Lucius. We saved them. We made them happy :)")
                    time.sleep(5)
                    trigger_genocide_deletion()
        else:
            print("""

        ̷̨͉̼͇̗̤͔̝̭̙̯͘ͅ ̴̡̡̧̧̛̛͉̜͈̟͍̪͔̖̱̫̦͇͉̯̬͙̥͉̘͓͓͔͎͈̹͕̮͖̎̎̌͊́͒̾̅͊̾͒͌̍̅̍͒̔̈́̏̈̎͑̉̕̚͘͝ͅ ̸͙͚͍̜͈̩̪̥̣̤̰͉͎̠̖̩̘̥̗͎̯̖͖̗͉̤̓͂̅̋͆̏̏̓̈́̏͜͠͠ͅ ̴̨̢͙͔̮̞͈͙̙̳̞̫͙̯͉͕͙͉̠͈̬̖̯͔͓̱͓͚͇͚̀͒͌̾͋̍̕͜ ̶̢̧̡̧̖̼̱̣̝͔̰͉͖̟͇͈̺͙̙̫̮̮̘͍̫͉͉̫̜͚̬̬̘͔̞̬̞̱̘̩̏̂̋̈̅̆̃̓̽͂̔̐̄̌̃͑͒̓̓̈́͘̕͝ͅͅ ̸̨̨̧̛̦̠͎̯͎͓͚̺̝̖̱̰͇͔̦̬̪̲̫̫̺̫͔͍͔͓̗̻̳̟͙̳̯͉͓̓̀̓͂̈́̐͊͛̉͊̓͗̎̈́͐̈́̔̓͑̿̀̒̐͊̄̑̅̂̀͊̌̚̕͠ͅͅ ̷̡̡̢̧̨̧̡̯̳̘͇̠̮̻̹̮̼̺̼̭̗̪͍̹̜͖͈͎̮̳̦͔̖̫͍̟͇̗̬̙̘̥̻͇͔̣͎̭̬͗̄̂̃͐̅͛̐̾̎͆̂̉̊̇̒̔̀͐̑̄̑́̈̈́̈́̎̔̐͐̿̂͝͝͝ͅ ̴̩̙̪̪̯̪̘͍̫̝͙̖̻͈͈̲͕̘̼̿̅̆́̃͒̌̉̈́̾̆̐̋̊̀̐̔̋̀̓͐̈́̽͐̀̇̐̌͑͘̚͠͠͝ͅͅ ̴̢̦͔̙͍̺̤̖͕̬̮̭͉̝̠͈͖̩̰̺̗̲̲͚̩̫̳̅̍͑͒̃͊̀̈́͆̒́͌̌̑͋̈͂̋̇̆̒̿̓̓̉̑̈͂͐̉̏̏̆̾̅̽̾̚̕̕͘͜͠ͅͅ ̴̡̛̰̙̇̍͛͋͂͗́̈̊͊̇́͘̚̚͘ͅ ̵̡̧̡̡̧̩̘͉̣͈͚͍͇̝̥̹̣̭͍̙̥̳̭̫̻̪͇̝̱̞̠͚̖̜͙̹̮͕̞̦̯̭̈̅̆͆͌̈́͐̄̀̉̇̍͛̇̉͑̎̈͊͘͘͜͜͜͝͝͝ͅ ̴̢̜͔͍͚̰̱̘̻̺̹͕̟͇̰͔̝̥͓̫̩̤̲̻̲̮̮̺͍̝̻̜̰̐̈́̉̃́̈́̓̌̈́͛̅͒̓͘͜ ̷̢̧̛̠̪̳̔̓̅̐͂́̆̓̓̅͑̾̃̅̀͋̒̍͐͗́͋̔̍̈́̊̿͛̿̅̕͘̚͘͝͝͝͝(̷̢̢̡̛̠̗̟͔͖̳̦͖̭͔͚̖̣̦̼̼̳̲͉̦̦̙̝͔͈̗̼̯̙̣̱̈́̿̀̽̐̆̓̈́́͋̄͗́͑́̐̈̉͂̚̚͘͜͝͠͝1̴̨̧̛͈̮͈̘̳̥̗͉̠̭͔̙̹́̅̀͛́̀̿̓͊̈́̈́̍̈́̉̏̅́͋͆̒͆̀̿̊͋̌̄̒̈͆̉̓̃̌̂̇̇͑͂̓̑̎͘̚̕͠͠͝)̸̻̗̲̱̱͖̣̣̰̝͈͙͙̟̤͌̅̇̎͋̎̌͋̉̏̈̐͒̋̈́̈́͜͠ ̷̧̨̡̧̢̼̝̟̪̖̤̞̩͇̣̞͕̳̰̝͓̬͔̗̣͓̺͎͕̬̂̈̆̑͋̄̈́̑͊̓͐̀͂̈́͋̇̒̋̄͑̈͂̀͑̿̋̎̂̈́̽̒̂́́̀̋̀́͘̚̕͜ͅͅB̸̢̧̨̨̧̨̛͔̻͈͕̤̳̻̼̤̝̬͓̱̬͍̹̬̫̖͈̭̗̰̦̬̦̩͙̮̱̯̼̪͍̤͍͖̻̩̩͔̟̒̆̃͊̅͑͒͐͆̇̅̊̀̋̾̾̄͊̀́͑͋͒̿̿́̈́̎͘͘͘͝ư̶̡̡̧̛͚̥͉͉̠̦̼̙̩͇̬͇̘̫̖̘̯͙͔͔̱̪̘̜̔́̄̌̃̽͊́̾͗̍̊̌́̓͒͗̒̆̌̽̂̽̓̽̽͐̾͗͐̉̅̆̈́̈͒̂̕͘̚͘̕̚͠i̶̛̛̝̝͖̝͖͚̯̯̝̰͔̮̝͓͈̭̬̥̰̭͔͙͙̮̓̈͗̔̀̏̍̍̅̎̾̈́̿̑͋̀̒͗̐̀̄̔̂̿̓̕͜͜͠l̶̨̡̡͚̮͍̯̥̪̣̩̳̰͓̄̄̅̆̒̀̍̈́̅d̴̨̙̙̮̟̭͈̟̥̼̭͎͑̀̀͛̀̈̄́̎̿̂̾̈́̌̓̕̚͘͜͜͠
        ̴̛̖̮̺̏̐̇͑̊͗̀̂́́̑͊̀̽̿̌͆̇͆̈̐̅̍̂͌́̔̑̏̍̍͗̃̅̇͐̇̑͒̍́̾͊͐͘͘͝͝͝ͅ ̴̡̹͙͈͍̯̘̹̭̝̤̖̹̫͇̬̪̰̖̣̀̓̈́̃͂̀̋̈͐̓́̎̃̃̈́̆̀̾̎͗͜ ̴̛̭͂͐̇̐̍͊́͗͂͒̾͒̒̎̎̀̆̊̓͗͌̂̓̿̾͌̽̄̄̈́̒̉̐͘̚̕͝ ̴̡̢̖̞̯͔̟̳̳͓͖̤̼̦̻̩͚̳̠̝͉̘͚̳͎͍̉͋̈́͐͑͆̆̿̇͂͛́̈̌̀͗͌͆̏̈́̈́́͆̎͆̍͐̿͒̈̀̍̌̄̕̕̕͘͘͝ ̷̡̧̞̬̲̲͇̻̻̤̼̩͓̯̱͍͎̤̟͎̪̬̣̀̏̄͌̓̈́̈̔͆̀̎̂̉̃̋͋͘̚͘͘͠͝͝ͅͅ ̸̢̧̨̨̨̢͕̭̭̺͔̩̮̝̞̳͓͔͙̳̼͙͕͖̳͙̎͗͑͐͗̀̈̐̕͠͝ ̷̧̡̡̛̤͓͚͍̰̩̳̬̪̠̺̥̥̮̥͖̹̞͍̫͙̪̯̦͍̪̹̠̹́̎͛̽̍͐͐͐͐̊̌̏̇̈́̿͂͑̍̏͋͌̓͊́̌̐̊̓̃̎̉̈́͘͜ͅͅ ̸̧̧̮̺̳͓̟̟̳͖̳̝̞̋̏͋̍̂̎̿͐͐͊̀̽̈́̐̄͛̈́͊͋͋̓̄͛̆͑̀͊͑̀̉̾̓͊̚̕͜͝͝͝ ̴̢̧̛̲̞͎̳̹̹̝̻͈̟̲͉̖̫̜͉̖̖̺͎͉̝̖̝͖̠̝̥͇̺͍͎̘̝̟͇̰͊̔̑̑̍͒̓̄̍͗̎͋̍̇̂́́̒͌͊͒̆͛̀̆́̒̋͂̈́͌͊͌͆͑̓͋̚̕͘̚̕̚̚͜͠͝͝ ̶̢͇͖̩̼̱̠͚̘̪̠̞͙̱̳̼͙̻̩̲͕̖̱̔̓̋̉̔͑̂̋̐͗͊̓̈́͗̉̎̊͂̈́̐̓̈́̏͂̆̉̎́̕̕͠͠͝͠ ̵̡̢̢̨̨̨̧̨͉̲̫̫̠̪̫̯̻̱̫̹͖͙̮̰̳̫͙͕̝͕͎̪̖̩͎͈̗͔̮̳̮͇̟͓͛͑͒̾̿̇̆̔̌̀̕͜͜͜͝͝͝͠ ̶̨̢̧̛̘̯̰̱͕͔̩̠̱̳̟̹̼̩͕͔͈̦̣̗͈͔̮̱̯͓͎̯͖̄̈́̿̅͛̇̑̉͐́̈̅̓͊͜͠͠͝͝ͅͅ ̶͎̀͗͆̀̅̓̆́̇̆͌̒̀͒̀͋̈́͛̈́́̎̑̀̀͑̐̈́̾̈͒̅͂͌̎̉̋̿̚̚̚͘͘͝͠͠͝(̴̲̜̭̽̑̋́̈͆͛͗͂̔̄͑̀̅͌̎͘͠͝2̸̨̻̮͇͚̬͎̄͒ͅ)̵̨̨̧̡̮̯̺̮̹̹̰̞̝̜̰̭̝̙̠̤̳̠͇̱̪͉̭̹̭̖̖̯͓͎̞̮̬̝̣͎̻̲̺̩̻̲͇̺̐́̓̉͋́̉͗̾̾̄̔͂̓̈́͛́́͛̃͒̃̔̈́̈́̿̃̅̋̂̂̆́̎̇͑̚̕̚̕͜͠͠͝͠ͅ ̴̢̨̰͖̜̬͈̭̣̗̬̝̜̗̺̻̝͇̹̳͓̜̦͕͉͎͎̟̻͉͔̙͈̬̫̜̜̑͜ͅͅB̵̡̧̢̧̳̮͓͔͔͓̘̣̞̻͕̟̞̜̬̳̖̯̭̰̤͙̃̎̀̈́͋́̔́͋̈̎́̃͗̈̇́̐̄̔̎͒̉͌̿̎̚̚̕͜͠ͅͅu̸̡̧̘̭̺̙̖̬̜̬̘̰̝̲͉̙͉̥̦̘͆̏̾̈́̃̂̀̀͒̽̓̓͊̍̽͑̄̚̕͘͜͠͝ͅy̸̡̨̧͙̪̭̟͔͖̙̖̠͍̩̲̮͔̟̮̼̥͕̳̙̣̳͈̝͙̫̹̣͕̹͔̩̭̥̰͚̞̼̮̹͓͔̳̦͗̊̀̎̐̋̄͗̿͊͐͜͜͝
        ̶̨̢̧̛͖͈̮̰͕͖̜̞̪̯͔̟̮́̈́̓͛͊̇̐̋͗̉͂͗̍̇̈́̾̀̊̎̇͋̄̈́̉̚͜͝͝ ̷̨̡̧̡̨̡̮̝͕̩͍͙̭̤̪̘͇̤̠͍̖̩̯̟͉̣̜̱͈͓̳͚͍͈̺͗͗̋̍́̈́͑̈́̑̉͆͆́͐́̄͆̀͛̋̑̎̾̂͊̚̚̚̕͝ͅ ̸̡̨̢̡͉̜̝̖̙̱̤̞͔͙̦̗͖̖̦̣̣̜̗̣͓̻̖̗̪͓̳̻̮̘̾̇́̑͌̓́̈̽̍̑͊͋̈͐̚̕͜͜͝ͅͅ ̵̛̛̛̼͉̙̺͚̟͔̗̺̺̤̗̩͙̥̻̣̰̳͍̹͔̠̃̅̈̊̽̇̑̎̓͑͐̄̇̀̾̅͌̓̃̾̒͆̿̍̊̓̚͘͝ͅ ̸̡̧̡̡̛̙̼̻͎̞̠̰͓̥̬̭̻̖͔̭͇̙̟̟̥̭̠̥͚̞̹͕̙̼͕̦͙̟͔͂͋̍͊̓̿ ̴͍̠̳̻̼̼̤̼̩̹̟̬̻̠̅̍̂͒̉̉̄͗̈́͑̉͗̏͗̂̍̿̌̈́̅̀̔̒̌͑̃̽͘͘̕͝͝͠͝͝ ̴̢̨̨̢̮̰̰͉̦̞͈̠̜͙̼͕̜̥͎͖̹̺̮̰̱̙͕̫̲̫̪̦̑͐̀̄͒̋͊͛̎̈́̈́͜͜͠ͅ ̸̧̨̞͚̲͙̪͇̮̗͍̯̃̀̄͆̇̈́̃̔̏̇́̈̔̿͒̀̀͆͆̆̚̕̚̕͘͜͝͠ ̷̛̛̛̲͚̝̘͈̌͌̂̈́̔̈́̆̎̊̑̄̋̇̉̄̃̈̿̅̈́̒̉̈́̅̄̆̈́̽̚͘̕͠ ̸̢̡̨̞̠̱͈͇̻͔̦̩͇̰̪̠̜̥̈́͗̓́́̐͛́ ̵̧͈̳̱̪̝͇̜̯̮̬̆̓̓̓̓̓̀́͒̄͌̄̄̂͋̀͗̐̋̉͗͗̇̅͒͗̽̈́̄̈̚̕͘̕̚ ̵̨̢̧̨̡̢̡͖̫̼̗̭͓̪̤̳̱̞͉̜̖̳̟͇͚͈̙͖͇̮̹̹̺̣̪̩̗̪̥̞̦̮̩̺̜̐͗̉͒́̀͑̍͂͊̆̅̐̃̚͜͝ ̷̢̨̨̧̧̢̛͚̗̘͓̖̦̣̤͎̠͎̘̱̖̝͚̱̣̗̼͕͍͇̱̜̞̖͇̦̖̰̯̦͉̹̙͚̭͙̣̻̗͂̈́̄̾̔̑̑͌̂̾̒̇̒̐̐͐̔͗̇̄̔̏̈͆̈́͒̿̈̈́̓̏̎́̽̕̕͝͠͠͝͝͝(̵̨̭͈̠̤̻̟͔͉̬̭́̓̿̉͑̈̂̽̓̊͐̐͛̃͌̕̕̕ͅ3̵̨̨̗̩͖͕̤̟̯̱͉̳̳͔̘͔̩̠̳̗̰̣́̾̂̾̿͐͐͒̏͊̊̍̈̓̌́̇̋̉̾̍̈̈͊̇̒̕̚͘̕͘)̵̛̼̥̀̅̂͂́͛̔͊̀͛̎͊̓̋̚̕͝͠͝ ̸̡̢̢̛̫̘̠̗̗͖̘͕͕̗̣̈̑͗̓̑̈͗́̎̿̐̓̅̒̈̇͌̈́̿̎̈́̒͑̔̿̈͗̽̽̇̀̇͊͒͘͘͝Ì̵̡̛̳̟̹̦̙̼̘̈́̅̿̇́͊̎͌̂̏͋͋̀̈̃͋̐͋̎͆͂̓͆̍̄͆͊́̑̍͆́̔͂͐̚͝͝͝͝n̶̢̡̨̧̺͔̫͔̻̫̦̭̻̦͖̫̖̬͈̘̺̼̬̳͍̻͓͉̗͔̻̦͚͖̪͇̻͙͔̠͍̜̫͇̪̼̤̏̇͜͜͜ṿ̵̼̯̃̚͜ͅa̵̧̧̱̼̲̳͙̺̱̹̼͎͇̞͉͙͙͍̺͙̘͍̗̦͖͚̪̝͉͎̹̲͇͔̖̘̞̬͙̯͈̣͌͊̽͊͌̄̈́́̿̒͠͠ͅͅḑ̵̢̧̧̡̧̱̘̦̯̘̜͚̭̟̤̳͓͙͎̟̥̙̖̮̠̱̪̻̤͖̳̳̰̜̝̥̪̑̒̎̀̈́́̍̍̇̏̾̎̐̊̑̋͘͜ͅę̵̤̌͌̅̉̀͐̇̿̃̃̔͘͘͘͝͠ͅ ̵̧̡̛͎̟͓̼̭͓̝̯͓̻͕͈̯̣͇͙͎͓̭̔̀́̆͆̋̀͗̄̋̈́͊̂͊͆̿̍̈́̿͂͌̇́͑̽͘̕͝͝(̴̨̡̥͇̖̰͍̺̘̼̰̺̻̈́̊̅̽̑̀͆͑͌͗̈̌̆̈́͆͗͋̾̂̃̚͝M̸̡̛̛̲̗̦͍͙͈̘̱͍̰͉̝̱̱̙̜͉̟̱̰̤̘̻̦̜̰̯̈̏̉͐͊̓̂͂̅͌̐̂̿̔̏̓̿͆̽̓͐̌̀̉̀̏͋̍̾́̔̈́̄̒̃̄͝͝͝͝͠͠i̷̧̢̛̛̗̙͔͈̥̯̻̳̥̰̻̖̫̜̦̭̽̀̈́̃̍̉͛̂̐́͑̈͛̀̄̊͛̕̚ḷ̴̡̢̢̢̧̢̛͍̥̮̦͇̰̘̦͚͖͍͉̺̗̰̪͔̟̩̟͕̤͓̺͖̻͎̱̩͙͔͍̣̬͚̮͋͐͋̌̓̊̈́̍͛́͊̊̿̍̌̏̔̓̀̑̇͑́̓̈̈́͂̀̈́̂̒͌̆͌͘̚͜͜͜͝͝͝ͅi̴̡̡̡̨͓̝̤̗͖̗̭̝͇̫͕͔̞̥̖͍͓̩̹̬̦̪̤͙̙̓̃̈́͂̓̾̐̾͘̚͝ͅͅţ̷̧̡͚͖̰̮̳̮̲͕̘̬̼͖̺͎̟͖̺͓̰͉͎̗́̒̈̐̈̊̊̈̀̓͗̈̇͗̍̀̔̈̿̽̋̽̀̂̈́̑́̊̓͆̇͂́̕͝ͅą̴̛͓̟̺̝̮͔͕̬͔̭̗̲̄͌̒̈́́̔̎̓͒̆̄̿̑̾͋̾́̍̂͑̓̽́̇̀̊̄̿̆͛͆̿͂͗͗̌̀͊͐̐͘̚͠͝ṛ̴̨̨̛̯͔̤̙̜̫͔̬͇̼̬͙̰͓͔͎̲͖̿̽͐̉͒̍͗̾̂͂̅̀͐̿͌̀̆̔̌̏̍̈́́̽̑͐̎̈́̍̈́̿̈̚͝͝͝ȳ̶͎̥̦̼̦͈̼̯̞̲͚̺̺͔̰͙͆͗́͊̏ ̷̨̯̟͈̼̙͖̟̘̠͎̞̼̟̙̈́̿̇̑̓̀͛̀̄̽͑̋̿̂̂̎̐͆̅͌̔̂͐͜͠s̴̡̛̹̤̭̜̬̭̰̳̯͎̯̟͎̺̹̟̖̯͍͓̝̻̙̹̖̟̳͚̻͍͙͔̈́̒̀̑̈́̀̎́̿̓̍͗́̓̑̌̏̅͌̏̑͊̈́͊́̀̾͘̕̚͜͝͠ͅt̴̢͓̜̂̃̂̿̆̒̂̐͋̈͂̕͝͝r̷̡̧̙̮̺̲͕̖̲̖̞͚̖͎̗͈̲͎͆̀͜͝ę̴̧̢̧̧̢̢̛̹͔̜̬̭͇͓͚͖̰͍̝̠̺̗̹̘̼͈̥̳͉̙̦̻̣͔̜̺̩̪͉̞͎̝̻̖̖͍̞͕̓̀̂̽̔͂͂͛̈̎̉̉̊̀̅̋͌͋̊͑̍̎̒̓̉͛̾͊̉̇̓́͂͛͛͊́̿̀͒̊̽͆͘͘̕̚̚͜͝ͅn̴̘͎̻̖̪̞̙̳̆͑́͘ğ̶̡̧̼̳͈̜̤̱̼̩̯̞͉̣͔̯̬̮̬͖̦̦̉͑̂̌̒̃̈̆̄̂͂͛͐̓̋̒͂̀͂̈̈́̀̓͛͛̇͆͋͗͌̔̓͑̋͋̄̓̓̋̐̚͠͝͝͝ͅͅͅt̵̡̧̨̧̤̗̬̝̻̖̙̼͉͖̝̺̩͙͊͆̄̄̌̇̈́̈̏̎̓͗̈́̊̋̋̒̑̅͌͂̎̍̈́͛͂͊̂͘̕͠h̵̛̘̳͒͊͑̀̓̐̌͆͑̂̽̈́͆̾̇̋̇̑͗́̾̃̀̇͋̋͂͆̐̏̎̎̕͘̕̚͘̚̚̚͠:̴̧̧̧͍̻̰̮̗̖͚̙̥̥̻͖̰͕͓̥̞̫̰̺̬͍̝̘͚̩͓̝̲͍̰͎̖̘̠͙́̏̎̒͌͒͆͗̂̃̌̐͊͛̈́̏͒͐̕͝͝͠ ̸͙̪̯̤̠̜̺͙͕͇̼̤̠̹̱̭̣͙̳̖͇̞̞̺͊͜͝{̸̧̧̡̢̛͍͕̠̤̱̜͙͍̠͙̫͙̹͍͖͚̞̙̖̜͎̜͈͕̼̺̗͓̭͎̝͈̲̠̞̏̇͑͐͂̉̌͆̏͊͊̂̋̈̎̾̒̆́͊́̅͆̌̚͜͜͜͝͠͝͠͠ͅK̵̨̧̢̛̛̛̮͉̹͈̘͖̝͚̳̳̺͉̮̮̟͓̙͓͉̝̙̪̼̲̫̦̓́́͑̄́͒́͋̈́͐͐̀̃̏͂̾̔̄̄̉̿̍̋̓͒̕͜͝͝͠͠į̵̨̛̺͎͕͔͚͓̯̪̖̳̬͓̜̦͖͕̱͚̤͈͖͎̠͍̝̭̰̼͖̿̽̿́̆̈̔̒͊̔͌́͒̈́̾̆̈̏͑͐̇͛͑̆̓̋̋͒͌̾̎͘̕̕͜͜͝͝͝͠͠͝͝ͅņ̵̧̨̡̥̙̳̤̖͙̹̺̭͕̝̯̗͕͕͙͔͎̘̩̹͉̪̮̰̤̳͙̓̿͑́̊̍̀̎̚͘͜͠g̵̢͓͈͎̫̗̳͙̫̠̺̩͔͕̙̤͍͇̞̺̓͛̈́̂́͗̄̓̾͛̚d̷͎̃͛̅͋̃̈́̀̈́̈̈́̃͒̀̃̑́́̎̅̇̆̋͌̑̇̽̿́̍͘͝͝o̴̭͔͕̻̐́͒̿͛͋͊̀̍̊̑̈̈́̒́̽̈́̍̈̾̕̚̚͘͠͠m̷̢̆̓͒̀_̶̨̨̢̛̛̗̪̰͔̩̱̱͚̞̝͇̻̳̞̟͈̫͙̝͔̭̦͑̊̑̋̽̓̈́̍͆̌̾̃̀̌̂̈́̒̉͆́͒̒̒̀̒̑̈̅͐̀̇̑́̓͘͜͜͠͠ͅE̴̢̨̡̢̛͖̠̱͖̼̗̦̬͉̹͎̜̣̦͚̤͍̫̮͚͖͇̟̜̳̹̣͈̙̝̘̋̀̈́̀̎́̇̑̑͛̃̉̀̈̀́̓̔̋͋̎̀̒͒͗̇͌͊̆̈́͋̊̏̀̅̔̃̓̆̿̕͘͜͝͠͝͝͝ͅx̴̛̛̛̭̜̙͓͔̖̟̝͓̮͉͇̏̈͑̄̓̐̂̾̆̋͗̒̀̑̎̉̓̉̉͊̃̽͋̌͑̈́͛́̓̓̉͂̉̕͠͝͝ţ̵̢̛͈̼̠͎̼̖̗̪̼̤̱̫̘͓͙̖̙͍̰̳̤̳͖̖̮͔͎̮͈͊͐̂̎̈̽̽̊͒̏̅͊͋̅̿͌̑̀̓̓́̈́̍̂̽͋̋̇̋̃̄́̒̚̚͝͝͝r̷̢̡̢̙̜̮̼̠͉̠̥̗̠̩͉̙̩̻͍̥̙͑̀̐̔͑̀̉ͅͅa̷̢̡̦̩̺͔͍̗͙̪̮͉̰͈̬̰̱̱͇͓͔̭͍̗̳͆̒͂͌͆̒̄̓͛̉̔̃̈́̈́̑̀̃̾̑͆̚̕͘͘̚̕͝͝ͅͅs̷̡̧̤̯̪͎̲̩̘̼̹̝͍̮͖͈̗̺͔͉̄̈́̀̋̌̽̈́͂͛̔̀̏̅̆̌̈̾̋́̈͘̕ͅ[̷̡̢̨̧̧̧̛͔̻͍̹̺̬̗̝̙̦̖̜̱̠͔͕̖̪̖͚͕͚͍̳͈̦̙̤̱̣̭̬̪͍͔͈̬̤͒"̶̧̢̢̡̧̢̜͕͔̦͖̳̞̮̫͎̪̲͈͙͓̝̤̼̟̜̰͚̝̹̙̤̹͍̟̲̦̣̖̅̔͐͌̀̎͘͝͠ͅͅP̸̢̛͍̱͕̬̖̣͍̬͇͚̥͕̪͕̻̺̗̣̙͖̖̍͐͋̊̔̉̔͆̑͌̏̾̿̄̾͌̽͂̕͜͜͝o̵̢̨̡̢̨̨̢̨̬̤̦̲̟̣͔̣̼͙͍̼̱̻̺̰̬͉̭̯̘͎̖͍̣͚̫̟̤̝̜͈̳̻͕̖̼͋́͗̌̊̌̊̄̐͛̀́̈́̏͐͋̿̀̎̋̉̅̆̇̒͑̊̊̆̈́̐̕̕͘͘̚̕̚͠ͅw̵̢̧̧̨̢̧̧̛̛͈̼̹̙̻̫̰͕̳̮͚͎̦͕͍̞͍͇̺͇̺͚̫̦̻̹̼͈͎̭̺̪̞̖̻̜̲͈̠͚͓̏͆͌͋́̋̿̀̾̀̒́̔̿̈̏̏̋̀̀̀̅́̾̔̍̈̇̾̋̈́̏̈́̃̂͗͂̾̆̒̋̈́̐͘̚̕͜͝͝ͅě̷̡̼̞͙̤̱̭̘͙̫̦̠̥̺̬̣͖̳̼̀͐͘ͅr̸̡̢̡̨̛̝̜͉̲͔̺͈̱̺̤̭͚͔̯͙̬̻͉͚̞̱͈̩͙̞̞̝̩͈͉͈̩̖̍̎͆̊̀̿͂̉̅̇̅͐̃̿́̒͛̚͘͜͜͜ͅ"̵̨̡̧̡̨̨̛̛̛̛̥̠̯̳̙̘͍͙̳͉̹̭̻̠͖̤͇̲̬̟͕͍̘̭̰̗̗̙̫͍͈̥̩͖̋̌͛̈́̎̅̄̅͛̕̕͜͠]̵̨̧̡̡̢̛̛̬͔̼͖͖͕͕̗̣̤̠̮͖͖̯̦̣̰̟͍͓̩̘̮̪̤͎̘̀̏̓̏̎͌̇͂̄͒͌̉̅̓̍͗̉̒͒̎̀͊̄͋̋̋̾͂̚̕͜͜͠ͅͅ}̵̥̞͈̝͋̽̀́̈́̎̑̾͗̅̈́͋̈́́̍̀́̓̍̒̋̏́̀̈́̇̿͆́͋̔̚̕̕̕͘͜͝͝͝ͅ)̶͕̤̺̠̅̊̈͊̉̽͆̋̽͒̕͝
        ̴̡̧̪̪̜̙͕̦̪̜̰̗̟̤̯̙̳̟͙̦͍͒̀͘͝ ̸̧̡̡̡̧̭̼̫̗̱̘̺̦̲͎̣̪̭̯̲̠̣̪̞͔̖͙̯̗͔͈̫͙̱͎̟̠̖̭͔̝̞͚̤͖͗̉̒̿̋͒̉̆̃̋͛̆͗͂̇̒̈́̇̋̎̐͐͋̅̏͒̃̈̿̍̿̓̌͐͘̚̚͜͝͠ͅͅͅͅ ̴̨̡̨̧̡̧̢̝͕̲̙̖͍̲̟̝͖̥͔̟̞͍͓̪̗̙̣͇̯͖̮̘͖͔̖̤̟̭̬̰̖͙́̆̌͗̆̄̀̏́̾͆̄̑̒͐͑̾̍͛̋̐͆̎̈́͂̅̽̈̏̎̇̔̓̈́̈́̑̍̈́̄̓̊͒̈̕̕̕͠͝͝ ̶̨̡̡̧̱̩̪̥͎̤͍̦̯̠̩̤̦̘̩̘̦͙͖̱̙͓͖̤̰̗̭̻͉̈́̂̏̊̈́̉̃̚ ̴̡̛̛͍̩̩͎͖̪̰̱͕̬̟̗͇̻̠͛͒͆̇̈̋́̄̓̀͑̅̇̀̃̄̽̔́̂̓͐͊̐̂̋͆̊́̊̄͂͆̈́̾̈̔͆́͘̚͘͜͜͝͠͝͝ͅͅ ̵̢̧̧̧͚̬̟̳̰̯̥̤̳͓̞̰͓͚̜͇͚̫̦̦̭͍̠̟̝̙͔̺͙̩̂̓́͊̈́̋̉͛͋̆̓͒̀͑̇̒̎̏̈́̈́͘͜ͅ ̵̡̨̢̣͚̯͓̤̰̬͕̫͓̩̠̰̠̦͈͐̇͐̓̐̌̊̑̈́͊͂̋̉̅͆̈́́̉͆̒̒́́̆͐̔̓̂̍̆̍͋͛͗̓̎́̀̏̋́͗̉̕͘͝͠͝ͅ ̵̡̨̡̨̢̮͔̙̘̲̘̥͚̳͉̭̥͚̮͙̼̤̣̳͖̩̻̥͔̪̤̹̰̟͖̦͎̣̦̳͓̥͕̦͕̘̣̎̈́̔̄̆̈́́͂̅͑̐̊̈̾̍͑͊̍́̀́̚̕͘͠ͅͅ ̴̢̛̮̘̻͈͚̦̺̠͔͇͕̮̳̠̲̘̝̜̳̻͍͖̯̬̮̠͕͍̗̹̦̭͇͙͎̯̯̮̤̙̒́͐̃̈́̾́́̿̎̈͜ͅ ̴̢̲̖̟͖͙͑̄͒̀͌̊͠ ̷̨̨̢̢̛͉̩̖̦̙̣̣̜͍̝̙̗̟̥͚̻̳͖̱͇̤͈͈͈̲̯̝͓͍̗͖̤̙̣͖͈͇̺͓͇̳̲̉̈́́͑̂͜͠ͅͅͅ ̷̧̛̥̭̻̻̖͇͕͍̖̳̼̼͎͕̘̺̳̯̗̘̭̰̳̥͈̖͍̘̥̫̣͈̺̯̝̫̓̉́̌̎͗͊͋̈́́̾̾̀́̇̏̔̄̏̍́͌̍̀̔̒̊̋̇̅͗̅̕͝͝͝͝͝͝͝ͅ ̴̨̨̡̡͎̲͚̩͕̺͖̩͚̻̪͔̰̟̺̲̲̺̞̤̼̩̮͇̖͓̬͔̝̖̻̼̫̻͇͋́͂͘̕͜͜(̵̨̡̡̝͚͉̠̤̙̺̲̫͓̟̱̩̱̫͖͈̪͓̩̞̝̦̿͌̉̒̾̇̑̓̀̍̋͋̑̆̎̈́̕͜͝͠͝4̷̡̛̼́̐̆̆̍̃͑̾̀̎̌̅̄̈́̽̒͂̋̋̑̓̀̓̊̒͂͗̈́̎̄̀̽͋͛̂̆̅̕͘̚͝͝͠͝)̷̛̱͓͔͇̣̻̑̅̓̆̋͑̍̂͌̍̊̑̑͂͆̈́̈͌͗̈́̉̀͌͗̑͆̈́̕̚͘̕͠͠͝ͅ ̷̛̳̺̥̺̎̈́̋̂͋̄̇̃͐̑͗́̆́̔̓̾̉̆͒͂͘̕̕͝͠͠C̸̨̛͙̎̐͌͌̎͑̅̏̆͊̀̅̽̀̀͌́̓͛̓̓̓͗̃̎̐͑̊͐̇͌̆͐̕̕͝͝͠ĥ̸̞͍͔̦̜͍̬̲̲͙͉͔̰͙̠̖͔̟͉̙̺̣̜͙̈́͋͗̑̅͒̂̄̊̎̽̿̎̑̾̈̒̎̄̔̉͛̀̐̒̽̈́̊̊̚͘͜͝͝e̷̡̛͈̯̮͔͌̎̿̔̐͂͋͂̊̏̀̉̇̉̊̂̊͗̈̊̕͘c̴̛̛͕͇̓̈́̅̂͆̈́̐̐̑̎͒́̐̒͋̌̌͑̈́͊̔͗̓́̈́̒͂́̉̋̇̎̃̒́͆͗̒̚̚̚͠͝͝ķ̵̡̧̛̠̞̖͈͍͉͓̭̺̟͔̘̤̰̤̺̩̱̦̣̹̠̗͇̫͓͚͖̖̦͖̖͕̱̩̑́̌͊́̌̆̈́̍̓̌̾͊͗̅̅̄̎̑́͒͊̎̈̆͐̈́̌̍̈́͛̇̄̾̿̕̕͝͝͝͝ ̷̧̨̲̻̺͕̦͍̥͓̙̩̗̾͌̀́̿̐̀̎̾͛̆̊̉̔͐̍̈́̑̓̌̉͛̎̐̑̈̿̂͆͑̇̀̚̕͜͝͝ͅK̷̡̛̪̫̰͕̙͔̋̀̌̂̓̍̍̾̊̌͐̈́̈́̾̇̅̓̈̽̑̾̌́̔̓̍͗̅͌͘͝͝ͅį̵̻̣̙̘̲̬̥̺̪͂͒̍͑n̶̤͇̈́̈́̾̀̄̉̇̔̑̽̅̅͌͆̂̉͆̏̒̂̄͐̆̈́̑̓͂̈́͗̄̆̓̅̓̈́͋̽̉̆̃͐̚̚͘͝͝͝ǵ̴͈̹̝̣̹̺͖͇̭͚̬̩̄́̓̅̐̆͗͆̆̈́̍̂̿̊͐͐̾́͐̏̇̚͘̕͠ͅd̶̢͎̘̺̹̳͔̫̻͇̎̊̂̈́̂̈́̄͌͘̕ö̵̡̧̧̧̧̖͉̩̯͔̱̠̱̰͓̫̣̼̲̬̹͔̟̖̫́̇̂͘͝m̷̢̧̨̟̝̝̝̠̗̺͕̭͍͙͎̣̲̖̯̘̟̞̟̜̰̠̼̞̖̯͍̹̥̫̻̂̀̉̀̐̇̈̊̎̓͆͜͝ͅ ̸̢̛̼̘͍̩̝̑͂͒̀̊̀͆̆͊͐̾̓̀̓̇͂̄͘͝S̸̢̧̡̡̡̨̧̹͈͙̖̼̣̱͇̪͙̲̹̲͓̞͙̱̘͖͎͍̦͇͙͎̪̓͒̀̔̇̀͌̀́̆̎̐̈́̉͒͘̚ͅt̴͓͔̱͙̱̺̝̜̹͂̈́̀̑̔͊a̶̢̧̡̡͚͎̥̟̪͙͇̦̱̭̟̣͖͙̹̟͓̙̫̖͉̪̙̱̥̥̱̞̫̭͙̫̞̻̞̱̜͕͖͊̄͛̐̃́͊͊͐̋͊͐̎̂͊͒̃́͗̔̎̓͐̐͒̒̄̕͠͠͝͠t̶̨͉̬̪̠̤͔͙̯̠̠͖͖̤͖͓̟͉͙̲͍̖̭͈͐̍͜ͅs̷̛͔̥͚̭̲̳͍̽̀̂͗̎
        ̷̢̧̨̛̛̱̥͙̟͖̜̟̦̫̺͈̲͙̙͍̝̬̠̬̺̙̝̹͎̣͕͓̗̤͇͍̠̻̲͎̅̋̈̔̈́͑́̔̈̿̉̉̊̇͌̑͋̀̈́̓̐̊̎͐͒͗̀̅ͅ ̴̧̹̻̺̲͍̖͍̯͚̬͂͊͋͊̔̓̉̍̓̐̈́̅́̋̊̌͑͂́̍͛̍̄́̿̃̈́͛̆͗̎̓̆̽̀̎̌̇̂̑̂̅̚̚͝͝͝͠ ̴̡̧̨̛͉̭͚͈͓̫͉̈́̈́͊̑̈́̃́́̏͑̋̋̄̓̌̅̀̀̉̍̈́̿͂͑̈̿̊̚͠͝͠͝ ̶̨̡̨̢̗̫͇̣̬̫̗̩̻͎̼̪̳̮̗̖͚̟̤͉͔̠͙̼̗̜͔͈̼̳̼͙͚͔͔̼̖́͗͛͌̒͂̃͊̀͋́̉̀̅̋̄́̒͛̋̀̓͛̓͋̇̋͐̽̇̓͑͐̉̚͘͘͘̕͘͜͝͝͝ ̷̨̨̡̮̪͈̹̰̬͓̺͈̻̦̮̻̲̲̦̩̜͙̳͙̹͚̼͉͙̩̏̑͗́͗̓̋̋̎̓̅̓̇̂̀̂̚͜͜͝ ̴̦̣̩̯͚̟̘͈̘̘̼̖̳͔̲̘̜͇̬̪͓͕̼͙͇̬̖̞̩̰͔͍̮̟̜̺̳̍̈́̃̊̋̆̐̆́̓̓̓̾̄͑̓͛̋͑̿͐̽̋̽̈́̾͋͆̓̓͒̍͋̐͌́͐͂̆͐̂̋̿͘͘̚͘̕͜͝ ̸̥̪́͗̀̍̓̐͐̓͗͋ ̶̜̥̼̘͈̉̊̇́́̏͆̔̚͘͝ ̸̧̡̛̜͈͇͎͚̜͈̠̬̠̗͎̮͚̖̪͎̻̦̭̻̀͋̈̔͆̈́̐͒̀͗͐̂̽͑͛̓̎̈̕̚͜͝͝͠͝ͅ ̸̡̧̧̡̧̢̛͎̭̣̻̰̜̟͓͈͙̠̲͔̪̜̻̟̫̰͔͚̀͂̎̊̇̊̆͋̀̑͒̐̉̿̂̐̌́̕͠ ̸̢̨̢̹͕̤̫̩̗̖̤̰͉͈̫̲̩̜̤͖͕̞̭̙͍̬͎̝̰͍̳̝͍̖̼̝̖̮̳̠͖̣͍̃͐͐͑̀̃́̉̌̌͆́̓̀̈̾̽͂̐̉̋̓̓̈́̿͋̏̍̏̊͗͗͗̿̋͂͘͜͜͜͠͝͝͝ͅ ̷̢̢̢̲͕̰̬̳͉̥͙̭̙̭͙̠̘̯̭͖͖̙͎̳͈͕͔͔͖̀̓̃͛̈́̒̈̄͒͊͂̂͒̋̆̒̃̋̀̎̄̓̅̑̅̂͑̂̽̈́̇̚̚͘͘͝͠ͅͅ ̸̦͈͕͔͉̰̖̫̞̗̎́͋̑͗̆̊̂̐͠͝ͅ(̷̳̙͔͓̻̖̳̪̗̈̾̅̐̍͐̎̂̕̚̚͝͝͝5̷̛̹̭̩̗̟͖̖̟̮͕͇̗̝͕̮̜̤̦̞͍̜̱͚͔̙̮̋͑̊̍̿̉̄͜͜͠ͅ)̸̡̛̛̛̛̦͇̰͈̱̩̘̙͍̩͓͍̙̠̗̣́̈͑̒́̓̏͛̅̈́̓̈́̀͊̿͗̑͑͑̈́̅̒͑́͒͘͝ ̴̨̛͉̩̮͇͕̠̩̥̠͔́͗̐̓́̂̃̓̽̇̊̄̊̾͊͌̄̊̀̈̆̒̽̄͗͛̿̓̂̓̈́̎̾̓̌̌̾̾̆́̃̃̚̕͠͝Ḩ̴̡̧̧̛̪̭̻̪̺̭̯̺͚͙͍͖̝͍̝̘̦͔̳̼͚̼̲̳̞̺͖̾̅̓̀̿̔̎̀͛̅́̅͛̌͐͘̚͜͜i̸̡̢̧͕̪͓̝͙͚̥͉͎̣̩̭̻̫̣̙͖̞͈̪̻̙̻̘͍̯͎͉̻͙̝̫̣̦͔̳̭̮̜͚̹̝̟͓̋̀̏͂̈́͝ŗ̸͈̰̞̬̗̳̩̺̹̟͔͙̮̠̰͖̖̈͆̑͌̏̓̏͗͑̃̾̾̋͋͆̈̑͂̑̄̌̇̇̀̏̏͊̍̂̑̐̈̿̃́̋̚̕̚̚͘͠ę̵̡̡̛͇͉͙̮̜̫̟͕̋̌̓̄̏̓͆̓͆͛̽̒̐͐̔͋̃͑͂̅̽̆̀̍̔̈́͒̎̽͋͘͜͠
        ̸̡̡̳̫̥̺͇̺̲̥̗͖̳̠̮̭͉͉̰͍̳̳̍̌̿͂́̿̽͛͛̆̃͜ ̸̡̡̛̼̻͎̙̖͕͓̣̳̞̯͚̙̘͔́̍̽͌̿̓̓̑̆̾̿͗̈́̇̓́͋̎͋ͅ ̶̡̨̛͓̺̫͉͚̩̟̦̬͚̩̺̞͍̥̟̋͒̇̈́͛̇̐̄̒̐͂̾̔̑̓̿̍̓͒̽̏̈́͊̌͒̋͒̃̏̊͌̿̈́̄̆͘̚͝͠͠ ̸̡̢̢̡̧̧̢̝̬̙̰̱̦̫͍̘̳̝̙̪̩͓̭̫̞̗̱̘͕̹̣̲̤̥̼͚̰̱͙͚́̔͜͜͠ͅ ̴̢̨̻͓͇̲̖̙̬͍̝͓̠̹̬̐͋̉̋̅͒̈́̃͆͊͑̿̎̓̾̃͐̈́̚͝ ̶̛̛̟͖̳͇̱̩͍͍̗͕̖̜͍̲̀̒̎͒͗̀͂͋̑͂͊̈́͒̀̏̓̃͋̎͒͗̓͌͒̍̍̋͘͠͝͝͠ ̷̢̨̛̛͓̫̱̲͎͓͇̬̘̱͔̻͚͍̟̹̺͙̹̱̣̱͓̯̞͓̯͔̰̙͍̝̙̗̙̃̒͒̂͋̓͐̂̿͐̉̒̑̎́͐̋̾̆̋̍̈̒̔̀̔̓̑̓̅̄̍̀̀̏̈́͛͆͜͝͝ ̸̺͙̮͎̫̬̱̣̭̼̟͕̳̩̭͚͓̗̔̊̿͗̉̈́͗̽̄͛̔͜͝͝ͅ ̷̨̨̨̩̞̙̱͕̣̠͖̫̩̫̦̩̰̭͚̲̥̘̪̙̫̱̪̭̩̥͓̝̫͙̼͈̪͇̤̲͎̳͑̚ ̶̧̬̲̤̻̜͎͍̻̱̤̝̣̞̘͓̜͋͊͂͗̇̆͋̎̋̿̐̒͒̆̔͗̀̒̃̈́̅̂̒͑̈́̐́̀̆͗́̌̈͛̔̓̒̄̚͘̚̕͘͝͝͠͠ ̵̡̛̰̰͔͎̲̹̙̘̙͎͈͍̗̿̅̀̉̋̅̎̐̏͑̓͋̊͌̑̐́̄͋͠ͅ ̸̧̨̧̥̣̣͔̯̫̩̮̺͔̘͇͖̣̯͇̟̣̠͓͎̣͕͉̬̘͚̟̙̭͍̝͎̙̘̰͙͍͈̮̮̞̮̰͈̠͑͐̏̽̀̏͋ ̸̨̛͕̞͍̬͓͔̼͉̦͈̟͇̤̘̜͙̤̟̜̦̖͔̩̗̳͐̂͆̿̔̍̉͗̇́̉̎̈̈́͌̈́̔̌͒͒͋̉̃̍̾̌́̈́͜͜͠(̸̢̢̡̢̨̟̩̠̮̭̘̞̲̞͈̼̪̞͖̣͓̼̼̲̯͚̝̺͙̥̯̤̽̔͐̄̄̈́̇̑͆̑̄́̍̑̈́̐̐̾̾͐͐̑̐̏̊̓͛̊̌̋̀̚̚̚̕̚͘͝6̸̥̙̞̬͍̹̦̖̳͚̣̱̩͍̓̚ͅ)̷̭͇̣̯͇̣͙̘̰̪̥̯̭̺̪͕͆̍̅̋͆͌̂̒̋́̈͊̃̐̂̆̚͜͜͝͝ͅͅ ̸̼͍̱́̓̈́͌̊̑̆̔́̍̎̓̔͂̈̋̃͂̑̈́̃͊̄̓̕̕͝͠Š̷̢̨̨̛̰͎̘͎̳̹͍̜̠̼͉̺̜͕̬̤̲̲̰̫͔̯̜̫̤͎̭̰̏͆̌̾̾̇͑͂̀̍̂̆͆̀̇̅̉̀͋͐͒̌͐̋͐̔̊̆̐̏̀̐͋͛̏͂̏̓̕͘͜͝͠ͅͅe̶͍̱̓̉̒͂̄̆̈̐͂̿̀͊̉̒̊͑̆̿͗̊̀̅̃͌̓̚͘͠͝͝t̶̢̢̢̛̰͎͉̖͙̪͍̟̯͎͕͚̣͙̬̭̣̣͖̩̠͓̘͓̜͖̄̒͆͋̒͊̆́̓̓͛̽͆̒̐̃͌̒̍̔̽̈́̉͂́̀̇͒̀̆̿̆̔̊̀̄̀̃̕͘͝͠͝͝ͅͅt̷̡̧̛̳̦͈̪̪̺̫̲̱̪͕̩͎̫̥̥͕̻̙̰̥̱̜̬̰̹̄̉̈́͂̉̒̄̆́͛̋̄͗̌̆̓̇͆͑̀̓͋͛͋͐̓͘̕͝͝͠ͅi̷̮̤̩̼͓̣̬̭̩̳̼͖̮̤͍̝̠͙͓̹͈̺̼͙̲̋̄̏͛͐̉̆͜n̷̨̢̧̞̱͖͖̙̫̪̯̭̙͙̖̳̼̰̰͙͍̻̝̖͍̭͔̯̺̫͉̩̅̎̐̌̊̃̅͒̒̀̒̿͛̃̾͌̽̾̈́̎̎̀̔̐̆̏̊̽̎̆̍͐̌̑́͘̚̕̕̕̚͠͝͠͝g̷̨̧̨̡̧̨̨̨̡͎͖̫̞̮̝͚̬͈̺̺͇̫̹͎̳̗̩̝̣̩͉͕̲̖̻̲̰̦̩̩̗͔͔͌̌̂́̋̋̄̆͂̏͛͆̑͒̎͌̋̄͌̔͜͜͝ͅs̵͔͉̗̞̪̦͓̹̯͍̺̯̝͚̞̺̰̖̫̬̞͓̺͖̦̥̰͖͕̳̞͍͆̈́̄͌͗̈̋̄̆̾̌̽̈́͌̌͊̔̃͂̾͌͆̄̐͌̃̏͐̓̑̅̓̓̈́́̃̍̚͘̕̕͠͝͝͝͝͝
        ̶̨͔̬̥̰͉̖͙̟̪̗̲̤̝̘̥͍̘̼̯̠̔̓̓̊́̀̃͒̾̒͐͗́̀̈́͐͌̃̑͗̄̈́͋͌̄̍̉̓̎̉̊͋̋̇͗̐̀̕̚ͅͅ ̶̨̢̢̧̨̛̗͔̳͚͚̯̗͖̜͉̰̗͚̗̲̼͓̠̜͈̩̺̳̬̭͕̪͈͓̳̘̌̑͆͒͋̌̍̀̈́̒̄̀́̑̈̉͛͊̐͑̂͛͑̾̓͘̕̚̚͜ͅͅ ̶̧̧̛̛̛͕͈͎̤̼̝̪̤̭͔̱̺̟̲̠̩̙̬̖͓̜͓͉̠͎͙̘̗̟͎͙͙͉̻̗̲͙͐͐̃͌̀́̽̑̃͊̿̂͊̌̇͗͑̉̀̄͒̆̎̏̄̈̉̎̍̏͑̋̓̈̊̒̉̚̕̕͝͝ͅͅ ̸̡̛̛̼̠̺̞̤͖̻̪̫͕̙̯̱̩̦͉̠͙̬̎͆̇̉́́̍̍̿́͊̓̐̍̄̉̀͒͋̾͂̌̊̊̊͂̋̕̚͜͝͝͝͠ͅ ̷̡̧̢̡̢̢̼̼͈̫̲͓̙̲̰̟̩̺̬̙̖͈̹͎̗̫̰͉̞̝̘͙̙̲̝́̐̆̆͋̿̈̀͋̀̄͐̐͆̕͘͜͜͠͝ͅ ̸̢̧̢̟̱̭͎̱̝̺͎̪͙͈̺̼͉͔͕̑̓̀̈̈́̓̊̉̂͑́̆̈́̐̋́͊̈́̕̕͝͝͝ ̸̢̢̢̡̧̩̙͇̬͍̦̞̲͎̠̺̬̱̹͍̰̫͕͙͕͉̮̪͔̞̘͕̰̞͎͓̰͒̆̎̋͊̌̈́̈̿͐̈̿̌͊̃̐̌̍̀͘̚͝͠͝͝͝ͅ ̴̡̨̧̪͖̘̫͍̗͓̘͙͚̼̼̥͖̌̉͋͛̽̋͋̎̌̈́͐̏̊̉͛͐̈̀͑̀͗̽̌̿́̈́̈̀͒̚͘͝͝͝͝ ̴̢̨̧̨̢̛͔̘̫̱̙͙̥̫̗̤͖͉̟̱̲̯̟̺̼̲̭̙̗̼̯͇͍̝͙̯̬̗͎̩̺̦̟̼͎̠̬͇̘͎͖͋͆̓̍͒̽͆̽̆́̊͌̓͊͂̎̓͑̊̀͐̽͗̈́͋̈̂͂̇͛͗̃̾̃̚͘͠͝͝ ̵̧̢̛̛̩̗̲͔̙͕͚̙͇̹̬̟̬̥̣̤͖̤̹̻̤͈͈̹̩͎̭̙̲͇̟̜̺̣͚͍̭̹̯̜͔̺̞̩̫̳̇̈͒́͗̏̐̍͑̾̂͋̈́̀͑́̈́͑̽̊̅̒̒́̓̍̿̈́̓̓̆̐̆̓̓̅̔̐̕̚̚͝͠͠͝ͅ ̸̧̡̛̥̬̫̦̻̺̱̰̠͍̪͉͚̙̜̺̮͇̰͔̫̻̘̮̘̬̰̫̯̦̗̥̟͖͓͚̥͓͕͙̘͕̎̾̌̆̿̅͜͠͠͠ ̴̡̧͕̣͖̦̥͉̠̘̱͕̞͓̗̼̙̣̭̳͖̼̗̦̼̹̩̓̏͂̇̊͋̅̋͆̉̈́́̕̚͘͠ͅ ̴̧͔̳͎̽̈͜(̷̡̨̤̲̝̞͎͒̄͊́̈́̽͊̽͑̀͑́̋̆̚͜7̴̡͔̦̙̭̖͎̥̂̌̃͒̅̾͗͒̒̈́̄̄̑̓͊̔̈́̽͘͝͝͝͠)̸̢̧̧̢͚̻̟̤͎̤͔̬̩͎̬͇͔̙͎̦̤͉͇̫̼̪̙̻̬͙̰̤̤̼̩̰̮́̎̾̃̒̔̓͒̌̌̅͛̅͋͋̇̈́̅͆̾̈́̔́̈́͂̈́̚͠͠ ̸̖͛̍̍́̌̿́͝Ų̷̡̧̢̨̰͙̟͚̰͎̲͍̺͚̞͕̻̯͙̹̞̫͙͙̻̗̩̙͚͓̹̉̅́͊̿̀̔̑͜͜͠͠p̴̛̱͍͖̲͔̼͓̳̱̻̯̮̘͔̎͌̀̓̄̋̏̉̔̈̉͗̈̀̊̄̅̍̾̀̓̃̐̀͒͛̎̈͆̚ģ̸̳̪̳͇̪͇͚͇͔̭̜̟̭̹̘̤̖̫͍́͛̊̋̋͒̃͠͝͝ͅͅŗ̵̧̛̛̘̺̻̯̩̜̜̗̟͔̟̠̺̲͈̖̰̭̬̥̬̗̙̺̙̀̎̆͌̅͒̊̌̾̊͌̅̋̋̊̀̈̍̓̈́̓̃̏̀̈́͋̑̂̃̿̓̆̓̈́͘̚̕̚͜͝͠͝a̶̧̡̡̢̢̢̢̨̧̛̛͕̲͙̮̯̹͉̺̥͇͔͓̲̱̘͓͔̲̬͈̤̜̲̞̼͈̜͈͇̱̮͙͓̳͔̖͔͋̈́̿̍͋̊̂̔̎̅͌̐̐̇́͒̎̓̄͒̽̆̈́͐̈͛͆̚̚͜͜ͅd̵̢̨̗̭̘̠̙̱̪͙̹̜͕̞̀͌̓̋́̋̀̎͌͒͛́̈́̇̍̇͊̇̈̄̆̽̓̀̓͘͘̕͜͠͠ͅͅè̵̢̡̨̛̳̦̖̖͚̠̝̥̯̖͙͙͈͕̝̯̞̱̱̬̩̹̘̥͍̹͔͈̲̲̪͍͕̩̰͈̥̠̹͔͛͊̒̏̃͌́͒͐̒́̒̄̇̉̃̋̓̈́̈́͋̾̐̽̌̇͛̆́̂̄̋̋͋̒̐̆̒͒͛͐̓̄̕̚͜͜͝ͅ ̶̧̤̳̰̜̳̫̃̉͝I̵̡̛̛͍̤̼͙̙̯̝͙̼͙̘̠̫̲̫̅̍̅̿͗̂̌̉̈́̂̓̏̏͊͊̑͛̈̆͐̈͗̇̇̚̕̚̚͜͝͠n̴͖͖̘̭̱̦̘͔̤̽̎́͑͑͐̌͜͝f̵̡̢̙̘̻͎̺̮̮̬̮̫̦̜̤̬̱͔̟̣̫͙͓̱̮̟̹̭̲͈̫̀̒̀̃͐͜͝a̸̛͕̪͉͛͋̀̃̊ͅn̶̨̝͎͎̪̣̺͎̻̺͍̜͔̲͙̖̙͕̱͇̹̤͈͔̮̣͙̽̈͗̾̂̈̎̌̇͊͒́̋̀͋̃̿͑̔̿̐̇̕͘͝ͅţ̴̢̢̡͉͉̝͙͈̲̹͕̫͓̣̪̮͚̲͚͎̜͈͓͈͉̣̩̻̫̯̭͕̬̤̯̤̳͚͖̰͖̀̈̊̈́̋̽̄̐̂̄̀͂͛̊͂̔͜͜ṙ̶̡̧̡̨̡̛̺̰͇͍̠̗̭͚͍͈̤̮̟͔͚̙̻̫̖͉͕͎͔͉̻̪̭̣̱̗͓̣͙̣̉̄͊̋̎̊̑̋͒̉̓̎̀̾͌̑̔͛̚͜͠ẏ̷̢̛̥͉͇̤͉͚̙̤͕͍̇̇̀͐̈́͒̔̉̅̉̉̽̏̒͐̈͆͘͘͝ͅ ̷̢̨̧̨̨̧̛̛̛̱͓̻͍̟̺̠͕̮̖̺͈̰̭̙͕̫͉͔̥̘̼͉͉̅͒͂̂̄̃̈̓̏̑͋́̔̽͒̂͆̃̽̿̉̀̍͋̽́̃̆̎̔͛͗̉̚͘͘͘͘̕͜͜͜͠͝ͅP̴̡̡̟͎̣̺̪̳̯͔̫̰̦̝̙̺̠̙͚͉̩͊̇̾̀̈́̒̀̃̈́͊̒̈̎̿͑͗̌̑̇͛̓̕͝ơ̸̧̡̛̭̠̪͙̮͉͔͓̫̯̬̼̭̲̗̤̬͕̣͒̈́͑̄̽̎́̔̈̈́͆͆̾́̈̈́̑̀͆̑̒̓́̈́͆̓̋̔͛̊͆̈́͋́̈̇͊́͛́́̓̀̃̚͘͜͝͝w̸̢̡̨̨̡̢̨̬̰̠̲̰̱̪͔̟̞̬̠͚̟̙̣͚̣̲̞͚̼͙̫̗͔̖̲͍̫̫̥̞̪͚͒͑̍̋̇̏͊̎̒̐̀̊̔͘͜͜͠͠ͅe̸̡̡̡̨̛͙͔̥̱̙̤̱͓̦̞͕͎̞̖͇̠̘̣̐̃̓̓̌̔͋̓̏͜͜ŗ̶̙͇͕͑̾͝
        ̸̻͚̳̖͕̟͙̅̿͒͜͠ ̵̡̡͇̙͖̳͖͈̳̞̪̻̪̥͕̯̜̪̠̩͎̹͎̰͎̦̻͚̹͇̙͚̦̘̝̰͕͍̙̺͕̻̙̘̠̂͛̉̔̿͋͐̑̂͆̐̽̾̐͒̒̈́͜͠ͅ ̸̧̢̨̢̛͉̙̦͉̹̭̲̼͈͙̣̬̹̱̻̱̗̒̈̅͗̐͂̒̊͛̆̀̃̊̇̒̈́̂͘͘͝ ̵̡̡̢̧̛̜̲̖͍̞̣͚̪̟̺͓̠͕͈̳͇̗̯͎̥̙͇͚͇̗̬̞̗̮̮͉͇̬͓̩̼̉͊͊̆̅͒̓̓̾̓́ͅͅͅ ̸̨̡̛̥̞͇̹̘͙͚̠̜̩͎̻̦̲͈̭̳̥͍̣͉̰̈́̄̈́̋̽͌͂ ̸̢̢̨̧̨̬͖͎̞͔͕̜͎̠̖͔̦̙͓͙̖̼͖̣̽́̔͒͊̃̅̓̄̓̆̍͂̆̋͑͆͌̓̂̄̾͒̃̅̍̔͆̂̄̈́̒̐͘͠͝͠͝ ̸̡̨̛̦͙̺̮͉̣͇̻͉͎̟̯̖̩͙͔̺̦͍̬̜̺͎͚̥̩̣̜͚̠͈͔͔̂̊̅͛́̅̓̓̐̉̓́̍̀̆̎͒̍̂̐̃̽̅͛̈͑̂́̂̔̽̈͆͊̐͜͝͝͝͝͝͝ͅ ̴̢̢̡̪̙͎͍̯̳͈̩̥͓͕̮̻̞̼͕̯̙̮͎̬̤̟̣͙͍͙͇̺̖̥̞͍̪̟̺̬̲͉̩̘̿̉̿̉͠ͅͅ ̷̧̡̨̛̜̮̱͇͕̺̦̼̬̻̰̫̰͙̜̫̟̙͖̹̿̓̂̏̽̈́͜ ̷̺͖̭̹̙̬̈̽͐̎̓̂̔̉̍̇́́̾͒̔̒̍̂̉͋̈́̆̀͛̈́́̅͒̔̏͆̑̊̅̃̃͘̕͝͝ ̴̨̡̛͖̤̭̙̝̱͔̖͇̦̞̤̱̼̩̜̞̲̠̯͔͍̫͓̖͕̃̈́̄͊͆̍̋͋̀̒̇́͗̍̾́̄̀̓̈͛͋̈́̀̿̀͐̄̊̉͌̑͊̌̃̋́͑̆̈̃̀͋̄̆͝͠͝ ̴̰̼̰̪̻̬͚̪͙̪̘̞̘́͋́̄̈́̈̓͆͆́͂̑̇͆͐̈́̏̈́̐͌̈̒́͊̀̒̌̕̕͝ ̷̡̻̺͇͇͓̯̮̣̜͎̺͎̩͇̫͓̝̥̼̞̺̼̞̳͚͈̞̖͖͓̫͈͔̘̯̎̈́́̏͒̃͒̒̿͋̽̓̈́̓̃̄̚̕(̶̧̡̧̧̘̪̥̭̤͓͈͚̹̜̯͔̗͙̆̔͒́͂̏̅͛̔̉̑̓͒̍̓̽̎͊̅̕̚͠ͅ8̷̧̛̛̱̳̗̱̘̤̞͉̦̻̖̣̰͔̦͇̇̂̾̂́̆̅̇̓̑̈́̈́̌̒̉̇̿̈́̒ͅ)̵̧̢̧̖̙͍̲̼͈̱̯̞͕̺̣͇͔͖̰̝̪̩͍̠̺̯͎̼͎̤̞̥͖̪͙̞͈̤͚̻͕̝̅̎̾̏̏̐̓̂̍͆͗͊̐̊̇̎̐̑̅͋̈̐͑̾̃̅̾̽͋̂͌͜͝͠͠͝ͅͅ ̵̡̨̨̢̛̤̥͕̜̹̥̦̟̤̺̯͙͈̗͔̘̞͙͓̱͓̪̮̤̣̰̘̖̬́̏̌͌͋̈́͒͌͑̓̄͊̏̽̀̓̍̄̎̋̔̌͋̓͛̐̒̒̐̎̋͗̉͒̄̽̎̕̚̕͝͝ͅͅP̸̧̨̧̛̛̪̘̫̻͓̮̜̦̖̟̪̪̱͓̬̪̹̘̙̺͍̣̲̙̳͉͔͓͎̈́̈́͒̈̏̇̾̇́̎͆͒͂̆̊͋̒͝͝͝ͅę̸̨̧̨̖̖̫̹̲̻̗͔͚̘̺͚̮͆͜͝ͅa̶̢̢̨̧̫͈̩͓͍͙̼̪͈̯̩̲̠̘̟͇̣̽̓̿̇͋̉̈͊̒͝ͅc̸̨͕͉͚͚̰̗̭̻̼̤̜̝̱̪̖̠̠͈͖͕̫͎̗͙͖͂̒͂͋̈́͑̄̀̋́̈́͗̓̂̀̃̾͊͑̏̇͂̋̍̾̓͐̂̋̿̽̑̐̕͘͘̕̕͜͜͝͝͝ͅế̸̡̢̡̢̡̧̧͓̤̹͔͕͇̠͇͓̺͙͇̦̳̯͇̝̤͈̯̝̟̩̼̜̻͖̱̞̩̙̭͉̭͉̲̮̰̜̔͂̓͗̄̾̎̽̍̀͒̾̈́͌̽̈͑̔͊̌̀͌͐̀̏̀̽̈̎̋̈̎̃̋̈́̐̍̆̋̏͘̕̚͜͝͠͝ͅͅ ̶̧̧̧̧̡̝͇̲̻̩̹̞͇͙̮͈̥̹͚̞̯̰̫̣̪͓̲͖͖̙͓͎̞̬̲̳̉͂̽͗͜ͅT̶͎̦̘͂͒̈̓̅̿̏̑̍́͌͑̀̔͑̓͒̾̊̾͂̓͗͒̀͒͆̕͘͝͠r̴̨̛̯̋̍̈͌̊͋̈́̽͛̏̒̍̏̆͋̿̈́̿̕͜͝͝͠ẽ̸̙͓͖̺̬̺̱͎̮͎̣̀̏̇͂̀̋̔̀̾̈́̓́͛̉͗̀̎̈́́́̐͐͆̑̉́̂͌͊̆̓͘͘͜͝͝a̷̡̨̨̝͖̼̰͓͕̦̗̙̜͚̥̻̺̩̜̓̀͂̈́͑̒̀̈̉͒̉͒̽͆͂́͆̔́̐̆͘͠͝t̷̢̢̧̡̜͕̬̠͖̙̰͇͇̰̭̼̮̗͚̣̤̬̥̺̪̗̓͛̇͋͆̑͊͒͝͠ͅy̴̧̧̛̺̼̻͚̗̠̙̖͈̺͙͓͎̞̻͔̯̭̗͎̺̟͙̭̱̟̰͈͚̟̤̘͙̙̼̝̮͆̾̊̓̓̉͂̑͋͆́͋̈́̓̌̽̽̈̎͑͑́̒̅̅̿̔̂͌́̃̿̚̚̕̚͜͠͝ͅ
        ̶̢̗͔͚͙͔̲̰͈͕̲̯̟̟̣̠̝̤̞̙̋̀̍̈̌͊̀̅̓̀͗́̽̅́͐̈́͒̈̋̒̿̌̈͌̔͂͆̕̕̕̚̕͝͝ ̸̨̧̧̬̬̲̝͔̜̫͇̬̜͍͎͈͖̼͙̣̐̅͛̀͆̓͜͝ ̴̢̧̧̢̡͖̝͇̮͓̟̻̘̲̳͎͎͚̩̜͈̭̖͓̤̞̣̪̙̺̳͕̭̮̱̗̺̩̥̫͔̼̟̹͉̜͕͒̂̓͗͌͂̌̇͛̐̿̈́̐̂̒͐̓̿́́̾͑͂̐̎͊̌̊̈͒̚̚̕̕͝͝͝ͅ ̶̢̡̢̡̡̜̩͙͈̜̭̪͍͔̮͖̼͉̹̹̗̞̞̻͈̣͎͕͇̘̗͉̯͈̝͓͇̻̭͍̯̭̖͇̽̓̀͒̆̇̔͑̍̾̾͋́͐͛̑̒̐͊̇̍̎̉͗̄̃̀̀̄̾͋͌̾̑͛̃͜͜͜͜͝͝ͅͅ ̸̢̡̨̛̻̺̞̭̻̗̮͎̟̻̠̲̲̺͉̬̰̭̱̳̟̮̳̤̹̗̘̬̱͇̣̅̀̚͜ ̷̢͇̱͈̜́̆̈́̅̒̌́͒̈́̉̏̔̈͋̔͒͛̎̐̋̉̆̔͊̋̎̍̌̊͛̃͌͐̎̂̍̊́̐͒̚̕̕͝͠͝ͅ ̷̢̡̭͎̹̺̠͓͎̝̓̐͌̽̋̆̽͐̅̔̑͋̈́̏̌̌̑͌̄̈̀͛͐̍̅̋̃͑͜ ̵̢̡̛̣͕̩͚͍̜̜̮̫̮͍̤̪̹̰̳͉͍̟̥͕̣͎̼͍̯̭̜̥͓̠̳̗͖̫̱̱͚̩̿̿̊̒̍̌͒͜ͅͅ ̶̡̛͎̪̖̟͙̟̝̹̠̥̩̀͂̈͛͊͑̏̍̓͆̾͋̉͗̈̈̈́̐͋̊̈́͜͝ ̶̛͇̜͚̖̤̃̅͌̾̀̂̌̓͌͂͗̄̋̆͌̈́́̇̄͛̀͒́̚͘͜͠͝ ̷̡̣̥̳̯̖͎̟̬͆͛̋̾̐̑͊̌̈̌̀͗̉͝ ̵̧̢̡̧̢̧̪̮̩̹̲̫̺̳͉̲̬͙̜̩̘͖̩̮̩̩̮̯͇͍̤͈̣͓̟̩̫̗̠͔͎̇̈́̐̎͆̿̿̑́̂͂̇͋͗̐̂͒͋͊̾͛͑̏́͛̄̀̅͊̚͘ͅ ̵̨̡̡̟͇̪͎̜͍̜͇͚͚̲̮̹̎̏̈́̎̄̀̈́̀̿̿̅̔̌̀̀̇̍͘͘͜ͅͅ(̵̨̨̢͖̤̠̬̝͉̤̘̼͕̯̠̟͕̦̗̭̲̥̬̠̗̼̖͙̹͍̻̜̬̞̮̞̺̯͓̝̭̖̯̳̰̠̤͑́͜ͅͅ9̴̧̢̨̩̮̲͉͙̯̬͉̱̣͎̟̞̬̰̻̘̳̱̬̰̝̠͚̜̗͓̩̫͙͍̲̙̤̩̟̂̌̈́͜)̵̢̢̧̛̩̣̪̪̭̜̬̪̣̖̻̥͕̫͎̼̖̪̻̖͓̘͖̭̪̘̬̎̇̾̂͑̽̄̓̌͌̏͐̒̔͑̀̏́͒̔̂̆̊͗͒̉͗̅͂̓̚̕̚͜͠͝ͅͅͅͅ ̴̨̡̨͚̱̦̘̣͍̫̲͚̭̪̟͈̞̲̩̞̞̟̬͖͚̼̖̠̮͕̙͓̱̺̖͈̪͇̜͓͇̣͇̻̙̒̓̉̂͛̔̀̅̋̒̄́̕͘͝B̴̡̤̻̥̭͍͍͚̝͍̹͕͙̺̭̣̪͉̮͇̯̠̣̗̌̾̒̐̈́͐͒́͒̒̋̋̊̇̒͋́͊͊͊̄̆͝͝͝͝͝ơ̷̝̟͖̹͊͛̑̅́̓͆̿͗́̔̋͊̅͌̐̆͛̓̅̄̈́̇͆̅͋̌̃̓̉͑̑͘̚̚͘͘͝͠͠͝͝ổ̷̪͓̱̘̹̝̤̙̗͔̝̏̓͐̓͐͊̀͂́̈́̒́̄̿̍̋̽͒̌̇̄̇͆̈͛̿̈̌̇̀̉̈̈́̾̕̕̕̕͠͝k̴̡̧̨̨͍̙̥̼͇̞̰͖̖̦̙̰̖͎̩̻̺͓̞͔̥̠̼͈͈̥̙̝̰͎̰͓̰͔̊̓̿̈́̂̑̚͜͜ͅ ̶̧̨̧̨̼̹̲͔̭͕̗̟̠̰̩̯̬̪͓̥̫̺̬̼̺̜̤̹̹̱̭͉̻͕̩̖͙̬̺̰̳̻̲̫̯̓̍̎͛́͌͗͋́͂́̓̀̐͠͠ͅǫ̸̧̛̛̣͚͎̥͔̣̥̘̱̲͛͂́̔͂̏̔͐̆̑̍̈̄̅͗̋̂̆͛̾͊̂̈́̈́̓̔̓̂͐̄͆̂̌̆̈́̇̅̕̕̚͘̚͘̕͘͝͝f̵̛̛̛͚̋̅̏̇̒͐̎̈̈́͊̌͗̇̀̐̾̚̚̚͘͝ ̴̨̰̰͍͙̮̜͚̲͋̈̊̀̈̊̌̈͊̍̓̎͛̑́̃͒̈́̈͌̆́̓̓̈́͒̓̔͐̾͆̍̓̐̊́̄̔̍̇͌̎͑̀͋̕̕͜͝͝͝Ķ̷̢̨̡̨̹̺͙͙͚̙̜͎͇̰̺̜̯͖̠̘͈̠̝̖̮̪̭̞̱̙̯͔͖̖̯̪̬͓̹͖̗̠̰̜̅͛́̀̃́͗̇̿̑͐̈́͋̈͛͊́̄̃̈́̓́̄̍̕̕͘̕͜͠͝͝͠͠͝n̵̢̨̢̨̡̡̛̰͍̝͇̻̘͚͈̻̩̦̰̣͍̠͎͓̺̞̩̝̫̘̱̳̮͎̗̄̾̍́͌̓̉̀́̐̔̅̿͛͑̌̅̑̈́̏̈̓̐̕̕͝͝ͅͅő̷̢̡̤̔̑̈̒̋̆̎͑͛̂̍̂̒̉̏̍͋́͘͘͘͠͝͠͠͝͝w̶̛̛͐̓̈́̐̒̔̓͐̉̉̅͌̅̿́͒̀̋͆̽̊̉͌̊̍̈̎̔̒̊̊̅̇̇̎̕͘̕͝͝ͅļ̴̟̞͍̬̙̰̦̖̰̥̬̮̙̱̹̤̮̥̦̟̤̻̖̼͖̳̼͖̠̺͖̗͉̐̄̈́̒͗͊͂̄̆̅̏͆̎̏̀̀̾̀̓͜͝͠ȩ̶̧̧̛̥̥̙̦̝̖̫̟̠̟̺͚̮̻̻̪͇̗̬̘̥̼̪̪̱͎͇̦̔̒͌̄́̓̆͌̏͒̎̃͐̊͂́̉̃̕͝͝ͅd̷̨̨̨̡̘̼̞͉̳͔͙͎̙̜̖̣̪̰̺̳͉̜̮̳̞̮̙̫̥͍̪̥͍̩͕̯̩̪̗̱̽̈͋͐̔͂̌̄̈́̒̽̄͛͋̽͛̇ͅͅg̵̢̡̧̧̹̯͕̙̪͖̩͚̟̘̬̙̻̰͇̰̳̺̝̻͕̮̞̈́͐̓̄̂͊̽̊͊̊͒̍̈́̽͗͘͘̕͜͝e̵̛̛̻̮̹͇̰̺͚͕͈͓͐̀̄͊͛̿̅͆̄̀͐̓͐̽͗̂̃͗͆̾̓́͆͌́̅̄͘͘̚͜͜͝
        ̷̛̘̭̺̳͙̩̅͆̅̔̄̓̌̍̔̒̈́̋̎̈́̈́̚͝͝ͅ ̷̢͙͕̭̝̤̝̺̗͉̼͈͍̩̝̯̲̠̻̤͕̻̦̖̫̻̬͓̬͉̈͒̃͐͑̔̍̏̈́̃͊̆̈͋́͑̀̀̃͘ ̸̨̧̧̛̭̞͉̼̟̪̦̲̼̥͕̘͉̳͍̝̙̱̘̫̗̤͖̦̦͚̞͙͇̝̭͉̘̃͑͗̓̈͂̓͋̔̊̑̈́̅̃̀̀̈́̈́͐̔͒̇͑͐́̅̊͘͝͝ͅͅ ̷̢̛̮̯̳͙͙̖͍̦͙̹̥̗͉̳̬̤̜̣͕́͛̽̆̋͂͊͊̃̉͐̍̌́͊͌̈̋͌̀̆́͊̈́̑̓̆̆͝͝ ̶̧̛̮͓̘̝̰̗͇͔̻̲̮̪͚̮̘͔̫̙͈͖͇̙̱̖̇̈́̇͊̉͗̒̽͋͘͘ ̵̨̛̟̲̣͕̬̞͇̝͈̫̼̮̳̹̭̼͖̣̩̪̙̫̻̭̥͓̘͇̱͓̋̓̏͆̈̅̏̐͗͗̊̀̃̐̏̎̀͗͌͋͋͂̍̈́̾͂͆̃̽͐̿͒̌̈́̊̌͊͋̈́͘̚̕͘͠͠͝ ̶̧̢̢̧̛̛̤̰͇͙͇͔̣̤͕̱̭̱̬̠͕̯͎̝͚̩̣͇̦̪̗͕̹͉̹̟͚̪̘̤͎͌̆͑͋̈́͛̐̇͋̉͛͋͋̄͑͒̋̾̈̉̆̀̑͐̾̀͗́̀̇̇̋͘̕̚̚͜͝͝͠ͅ ̸̪̪̲̜̭͇̦͚̼̳̙̣̥̼̳̱̹̣̬̲̊̀͌͑̐̈́͗̈́̒̏͆̍̑̚͘̕͜͠͠͠ ̸̧̧̧̨̧̡̟͚̼̟͍̫̜̱̖͔͈͖̮̜̟̜̥̝͉̺̘͚̠͖̙̞̼̗͙̳̼͔̠̜̭̙̤̩̖̦͊̌̊̍̓̽͋̀̀̒̊̓̈̐̏́̿̂̏̆̃͗̆̓͜͝ͅͅ ̵̗̹̟̦̠̬͈̺̦̝͖̯͓̎̐̀͌̊̓͆͛̅̀̎̀̏͗͊̇̎̚͝ ̸̧̢̛͙̝̮̰̣̠̖͔͙̳̞̣̩̖͕̞̯͇͍̥̯̲͇̰͕̘͙̲̞̔̐̆̾̿͊͌́̀̌̊ ̷̛̛̬̱̍̓̽̆̿͑̃̃̐̌̅̃͊̒̒̄͋́͐̑̐̚͠͝ ̵̡̢̢̢̰̥̤̙̠̰̖̻̞͚̮͓̪̰͎͎̞͍͚͕͖̞̪͕̦͍̘͈͎͙̯̗͕̟̬̘̩̬̄̾͐̄̋̽̊̈́̆̏̄̏̋̓̀͂́̀̆͌̓̽̎̊̂̿̈̌̓̈́̆͗͘͘͜͠͠ͅͅ(̶̦͓̠̯̹͇̝̱͑̒̇̎͂̇̀̓̋͜͜͝1̴̨̛̪̱͍̠͇͈͚̬̖̘̻̤̻͎̠̘̱̗͍̘͎͆̈́̽͌͗̕0̷͕̎̅̏̽̈́͐̀̂́̏͛̏̏̑̔̎̍̋͒͒͘͠͠͝͝)̷̨̛̛̬͕͖̹͉̝̥̐̄̋̉̃͑͊͐̉͠ ̶̡͖̙̈́͒͂̔̏̏Ţ̸̡̢̡̡̺̞͓̬̮͇̳̳͚̥͍͓̗̝̩̙͈̖̺̣̠͖͉̻̼̞̖̮̲̹̜̭̗̮̦͎̹̩̰͕̰͍̰̊̂̅́̑̀̓̊͌̏͑̇̽͗̈͊̊̅͒̑̒̓r̶̡͓̻͍̝̩̰̦̝̲͖̲̖̖͖͎͇̠͔̼̜̬̥͍̙̣̟̜̱̳̥̲͍̗̀́̌̿͒͋̆͘ͅa̵̡̨̢̛̮̯̤͔̟̝͉͈̯̟̱͍̮̣̤̪̲̠̘̺̰̪̤̻̙͔̖̬͔̼̗̹͗̄̄̅̔̍̓̐̓́̀͂̾̈́͐̍̀̌̇̐̔̌͛̍̒̓͂͆͠͝ͅͅͅͅd̵̛̛̛̝̘̠̞͂̔̀͛́̿̌̃̌̎̏̈̑̋̐́̿͒̃͛̍̏̆̐́̔̐̈́̇̐̀̋̆͘̚͠ë̴͕̝̤̹̯̞̙́̈̊͊̈̓̽̅̓̈́͗̈́̍͜ ̵̢̢̛̹͈̻̩̩̪͉̹̣̦̫͚̮̙͙̜͚̭̑̄̒̓̈̅̀̀͋̅̈̇̅͜ͅw̵̨̹̺̪̜͚̯̟͕̗̗̙̘̣̩͍̣̯̬͐́̊̈́̅̂̊͂͛͋̈́͐͒̎̎̑̊̀̃̀́͒͗̍͝ͅͅí̷͔̳͕̮̝͕͓̥͎͜ť̸̨̢̨̧̨̢͍͎̣͔̬̹͎̥̭̯̠̳̘͙̬̱͎̤͙̮͔̺͔̹̭͈̮̦̲͓̮͙̭͚̪͖͈̮̖͉͊͆̌̋͑̊̈́͘͜͜ḩ̵̡̨̰̯̣͙̤̙̪̮̜̺̯̟̝̺̟̮̦̼̪̖̭͕͇̗̦͕̗̗͔͊̀̃̇͑̀̕̕͜͝ͅ ̷̨̡̡̨̨̞̯̖͎̪̭̥̟̠̟̩͉͓̠͕͚̹͖̘̠͙̪̰͇̳̗̦͕̭̘̹̲̥͕̯͕̘̝̺͙̺͛̽̉͛̆̅͐̂̈͋̔̆̄͋̂̈̏͒̽̑̄̓̒͊̊̉̋̆̌͜͠͝͠ǫ̴̡̢̢̡̢̗͙̖̥͓̘̗̹̠̥̣̹̟̟͙̖̳͎͙̱͙̤̘͍̻͙̟̺̯͙̮̰͙̳̑́̃̅͐͐̂̏̊̎̒͒̄̀̇̔͌͋̎̇̚͜͜͠͠͠͠ͅͅẗ̸̢̡̡̢̢̢̛̛̘̗̟̳̦̤͙̤͍̺͖̲̫̟͈̟͍̮̰̠̱̯̮̞̗͇̩͕̣̝̠͎̻͍́͗̂̀́͗̀͐͜͜h̸̡͇͇̦̫̬̫̹̦̰͙̼̫̺̝̱̼͕̱̪͇͎͉̝͎̹͎̞̖̤̙̟̆̋̉̍̊̊̈̽̈́̅̎̃̓̀̅̐̑̾̆̃͗͋̂̍̀͐͘͜͠ͅę̵̡̧̡̠̥͓̟̹̖͎̺̤̤̰͕̦̗̘̦̫̫̗͓̖͉̗̥̼̬̻̙̰̮̙̩̞̦͖͓͓͖̰̭̫̅͒̈͆̇̌̉͑͠ͅͅr̴̨̢̢̧̯̖̹̝͇͍̝̪̩͙̜̠͉̣̤̣̟̝͚̫̜͕̲̥͉̩͍̠͊̓̉̋̄̈̄͑̓̎̆̈́͌̈̎̐̈́̈̈́̑̽̌͑̀͘̕͘͜͝͝͝ ̵͍̳̣̪̼̳͈̤̦͍͉̹̲͇̟̝͓̉͊͊̏͌͊͑͋̈́̋̓͛̀̀̓̒͒̂̊̏̃͠k̴̨̛̪̤̜͔̳̹̜̤̘͌̇̎̏̃̐͌͐̐̊́͐͋̀̓͋̐͛͘ĩ̶̧̡̛̛̛̥̱͍̳̺̫̦̤͚̹̜̖͇̝͇̯͓͕̩̩̲͓̬͕̣͓̥̦̞̬̻̥̟̋͌͊̓̎̆́̏͑̀̉͐͋̈́̿̎̋̆̄̔̐̇͒̀̂̔̿͂̎́̈́̀̾̑̕͘͝ͅͅͅͅn̶̨̛̝͚̫͇̜̼̝̘̻̣͐͋͑͜͠͝͠g̴̥̪͎͓̫͉̹̱̻̯̟͓̰̩̼͓͆̾̒̈́͗͂̀͊̇̎̒͂̐͛̆͠͠d̷̞͔̾̀͌͌̓͗̒̅̎̇́̒̈́̈́̃̃̇̓̓͛͛͛̓͘͠͝͝ơ̵̤̮̫͈̞̳̺̙̬̠͒͗m̵̨̡̧̨̡̼̱̬̪̱̮̩̝̠̙͍̝̲̗̣̤̳̪̬̝̱͖̝̲̭͙̹̝̻̤̲͇̣̜͓̥̘̟͇̤̈́̒̐̂̅̓͂̔̆͛͜͜͠ͅͅs̵̡̡̡̧̛̳̲͓̞͓̟̫̻̟͚͙͍̫̠̗̭͚̪͛̃̈̅͌̅̉̿̃̃͑͋̔̇̀̏̕ͅͅ
        ̶̡̛̦̞̟͍̲̩̫͕̿͒̇̑̑͐́̃̅̐̓̑͗̌̕̕͠ ̷̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝̋̈́́͂̐̇̊̑͋͒͑͐̾̈̑́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄͘̕̚̕̚̕͜͜͜͜ͅͅ ̷̨̛̛̛̝̥̩̫̜̰̘͓̠̖̼̯̊̉̐͂̊̅̌̈́̇̈́͐̈́͛͂̂̌̀̅̄̋̀̉͆̎̽̀̑̎̌̌̚̕̚͠͝͝ ̶̻̬̺̞̫͚̲̙̠̬͓̬̰̫̜̦̗͖̦͔̥͔̺̒̈́̽̈́̈́̌̂̇̐̀̀̂̀͒͋̅̈́ͅ ̷̡̧̣̖̝͚͈̣͚̫̮̱̼̳̫͖͚̖̼̤̟̟̱͉̤̹̖͈͍̻̩̥̮̈̊͑́̀̒̽́́͗̈́̈́͑̒̈́̅͒̎̇̈̍̎̈̓͗̈́͗̀͆̽̈́̕̚͘̚̕͠͝͠ͅ ̵̨̡̛͈͓̱̪̣̠̖̼͍̮̻̯̫̟̠͕̻̗̳̤̠̎̌̌̑̿̿̈̇̆͊͒̓͛͗̉͋̽́͑̀̒̃̎̔̂̇̊̂̿͗̾͗̑̿̍̔͛͗̓͠͝͠ ̸̢̨̡̢̛̰͎̖͇̦͎̩̲̹̼͚̳̞̣̝͙͖̱͎͎͇̜̟͈̣͖̰̺̼͉̬̘̜̭̖̗̤̲̔̀̈̋̂͆̊̐̓̊̓͛́̍̀͗̂́̒̅̃͒̽̀́͒͋̽̏̕̚͝͝͝ͅͅͅ ̷̩̜̤̥̼͖̎̏̆͒̃̀̈̾̈́͐͌̔̂̽̑̃͊̄̃͛̓̏͛̕͘͠͝͠ͅ ̸̢̲͉̻̪̞̲͓̤͓̻̤̬̮̫̞͔̰̰̞̗͖̣̙͙̙͚͇̭̪͉͔̳͙̠̭̭͔̠͕̤̟̩̱̱̪͚̗̓̿̌̈͑͌̔̒̾͋̈́̽̿͐̄͗͑̑́̐͌̆̽̈́̍̀̿̚͜͠͝͠͝ ̵̨̡̛̛̣̮̮͓̣̼͚̹͙̙̰̪͎̈́͂͋̾̀́̃̀̏͑͆̈́̏̎̇̿̿̄̀̈͂̿̀̏̏̈́̎̒͆̑̏͂̈͐̕͘̕͘̚͝͝͝ͅ ̶̨̡̡̛̛̹̬̗͍̜͈̫̙̬͉̪̯̦̜̲̞̱̬̖̫̳̜̙̜̯̈́̇̑͂̉̋͋̅͛̂͗̀̈͒̋̕͝͝ ̴̢̢̺̠̣̠̪̯͕̱̰͚̗̰̮̖͖̝̖͓͇͕̼̥̗̬͉̗̦̝͎͍̺̯͍̥̪̥͙̫̦̰̩̝̫͒͆͋̈̄́̋̾͗̽̍͊̈́͊͋̄͂͑̆̆̀̓͘̚͘͘͜͝͠͝ ̴̧̞̩͎̻̫̖̹̹̝̬͈̠̬͇̥̜̠̍̀̅̆͑͘͜(̶̢̲̦̙̘͉̳̺̪͎̤̲̟̮͍͇̫̼̺̗̫͚͚̩̺̲͖͓̹̪̲͓̃̋̓̓͂́̈́̑̾́̆͒̍̐̔͊̓̔͂̉̏̚͜ͅE̵̢̧͎̰̙͕̬̮̼͚̟̝͓̟͉̳̳͓͚̥̝̣̤̲̦͙͍̻̜͒͜͠ͅͅͅļ̶̛͉̙͚͇͙̬͕͙͈̩̹͙̬̀͐͆͆̈́̄͌̔̌͌͆͛̎̑͑̓͆̈͛́̈́̏̽̀͛́̃̐͐̓̽͊̓̚̕͠͝s̵̡̨̡̮̙̦̩̩͚̗̩̻̳̻̫̦̫̺̠͙̮̓́͂́̂̄̀̋͆́͐͋͠ͅͅe̶̡̧̡̠͔̳̮̬̖̝̗͍̳̹̝̗͙̯̻̘̗̪̱̳̲͉̻̫̟̣͇͓͉͍͗̇̊̉̃̆͂͆̈́͂͝)̸̛̛̛̛̮̼͓̣̪̻̲̤͚̳̲̥̳̱͎̩͙̋͑̈́̅̀͌̍͌̒͊̔̾̅͆̓̇͐̐̈́́̆͌̑̈́̐̾͜͝ ̶̡̧̧͙̣͇̲̳͈̠̣̼̟͙͙͇̺̜͒̏̍̄̂̆͛̎̂̀̓̎̈́͐̀́̐̋̀̈́́͒̒̂̅̀́̇̌̑͋̒̄͊͐̈̂̕̕̕͘̚͜͠͝͝͝ͅͅḐ̸̨̡̘̳̼̥͈̲͎̩̪̤̺͙̰̙͉̼͙͖̀̒̂͐̕͜͠͝o̷̻̦̬̺͌̀̊̉̄̈̎̉̑͌͑͋̂̐̈́̽̔̈́͛̏͋̆̊͘͘͝ ̴̢̨̛̲͙̞̬̪͍̰͖̭̺͙̫̺̯̟̙̤͍̜̹̲̙́̒̐̓͛̍̃̈́͊͊̂́̍̎́̇̄͗̓͊̒̍͗̔̔̽͒̔̀̓͒̽͌̌̉͋͗̚̚͝͝͠ͅͅń̴̨̡͔̟̩͙̘̞̱̬͈̜͕̘̫̦̼̼̪̭͍̜̦͔̞͓̯͔̣̹̼̜̫͈͙͍͉̭̿̉̑̑͐̀͗̔̎̅̑̃͊́̈̇̔̓̌̓̓̔̿̕̚ͅò̴̢̢̨̗̦͇͓̳̖̥̻̫̥̪̼̪̘̣͎̘̗͈͖̬̮̮̟͍̺̍͛́̔̄̍̽̏̀̽͂̈́́͐̉͋͑̂͑͗͋̕̕͝ͅt̷̛̹̮̝̠̜̪̞̲̜͖͍̮͉̜̜̞̦͉͙͇̗͎̠̞͇͖͉͓́͋̿̅͋̀̊͛̈͆̈́̉̈́͌̄̓͐̄̈͆̿̄͋̔̐̀͑̈̍͘͜͝͝ḩ̵̣̘͉̺̬̞̩̤̺̞͚̟̼̟̮͚̦̽̃͗̌͑̄͂̄̒̉̿̅̅̂̌͜͜͝͝ͅi̷̡̢̡̧̨̗̟̜͕͓̬̯̼̱͕̖̖͎̞̳̙͚̝̙͛̉̌͆́ņ̸̛̱̦͚͔̮͕͓̣͕̦̤͕͓̣̙̬̜̍̑̓̌̀̋̎͋͋̃̄̂̂͌̔͗̅̎̋̚͝͝g̴̡̨̭̬̟̜̦̞̥͇̐̃̀̈́̄̎̇̃̉̐̑͗͊̑̓́̚͝͝͠͝ͅ
        ̷̢̧͖̦̼̼͈̟̩͕̳̣̪̳̬͚̬̺̰̰̹̲̺͚̭̤͔͚̣̭̳̭̻͖̻͚͔̺̝̫̼͎͔̺̂̀̇͊͂͊͊̃̂ͅͅ""")
            Action = input(">")
            if Action == "1":
                print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                buildchoice()
            elif Action == "2":
                print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                buy()
            elif Action == "3":
                print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                invade()
            elif Action == "4":
                print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                stats()
            elif Action == "5":
                print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                Hire()
            elif Action == "6":
                print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                settings()
            elif Action == "7":
                print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                upgradetroops()
            elif Action == "8":
                print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                peace()
            elif Action == "9":
                print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                help()
            elif Action == "10":
                print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                negotation()
    else:
        for i in range(timeskipvalue["TimeSkipValue"]):
            people()
            Tax()
            invaded()
            negativemoney()
            MerchSale()
            KNIGHT_FROM_HELL()
            HellInvasion()
            Days["Days"] += timespeed["speed"]
            BlackKnightEvent()

            if LOVE["LOVE"] == 1:
                print("You feel a little good...")
            if LOVE["LOVE"] == 5:
                print("Your feeling better...")
            if LOVE["LOVE"] == 7:
                print("You feel amazing...")
            if LOVE["LOVE"] == 10:
                print("You whisper in your dreams, Death... what an amazing word")
            if LOVE["LOVE"] == 11:
                print("You whisper in your dreams, Death... what an amazing word")
            if LOVE["LOVE"] > 12:
                if LOVE["LOVE"] < 14:
                    print("You've entered a state of megalomania... YOU WANT MORE POWER")
                else:
                    print("Let all die... let all who dream, see there death.")
            if LOVE["LOVE"] == 10:
                if cutscene == True:
                    cutscene = False
                    print("Crescit potestas mea...")
                    time.sleep(5)
                    print("I WANT TO SEE THE END!!!")

            if The_Devil["HATE"] <= 9999:
                print("What will you do?")
                print(f"""
                                            (1) Build
                                            (2) Buy
                                            (3) Invade (Military strength: {Kingdom_Inhabitants["Power"]})
                                            (4) Check Kingdom Stats
                                            (5) Hire
                                            (6) Settings
                                            (7) Upgrade Infantry Power
                                            (8) Peace Treaty
                                            (9) Book of Knowledge
                                            (10) Trade with other kingdoms
                                            (11) Do nothing for multiple turns
                                            (Else) Do nothing
                                            """)
                if HELL["HELL"] == True:
                    print("""
                                                (12) Destroy this world.""")
                Action = "Nothing"
                if Action == "1":
                    buildchoice()
                elif Action == "2":
                    buy()
                elif Action == "3":
                    invade()
                elif Action == "4":
                    stats()
                elif Action == "5":
                    Hire()
                elif Action == "6":
                    settings()
                elif Action == "7":
                    upgradetroops()
                elif Action == "8":
                    peace()
                elif Action == "9":
                    help()
                elif Action == "10":
                    negotation()
                elif Action == "11":
                    try:
                        timeskipvalue["TimeSkipValue"] = int(input("""
                                                How much turns do you want to skip ahead to?
                                                >"""))
                        timeskipvalue["TimeSkip"] = True
                    except ValueError:
                        print("That is not a number.")



                elif Action == "12":
                    if HELL["HELL"] == True:
                        print("Good...")
                        time.sleep(5)
                        Game = False
                        for i in range(100000):
                            print("""

                                                    """)
                        time.sleep(5)
                        print("Love, Hopes, and Dreams")
                        time.sleep(2)
                        print("Are all not reality")
                        time.sleep(3)
                        print("See all those die...")
                        time.sleep(2)
                        print("Let them scream...")
                        time.sleep(2)
                        print("See them run...")
                        time.sleep(2)
                        print("See the children cry...")
                        time.sleep(2)
                        print("See the mothers die...")
                        time.sleep(2)
                        print("See them run...")
                        time.sleep(2)
                        print("Let them scream...")
                        time.sleep(2)
                        print("They all die...")
                        time.sleep(2)
                        print("Let their tears fill the sky...")
                        time.sleep(2)
                        print("Their blood brings more love to our lives...")
                        time.sleep(2)
                        print("Hear them scream, hear them die...")
                        time.sleep(3)
                        print(f"Don't you like this? Lucius. We saved them. We made them happy :)")
                        time.sleep(5)
                        trigger_genocide_deletion()
            else:
                print("""

                                ̷̨͉̼͇̗̤͔̝̭̙̯͘ͅ ̴̡̡̧̧̛̛͉̜͈̟͍̪͔̖̱̫̦͇͉̯̬͙̥͉̘͓͓͔͎͈̹͕̮͖̎̎̌͊́͒̾̅͊̾͒͌̍̅̍͒̔̈́̏̈̎͑̉̕̚͘͝ͅ ̸͙͚͍̜͈̩̪̥̣̤̰͉͎̠̖̩̘̥̗͎̯̖͖̗͉̤̓͂̅̋͆̏̏̓̈́̏͜͠͠ͅ ̴̨̢͙͔̮̞͈͙̙̳̞̫͙̯͉͕͙͉̠͈̬̖̯͔͓̱͓͚͇͚̀͒͌̾͋̍̕͜ ̶̢̧̡̧̖̼̱̣̝͔̰͉͖̟͇͈̺͙̙̫̮̮̘͍̫͉͉̫̜͚̬̬̘͔̞̬̞̱̘̩̏̂̋̈̅̆̃̓̽͂̔̐̄̌̃͑͒̓̓̈́͘̕͝ͅͅ ̸̨̨̧̛̦̠͎̯͎͓͚̺̝̖̱̰͇͔̦̬̪̲̫̫̺̫͔͍͔͓̗̻̳̟͙̳̯͉͓̓̀̓͂̈́̐͊͛̉͊̓͗̎̈́͐̈́̔̓͑̿̀̒̐͊̄̑̅̂̀͊̌̚̕͠ͅͅ ̷̡̡̢̧̨̧̡̯̳̘͇̠̮̻̹̮̼̺̼̭̗̪͍̹̜͖͈͎̮̳̦͔̖̫͍̟͇̗̬̙̘̥̻͇͔̣͎̭̬͗̄̂̃͐̅͛̐̾̎͆̂̉̊̇̒̔̀͐̑̄̑́̈̈́̈́̎̔̐͐̿̂͝͝͝ͅ ̴̩̙̪̪̯̪̘͍̫̝͙̖̻͈͈̲͕̘̼̿̅̆́̃͒̌̉̈́̾̆̐̋̊̀̐̔̋̀̓͐̈́̽͐̀̇̐̌͑͘̚͠͠͝ͅͅ ̴̢̦͔̙͍̺̤̖͕̬̮̭͉̝̠͈͖̩̰̺̗̲̲͚̩̫̳̅̍͑͒̃͊̀̈́͆̒́͌̌̑͋̈͂̋̇̆̒̿̓̓̉̑̈͂͐̉̏̏̆̾̅̽̾̚̕̕͘͜͠ͅͅ ̴̡̛̰̙̇̍͛͋͂͗́̈̊͊̇́͘̚̚͘ͅ ̵̡̧̡̡̧̩̘͉̣͈͚͍͇̝̥̹̣̭͍̙̥̳̭̫̻̪͇̝̱̞̠͚̖̜͙̹̮͕̞̦̯̭̈̅̆͆͌̈́͐̄̀̉̇̍͛̇̉͑̎̈͊͘͘͜͜͜͝͝͝ͅ ̴̢̜͔͍͚̰̱̘̻̺̹͕̟͇̰͔̝̥͓̫̩̤̲̻̲̮̮̺͍̝̻̜̰̐̈́̉̃́̈́̓̌̈́͛̅͒̓͘͜ ̷̢̧̛̠̪̳̔̓̅̐͂́̆̓̓̅͑̾̃̅̀͋̒̍͐͗́͋̔̍̈́̊̿͛̿̅̕͘̚͘͝͝͝͝(̷̢̢̡̛̠̗̟͔͖̳̦͖̭͔͚̖̣̦̼̼̳̲͉̦̦̙̝͔͈̗̼̯̙̣̱̈́̿̀̽̐̆̓̈́́͋̄͗́͑́̐̈̉͂̚̚͘͜͝͠͝1̴̨̧̛͈̮͈̘̳̥̗͉̠̭͔̙̹́̅̀͛́̀̿̓͊̈́̈́̍̈́̉̏̅́͋͆̒͆̀̿̊͋̌̄̒̈͆̉̓̃̌̂̇̇͑͂̓̑̎͘̚̕͠͠͝)̸̻̗̲̱̱͖̣̣̰̝͈͙͙̟̤͌̅̇̎͋̎̌͋̉̏̈̐͒̋̈́̈́͜͠ ̷̧̨̡̧̢̼̝̟̪̖̤̞̩͇̣̞͕̳̰̝͓̬͔̗̣͓̺͎͕̬̂̈̆̑͋̄̈́̑͊̓͐̀͂̈́͋̇̒̋̄͑̈͂̀͑̿̋̎̂̈́̽̒̂́́̀̋̀́͘̚̕͜ͅͅB̸̢̧̨̨̧̨̛͔̻͈͕̤̳̻̼̤̝̬͓̱̬͍̹̬̫̖͈̭̗̰̦̬̦̩͙̮̱̯̼̪͍̤͍͖̻̩̩͔̟̒̆̃͊̅͑͒͐͆̇̅̊̀̋̾̾̄͊̀́͑͋͒̿̿́̈́̎͘͘͘͝ư̶̡̡̧̛͚̥͉͉̠̦̼̙̩͇̬͇̘̫̖̘̯͙͔͔̱̪̘̜̔́̄̌̃̽͊́̾͗̍̊̌́̓͒͗̒̆̌̽̂̽̓̽̽͐̾͗͐̉̅̆̈́̈͒̂̕͘̚͘̕̚͠i̶̛̛̝̝͖̝͖͚̯̯̝̰͔̮̝͓͈̭̬̥̰̭͔͙͙̮̓̈͗̔̀̏̍̍̅̎̾̈́̿̑͋̀̒͗̐̀̄̔̂̿̓̕͜͜͠l̶̨̡̡͚̮͍̯̥̪̣̩̳̰͓̄̄̅̆̒̀̍̈́̅d̴̨̙̙̮̟̭͈̟̥̼̭͎͑̀̀͛̀̈̄́̎̿̂̾̈́̌̓̕̚͘͜͜͠
                                ̴̛̖̮̺̏̐̇͑̊͗̀̂́́̑͊̀̽̿̌͆̇͆̈̐̅̍̂͌́̔̑̏̍̍͗̃̅̇͐̇̑͒̍́̾͊͐͘͘͝͝͝ͅ ̴̡̹͙͈͍̯̘̹̭̝̤̖̹̫͇̬̪̰̖̣̀̓̈́̃͂̀̋̈͐̓́̎̃̃̈́̆̀̾̎͗͜ ̴̛̭͂͐̇̐̍͊́͗͂͒̾͒̒̎̎̀̆̊̓͗͌̂̓̿̾͌̽̄̄̈́̒̉̐͘̚̕͝ ̴̡̢̖̞̯͔̟̳̳͓͖̤̼̦̻̩͚̳̠̝͉̘͚̳͎͍̉͋̈́͐͑͆̆̿̇͂͛́̈̌̀͗͌͆̏̈́̈́́͆̎͆̍͐̿͒̈̀̍̌̄̕̕̕͘͘͝ ̷̡̧̞̬̲̲͇̻̻̤̼̩͓̯̱͍͎̤̟͎̪̬̣̀̏̄͌̓̈́̈̔͆̀̎̂̉̃̋͋͘̚͘͘͠͝͝ͅͅ ̸̢̧̨̨̨̢͕̭̭̺͔̩̮̝̞̳͓͔͙̳̼͙͕͖̳͙̎͗͑͐͗̀̈̐̕͠͝ ̷̧̡̡̛̤͓͚͍̰̩̳̬̪̠̺̥̥̮̥͖̹̞͍̫͙̪̯̦͍̪̹̠̹́̎͛̽̍͐͐͐͐̊̌̏̇̈́̿͂͑̍̏͋͌̓͊́̌̐̊̓̃̎̉̈́͘͜ͅͅ ̸̧̧̮̺̳͓̟̟̳͖̳̝̞̋̏͋̍̂̎̿͐͐͊̀̽̈́̐̄͛̈́͊͋͋̓̄͛̆͑̀͊͑̀̉̾̓͊̚̕͜͝͝͝ ̴̢̧̛̲̞͎̳̹̹̝̻͈̟̲͉̖̫̜͉̖̖̺͎͉̝̖̝͖̠̝̥͇̺͍͎̘̝̟͇̰͊̔̑̑̍͒̓̄̍͗̎͋̍̇̂́́̒͌͊͒̆͛̀̆́̒̋͂̈́͌͊͌͆͑̓͋̚̕͘̚̕̚̚͜͠͝͝ ̶̢͇͖̩̼̱̠͚̘̪̠̞͙̱̳̼͙̻̩̲͕̖̱̔̓̋̉̔͑̂̋̐͗͊̓̈́͗̉̎̊͂̈́̐̓̈́̏͂̆̉̎́̕̕͠͠͝͠ ̵̡̢̢̨̨̨̧̨͉̲̫̫̠̪̫̯̻̱̫̹͖͙̮̰̳̫͙͕̝͕͎̪̖̩͎͈̗͔̮̳̮͇̟͓͛͑͒̾̿̇̆̔̌̀̕͜͜͜͝͝͝͠ ̶̨̢̧̛̘̯̰̱͕͔̩̠̱̳̟̹̼̩͕͔͈̦̣̗͈͔̮̱̯͓͎̯͖̄̈́̿̅͛̇̑̉͐́̈̅̓͊͜͠͠͝͝ͅͅ ̶͎̀͗͆̀̅̓̆́̇̆͌̒̀͒̀͋̈́͛̈́́̎̑̀̀͑̐̈́̾̈͒̅͂͌̎̉̋̿̚̚̚͘͘͝͠͠͝(̴̲̜̭̽̑̋́̈͆͛͗͂̔̄͑̀̅͌̎͘͠͝2̸̨̻̮͇͚̬͎̄͒ͅ)̵̨̨̧̡̮̯̺̮̹̹̰̞̝̜̰̭̝̙̠̤̳̠͇̱̪͉̭̹̭̖̖̯͓͎̞̮̬̝̣͎̻̲̺̩̻̲͇̺̐́̓̉͋́̉͗̾̾̄̔͂̓̈́͛́́͛̃͒̃̔̈́̈́̿̃̅̋̂̂̆́̎̇͑̚̕̚̕͜͠͠͝͠ͅ ̴̢̨̰͖̜̬͈̭̣̗̬̝̜̗̺̻̝͇̹̳͓̜̦͕͉͎͎̟̻͉͔̙͈̬̫̜̜̑͜ͅͅB̵̡̧̢̧̳̮͓͔͔͓̘̣̞̻͕̟̞̜̬̳̖̯̭̰̤͙̃̎̀̈́͋́̔́͋̈̎́̃͗̈̇́̐̄̔̎͒̉͌̿̎̚̚̕͜͠ͅͅu̸̡̧̘̭̺̙̖̬̜̬̘̰̝̲͉̙͉̥̦̘͆̏̾̈́̃̂̀̀͒̽̓̓͊̍̽͑̄̚̕͘͜͠͝ͅy̸̡̨̧͙̪̭̟͔͖̙̖̠͍̩̲̮͔̟̮̼̥͕̳̙̣̳͈̝͙̫̹̣͕̹͔̩̭̥̰͚̞̼̮̹͓͔̳̦͗̊̀̎̐̋̄͗̿͊͐͜͜͝
                                ̶̨̢̧̛͖͈̮̰͕͖̜̞̪̯͔̟̮́̈́̓͛͊̇̐̋͗̉͂͗̍̇̈́̾̀̊̎̇͋̄̈́̉̚͜͝͝ ̷̨̡̧̡̨̡̮̝͕̩͍͙̭̤̪̘͇̤̠͍̖̩̯̟͉̣̜̱͈͓̳͚͍͈̺͗͗̋̍́̈́͑̈́̑̉͆͆́͐́̄͆̀͛̋̑̎̾̂͊̚̚̚̕͝ͅ ̸̡̨̢̡͉̜̝̖̙̱̤̞͔͙̦̗͖̖̦̣̣̜̗̣͓̻̖̗̪͓̳̻̮̘̾̇́̑͌̓́̈̽̍̑͊͋̈͐̚̕͜͜͝ͅͅ ̵̛̛̛̼͉̙̺͚̟͔̗̺̺̤̗̩͙̥̻̣̰̳͍̹͔̠̃̅̈̊̽̇̑̎̓͑͐̄̇̀̾̅͌̓̃̾̒͆̿̍̊̓̚͘͝ͅ ̸̡̧̡̡̛̙̼̻͎̞̠̰͓̥̬̭̻̖͔̭͇̙̟̟̥̭̠̥͚̞̹͕̙̼͕̦͙̟͔͂͋̍͊̓̿ ̴͍̠̳̻̼̼̤̼̩̹̟̬̻̠̅̍̂͒̉̉̄͗̈́͑̉͗̏͗̂̍̿̌̈́̅̀̔̒̌͑̃̽͘͘̕͝͝͠͝͝ ̴̢̨̨̢̮̰̰͉̦̞͈̠̜͙̼͕̜̥͎͖̹̺̮̰̱̙͕̫̲̫̪̦̑͐̀̄͒̋͊͛̎̈́̈́͜͜͠ͅ ̸̧̨̞͚̲͙̪͇̮̗͍̯̃̀̄͆̇̈́̃̔̏̇́̈̔̿͒̀̀͆͆̆̚̕̚̕͘͜͝͠ ̷̛̛̛̲͚̝̘͈̌͌̂̈́̔̈́̆̎̊̑̄̋̇̉̄̃̈̿̅̈́̒̉̈́̅̄̆̈́̽̚͘̕͠ ̸̢̡̨̞̠̱͈͇̻͔̦̩͇̰̪̠̜̥̈́͗̓́́̐͛́ ̵̧͈̳̱̪̝͇̜̯̮̬̆̓̓̓̓̓̀́͒̄͌̄̄̂͋̀͗̐̋̉͗͗̇̅͒͗̽̈́̄̈̚̕͘̕̚ ̵̨̢̧̨̡̢̡͖̫̼̗̭͓̪̤̳̱̞͉̜̖̳̟͇͚͈̙͖͇̮̹̹̺̣̪̩̗̪̥̞̦̮̩̺̜̐͗̉͒́̀͑̍͂͊̆̅̐̃̚͜͝ ̷̢̨̨̧̧̢̛͚̗̘͓̖̦̣̤͎̠͎̘̱̖̝͚̱̣̗̼͕͍͇̱̜̞̖͇̦̖̰̯̦͉̹̙͚̭͙̣̻̗͂̈́̄̾̔̑̑͌̂̾̒̇̒̐̐͐̔͗̇̄̔̏̈͆̈́͒̿̈̈́̓̏̎́̽̕̕͝͠͠͝͝͝(̵̨̭͈̠̤̻̟͔͉̬̭́̓̿̉͑̈̂̽̓̊͐̐͛̃͌̕̕̕ͅ3̵̨̨̗̩͖͕̤̟̯̱͉̳̳͔̘͔̩̠̳̗̰̣́̾̂̾̿͐͐͒̏͊̊̍̈̓̌́̇̋̉̾̍̈̈͊̇̒̕̚͘̕͘)̵̛̼̥̀̅̂͂́͛̔͊̀͛̎͊̓̋̚̕͝͠͝ ̸̡̢̢̛̫̘̠̗̗͖̘͕͕̗̣̈̑͗̓̑̈͗́̎̿̐̓̅̒̈̇͌̈́̿̎̈́̒͑̔̿̈͗̽̽̇̀̇͊͒͘͘͝Ì̵̡̛̳̟̹̦̙̼̘̈́̅̿̇́͊̎͌̂̏͋͋̀̈̃͋̐͋̎͆͂̓͆̍̄͆͊́̑̍͆́̔͂͐̚͝͝͝͝n̶̢̡̨̧̺͔̫͔̻̫̦̭̻̦͖̫̖̬͈̘̺̼̬̳͍̻͓͉̗͔̻̦͚͖̪͇̻͙͔̠͍̜̫͇̪̼̤̏̇͜͜͜ṿ̵̼̯̃̚͜ͅa̵̧̧̱̼̲̳͙̺̱̹̼͎͇̞͉͙͙͍̺͙̘͍̗̦͖͚̪̝͉͎̹̲͇͔̖̘̞̬͙̯͈̣͌͊̽͊͌̄̈́́̿̒͠͠ͅͅḑ̵̢̧̧̡̧̱̘̦̯̘̜͚̭̟̤̳͓͙͎̟̥̙̖̮̠̱̪̻̤͖̳̳̰̜̝̥̪̑̒̎̀̈́́̍̍̇̏̾̎̐̊̑̋͘͜ͅę̵̤̌͌̅̉̀͐̇̿̃̃̔͘͘͘͝͠ͅ ̵̧̡̛͎̟͓̼̭͓̝̯͓̻͕͈̯̣͇͙͎͓̭̔̀́̆͆̋̀͗̄̋̈́͊̂͊͆̿̍̈́̿͂͌̇́͑̽͘̕͝͝(̴̨̡̥͇̖̰͍̺̘̼̰̺̻̈́̊̅̽̑̀͆͑͌͗̈̌̆̈́͆͗͋̾̂̃̚͝M̸̡̛̛̲̗̦͍͙͈̘̱͍̰͉̝̱̱̙̜͉̟̱̰̤̘̻̦̜̰̯̈̏̉͐͊̓̂͂̅͌̐̂̿̔̏̓̿͆̽̓͐̌̀̉̀̏͋̍̾́̔̈́̄̒̃̄͝͝͝͝͠͠i̷̧̢̛̛̗̙͔͈̥̯̻̳̥̰̻̖̫̜̦̭̽̀̈́̃̍̉͛̂̐́͑̈͛̀̄̊͛̕̚ḷ̴̡̢̢̢̧̢̛͍̥̮̦͇̰̘̦͚͖͍͉̺̗̰̪͔̟̩̟͕̤͓̺͖̻͎̱̩͙͔͍̣̬͚̮͋͐͋̌̓̊̈́̍͛́͊̊̿̍̌̏̔̓̀̑̇͑́̓̈̈́͂̀̈́̂̒͌̆͌͘̚͜͜͜͝͝͝ͅi̴̡̡̡̨͓̝̤̗͖̗̭̝͇̫͕͔̞̥̖͍͓̩̹̬̦̪̤͙̙̓̃̈́͂̓̾̐̾͘̚͝ͅͅţ̷̧̡͚͖̰̮̳̮̲͕̘̬̼͖̺͎̟͖̺͓̰͉͎̗́̒̈̐̈̊̊̈̀̓͗̈̇͗̍̀̔̈̿̽̋̽̀̂̈́̑́̊̓͆̇͂́̕͝ͅą̴̛͓̟̺̝̮͔͕̬͔̭̗̲̄͌̒̈́́̔̎̓͒̆̄̿̑̾͋̾́̍̂͑̓̽́̇̀̊̄̿̆͛͆̿͂͗͗̌̀͊͐̐͘̚͠͝ṛ̴̨̨̛̯͔̤̙̜̫͔̬͇̼̬͙̰͓͔͎̲͖̿̽͐̉͒̍͗̾̂͂̅̀͐̿͌̀̆̔̌̏̍̈́́̽̑͐̎̈́̍̈́̿̈̚͝͝͝ȳ̶͎̥̦̼̦͈̼̯̞̲͚̺̺͔̰͙͆͗́͊̏ ̷̨̯̟͈̼̙͖̟̘̠͎̞̼̟̙̈́̿̇̑̓̀͛̀̄̽͑̋̿̂̂̎̐͆̅͌̔̂͐͜͠s̴̡̛̹̤̭̜̬̭̰̳̯͎̯̟͎̺̹̟̖̯͍͓̝̻̙̹̖̟̳͚̻͍͙͔̈́̒̀̑̈́̀̎́̿̓̍͗́̓̑̌̏̅͌̏̑͊̈́͊́̀̾͘̕̚͜͝͠ͅt̴̢͓̜̂̃̂̿̆̒̂̐͋̈͂̕͝͝r̷̡̧̙̮̺̲͕̖̲̖̞͚̖͎̗͈̲͎͆̀͜͝ę̴̧̢̧̧̢̢̛̹͔̜̬̭͇͓͚͖̰͍̝̠̺̗̹̘̼͈̥̳͉̙̦̻̣͔̜̺̩̪͉̞͎̝̻̖̖͍̞͕̓̀̂̽̔͂͂͛̈̎̉̉̊̀̅̋͌͋̊͑̍̎̒̓̉͛̾͊̉̇̓́͂͛͛͊́̿̀͒̊̽͆͘͘̕̚̚͜͝ͅn̴̘͎̻̖̪̞̙̳̆͑́͘ğ̶̡̧̼̳͈̜̤̱̼̩̯̞͉̣͔̯̬̮̬͖̦̦̉͑̂̌̒̃̈̆̄̂͂͛͐̓̋̒͂̀͂̈̈́̀̓͛͛̇͆͋͗͌̔̓͑̋͋̄̓̓̋̐̚͠͝͝͝ͅͅͅt̵̡̧̨̧̤̗̬̝̻̖̙̼͉͖̝̺̩͙͊͆̄̄̌̇̈́̈̏̎̓͗̈́̊̋̋̒̑̅͌͂̎̍̈́͛͂͊̂͘̕͠h̵̛̘̳͒͊͑̀̓̐̌͆͑̂̽̈́͆̾̇̋̇̑͗́̾̃̀̇͋̋͂͆̐̏̎̎̕͘̕̚͘̚̚̚͠:̴̧̧̧͍̻̰̮̗̖͚̙̥̥̻͖̰͕͓̥̞̫̰̺̬͍̝̘͚̩͓̝̲͍̰͎̖̘̠͙́̏̎̒͌͒͆͗̂̃̌̐͊͛̈́̏͒͐̕͝͝͠ ̸͙̪̯̤̠̜̺͙͕͇̼̤̠̹̱̭̣͙̳̖͇̞̞̺͊͜͝{̸̧̧̡̢̛͍͕̠̤̱̜͙͍̠͙̫͙̹͍͖͚̞̙̖̜͎̜͈͕̼̺̗͓̭͎̝͈̲̠̞̏̇͑͐͂̉̌͆̏͊͊̂̋̈̎̾̒̆́͊́̅͆̌̚͜͜͜͝͠͝͠͠ͅK̵̨̧̢̛̛̛̮͉̹͈̘͖̝͚̳̳̺͉̮̮̟͓̙͓͉̝̙̪̼̲̫̦̓́́͑̄́͒́͋̈́͐͐̀̃̏͂̾̔̄̄̉̿̍̋̓͒̕͜͝͝͠͠į̵̨̛̺͎͕͔͚͓̯̪̖̳̬͓̜̦͖͕̱͚̤͈͖͎̠͍̝̭̰̼͖̿̽̿́̆̈̔̒͊̔͌́͒̈́̾̆̈̏͑͐̇͛͑̆̓̋̋͒͌̾̎͘̕̕͜͜͝͝͝͠͠͝͝ͅņ̵̧̨̡̥̙̳̤̖͙̹̺̭͕̝̯̗͕͕͙͔͎̘̩̹͉̪̮̰̤̳͙̓̿͑́̊̍̀̎̚͘͜͠g̵̢͓͈͎̫̗̳͙̫̠̺̩͔͕̙̤͍͇̞̺̓͛̈́̂́͗̄̓̾͛̚d̷͎̃͛̅͋̃̈́̀̈́̈̈́̃͒̀̃̑́́̎̅̇̆̋͌̑̇̽̿́̍͘͝͝o̴̭͔͕̻̐́͒̿͛͋͊̀̍̊̑̈̈́̒́̽̈́̍̈̾̕̚̚͘͠͠m̷̢̆̓͒̀_̶̨̨̢̛̛̗̪̰͔̩̱̱͚̞̝͇̻̳̞̟͈̫͙̝͔̭̦͑̊̑̋̽̓̈́̍͆̌̾̃̀̌̂̈́̒̉͆́͒̒̒̀̒̑̈̅͐̀̇̑́̓͘͜͜͠͠ͅE̴̢̨̡̢̛͖̠̱͖̼̗̦̬͉̹͎̜̣̦͚̤͍̫̮͚͖͇̟̜̳̹̣͈̙̝̘̋̀̈́̀̎́̇̑̑͛̃̉̀̈̀́̓̔̋͋̎̀̒͒͗̇͌͊̆̈́͋̊̏̀̅̔̃̓̆̿̕͘͜͝͠͝͝͝ͅx̴̛̛̛̭̜̙͓͔̖̟̝͓̮͉͇̏̈͑̄̓̐̂̾̆̋͗̒̀̑̎̉̓̉̉͊̃̽͋̌͑̈́͛́̓̓̉͂̉̕͠͝͝ţ̵̢̛͈̼̠͎̼̖̗̪̼̤̱̫̘͓͙̖̙͍̰̳̤̳͖̖̮͔͎̮͈͊͐̂̎̈̽̽̊͒̏̅͊͋̅̿͌̑̀̓̓́̈́̍̂̽͋̋̇̋̃̄́̒̚̚͝͝͝r̷̢̡̢̙̜̮̼̠͉̠̥̗̠̩͉̙̩̻͍̥̙͑̀̐̔͑̀̉ͅͅa̷̢̡̦̩̺͔͍̗͙̪̮͉̰͈̬̰̱̱͇͓͔̭͍̗̳͆̒͂͌͆̒̄̓͛̉̔̃̈́̈́̑̀̃̾̑͆̚̕͘͘̚̕͝͝ͅͅs̷̡̧̤̯̪͎̲̩̘̼̹̝͍̮͖͈̗̺͔͉̄̈́̀̋̌̽̈́͂͛̔̀̏̅̆̌̈̾̋́̈͘̕ͅ[̷̡̢̨̧̧̧̛͔̻͍̹̺̬̗̝̙̦̖̜̱̠͔͕̖̪̖͚͕͚͍̳͈̦̙̤̱̣̭̬̪͍͔͈̬̤͒"̶̧̢̢̡̧̢̜͕͔̦͖̳̞̮̫͎̪̲͈͙͓̝̤̼̟̜̰͚̝̹̙̤̹͍̟̲̦̣̖̅̔͐͌̀̎͘͝͠ͅͅP̸̢̛͍̱͕̬̖̣͍̬͇͚̥͕̪͕̻̺̗̣̙͖̖̍͐͋̊̔̉̔͆̑͌̏̾̿̄̾͌̽͂̕͜͜͝o̵̢̨̡̢̨̨̢̨̬̤̦̲̟̣͔̣̼͙͍̼̱̻̺̰̬͉̭̯̘͎̖͍̣͚̫̟̤̝̜͈̳̻͕̖̼͋́͗̌̊̌̊̄̐͛̀́̈́̏͐͋̿̀̎̋̉̅̆̇̒͑̊̊̆̈́̐̕̕͘͘̚̕̚͠ͅw̵̢̧̧̨̢̧̧̛̛͈̼̹̙̻̫̰͕̳̮͚͎̦͕͍̞͍͇̺͇̺͚̫̦̻̹̼͈͎̭̺̪̞̖̻̜̲͈̠͚͓̏͆͌͋́̋̿̀̾̀̒́̔̿̈̏̏̋̀̀̀̅́̾̔̍̈̇̾̋̈́̏̈́̃̂͗͂̾̆̒̋̈́̐͘̚̕͜͝͝ͅě̷̡̼̞͙̤̱̭̘͙̫̦̠̥̺̬̣͖̳̼̀͐͘ͅr̸̡̢̡̨̛̝̜͉̲͔̺͈̱̺̤̭͚͔̯͙̬̻͉͚̞̱͈̩͙̞̞̝̩͈͉͈̩̖̍̎͆̊̀̿͂̉̅̇̅͐̃̿́̒͛̚͘͜͜͜ͅ"̵̨̡̧̡̨̨̛̛̛̛̥̠̯̳̙̘͍͙̳͉̹̭̻̠͖̤͇̲̬̟͕͍̘̭̰̗̗̙̫͍͈̥̩͖̋̌͛̈́̎̅̄̅͛̕̕͜͠]̵̨̧̡̡̢̛̛̬͔̼͖͖͕͕̗̣̤̠̮͖͖̯̦̣̰̟͍͓̩̘̮̪̤͎̘̀̏̓̏̎͌̇͂̄͒͌̉̅̓̍͗̉̒͒̎̀͊̄͋̋̋̾͂̚̕͜͜͠ͅͅ}̵̥̞͈̝͋̽̀́̈́̎̑̾͗̅̈́͋̈́́̍̀́̓̍̒̋̏́̀̈́̇̿͆́͋̔̚̕̕̕͘͜͝͝͝ͅ)̶͕̤̺̠̅̊̈͊̉̽͆̋̽͒̕͝
                                ̴̡̧̪̪̜̙͕̦̪̜̰̗̟̤̯̙̳̟͙̦͍͒̀͘͝ ̸̧̡̡̡̧̭̼̫̗̱̘̺̦̲͎̣̪̭̯̲̠̣̪̞͔̖͙̯̗͔͈̫͙̱͎̟̠̖̭͔̝̞͚̤͖͗̉̒̿̋͒̉̆̃̋͛̆͗͂̇̒̈́̇̋̎̐͐͋̅̏͒̃̈̿̍̿̓̌͐͘̚̚͜͝͠ͅͅͅͅ ̴̨̡̨̧̡̧̢̝͕̲̙̖͍̲̟̝͖̥͔̟̞͍͓̪̗̙̣͇̯͖̮̘͖͔̖̤̟̭̬̰̖͙́̆̌͗̆̄̀̏́̾͆̄̑̒͐͑̾̍͛̋̐͆̎̈́͂̅̽̈̏̎̇̔̓̈́̈́̑̍̈́̄̓̊͒̈̕̕̕͠͝͝ ̶̨̡̡̧̱̩̪̥͎̤͍̦̯̠̩̤̦̘̩̘̦͙͖̱̙͓͖̤̰̗̭̻͉̈́̂̏̊̈́̉̃̚ ̴̡̛̛͍̩̩͎͖̪̰̱͕̬̟̗͇̻̠͛͒͆̇̈̋́̄̓̀͑̅̇̀̃̄̽̔́̂̓͐͊̐̂̋͆̊́̊̄͂͆̈́̾̈̔͆́͘̚͘͜͜͝͠͝͝ͅͅ ̵̢̧̧̧͚̬̟̳̰̯̥̤̳͓̞̰͓͚̜͇͚̫̦̦̭͍̠̟̝̙͔̺͙̩̂̓́͊̈́̋̉͛͋̆̓͒̀͑̇̒̎̏̈́̈́͘͜ͅ ̵̡̨̢̣͚̯͓̤̰̬͕̫͓̩̠̰̠̦͈͐̇͐̓̐̌̊̑̈́͊͂̋̉̅͆̈́́̉͆̒̒́́̆͐̔̓̂̍̆̍͋͛͗̓̎́̀̏̋́͗̉̕͘͝͠͝ͅ ̵̡̨̡̨̢̮͔̙̘̲̘̥͚̳͉̭̥͚̮͙̼̤̣̳͖̩̻̥͔̪̤̹̰̟͖̦͎̣̦̳͓̥͕̦͕̘̣̎̈́̔̄̆̈́́͂̅͑̐̊̈̾̍͑͊̍́̀́̚̕͘͠ͅͅ ̴̢̛̮̘̻͈͚̦̺̠͔͇͕̮̳̠̲̘̝̜̳̻͍͖̯̬̮̠͕͍̗̹̦̭͇͙͎̯̯̮̤̙̒́͐̃̈́̾́́̿̎̈͜ͅ ̴̢̲̖̟͖͙͑̄͒̀͌̊͠ ̷̨̨̢̢̛͉̩̖̦̙̣̣̜͍̝̙̗̟̥͚̻̳͖̱͇̤͈͈͈̲̯̝͓͍̗͖̤̙̣͖͈͇̺͓͇̳̲̉̈́́͑̂͜͠ͅͅͅ ̷̧̛̥̭̻̻̖͇͕͍̖̳̼̼͎͕̘̺̳̯̗̘̭̰̳̥͈̖͍̘̥̫̣͈̺̯̝̫̓̉́̌̎͗͊͋̈́́̾̾̀́̇̏̔̄̏̍́͌̍̀̔̒̊̋̇̅͗̅̕͝͝͝͝͝͝͝ͅ ̴̨̨̡̡͎̲͚̩͕̺͖̩͚̻̪͔̰̟̺̲̲̺̞̤̼̩̮͇̖͓̬͔̝̖̻̼̫̻͇͋́͂͘̕͜͜(̵̨̡̡̝͚͉̠̤̙̺̲̫͓̟̱̩̱̫͖͈̪͓̩̞̝̦̿͌̉̒̾̇̑̓̀̍̋͋̑̆̎̈́̕͜͝͠͝4̷̡̛̼́̐̆̆̍̃͑̾̀̎̌̅̄̈́̽̒͂̋̋̑̓̀̓̊̒͂͗̈́̎̄̀̽͋͛̂̆̅̕͘̚͝͝͠͝)̷̛̱͓͔͇̣̻̑̅̓̆̋͑̍̂͌̍̊̑̑͂͆̈́̈͌͗̈́̉̀͌͗̑͆̈́̕̚͘̕͠͠͝ͅ ̷̛̳̺̥̺̎̈́̋̂͋̄̇̃͐̑͗́̆́̔̓̾̉̆͒͂͘̕̕͝͠͠C̸̨̛͙̎̐͌͌̎͑̅̏̆͊̀̅̽̀̀͌́̓͛̓̓̓͗̃̎̐͑̊͐̇͌̆͐̕̕͝͝͠ĥ̸̞͍͔̦̜͍̬̲̲͙͉͔̰͙̠̖͔̟͉̙̺̣̜͙̈́͋͗̑̅͒̂̄̊̎̽̿̎̑̾̈̒̎̄̔̉͛̀̐̒̽̈́̊̊̚͘͜͝͝e̷̡̛͈̯̮͔͌̎̿̔̐͂͋͂̊̏̀̉̇̉̊̂̊͗̈̊̕͘c̴̛̛͕͇̓̈́̅̂͆̈́̐̐̑̎͒́̐̒͋̌̌͑̈́͊̔͗̓́̈́̒͂́̉̋̇̎̃̒́͆͗̒̚̚̚͠͝͝ķ̵̡̧̛̠̞̖͈͍͉͓̭̺̟͔̘̤̰̤̺̩̱̦̣̹̠̗͇̫͓͚͖̖̦͖̖͕̱̩̑́̌͊́̌̆̈́̍̓̌̾͊͗̅̅̄̎̑́͒͊̎̈̆͐̈́̌̍̈́͛̇̄̾̿̕̕͝͝͝͝ ̷̧̨̲̻̺͕̦͍̥͓̙̩̗̾͌̀́̿̐̀̎̾͛̆̊̉̔͐̍̈́̑̓̌̉͛̎̐̑̈̿̂͆͑̇̀̚̕͜͝͝ͅK̷̡̛̪̫̰͕̙͔̋̀̌̂̓̍̍̾̊̌͐̈́̈́̾̇̅̓̈̽̑̾̌́̔̓̍͗̅͌͘͝͝ͅį̵̻̣̙̘̲̬̥̺̪͂͒̍͑n̶̤͇̈́̈́̾̀̄̉̇̔̑̽̅̅͌͆̂̉͆̏̒̂̄͐̆̈́̑̓͂̈́͗̄̆̓̅̓̈́͋̽̉̆̃͐̚̚͘͝͝͝ǵ̴͈̹̝̣̹̺͖͇̭͚̬̩̄́̓̅̐̆͗͆̆̈́̍̂̿̊͐͐̾́͐̏̇̚͘̕͠ͅd̶̢͎̘̺̹̳͔̫̻͇̎̊̂̈́̂̈́̄͌͘̕ö̵̡̧̧̧̧̖͉̩̯͔̱̠̱̰͓̫̣̼̲̬̹͔̟̖̫́̇̂͘͝m̷̢̧̨̟̝̝̝̠̗̺͕̭͍͙͎̣̲̖̯̘̟̞̟̜̰̠̼̞̖̯͍̹̥̫̻̂̀̉̀̐̇̈̊̎̓͆͜͝ͅ ̸̢̛̼̘͍̩̝̑͂͒̀̊̀͆̆͊͐̾̓̀̓̇͂̄͘͝S̸̢̧̡̡̡̨̧̹͈͙̖̼̣̱͇̪͙̲̹̲͓̞͙̱̘͖͎͍̦͇͙͎̪̓͒̀̔̇̀͌̀́̆̎̐̈́̉͒͘̚ͅt̴͓͔̱͙̱̺̝̜̹͂̈́̀̑̔͊a̶̢̧̡̡͚͎̥̟̪͙͇̦̱̭̟̣͖͙̹̟͓̙̫̖͉̪̙̱̥̥̱̞̫̭͙̫̞̻̞̱̜͕͖͊̄͛̐̃́͊͊͐̋͊͐̎̂͊͒̃́͗̔̎̓͐̐͒̒̄̕͠͠͝͠t̶̨͉̬̪̠̤͔͙̯̠̠͖͖̤͖͓̟͉͙̲͍̖̭͈͐̍͜ͅs̷̛͔̥͚̭̲̳͍̽̀̂͗̎
                                ̷̢̧̨̛̛̱̥͙̟͖̜̟̦̫̺͈̲͙̙͍̝̬̠̬̺̙̝̹͎̣͕͓̗̤͇͍̠̻̲͎̅̋̈̔̈́͑́̔̈̿̉̉̊̇͌̑͋̀̈́̓̐̊̎͐͒͗̀̅ͅ ̴̧̹̻̺̲͍̖͍̯͚̬͂͊͋͊̔̓̉̍̓̐̈́̅́̋̊̌͑͂́̍͛̍̄́̿̃̈́͛̆͗̎̓̆̽̀̎̌̇̂̑̂̅̚̚͝͝͝͠ ̴̡̧̨̛͉̭͚͈͓̫͉̈́̈́͊̑̈́̃́́̏͑̋̋̄̓̌̅̀̀̉̍̈́̿͂͑̈̿̊̚͠͝͠͝ ̶̨̡̨̢̗̫͇̣̬̫̗̩̻͎̼̪̳̮̗̖͚̟̤͉͔̠͙̼̗̜͔͈̼̳̼͙͚͔͔̼̖́͗͛͌̒͂̃͊̀͋́̉̀̅̋̄́̒͛̋̀̓͛̓͋̇̋͐̽̇̓͑͐̉̚͘͘͘̕͘͜͝͝͝ ̷̨̨̡̮̪͈̹̰̬͓̺͈̻̦̮̻̲̲̦̩̜͙̳͙̹͚̼͉͙̩̏̑͗́͗̓̋̋̎̓̅̓̇̂̀̂̚͜͜͝ ̴̦̣̩̯͚̟̘͈̘̘̼̖̳͔̲̘̜͇̬̪͓͕̼͙͇̬̖̞̩̰͔͍̮̟̜̺̳̍̈́̃̊̋̆̐̆́̓̓̓̾̄͑̓͛̋͑̿͐̽̋̽̈́̾͋͆̓̓͒̍͋̐͌́͐͂̆͐̂̋̿͘͘̚͘̕͜͝ ̸̥̪́͗̀̍̓̐͐̓͗͋ ̶̜̥̼̘͈̉̊̇́́̏͆̔̚͘͝ ̸̧̡̛̜͈͇͎͚̜͈̠̬̠̗͎̮͚̖̪͎̻̦̭̻̀͋̈̔͆̈́̐͒̀͗͐̂̽͑͛̓̎̈̕̚͜͝͝͠͝ͅ ̸̡̧̧̡̧̢̛͎̭̣̻̰̜̟͓͈͙̠̲͔̪̜̻̟̫̰͔͚̀͂̎̊̇̊̆͋̀̑͒̐̉̿̂̐̌́̕͠ ̸̢̨̢̹͕̤̫̩̗̖̤̰͉͈̫̲̩̜̤͖͕̞̭̙͍̬͎̝̰͍̳̝͍̖̼̝̖̮̳̠͖̣͍̃͐͐͑̀̃́̉̌̌͆́̓̀̈̾̽͂̐̉̋̓̓̈́̿͋̏̍̏̊͗͗͗̿̋͂͘͜͜͜͠͝͝͝ͅ ̷̢̢̢̲͕̰̬̳͉̥͙̭̙̭͙̠̘̯̭͖͖̙͎̳͈͕͔͔͖̀̓̃͛̈́̒̈̄͒͊͂̂͒̋̆̒̃̋̀̎̄̓̅̑̅̂͑̂̽̈́̇̚̚͘͘͝͠ͅͅ ̸̦͈͕͔͉̰̖̫̞̗̎́͋̑͗̆̊̂̐͠͝ͅ(̷̳̙͔͓̻̖̳̪̗̈̾̅̐̍͐̎̂̕̚̚͝͝͝5̷̛̹̭̩̗̟͖̖̟̮͕͇̗̝͕̮̜̤̦̞͍̜̱͚͔̙̮̋͑̊̍̿̉̄͜͜͠ͅ)̸̡̛̛̛̛̦͇̰͈̱̩̘̙͍̩͓͍̙̠̗̣́̈͑̒́̓̏͛̅̈́̓̈́̀͊̿͗̑͑͑̈́̅̒͑́͒͘͝ ̴̨̛͉̩̮͇͕̠̩̥̠͔́͗̐̓́̂̃̓̽̇̊̄̊̾͊͌̄̊̀̈̆̒̽̄͗͛̿̓̂̓̈́̎̾̓̌̌̾̾̆́̃̃̚̕͠͝Ḩ̴̡̧̧̛̪̭̻̪̺̭̯̺͚͙͍͖̝͍̝̘̦͔̳̼͚̼̲̳̞̺͖̾̅̓̀̿̔̎̀͛̅́̅͛̌͐͘̚͜͜i̸̡̢̧͕̪͓̝͙͚̥͉͎̣̩̭̻̫̣̙͖̞͈̪̻̙̻̘͍̯͎͉̻͙̝̫̣̦͔̳̭̮̜͚̹̝̟͓̋̀̏͂̈́͝ŗ̸͈̰̞̬̗̳̩̺̹̟͔͙̮̠̰͖̖̈͆̑͌̏̓̏͗͑̃̾̾̋͋͆̈̑͂̑̄̌̇̇̀̏̏͊̍̂̑̐̈̿̃́̋̚̕̚̚͘͠ę̵̡̡̛͇͉͙̮̜̫̟͕̋̌̓̄̏̓͆̓͆͛̽̒̐͐̔͋̃͑͂̅̽̆̀̍̔̈́͒̎̽͋͘͜͠
                                ̸̡̡̳̫̥̺͇̺̲̥̗͖̳̠̮̭͉͉̰͍̳̳̍̌̿͂́̿̽͛͛̆̃͜ ̸̡̡̛̼̻͎̙̖͕͓̣̳̞̯͚̙̘͔́̍̽͌̿̓̓̑̆̾̿͗̈́̇̓́͋̎͋ͅ ̶̡̨̛͓̺̫͉͚̩̟̦̬͚̩̺̞͍̥̟̋͒̇̈́͛̇̐̄̒̐͂̾̔̑̓̿̍̓͒̽̏̈́͊̌͒̋͒̃̏̊͌̿̈́̄̆͘̚͝͠͠ ̸̡̢̢̡̧̧̢̝̬̙̰̱̦̫͍̘̳̝̙̪̩͓̭̫̞̗̱̘͕̹̣̲̤̥̼͚̰̱͙͚́̔͜͜͠ͅ ̴̢̨̻͓͇̲̖̙̬͍̝͓̠̹̬̐͋̉̋̅͒̈́̃͆͊͑̿̎̓̾̃͐̈́̚͝ ̶̛̛̟͖̳͇̱̩͍͍̗͕̖̜͍̲̀̒̎͒͗̀͂͋̑͂͊̈́͒̀̏̓̃͋̎͒͗̓͌͒̍̍̋͘͠͝͝͠ ̷̢̨̛̛͓̫̱̲͎͓͇̬̘̱͔̻͚͍̟̹̺͙̹̱̣̱͓̯̞͓̯͔̰̙͍̝̙̗̙̃̒͒̂͋̓͐̂̿͐̉̒̑̎́͐̋̾̆̋̍̈̒̔̀̔̓̑̓̅̄̍̀̀̏̈́͛͆͜͝͝ ̸̺͙̮͎̫̬̱̣̭̼̟͕̳̩̭͚͓̗̔̊̿͗̉̈́͗̽̄͛̔͜͝͝ͅ ̷̨̨̨̩̞̙̱͕̣̠͖̫̩̫̦̩̰̭͚̲̥̘̪̙̫̱̪̭̩̥͓̝̫͙̼͈̪͇̤̲͎̳͑̚ ̶̧̬̲̤̻̜͎͍̻̱̤̝̣̞̘͓̜͋͊͂͗̇̆͋̎̋̿̐̒͒̆̔͗̀̒̃̈́̅̂̒͑̈́̐́̀̆͗́̌̈͛̔̓̒̄̚͘̚̕͘͝͝͠͠ ̵̡̛̰̰͔͎̲̹̙̘̙͎͈͍̗̿̅̀̉̋̅̎̐̏͑̓͋̊͌̑̐́̄͋͠ͅ ̸̧̨̧̥̣̣͔̯̫̩̮̺͔̘͇͖̣̯͇̟̣̠͓͎̣͕͉̬̘͚̟̙̭͍̝͎̙̘̰͙͍͈̮̮̞̮̰͈̠͑͐̏̽̀̏͋ ̸̨̛͕̞͍̬͓͔̼͉̦͈̟͇̤̘̜͙̤̟̜̦̖͔̩̗̳͐̂͆̿̔̍̉͗̇́̉̎̈̈́͌̈́̔̌͒͒͋̉̃̍̾̌́̈́͜͜͠(̸̢̢̡̢̨̟̩̠̮̭̘̞̲̞͈̼̪̞͖̣͓̼̼̲̯͚̝̺͙̥̯̤̽̔͐̄̄̈́̇̑͆̑̄́̍̑̈́̐̐̾̾͐͐̑̐̏̊̓͛̊̌̋̀̚̚̚̕̚͘͝6̸̥̙̞̬͍̹̦̖̳͚̣̱̩͍̓̚ͅ)̷̭͇̣̯͇̣͙̘̰̪̥̯̭̺̪͕͆̍̅̋͆͌̂̒̋́̈͊̃̐̂̆̚͜͜͝͝ͅͅ ̸̼͍̱́̓̈́͌̊̑̆̔́̍̎̓̔͂̈̋̃͂̑̈́̃͊̄̓̕̕͝͠Š̷̢̨̨̛̰͎̘͎̳̹͍̜̠̼͉̺̜͕̬̤̲̲̰̫͔̯̜̫̤͎̭̰̏͆̌̾̾̇͑͂̀̍̂̆͆̀̇̅̉̀͋͐͒̌͐̋͐̔̊̆̐̏̀̐͋͛̏͂̏̓̕͘͜͝͠ͅͅe̶͍̱̓̉̒͂̄̆̈̐͂̿̀͊̉̒̊͑̆̿͗̊̀̅̃͌̓̚͘͠͝͝t̶̢̢̢̛̰͎͉̖͙̪͍̟̯͎͕͚̣͙̬̭̣̣͖̩̠͓̘͓̜͖̄̒͆͋̒͊̆́̓̓͛̽͆̒̐̃͌̒̍̔̽̈́̉͂́̀̇͒̀̆̿̆̔̊̀̄̀̃̕͘͝͠͝͝ͅͅt̷̡̧̛̳̦͈̪̪̺̫̲̱̪͕̩͎̫̥̥͕̻̙̰̥̱̜̬̰̹̄̉̈́͂̉̒̄̆́͛̋̄͗̌̆̓̇͆͑̀̓͋͛͋͐̓͘̕͝͝͠ͅi̷̮̤̩̼͓̣̬̭̩̳̼͖̮̤͍̝̠͙͓̹͈̺̼͙̲̋̄̏͛͐̉̆͜n̷̨̢̧̞̱͖͖̙̫̪̯̭̙͙̖̳̼̰̰͙͍̻̝̖͍̭͔̯̺̫͉̩̅̎̐̌̊̃̅͒̒̀̒̿͛̃̾͌̽̾̈́̎̎̀̔̐̆̏̊̽̎̆̍͐̌̑́͘̚̕̕̕̚͠͝͠͝g̷̨̧̨̡̧̨̨̨̡͎͖̫̞̮̝͚̬͈̺̺͇̫̹͎̳̗̩̝̣̩͉͕̲̖̻̲̰̦̩̩̗͔͔͌̌̂́̋̋̄̆͂̏͛͆̑͒̎͌̋̄͌̔͜͜͝ͅs̵͔͉̗̞̪̦͓̹̯͍̺̯̝͚̞̺̰̖̫̬̞͓̺͖̦̥̰͖͕̳̞͍͆̈́̄͌͗̈̋̄̆̾̌̽̈́͌̌͊̔̃͂̾͌͆̄̐͌̃̏͐̓̑̅̓̓̈́́̃̍̚͘̕̕͠͝͝͝͝͝
                                ̶̨͔̬̥̰͉̖͙̟̪̗̲̤̝̘̥͍̘̼̯̠̔̓̓̊́̀̃͒̾̒͐͗́̀̈́͐͌̃̑͗̄̈́͋͌̄̍̉̓̎̉̊͋̋̇͗̐̀̕̚ͅͅ ̶̨̢̢̧̨̛̗͔̳͚͚̯̗͖̜͉̰̗͚̗̲̼͓̠̜͈̩̺̳̬̭͕̪͈͓̳̘̌̑͆͒͋̌̍̀̈́̒̄̀́̑̈̉͛͊̐͑̂͛͑̾̓͘̕̚̚͜ͅͅ ̶̧̧̛̛̛͕͈͎̤̼̝̪̤̭͔̱̺̟̲̠̩̙̬̖͓̜͓͉̠͎͙̘̗̟͎͙͙͉̻̗̲͙͐͐̃͌̀́̽̑̃͊̿̂͊̌̇͗͑̉̀̄͒̆̎̏̄̈̉̎̍̏͑̋̓̈̊̒̉̚̕̕͝͝ͅͅ ̸̡̛̛̼̠̺̞̤͖̻̪̫͕̙̯̱̩̦͉̠͙̬̎͆̇̉́́̍̍̿́͊̓̐̍̄̉̀͒͋̾͂̌̊̊̊͂̋̕̚͜͝͝͝͠ͅ ̷̡̧̢̡̢̢̼̼͈̫̲͓̙̲̰̟̩̺̬̙̖͈̹͎̗̫̰͉̞̝̘͙̙̲̝́̐̆̆͋̿̈̀͋̀̄͐̐͆̕͘͜͜͠͝ͅ ̸̢̧̢̟̱̭͎̱̝̺͎̪͙͈̺̼͉͔͕̑̓̀̈̈́̓̊̉̂͑́̆̈́̐̋́͊̈́̕̕͝͝͝ ̸̢̢̢̡̧̩̙͇̬͍̦̞̲͎̠̺̬̱̹͍̰̫͕͙͕͉̮̪͔̞̘͕̰̞͎͓̰͒̆̎̋͊̌̈́̈̿͐̈̿̌͊̃̐̌̍̀͘̚͝͠͝͝͝ͅ ̴̡̨̧̪͖̘̫͍̗͓̘͙͚̼̼̥͖̌̉͋͛̽̋͋̎̌̈́͐̏̊̉͛͐̈̀͑̀͗̽̌̿́̈́̈̀͒̚͘͝͝͝͝ ̴̢̨̧̨̢̛͔̘̫̱̙͙̥̫̗̤͖͉̟̱̲̯̟̺̼̲̭̙̗̼̯͇͍̝͙̯̬̗͎̩̺̦̟̼͎̠̬͇̘͎͖͋͆̓̍͒̽͆̽̆́̊͌̓͊͂̎̓͑̊̀͐̽͗̈́͋̈̂͂̇͛͗̃̾̃̚͘͠͝͝ ̵̧̢̛̛̩̗̲͔̙͕͚̙͇̹̬̟̬̥̣̤͖̤̹̻̤͈͈̹̩͎̭̙̲͇̟̜̺̣͚͍̭̹̯̜͔̺̞̩̫̳̇̈͒́͗̏̐̍͑̾̂͋̈́̀͑́̈́͑̽̊̅̒̒́̓̍̿̈́̓̓̆̐̆̓̓̅̔̐̕̚̚͝͠͠͝ͅ ̸̧̡̛̥̬̫̦̻̺̱̰̠͍̪͉͚̙̜̺̮͇̰͔̫̻̘̮̘̬̰̫̯̦̗̥̟͖͓͚̥͓͕͙̘͕̎̾̌̆̿̅͜͠͠͠ ̴̡̧͕̣͖̦̥͉̠̘̱͕̞͓̗̼̙̣̭̳͖̼̗̦̼̹̩̓̏͂̇̊͋̅̋͆̉̈́́̕̚͘͠ͅ ̴̧͔̳͎̽̈͜(̷̡̨̤̲̝̞͎͒̄͊́̈́̽͊̽͑̀͑́̋̆̚͜7̴̡͔̦̙̭̖͎̥̂̌̃͒̅̾͗͒̒̈́̄̄̑̓͊̔̈́̽͘͝͝͝͠)̸̢̧̧̢͚̻̟̤͎̤͔̬̩͎̬͇͔̙͎̦̤͉͇̫̼̪̙̻̬͙̰̤̤̼̩̰̮́̎̾̃̒̔̓͒̌̌̅͛̅͋͋̇̈́̅͆̾̈́̔́̈́͂̈́̚͠͠ ̸̖͛̍̍́̌̿́͝Ų̷̡̧̢̨̰͙̟͚̰͎̲͍̺͚̞͕̻̯͙̹̞̫͙͙̻̗̩̙͚͓̹̉̅́͊̿̀̔̑͜͜͠͠p̴̛̱͍͖̲͔̼͓̳̱̻̯̮̘͔̎͌̀̓̄̋̏̉̔̈̉͗̈̀̊̄̅̍̾̀̓̃̐̀͒͛̎̈͆̚ģ̸̳̪̳͇̪͇͚͇͔̭̜̟̭̹̘̤̖̫͍́͛̊̋̋͒̃͠͝͝ͅͅŗ̵̧̛̛̘̺̻̯̩̜̜̗̟͔̟̠̺̲͈̖̰̭̬̥̬̗̙̺̙̀̎̆͌̅͒̊̌̾̊͌̅̋̋̊̀̈̍̓̈́̓̃̏̀̈́͋̑̂̃̿̓̆̓̈́͘̚̕̚͜͝͠͝a̶̧̡̡̢̢̢̢̨̧̛̛͕̲͙̮̯̹͉̺̥͇͔͓̲̱̘͓͔̲̬͈̤̜̲̞̼͈̜͈͇̱̮͙͓̳͔̖͔͋̈́̿̍͋̊̂̔̎̅͌̐̐̇́͒̎̓̄͒̽̆̈́͐̈͛͆̚̚͜͜ͅd̵̢̨̗̭̘̠̙̱̪͙̹̜͕̞̀͌̓̋́̋̀̎͌͒͛́̈́̇̍̇͊̇̈̄̆̽̓̀̓͘͘̕͜͠͠ͅͅè̵̢̡̨̛̳̦̖̖͚̠̝̥̯̖͙͙͈͕̝̯̞̱̱̬̩̹̘̥͍̹͔͈̲̲̪͍͕̩̰͈̥̠̹͔͛͊̒̏̃͌́͒͐̒́̒̄̇̉̃̋̓̈́̈́͋̾̐̽̌̇͛̆́̂̄̋̋͋̒̐̆̒͒͛͐̓̄̕̚͜͜͝ͅ ̶̧̤̳̰̜̳̫̃̉͝I̵̡̛̛͍̤̼͙̙̯̝͙̼͙̘̠̫̲̫̅̍̅̿͗̂̌̉̈́̂̓̏̏͊͊̑͛̈̆͐̈͗̇̇̚̕̚̚͜͝͠n̴͖͖̘̭̱̦̘͔̤̽̎́͑͑͐̌͜͝f̵̡̢̙̘̻͎̺̮̮̬̮̫̦̜̤̬̱͔̟̣̫͙͓̱̮̟̹̭̲͈̫̀̒̀̃͐͜͝a̸̛͕̪͉͛͋̀̃̊ͅn̶̨̝͎͎̪̣̺͎̻̺͍̜͔̲͙̖̙͕̱͇̹̤͈͔̮̣͙̽̈͗̾̂̈̎̌̇͊͒́̋̀͋̃̿͑̔̿̐̇̕͘͝ͅţ̴̢̢̡͉͉̝͙͈̲̹͕̫͓̣̪̮͚̲͚͎̜͈͓͈͉̣̩̻̫̯̭͕̬̤̯̤̳͚͖̰͖̀̈̊̈́̋̽̄̐̂̄̀͂͛̊͂̔͜͜ṙ̶̡̧̡̨̡̛̺̰͇͍̠̗̭͚͍͈̤̮̟͔͚̙̻̫̖͉͕͎͔͉̻̪̭̣̱̗͓̣͙̣̉̄͊̋̎̊̑̋͒̉̓̎̀̾͌̑̔͛̚͜͠ẏ̷̢̛̥͉͇̤͉͚̙̤͕͍̇̇̀͐̈́͒̔̉̅̉̉̽̏̒͐̈͆͘͘͝ͅ ̷̢̨̧̨̨̧̛̛̛̱͓̻͍̟̺̠͕̮̖̺͈̰̭̙͕̫͉͔̥̘̼͉͉̅͒͂̂̄̃̈̓̏̑͋́̔̽͒̂͆̃̽̿̉̀̍͋̽́̃̆̎̔͛͗̉̚͘͘͘͘̕͜͜͜͠͝ͅP̴̡̡̟͎̣̺̪̳̯͔̫̰̦̝̙̺̠̙͚͉̩͊̇̾̀̈́̒̀̃̈́͊̒̈̎̿͑͗̌̑̇͛̓̕͝ơ̸̧̡̛̭̠̪͙̮͉͔͓̫̯̬̼̭̲̗̤̬͕̣͒̈́͑̄̽̎́̔̈̈́͆͆̾́̈̈́̑̀͆̑̒̓́̈́͆̓̋̔͛̊͆̈́͋́̈̇͊́͛́́̓̀̃̚͘͜͝͝w̸̢̡̨̨̡̢̨̬̰̠̲̰̱̪͔̟̞̬̠͚̟̙̣͚̣̲̞͚̼͙̫̗͔̖̲͍̫̫̥̞̪͚͒͑̍̋̇̏͊̎̒̐̀̊̔͘͜͜͠͠ͅe̸̡̡̡̨̛͙͔̥̱̙̤̱͓̦̞͕͎̞̖͇̠̘̣̐̃̓̓̌̔͋̓̏͜͜ŗ̶̙͇͕͑̾͝
                                ̸̻͚̳̖͕̟͙̅̿͒͜͠ ̵̡̡͇̙͖̳͖͈̳̞̪̻̪̥͕̯̜̪̠̩͎̹͎̰͎̦̻͚̹͇̙͚̦̘̝̰͕͍̙̺͕̻̙̘̠̂͛̉̔̿͋͐̑̂͆̐̽̾̐͒̒̈́͜͠ͅ ̸̧̢̨̢̛͉̙̦͉̹̭̲̼͈͙̣̬̹̱̻̱̗̒̈̅͗̐͂̒̊͛̆̀̃̊̇̒̈́̂͘͘͝ ̵̡̡̢̧̛̜̲̖͍̞̣͚̪̟̺͓̠͕͈̳͇̗̯͎̥̙͇͚͇̗̬̞̗̮̮͉͇̬͓̩̼̉͊͊̆̅͒̓̓̾̓́ͅͅͅ ̸̨̡̛̥̞͇̹̘͙͚̠̜̩͎̻̦̲͈̭̳̥͍̣͉̰̈́̄̈́̋̽͌͂ ̸̢̢̨̧̨̬͖͎̞͔͕̜͎̠̖͔̦̙͓͙̖̼͖̣̽́̔͒͊̃̅̓̄̓̆̍͂̆̋͑͆͌̓̂̄̾͒̃̅̍̔͆̂̄̈́̒̐͘͠͝͠͝ ̸̡̨̛̦͙̺̮͉̣͇̻͉͎̟̯̖̩͙͔̺̦͍̬̜̺͎͚̥̩̣̜͚̠͈͔͔̂̊̅͛́̅̓̓̐̉̓́̍̀̆̎͒̍̂̐̃̽̅͛̈͑̂́̂̔̽̈͆͊̐͜͝͝͝͝͝͝ͅ ̴̢̢̡̪̙͎͍̯̳͈̩̥͓͕̮̻̞̼͕̯̙̮͎̬̤̟̣͙͍͙͇̺̖̥̞͍̪̟̺̬̲͉̩̘̿̉̿̉͠ͅͅ ̷̧̡̨̛̜̮̱͇͕̺̦̼̬̻̰̫̰͙̜̫̟̙͖̹̿̓̂̏̽̈́͜ ̷̺͖̭̹̙̬̈̽͐̎̓̂̔̉̍̇́́̾͒̔̒̍̂̉͋̈́̆̀͛̈́́̅͒̔̏͆̑̊̅̃̃͘̕͝͝ ̴̨̡̛͖̤̭̙̝̱͔̖͇̦̞̤̱̼̩̜̞̲̠̯͔͍̫͓̖͕̃̈́̄͊͆̍̋͋̀̒̇́͗̍̾́̄̀̓̈͛͋̈́̀̿̀͐̄̊̉͌̑͊̌̃̋́͑̆̈̃̀͋̄̆͝͠͝ ̴̰̼̰̪̻̬͚̪͙̪̘̞̘́͋́̄̈́̈̓͆͆́͂̑̇͆͐̈́̏̈́̐͌̈̒́͊̀̒̌̕̕͝ ̷̡̻̺͇͇͓̯̮̣̜͎̺͎̩͇̫͓̝̥̼̞̺̼̞̳͚͈̞̖͖͓̫͈͔̘̯̎̈́́̏͒̃͒̒̿͋̽̓̈́̓̃̄̚̕(̶̧̡̧̧̘̪̥̭̤͓͈͚̹̜̯͔̗͙̆̔͒́͂̏̅͛̔̉̑̓͒̍̓̽̎͊̅̕̚͠ͅ8̷̧̛̛̱̳̗̱̘̤̞͉̦̻̖̣̰͔̦͇̇̂̾̂́̆̅̇̓̑̈́̈́̌̒̉̇̿̈́̒ͅ)̵̧̢̧̖̙͍̲̼͈̱̯̞͕̺̣͇͔͖̰̝̪̩͍̠̺̯͎̼͎̤̞̥͖̪͙̞͈̤͚̻͕̝̅̎̾̏̏̐̓̂̍͆͗͊̐̊̇̎̐̑̅͋̈̐͑̾̃̅̾̽͋̂͌͜͝͠͠͝ͅͅ ̵̡̨̨̢̛̤̥͕̜̹̥̦̟̤̺̯͙͈̗͔̘̞͙͓̱͓̪̮̤̣̰̘̖̬́̏̌͌͋̈́͒͌͑̓̄͊̏̽̀̓̍̄̎̋̔̌͋̓͛̐̒̒̐̎̋͗̉͒̄̽̎̕̚̕͝͝ͅͅP̸̧̨̧̛̛̪̘̫̻͓̮̜̦̖̟̪̪̱͓̬̪̹̘̙̺͍̣̲̙̳͉͔͓͎̈́̈́͒̈̏̇̾̇́̎͆͒͂̆̊͋̒͝͝͝ͅę̸̨̧̨̖̖̫̹̲̻̗͔͚̘̺͚̮͆͜͝ͅa̶̢̢̨̧̫͈̩͓͍͙̼̪͈̯̩̲̠̘̟͇̣̽̓̿̇͋̉̈͊̒͝ͅc̸̨͕͉͚͚̰̗̭̻̼̤̜̝̱̪̖̠̠͈͖͕̫͎̗͙͖͂̒͂͋̈́͑̄̀̋́̈́͗̓̂̀̃̾͊͑̏̇͂̋̍̾̓͐̂̋̿̽̑̐̕͘͘̕̕͜͜͝͝͝ͅế̸̡̢̡̢̡̧̧͓̤̹͔͕͇̠͇͓̺͙͇̦̳̯͇̝̤͈̯̝̟̩̼̜̻͖̱̞̩̙̭͉̭͉̲̮̰̜̔͂̓͗̄̾̎̽̍̀͒̾̈́͌̽̈͑̔͊̌̀͌͐̀̏̀̽̈̎̋̈̎̃̋̈́̐̍̆̋̏͘̕̚͜͝͠͝ͅͅ ̶̧̧̧̧̡̝͇̲̻̩̹̞͇͙̮͈̥̹͚̞̯̰̫̣̪͓̲͖͖̙͓͎̞̬̲̳̉͂̽͗͜ͅT̶͎̦̘͂͒̈̓̅̿̏̑̍́͌͑̀̔͑̓͒̾̊̾͂̓͗͒̀͒͆̕͘͝͠r̴̨̛̯̋̍̈͌̊͋̈́̽͛̏̒̍̏̆͋̿̈́̿̕͜͝͝͠ẽ̸̙͓͖̺̬̺̱͎̮͎̣̀̏̇͂̀̋̔̀̾̈́̓́͛̉͗̀̎̈́́́̐͐͆̑̉́̂͌͊̆̓͘͘͜͝͝a̷̡̨̨̝͖̼̰͓͕̦̗̙̜͚̥̻̺̩̜̓̀͂̈́͑̒̀̈̉͒̉͒̽͆͂́͆̔́̐̆͘͠͝t̷̢̢̧̡̜͕̬̠͖̙̰͇͇̰̭̼̮̗͚̣̤̬̥̺̪̗̓͛̇͋͆̑͊͒͝͠ͅy̴̧̧̛̺̼̻͚̗̠̙̖͈̺͙͓͎̞̻͔̯̭̗͎̺̟͙̭̱̟̰͈͚̟̤̘͙̙̼̝̮͆̾̊̓̓̉͂̑͋͆́͋̈́̓̌̽̽̈̎͑͑́̒̅̅̿̔̂͌́̃̿̚̚̕̚͜͠͝ͅ
                                ̶̢̗͔͚͙͔̲̰͈͕̲̯̟̟̣̠̝̤̞̙̋̀̍̈̌͊̀̅̓̀͗́̽̅́͐̈́͒̈̋̒̿̌̈͌̔͂͆̕̕̕̚̕͝͝ ̸̨̧̧̬̬̲̝͔̜̫͇̬̜͍͎͈͖̼͙̣̐̅͛̀͆̓͜͝ ̴̢̧̧̢̡͖̝͇̮͓̟̻̘̲̳͎͎͚̩̜͈̭̖͓̤̞̣̪̙̺̳͕̭̮̱̗̺̩̥̫͔̼̟̹͉̜͕͒̂̓͗͌͂̌̇͛̐̿̈́̐̂̒͐̓̿́́̾͑͂̐̎͊̌̊̈͒̚̚̕̕͝͝͝ͅ ̶̢̡̢̡̡̜̩͙͈̜̭̪͍͔̮͖̼͉̹̹̗̞̞̻͈̣͎͕͇̘̗͉̯͈̝͓͇̻̭͍̯̭̖͇̽̓̀͒̆̇̔͑̍̾̾͋́͐͛̑̒̐͊̇̍̎̉͗̄̃̀̀̄̾͋͌̾̑͛̃͜͜͜͜͝͝ͅͅ ̸̢̡̨̛̻̺̞̭̻̗̮͎̟̻̠̲̲̺͉̬̰̭̱̳̟̮̳̤̹̗̘̬̱͇̣̅̀̚͜ ̷̢͇̱͈̜́̆̈́̅̒̌́͒̈́̉̏̔̈͋̔͒͛̎̐̋̉̆̔͊̋̎̍̌̊͛̃͌͐̎̂̍̊́̐͒̚̕̕͝͠͝ͅ ̷̢̡̭͎̹̺̠͓͎̝̓̐͌̽̋̆̽͐̅̔̑͋̈́̏̌̌̑͌̄̈̀͛͐̍̅̋̃͑͜ ̵̢̡̛̣͕̩͚͍̜̜̮̫̮͍̤̪̹̰̳͉͍̟̥͕̣͎̼͍̯̭̜̥͓̠̳̗͖̫̱̱͚̩̿̿̊̒̍̌͒͜ͅͅ ̶̡̛͎̪̖̟͙̟̝̹̠̥̩̀͂̈͛͊͑̏̍̓͆̾͋̉͗̈̈̈́̐͋̊̈́͜͝ ̶̛͇̜͚̖̤̃̅͌̾̀̂̌̓͌͂͗̄̋̆͌̈́́̇̄͛̀͒́̚͘͜͠͝ ̷̡̣̥̳̯̖͎̟̬͆͛̋̾̐̑͊̌̈̌̀͗̉͝ ̵̧̢̡̧̢̧̪̮̩̹̲̫̺̳͉̲̬͙̜̩̘͖̩̮̩̩̮̯͇͍̤͈̣͓̟̩̫̗̠͔͎̇̈́̐̎͆̿̿̑́̂͂̇͋͗̐̂͒͋͊̾͛͑̏́͛̄̀̅͊̚͘ͅ ̵̨̡̡̟͇̪͎̜͍̜͇͚͚̲̮̹̎̏̈́̎̄̀̈́̀̿̿̅̔̌̀̀̇̍͘͘͜ͅͅ(̵̨̨̢͖̤̠̬̝͉̤̘̼͕̯̠̟͕̦̗̭̲̥̬̠̗̼̖͙̹͍̻̜̬̞̮̞̺̯͓̝̭̖̯̳̰̠̤͑́͜ͅͅ9̴̧̢̨̩̮̲͉͙̯̬͉̱̣͎̟̞̬̰̻̘̳̱̬̰̝̠͚̜̗͓̩̫͙͍̲̙̤̩̟̂̌̈́͜)̵̢̢̧̛̩̣̪̪̭̜̬̪̣̖̻̥͕̫͎̼̖̪̻̖͓̘͖̭̪̘̬̎̇̾̂͑̽̄̓̌͌̏͐̒̔͑̀̏́͒̔̂̆̊͗͒̉͗̅͂̓̚̕̚͜͠͝ͅͅͅͅ ̴̨̡̨͚̱̦̘̣͍̫̲͚̭̪̟͈̞̲̩̞̞̟̬͖͚̼̖̠̮͕̙͓̱̺̖͈̪͇̜͓͇̣͇̻̙̒̓̉̂͛̔̀̅̋̒̄́̕͘͝B̴̡̤̻̥̭͍͍͚̝͍̹͕͙̺̭̣̪͉̮͇̯̠̣̗̌̾̒̐̈́͐͒́͒̒̋̋̊̇̒͋́͊͊͊̄̆͝͝͝͝͝ơ̷̝̟͖̹͊͛̑̅́̓͆̿͗́̔̋͊̅͌̐̆͛̓̅̄̈́̇͆̅͋̌̃̓̉͑̑͘̚̚͘͘͝͠͠͝͝ổ̷̪͓̱̘̹̝̤̙̗͔̝̏̓͐̓͐͊̀͂́̈́̒́̄̿̍̋̽͒̌̇̄̇͆̈͛̿̈̌̇̀̉̈̈́̾̕̕̕̕͠͝k̴̡̧̨̨͍̙̥̼͇̞̰͖̖̦̙̰̖͎̩̻̺͓̞͔̥̠̼͈͈̥̙̝̰͎̰͓̰͔̊̓̿̈́̂̑̚͜͜ͅ ̶̧̨̧̨̼̹̲͔̭͕̗̟̠̰̩̯̬̪͓̥̫̺̬̼̺̜̤̹̹̱̭͉̻͕̩̖͙̬̺̰̳̻̲̫̯̓̍̎͛́͌͗͋́͂́̓̀̐͠͠ͅǫ̸̧̛̛̣͚͎̥͔̣̥̘̱̲͛͂́̔͂̏̔͐̆̑̍̈̄̅͗̋̂̆͛̾͊̂̈́̈́̓̔̓̂͐̄͆̂̌̆̈́̇̅̕̕̚͘̚͘̕͘͝͝f̵̛̛̛͚̋̅̏̇̒͐̎̈̈́͊̌͗̇̀̐̾̚̚̚͘͝ ̴̨̰̰͍͙̮̜͚̲͋̈̊̀̈̊̌̈͊̍̓̎͛̑́̃͒̈́̈͌̆́̓̓̈́͒̓̔͐̾͆̍̓̐̊́̄̔̍̇͌̎͑̀͋̕̕͜͝͝͝Ķ̷̢̨̡̨̹̺͙͙͚̙̜͎͇̰̺̜̯͖̠̘͈̠̝̖̮̪̭̞̱̙̯͔͖̖̯̪̬͓̹͖̗̠̰̜̅͛́̀̃́͗̇̿̑͐̈́͋̈͛͊́̄̃̈́̓́̄̍̕̕͘̕͜͠͝͝͠͠͝n̵̢̨̢̨̡̡̛̰͍̝͇̻̘͚͈̻̩̦̰̣͍̠͎͓̺̞̩̝̫̘̱̳̮͎̗̄̾̍́͌̓̉̀́̐̔̅̿͛͑̌̅̑̈́̏̈̓̐̕̕͝͝ͅͅő̷̢̡̤̔̑̈̒̋̆̎͑͛̂̍̂̒̉̏̍͋́͘͘͘͠͝͠͠͝͝w̶̛̛͐̓̈́̐̒̔̓͐̉̉̅͌̅̿́͒̀̋͆̽̊̉͌̊̍̈̎̔̒̊̊̅̇̇̎̕͘̕͝͝ͅļ̴̟̞͍̬̙̰̦̖̰̥̬̮̙̱̹̤̮̥̦̟̤̻̖̼͖̳̼͖̠̺͖̗͉̐̄̈́̒͗͊͂̄̆̅̏͆̎̏̀̀̾̀̓͜͝͠ȩ̶̧̧̛̥̥̙̦̝̖̫̟̠̟̺͚̮̻̻̪͇̗̬̘̥̼̪̪̱͎͇̦̔̒͌̄́̓̆͌̏͒̎̃͐̊͂́̉̃̕͝͝ͅd̷̨̨̨̡̘̼̞͉̳͔͙͎̙̜̖̣̪̰̺̳͉̜̮̳̞̮̙̫̥͍̪̥͍̩͕̯̩̪̗̱̽̈͋͐̔͂̌̄̈́̒̽̄͛͋̽͛̇ͅͅg̵̢̡̧̧̹̯͕̙̪͖̩͚̟̘̬̙̻̰͇̰̳̺̝̻͕̮̞̈́͐̓̄̂͊̽̊͊̊͒̍̈́̽͗͘͘̕͜͝e̵̛̛̻̮̹͇̰̺͚͕͈͓͐̀̄͊͛̿̅͆̄̀͐̓͐̽͗̂̃͗͆̾̓́͆͌́̅̄͘͘̚͜͜͝
                                ̷̛̘̭̺̳͙̩̅͆̅̔̄̓̌̍̔̒̈́̋̎̈́̈́̚͝͝ͅ ̷̢͙͕̭̝̤̝̺̗͉̼͈͍̩̝̯̲̠̻̤͕̻̦̖̫̻̬͓̬͉̈͒̃͐͑̔̍̏̈́̃͊̆̈͋́͑̀̀̃͘ ̸̨̧̧̛̭̞͉̼̟̪̦̲̼̥͕̘͉̳͍̝̙̱̘̫̗̤͖̦̦͚̞͙͇̝̭͉̘̃͑͗̓̈͂̓͋̔̊̑̈́̅̃̀̀̈́̈́͐̔͒̇͑͐́̅̊͘͝͝ͅͅ ̷̢̛̮̯̳͙͙̖͍̦͙̹̥̗͉̳̬̤̜̣͕́͛̽̆̋͂͊͊̃̉͐̍̌́͊͌̈̋͌̀̆́͊̈́̑̓̆̆͝͝ ̶̧̛̮͓̘̝̰̗͇͔̻̲̮̪͚̮̘͔̫̙͈͖͇̙̱̖̇̈́̇͊̉͗̒̽͋͘͘ ̵̨̛̟̲̣͕̬̞͇̝͈̫̼̮̳̹̭̼͖̣̩̪̙̫̻̭̥͓̘͇̱͓̋̓̏͆̈̅̏̐͗͗̊̀̃̐̏̎̀͗͌͋͋͂̍̈́̾͂͆̃̽͐̿͒̌̈́̊̌͊͋̈́͘̚̕͘͠͠͝ ̶̧̢̢̧̛̛̤̰͇͙͇͔̣̤͕̱̭̱̬̠͕̯͎̝͚̩̣͇̦̪̗͕̹͉̹̟͚̪̘̤͎͌̆͑͋̈́͛̐̇͋̉͛͋͋̄͑͒̋̾̈̉̆̀̑͐̾̀͗́̀̇̇̋͘̕̚̚͜͝͝͠ͅ ̸̪̪̲̜̭͇̦͚̼̳̙̣̥̼̳̱̹̣̬̲̊̀͌͑̐̈́͗̈́̒̏͆̍̑̚͘̕͜͠͠͠ ̸̧̧̧̨̧̡̟͚̼̟͍̫̜̱̖͔͈͖̮̜̟̜̥̝͉̺̘͚̠͖̙̞̼̗͙̳̼͔̠̜̭̙̤̩̖̦͊̌̊̍̓̽͋̀̀̒̊̓̈̐̏́̿̂̏̆̃͗̆̓͜͝ͅͅ ̵̗̹̟̦̠̬͈̺̦̝͖̯͓̎̐̀͌̊̓͆͛̅̀̎̀̏͗͊̇̎̚͝ ̸̧̢̛͙̝̮̰̣̠̖͔͙̳̞̣̩̖͕̞̯͇͍̥̯̲͇̰͕̘͙̲̞̔̐̆̾̿͊͌́̀̌̊ ̷̛̛̬̱̍̓̽̆̿͑̃̃̐̌̅̃͊̒̒̄͋́͐̑̐̚͠͝ ̵̡̢̢̢̰̥̤̙̠̰̖̻̞͚̮͓̪̰͎͎̞͍͚͕͖̞̪͕̦͍̘͈͎͙̯̗͕̟̬̘̩̬̄̾͐̄̋̽̊̈́̆̏̄̏̋̓̀͂́̀̆͌̓̽̎̊̂̿̈̌̓̈́̆͗͘͘͜͠͠ͅͅ(̶̦͓̠̯̹͇̝̱͑̒̇̎͂̇̀̓̋͜͜͝1̴̨̛̪̱͍̠͇͈͚̬̖̘̻̤̻͎̠̘̱̗͍̘͎͆̈́̽͌͗̕0̷͕̎̅̏̽̈́͐̀̂́̏͛̏̏̑̔̎̍̋͒͒͘͠͠͝͝)̷̨̛̛̬͕͖̹͉̝̥̐̄̋̉̃͑͊͐̉͠ ̶̡͖̙̈́͒͂̔̏̏Ţ̸̡̢̡̡̺̞͓̬̮͇̳̳͚̥͍͓̗̝̩̙͈̖̺̣̠͖͉̻̼̞̖̮̲̹̜̭̗̮̦͎̹̩̰͕̰͍̰̊̂̅́̑̀̓̊͌̏͑̇̽͗̈͊̊̅͒̑̒̓r̶̡͓̻͍̝̩̰̦̝̲͖̲̖̖͖͎͇̠͔̼̜̬̥͍̙̣̟̜̱̳̥̲͍̗̀́̌̿͒͋̆͘ͅa̵̡̨̢̛̮̯̤͔̟̝͉͈̯̟̱͍̮̣̤̪̲̠̘̺̰̪̤̻̙͔̖̬͔̼̗̹͗̄̄̅̔̍̓̐̓́̀͂̾̈́͐̍̀̌̇̐̔̌͛̍̒̓͂͆͠͝ͅͅͅͅd̵̛̛̛̝̘̠̞͂̔̀͛́̿̌̃̌̎̏̈̑̋̐́̿͒̃͛̍̏̆̐́̔̐̈́̇̐̀̋̆͘̚͠ë̴͕̝̤̹̯̞̙́̈̊͊̈̓̽̅̓̈́͗̈́̍͜ ̵̢̢̛̹͈̻̩̩̪͉̹̣̦̫͚̮̙͙̜͚̭̑̄̒̓̈̅̀̀͋̅̈̇̅͜ͅw̵̨̹̺̪̜͚̯̟͕̗̗̙̘̣̩͍̣̯̬͐́̊̈́̅̂̊͂͛͋̈́͐͒̎̎̑̊̀̃̀́͒͗̍͝ͅͅí̷͔̳͕̮̝͕͓̥͎͜ť̸̨̢̨̧̨̢͍͎̣͔̬̹͎̥̭̯̠̳̘͙̬̱͎̤͙̮͔̺͔̹̭͈̮̦̲͓̮͙̭͚̪͖͈̮̖͉͊͆̌̋͑̊̈́͘͜͜ḩ̵̡̨̰̯̣͙̤̙̪̮̜̺̯̟̝̺̟̮̦̼̪̖̭͕͇̗̦͕̗̗͔͊̀̃̇͑̀̕̕͜͝ͅ ̷̨̡̡̨̨̞̯̖͎̪̭̥̟̠̟̩͉͓̠͕͚̹͖̘̠͙̪̰͇̳̗̦͕̭̘̹̲̥͕̯͕̘̝̺͙̺͛̽̉͛̆̅͐̂̈͋̔̆̄͋̂̈̏͒̽̑̄̓̒͊̊̉̋̆̌͜͠͝͠ǫ̴̡̢̢̡̢̗͙̖̥͓̘̗̹̠̥̣̹̟̟͙̖̳͎͙̱͙̤̘͍̻͙̟̺̯͙̮̰͙̳̑́̃̅͐͐̂̏̊̎̒͒̄̀̇̔͌͋̎̇̚͜͜͠͠͠͠ͅͅẗ̸̢̡̡̢̢̢̛̛̘̗̟̳̦̤͙̤͍̺͖̲̫̟͈̟͍̮̰̠̱̯̮̞̗͇̩͕̣̝̠͎̻͍́͗̂̀́͗̀͐͜͜h̸̡͇͇̦̫̬̫̹̦̰͙̼̫̺̝̱̼͕̱̪͇͎͉̝͎̹͎̞̖̤̙̟̆̋̉̍̊̊̈̽̈́̅̎̃̓̀̅̐̑̾̆̃͗͋̂̍̀͐͘͜͠ͅę̵̡̧̡̠̥͓̟̹̖͎̺̤̤̰͕̦̗̘̦̫̫̗͓̖͉̗̥̼̬̻̙̰̮̙̩̞̦͖͓͓͖̰̭̫̅͒̈͆̇̌̉͑͠ͅͅr̴̨̢̢̧̯̖̹̝͇͍̝̪̩͙̜̠͉̣̤̣̟̝͚̫̜͕̲̥͉̩͍̠͊̓̉̋̄̈̄͑̓̎̆̈́͌̈̎̐̈́̈̈́̑̽̌͑̀͘̕͘͜͝͝͝ ̵͍̳̣̪̼̳͈̤̦͍͉̹̲͇̟̝͓̉͊͊̏͌͊͑͋̈́̋̓͛̀̀̓̒͒̂̊̏̃͠k̴̨̛̪̤̜͔̳̹̜̤̘͌̇̎̏̃̐͌͐̐̊́͐͋̀̓͋̐͛͘ĩ̶̧̡̛̛̛̥̱͍̳̺̫̦̤͚̹̜̖͇̝͇̯͓͕̩̩̲͓̬͕̣͓̥̦̞̬̻̥̟̋͌͊̓̎̆́̏͑̀̉͐͋̈́̿̎̋̆̄̔̐̇͒̀̂̔̿͂̎́̈́̀̾̑̕͘͝ͅͅͅͅn̶̨̛̝͚̫͇̜̼̝̘̻̣͐͋͑͜͠͝͠g̴̥̪͎͓̫͉̹̱̻̯̟͓̰̩̼͓͆̾̒̈́͗͂̀͊̇̎̒͂̐͛̆͠͠d̷̞͔̾̀͌͌̓͗̒̅̎̇́̒̈́̈́̃̃̇̓̓͛͛͛̓͘͠͝͝ơ̵̤̮̫͈̞̳̺̙̬̠͒͗m̵̨̡̧̨̡̼̱̬̪̱̮̩̝̠̙͍̝̲̗̣̤̳̪̬̝̱͖̝̲̭͙̹̝̻̤̲͇̣̜͓̥̘̟͇̤̈́̒̐̂̅̓͂̔̆͛͜͜͠ͅͅs̵̡̡̡̧̛̳̲͓̞͓̟̫̻̟͚͙͍̫̠̗̭͚̪͛̃̈̅͌̅̉̿̃̃͑͋̔̇̀̏̕ͅͅ
                                ̶̡̛̦̞̟͍̲̩̫͕̿͒̇̑̑͐́̃̅̐̓̑͗̌̕̕͠ ̷̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝̋̈́́͂̐̇̊̑͋͒͑͐̾̈̑́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄͘̕̚̕̚̕͜͜͜͜ͅͅ ̷̨̛̛̛̝̥̩̫̜̰̘͓̠̖̼̯̊̉̐͂̊̅̌̈́̇̈́͐̈́͛͂̂̌̀̅̄̋̀̉͆̎̽̀̑̎̌̌̚̕̚͠͝͝ ̶̻̬̺̞̫͚̲̙̠̬͓̬̰̫̜̦̗͖̦͔̥͔̺̒̈́̽̈́̈́̌̂̇̐̀̀̂̀͒͋̅̈́ͅ ̷̡̧̣̖̝͚͈̣͚̫̮̱̼̳̫͖͚̖̼̤̟̟̱͉̤̹̖͈͍̻̩̥̮̈̊͑́̀̒̽́́͗̈́̈́͑̒̈́̅͒̎̇̈̍̎̈̓͗̈́͗̀͆̽̈́̕̚͘̚̕͠͝͠ͅ ̵̨̡̛͈͓̱̪̣̠̖̼͍̮̻̯̫̟̠͕̻̗̳̤̠̎̌̌̑̿̿̈̇̆͊͒̓͛͗̉͋̽́͑̀̒̃̎̔̂̇̊̂̿͗̾͗̑̿̍̔͛͗̓͠͝͠ ̸̢̨̡̢̛̰͎̖͇̦͎̩̲̹̼͚̳̞̣̝͙͖̱͎͎͇̜̟͈̣͖̰̺̼͉̬̘̜̭̖̗̤̲̔̀̈̋̂͆̊̐̓̊̓͛́̍̀͗̂́̒̅̃͒̽̀́͒͋̽̏̕̚͝͝͝ͅͅͅ ̷̩̜̤̥̼͖̎̏̆͒̃̀̈̾̈́͐͌̔̂̽̑̃͊̄̃͛̓̏͛̕͘͠͝͠ͅ ̸̢̲͉̻̪̞̲͓̤͓̻̤̬̮̫̞͔̰̰̞̗͖̣̙͙̙͚͇̭̪͉͔̳͙̠̭̭͔̠͕̤̟̩̱̱̪͚̗̓̿̌̈͑͌̔̒̾͋̈́̽̿͐̄͗͑̑́̐͌̆̽̈́̍̀̿̚͜͠͝͠͝ ̵̨̡̛̛̣̮̮͓̣̼͚̹͙̙̰̪͎̈́͂͋̾̀́̃̀̏͑͆̈́̏̎̇̿̿̄̀̈͂̿̀̏̏̈́̎̒͆̑̏͂̈͐̕͘̕͘̚͝͝͝ͅ ̶̨̡̡̛̛̹̬̗͍̜͈̫̙̬͉̪̯̦̜̲̞̱̬̖̫̳̜̙̜̯̈́̇̑͂̉̋͋̅͛̂͗̀̈͒̋̕͝͝ ̴̢̢̺̠̣̠̪̯͕̱̰͚̗̰̮̖͖̝̖͓͇͕̼̥̗̬͉̗̦̝͎͍̺̯͍̥̪̥͙̫̦̰̩̝̫͒͆͋̈̄́̋̾͗̽̍͊̈́͊͋̄͂͑̆̆̀̓͘̚͘͘͜͝͠͝ ̴̧̞̩͎̻̫̖̹̹̝̬͈̠̬͇̥̜̠̍̀̅̆͑͘͜(̶̢̲̦̙̘͉̳̺̪͎̤̲̟̮͍͇̫̼̺̗̫͚͚̩̺̲͖͓̹̪̲͓̃̋̓̓͂́̈́̑̾́̆͒̍̐̔͊̓̔͂̉̏̚͜ͅE̵̢̧͎̰̙͕̬̮̼͚̟̝͓̟͉̳̳͓͚̥̝̣̤̲̦͙͍̻̜͒͜͠ͅͅͅļ̶̛͉̙͚͇͙̬͕͙͈̩̹͙̬̀͐͆͆̈́̄͌̔̌͌͆͛̎̑͑̓͆̈͛́̈́̏̽̀͛́̃̐͐̓̽͊̓̚̕͠͝s̵̡̨̡̮̙̦̩̩͚̗̩̻̳̻̫̦̫̺̠͙̮̓́͂́̂̄̀̋͆́͐͋͠ͅͅe̶̡̧̡̠͔̳̮̬̖̝̗͍̳̹̝̗͙̯̻̘̗̪̱̳̲͉̻̫̟̣͇͓͉͍͗̇̊̉̃̆͂͆̈́͂͝)̸̛̛̛̛̮̼͓̣̪̻̲̤͚̳̲̥̳̱͎̩͙̋͑̈́̅̀͌̍͌̒͊̔̾̅͆̓̇͐̐̈́́̆͌̑̈́̐̾͜͝ ̶̡̧̧͙̣͇̲̳͈̠̣̼̟͙͙͇̺̜͒̏̍̄̂̆͛̎̂̀̓̎̈́͐̀́̐̋̀̈́́͒̒̂̅̀́̇̌̑͋̒̄͊͐̈̂̕̕̕͘̚͜͠͝͝͝ͅͅḐ̸̨̡̘̳̼̥͈̲͎̩̪̤̺͙̰̙͉̼͙͖̀̒̂͐̕͜͠͝o̷̻̦̬̺͌̀̊̉̄̈̎̉̑͌͑͋̂̐̈́̽̔̈́͛̏͋̆̊͘͘͝ ̴̢̨̛̲͙̞̬̪͍̰͖̭̺͙̫̺̯̟̙̤͍̜̹̲̙́̒̐̓͛̍̃̈́͊͊̂́̍̎́̇̄͗̓͊̒̍͗̔̔̽͒̔̀̓͒̽͌̌̉͋͗̚̚͝͝͠ͅͅń̴̨̡͔̟̩͙̘̞̱̬͈̜͕̘̫̦̼̼̪̭͍̜̦͔̞͓̯͔̣̹̼̜̫͈͙͍͉̭̿̉̑̑͐̀͗̔̎̅̑̃͊́̈̇̔̓̌̓̓̔̿̕̚ͅò̴̢̢̨̗̦͇͓̳̖̥̻̫̥̪̼̪̘̣͎̘̗͈͖̬̮̮̟͍̺̍͛́̔̄̍̽̏̀̽͂̈́́͐̉͋͑̂͑͗͋̕̕͝ͅt̷̛̹̮̝̠̜̪̞̲̜͖͍̮͉̜̜̞̦͉͙͇̗͎̠̞͇͖͉͓́͋̿̅͋̀̊͛̈͆̈́̉̈́͌̄̓͐̄̈͆̿̄͋̔̐̀͑̈̍͘͜͝͝ḩ̵̣̘͉̺̬̞̩̤̺̞͚̟̼̟̮͚̦̽̃͗̌͑̄͂̄̒̉̿̅̅̂̌͜͜͝͝ͅi̷̡̢̡̧̨̗̟̜͕͓̬̯̼̱͕̖̖͎̞̳̙͚̝̙͛̉̌͆́ņ̸̛̱̦͚͔̮͕͓̣͕̦̤͕͓̣̙̬̜̍̑̓̌̀̋̎͋͋̃̄̂̂͌̔͗̅̎̋̚͝͝g̴̡̨̭̬̟̜̦̞̥͇̐̃̀̈́̄̎̇̃̉̐̑͗͊̑̓́̚͝͝͠͝ͅ
                                ̷̢̧͖̦̼̼͈̟̩͕̳̣̪̳̬͚̬̺̰̰̹̲̺͚̭̤͔͚̣̭̳̭̻͖̻͚͔̺̝̫̼͎͔̺̂̀̇͊͂͊͊̃̂ͅͅ""")
                Action = input(">")
                if Action == "1":
                    print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                    buildchoice()
                elif Action == "2":
                    print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                    buy()
                elif Action == "3":
                    print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                    invade()
                elif Action == "4":
                    print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                    stats()
                elif Action == "5":
                    print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                    Hire()
                elif Action == "6":
                    print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                    settings()
                elif Action == "7":
                    print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                    upgradetroops()
                elif Action == "8":
                    print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                    peace()
                elif Action == "9":
                    print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                    help()
                elif Action == "10":
                    print("̧̡̡̢̛̹͔͕͚̖̹͇̼̞̟̱͙̬̳͖͍̟͔̮̩̙̟͉̥͓̝́̅͌̓̅̀̓̌͋́̍̐͆̀̓̿̄̕̚̕͜͜͜͜ͅͅ ̷̊̉̐͂̊̅̌̈́̇̈́͐̈́͛̚̕̚͠")
                    negotation()

        timeskipvalue["TimeSkip"] = False











