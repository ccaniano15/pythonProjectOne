#READ ME
# Puzzle Monster
# Coded by Caden Caniano

# How to play: 
# Open in IDLE and run.
# When a question is posed to a player, a separate window will pop up. Interact with the window to move through the game.





#imports

import tkinter as tk
import sys

#global variables

ph = 0
eh = 0
charaChoice = ""
c = ""
guess = ""

#Button Push Functions

def buttonYes():
    global choice
    choice = "yes"
    root.destroy()

def buttonNo():
    global choice
    choice = "no"
    root.destroy()

def buttonChara(x):
    global charaChoice
    charaChoice = x
    root.destroy()
    
def buttonMoves(x):
    global c
    global ph
    global eh
    c = x
    root.destroy()
    print(c.message)
    eh = eh + c.effectEnemy
    ph = ph + c.effectPlayer
    print(c.damage)
    
def healingCalc():
    global ph
    if ph <= 22:
        if charaChoice == nova:
            x = nova_glitter1
        if charaChoice == billy:
            x = billy_cry1
    elif ph > 22 and ph != 25:
        if charaChoice == nova:
            x = nova_glitter2
        if charaChoice == billy:
            x = billy_cry2
        ph = 25
    elif ph == 25:
        if charaChoice == nova:
            x = nova_glitter3
        if charaChoice == billy:
            x = billy_cry3
        ph = 25
    buttonMoves(x)

def charaMovesSelect(x):
    if x == nova:
        novaMovesGUI()
    if x == billy:
        billyMovesGUI()

def enterGuess():
    global guess
    global root
    global entry
    guess = entry.get()
    root.destroy()

# Pop Up GUIs

def yesNoGUI():
    global root
    global choice
    root = tk.Tk()
    yes = tk.Button(root, text='Yes',command=buttonYes).pack()
    no = tk.Button(root, text='No',command=buttonNo).pack()
    root.mainloop()

def charaGUI():
    global root
    root = tk.Tk()
    novaButton = tk.Button(root, text='Nova',command=lambda *args: buttonChara(nova)).pack()
    billyButton = tk.Button(root, text='Billy',command=lambda *args: buttonChara(billy)).pack()
    root.mainloop()

def novaMovesGUI():
    global root
    root = tk.Tk()
    moveOne = tk.Button(root, text='Elbow',command=lambda *args: buttonMoves(nova_elbow)).pack()
    moveTwo = tk.Button(root, text='Spit',command=lambda *args: buttonMoves(nova_spit)).pack()
    moveThree = tk.Button(root, text='Eat Glitter',command=healingCalc).pack()
    root.mainloop()
    
def billyMovesGUI():
    global root
    root = tk.Tk()
    moveOne = tk.Button(root, text='Stomp',command=lambda *args: buttonMoves(billy_stomp)).pack()
    moveTwo = tk.Button(root, text='Punch',command=lambda *args: buttonMoves(billy_punch)).pack()
    moveThree = tk.Button(root, text='Cry',command=healingCalc).pack()
    root.mainloop()

def unlockGUI():
    global root
    global entry
    root = tk.Tk()
    entry = tk.Entry(root)
    entry.pack()
    enter = tk.Button(root, text='Enter', command=enterGuess).pack()
    root.mainloop()
    
#Character Object

class characters:
    def __init__(self, name, health, desc):
        self.name = name
        self.health = health
        self.desc = desc
        
billy = characters("Billy", 25, "A boy always on the edge of tears. Always in a bright t-shirt and dark jeans. Wears big shoes. Likes to stomp on his enemies.")
nova = characters("Nova", 25, "A glitter girl who wrecks havok. Dyed black hair and long skirts. Likes to elbow her problems away.")

#Moves/Attacks Object

class moves:
    def __init__(self, moveName, message, damage, effectEnemy, effectPlayer):
        self.moveName = moveName
        self.message = message
        self.damage = damage
        self.effectEnemy = effectEnemy
        self.effectPlayer = effectPlayer

