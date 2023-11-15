import random

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
    aceChoice = 0

    for cards in turn:
        card = cards[0]
        try:
            if int(card) == int(card):
                value += int(card)
        except:
            if card == 'A':
                if value < 11:
                    aceChoice = int(input("Make ace 11 or 1? "))
                    while aceChoice != 1 and aceChoice != 11:
                        print("Invalid input, try again...")
                        aceChoice = int(input("Make ace 11 or 1? "))
                    value += aceChoice
                else:
                    value += 10
            else:
                value += 10
    return value



def main(seedValue):
    deck = createDeck
    dealer = []
    player = []

    def getCard(turn):
        card = random.choice(deck)
        deck.remove(card)
        return card
    
    def handBust(turn):
        bust = False
        while bust == False:
            if turn == dealer:
                if handValue(turn) < 16:
                    getCard(dealer)
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