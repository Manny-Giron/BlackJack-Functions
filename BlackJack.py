# Emmanuel GIorn
# CSC110 Final Project - Blackjack
#Due: December 14, 2023

import random
score = 0


def createDeck():
    faces = ['A','2','3','4','5','6','7','8','9','T','J','Q','K','A']
    suits = ['D','C','S','H']
    deck = []
    for face in faces:
        for suit in suits:
            card = face + suit
            deck.append(card)
    return deck

def handValue(turn):
    value = 0
    for cards in turn:
        card = cards[0]
        try:
            if int(card) == int(card):
                value += int(card)
        except:
            if card == 'A':
                value += 1
            else:
                value += 10
            
    return value


def dealCard(turn):
    card = random.choice(deck)
    deck.remove(card)
    return card
def checkPush()
    playerV = handValue(player)
    dealerV = handValue(dealer)
    if playerV == dealerV:
        return True
    else:
        return False


def handBust(turn):
        bust = False
        while bust == False:
            if turn == dealer:
                if handValue(turn) < 16:
                    dealCard(dealer)
                    print(f"Dealer Hand: {dealer}")
                    if handValue > 21:
                        bust = True
                        return True
                else:
                    if handValue(turn) > 21:
                        bust = True
                        return True
                    else:
                        return False
            else:
                if handValue(turn) > 21:
                   bust = True
                   return True
                else:
                    return False
def printAces(playerVals):
    print("You have ({numAces} ace(s) in your hand. Your current hand value is:\t{playerVal}")
        for i in range(1, len(playerVals)):
            print("or {playerVals[i]}")
            
            
def displayHands():
    print("Your hand is:\t{player}")
    print("Dealer is showing:\t{dealer[0]}")


def acesInHand(hand, handVal):
    numAces = 0
    for cards in hand:
        card = cards[0]
        if card == "A":
            numAces += 1
    if numAces > 0:
        if len(handValue) < (numAces + 1):    
            if numAces == 1:
                    handVal.append(handValue[0] + 10)
            else:
                handValue.append(handValue[0] + 1)
                handValue.append(handValue[0] + 10)
            return numAces

def checkBlackJack(handVals):
    for value in handValues:
        if value == 21:
            return True
        
def checkWinner(playerVal, dealerVal):
    if playerVal > dealerVal:
        return True
    else:
        return False


def main(seedValue):
    random.seed(seedValue)
    deck = createDeck
    dealer = []
    player = []
    
    for i in range(2):
        dealCard(player)
        dealCard(dealer)  
    
    displayHands()
    
    playerVals = [handValue(player)]
    dealerVals = [handValue(dealer)]
    pNumAces = acesInHand(player, playerVals[0])
    dNumAces = acesInHand(dealer, dealerVals[0])
    
    if pNumAces >0:
        printAces()
    
    haveBlackJack = False
    # .lower() to make it non-case sensitive
    while handBust(playerVals[0]) != True and hitStay.lower() != "h" and haveBlackJack != True:
        hitStay = str(input("\nType H to hit or S to stay: "))
        if hitStay.lower() == "h":
            dealCard(player)
            playerVals[0] = handValue(player[0])
            
            displayHands()
            pNumAces = acesInHand(player, playerVals[0])
            if pNumAces > 0:
                printAces(playerVals)
        elif hitStay.lower() == "s":
            pass
        else:
            print("Invalid input, try again...")
        
        haveBlackJack = checkBlackJack(player, playerVals)
    
    if handBust(playerVals[0]) == True:
        print("You have busted - too bad")
        print("\nYou busted, your total score for this round is -1")
    
    push = False
    if haveBlackJack == True:
        print("You have BlackJack!")
        print(f"")