billy_stomp = moves("stomp", "You stomp on the enemy!","It does 5 damage!", -5, 0)       
billy_punch = moves("punch", "You punch the enemy!", "It does 3 Damage!", -3, 0)
billy_cry1 = moves("cry", "You stand there and cry!", "You restore 3 health!", 0, 3)
billy_cry2 = moves("cry", "You stand there and cry!", "You restore 3 health!", 0, 0)
billy_cry3 = moves("cry", "You stand there and cry!","Your health is alrleady full!", 0, 0)

nova_elbow = moves("elbow", "You elbow the enemy!","It does 5 damage!", -5, 0)       
nova_spit = moves("spit", "You spit on the enemy!", "It does 3 Damage!", -3, 0)
nova_glitter1 = moves("eat glitter", "You eat a handful of glitter!", "You restore 3 health!", 0, 3)
nova_glitter2 = moves("eat glitter", "You eat a handful of glitter!", "Your health fills!", 0, 0)
nova_glitter3 = moves("eat glitter", "You eat a handful of glitter!","Your health is alrleady full!", 0, 0)

catMonster_bite = moves("bite", "The cat monster bites you!","It does 5 damage!", 0, -5)
catMonster_scratch = moves("scratch", "The cat monster scratches you!","It does 4 damage!", 0, -4)
catMonster_swat = moves("swat", "The cat monster swats at you!","It does 1 damage!", 0, -1)
catMonster_claw = moves("claw", "The cat monster claws at you!","It does 2 damage!", 0, -2)
catMonster_rest1 = moves("rest", "The cat monster takes a rest!","It restores 5 health!", 5, 0)
catMonster_rest2 = moves("rest", "The cat monster takes a rest!","It restores 5 health!", 0, 0)

troll_whap = moves("whap", "The troll guard whaps you with its club!","It does 5 damage!", 0, -5)
troll_slap = moves("slap", "The troll guard slaps you!","It does 2 damage!", 0, -2)
troll_growl = moves("growl", "The troll guard growls loudly!", "It does 1 damage!", 0, -1)
troll_throwRocks = moves("throw rocks", "The troll guard throws rocks! Its damaging and therapeutic!", "It does you 2 damage and restores 5 of its health!", 5, -2)
troll_throwRocks2 = moves("throw rocks", "The troll guard throws rocks! Its damaging and therapeutic!", "It does you 2 damage and restores 5 of its health!", 0, 0)

#Character Selection Function (start of game)

def charaSelect():
    global ph
    global charaChoice
    global choice
    print(":::: PUZZLE MONSTER ::::")
    print("Would you like an explanation of the game?")
    yesNoGUI()
    if choice == "yes":
        choice = ""
        print("Welcome to Puzzle Monster, the adventure game where you fight monsters and solve puzzles!")
        print("Answer prompts by clicking on your response in the pop up!")
    print('')
    choice = ""
    while choice != "yes":
        print("Select a character for their info!")
        charaGUI()
        print(charaChoice.desc)
        print('')
        ph = charaChoice.health
        print("Do you want to select this character?")
        yesNoGUI()
    print("You choose to be " + charaChoice.name + "!")
    choice = ""
    print("")
    print("::::::::::::::::::::::::::::::::::")
    print('')

#Players Attack Turn Function

def playerAttack():
    print("What do you do?")
    charaMovesSelect(charaChoice)

#All Enemy functions

def catMonster():
    import random
    global eh
    global ph
    moves = [catMonster_bite, catMonster_scratch, catMonster_swat, catMonster_claw, "rest"]
    attackMove = random.choice(moves)
    if attackMove == "rest":
        if eh <= 20:
            attackMove = catMonster_rest1
        else:
            attackMove = catMonster_rest2
            eh = 25
    print(attackMove.message)
    eh = eh + attackMove.effectEnemy
    ph = ph + attackMove.effectPlayer
    print(attackMove.damage)
    return

