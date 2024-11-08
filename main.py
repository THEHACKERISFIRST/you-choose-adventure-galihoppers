# Variables
#shop idems
from ast import Index

Sword = False
Shield = False
Armor = False
Bow_and_Arrows = False
Spear = False

coin = 350

print("Gladihoppers Choose Your Adventure.\n")


#accept
print("Julius Caesar challenged you to fight for 1,000,000 Gold Coins. \n")
YesNo = input("Do you accept?\nyes or no: ")

if YesNo.lower() == "yes":
    print("Yay!")
elif YesNo == "no":
    print("You died of being sad.")
    quit()

#small shop
print(f"you have {coin} coins what will you buy.\n1.Sword - 250\n2.Shield - 100")
print("Please put the number of the idem")
Buy = input()
if Buy == "1":
    Sword = True
    coin -= 250
elif Buy == "2":
    Shield = True
    coin -= 100
print(f"{coin} coins")

#fight
print("your first fight is with a swords man. Do you choose to \n1.fight\n2.run away\n ")
YesNo = input()
if YesNo == "1":
    print("You won but it was a close one")
    print("you won 200 gold coins")
    coin += 200
elif YesNo == ("2"):
    print("the swordsman caught up to you and stabbed you through the Heart.")
    print("you died")
    quit()

print("Who do you want to fight for you next match. \n1.Maceman\n2.Archer")
One_too = input()
if One_too == "1":
    print("you won but got hit in the leg. +250 coins")
    coin += 250
elif One_too == "2":
    print("the archer was too skilled for you.")
    print("you died. Julius Caesar said womp womp. the croud laughed at your dead body.")
    quit()

#heal or fight
print("Do you heal or fight? -100 coins if you heal.\n1.Fight\n2.Heal")
One_too = input()
if One_too == "1":
    print("your legs failed you and you fell to the ground and cryed to death")
    quit()
elif One_too == "2":
    print("you healed your self but lossed 100 coins from medical fees")
    coin -= 100

#big shop
in_shop = True
while in_shop:
    print("You went to gladiator's Menards.")
    print("What will you buy?")
    print("1. Spear - 300\n2. Sword - 250\n3. Shield - 100\n4. Armor - 500\n5. Bow and Arrows - 350\n6. Leave shop")
    print(f"You have {coin} coins")
    buy_item = input()
    if buy_item == "1" and coin >= 300 and not Spear:
        Spear = True
        coin -= 300
        print("You bought a Spear.")
    elif buy_item == "2" and coin >= 250 and not Sword:
        Sword = True
        coin -= 250
        print("You bought a Sword.")
    elif buy_item == "3" and coin >= 100 and not Shield:
        Shield = True
        coin -= 100
        print("You bought a Shield.")
    elif buy_item == "4" and coin >= 500 and not Armor:
        Armor = True
        coin -= 500
        print("You bought Armor.")
    elif buy_item == "5" and coin >= 350 and not Bow_and_Arrows:
        Bow_and_Arrows = True
        coin -= 350
        print("You bought Bow and Arrows.")
    elif buy_item == "6":
        in_shop = False
        print("You left the shop.")
    else: print("Invalid choice or not enough coins.\nor have that idem")
print("you miss your family and want to see them again. 1.See them 2.Keep fighting for them\n")
One_too = input()
if One_too == "1":
    print("you spent time with your family and lived happly ever after with them. you lived to the age 69.")
    print("You died a good death.")
    quit()
elif One_too == "2":
    print("you push on and keep fighting for the 1,000,000 coins")

print("you hear a bang in a ally way. you walk in the ally way and see a shady guy.")
print("he asks you if you want a sus potion. do you take the potion\n1.yes 2.no")
One_too = input()
if One_too == "1":
    print("500 coins apper in your pocket. you thank him and leave.")
    coin += 500
    print("1.Go to gladiator's Menards 2.go to next fight")
    One_too = input()
    if One_too == "1":
        print("you trip on a candy wrapper and get stabbed by a tree")
        print("you died by a tree. tree kill count 99,999,999,999 + 1")
        quit()
    elif One_too == "2":
        print("you leave and to to your next fight. your next fight is with a lion.")
elif One_too == "2":
    print("you leave and to to your next fight. your next fight is with a lion.")

print("when you fide out that your fight is with a lion you get scared.")
print("1.Bribe the guards to not fight for 50 coins 2.keep fighting while you are scared")
One_too = input()
if One_too == "1":
    print("The gards take you up on this deal.")
    print(f"when you walk away they stab you and rob you of your {coin} coin's")
    quit()
elif One_too == "2":
    print("you choose to man up and fight")
    print("you end up wining the battle and gain 150 coins")
    coin += 150
    print("Julius Caesar thought you paformance was wonder full he offers you 100,000 coins to retire.\n1.keep fighting 2.retire")
    One_too = input()
    if One_too == "2":
        coin += 100000
        print("you retire and get to ive happly ever after with a net worth of ")
        print(coin)
        quit()
    elif One_too == "1":
        print("you chose to keep fighting for more monney")