def trollGaurd():
    import random
    global eh
    global ph
    moves = [troll_whap, troll_slap, troll_growl, "throw rocks"]
    attackMove = random.choice(moves)
    if attackMove == "throw rocks":
        if eh <= 20:
            attackMove = troll_throwRocks
        else:
            attackMove = troll_throwRocks2
            eh = 25
    print(attackMove.message)
    eh = eh + attackMove.effectEnemy
    ph = ph + attackMove.effectPlayer
    print(attackMove.damage)
    return    

#List Of Enemy Functions

enemies = [catMonster, trollGaurd]

#Battle Function

def battle(t):
    print("You engage in battle! Fight!")
    while eh > 0 and ph > 0:
        ph2 = str(ph)
        eh2 = str(eh)
        print("Enemy health is at " + eh2)
        print("Your health is at " + ph2)
        print("")
        playerAttack()
        enemies[t]()
        print("")
    if eh <= 0:
        print("Enemy defeated! You win!")
    elif ph <= 0:
        print("You are killed by the enemy! GAME OVER!")
        sys.exit()

#Function For Unlocking Chest

def chest(word):
    global guess
    current_board = "_" * len(word)
    while current_board != word:
        print(current_board)
        print("Pick a letter!")
        unlockGUI()
        next_board = ""
        for i in range(len(word)):
            if guess == word[i]:
                next_board = next_board + guess
            else:
                next_board = next_board + current_board[i]
        current_board = next_board
        guess = ""

#Main Game Function

def mainGame():
    global eh
    global ph
    global choice
    print("You are in the doorway of a room. The room is dark, with only one torch lighting it from the back wall. From what you can tell, the room is empty.")
    print("Do you enter? ")
    print("")
    yesNoGUI()
    if choice == "yes":
        choice = ""
        print("Something steps out from the shadows. Its a cat monster!")
        eh = 25
        battle(0)
    elif choice == "no":
        print("You stand there untill you die.")
        print("GAME OVER")
        sys.exit()
    print("")
    print("As the battle ends, you take a deep breath.")
    print('')
    print(". . .")
    print('')
    print("Ok. You're ready to continue.")
    print('')
    print("You look around the room. You notice a single chest on the back wall that you didn't notice there before.")
    print("Do you try to open it?")
    yesNoGUI()
    print("")
    if choice == "yes":
        choice = ""
        #open the lock
        print("It has a lock on it! You need to put in a password!")
        chest("monster")
        print("Correct! The lock opens!")
        print(". . .")
        print("Its a bottle of Health Drink(TM)!")
        ph = charaChoice.health
        ph2 = str(ph)
        print("You drink it!")
        print("Your health fills! It's now at " + ph2 + "!")
    print("You move away from the chest.")
    print("You take another look around the room.")
    print(". . .")
    print("Something about the torch looks strange. Like you may be able to pull it?")
    print("Do you pull it?")
    yesNoGUI()
    if choice == "yes":
        choice = ""
        print('')
        print("A hole opens up in the floor...")
        print("")
        print("Somethings crawling out of it!")
        print('')
        print("Its another cat monster!")
        eh = 25
        battle(0)
        print("This place is more dangerous than you thought...")
        print('')
        print("You compose yourself yet again.")
    print('')
    print("You take another look out around the room. There doesnt seem to be an obvious exit besides the one you came through!")
    print("in fact . . .")
    print("Why. . . . ")
    print("Why did you even come in here? What was the point of all of this?")
    print("sigh")
    print(". . .")
    print("You sigh for so long your health fills back up to " + ph2 + ". . .")
    ph = charaChoice.health
    print("You should probably leave now.")
    print("Do you?")
    yesNoGUI()
    print("")
    if choice == "no":
        print("Oh. Okay.")
        print("")
        print("You sit there until you die of dehydration.")
        print("GAME OVER")
        sys.exit()
    elif choice == "yes":
        print("You go to leave.")
        print("")
        print("But... as soon as you step out...")
        print("A troll guard appears!")
        eh = 25
        battle(1)
        print("")
        print("As the enemy falls dead, you step around its body...")
        print("and with that...")
        print("You escape!")
        print("YOU WIN")

#Start Full Game

def fullGame ():
    charaSelect()
    mainGame()
    sys.exit()

fullGame()