print("you see a rich man and see that he drops a bag of coins.\n1.return it 2.keep it")
One_too = input()
if One_too == "1":
    print("the rich man thanks you and gives you a chest plate and the bag of coins with 250 coins in it.")
    Armor = True
elif One_too == "2":
    print("the guards see you take the money and kill you on the spot.")
    quit()

print("your next fight is with a archer.")
print("the archer shot you but you survived and just played dead. after everyone left you drank a potion to heal you.")

print("your next fight is in a maze")
print("do you 1.climb the wall and out smart the game meaker 2.go into maze")
One_too = input()
if One_too == "1":
    print("you climb the wall and die from the wall eating you.")
    print("you died")
    quit()
elif One_too == "2":
    print("you go through the maze and see shrek running to the center")
    print("1.kill shrek 2. best friends 3.run form shrek 4.sacrafice your self for shrek 5.all of thee above")
One_too = input()

if One_too == "1":
    print("you try to kill shrek but shrek releases donkey and kills you.")
    quit()
elif One_too == "2":
    print("you decide to dich your family and become best friends with shrek.")
    print("shrek gladly accseps")
    print("both of you win because of ceaser loves friend ships. 300 coins")
    coin += 300
elif One_too == "3":
    print("you try to run but shrek releases donkey and donkey anoyes you to death")
    quit()
elif One_too == "4":
    print("you sacrafice your self for shrek and that is how shrek memes where a thing (good ending)")
    quit()
elif One_too == "5":
    print("you do all of thee above. best friends, then try to kill shrek, run from shrek then sacrafice your self form shrek")
    quit()

#shop
in_shop = True
while in_shop:
    print("You went to gladiator's Menards.")
    print("What will you buy?")
    print("1. Spear - 300\n2. Sword - 250\n3. Shield - 100\n4. Armor - 500\n5. Bow and Arrows - 350\n6. Leave shop")
    print(f"You have {coin} coins")
    buy_item = input()
    if buy_item == "1" and coin >= 300 and not Spear:
        Spear = True
        coin -= 300
        print("You bought a Spear.")
    elif buy_item == "2" and coin >= 250 and not Sword:
        Sword = True
        coin -= 250
        print("You bought a Sword.")
    elif buy_item == "3" and coin >= 100 and not Shield:
        Shield = True
        coin -= 100
        print("You bought a Shield.")
    elif buy_item == "4" and coin >= 500 and not Armor:
        Armor = True
        coin -= 500
        print("You bought Armor.")
    elif buy_item == "5" and coin >= 350 and not Bow_and_Arrows:
        Bow_and_Arrows = True
        coin -= 350
        print("You bought Bow and Arrows.")
    elif buy_item == "6":
        in_shop = False
        print("You left the shop.")
    else: print("Invalid choice or not enough coins.\nor have that idem")
print("you enter the colssem and tou face the king the one alpha sigma shrek.\n1.commit suicide 2.fight")
One_too = input()
if One_too == "1":
    print("you commit. you saved the pain of fighting")
    quit()
elif One_too == "2":
    print("you fight")

print("what wepon will you use first \n1.sword 2.bow")
One_too = input()
if One_too == "1":
    if Sword == False:
        print("you dont have that")
        quit()
    else:
        print("you attack with the sword and he break the sword")
elif One_too == "2":
    if Bow_and_Arrows == False:
        print("you dont have that")
        print("he stabbes you in the heart")
        quit()
    else:
        print("he deflecs it and stabbs you")
        quit()

print("you charge at him and he throws a spear at you 1.deflect 2.dodge ")
One_too = input()
if One_too == "1":
    print("you deflect it the wrong way killing your self")
elif One_too == "2":
    print("you dodge it")

print("do you attack in the 1.head 2.chest 3.leg")
One_too == input()
if One_too == "1":
    print("blocks you and kills you")
    quit()
elif One_too == "2":
    print("blocks you and kills you")
    quit()
elif One_too == "3":
    print("you stab him in the leg")

print("you stab his leg and he falls do you 1.finish him 2.leave him 3.spare him")
One_too = input()
if One_too == "1":
    print("you kill your best friend and you die sad for the rest of your life")
    quit()
elif One_too == "2":
    print("you leave your friend and give him a pain full death then feona kills you with a panefull death.")
    quit()
elif One_too == "3":
    print("you help him and Julius Caesar liked what you did and made you champion and 1,000,000 coins")
    coin += 1000000
print("Julius Caesar gives you the coice of 1.contining to fight 2.")
One_too = input()
if One_too == "1":
    print("you become the richest man alive with lots of fame")
    quit()
elif One_too == "2":
    print("you retire, what will you do with your money 1.hide it 2.spend it all 3.charity")
    One_too = input()
    if One_too == "1":
        print("you hide your monny in a pace named atlastis and lose your money forever")
        quit()
    elif One_too == "2":
        print("you spend it all and still arent sadisfied.")
        quit()
    elif One_too == "3":
        print("you give all of your money to a charity and die happy")
        quit()
quit()
