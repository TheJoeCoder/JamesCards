import pygame
import time
import sys
import random
from itertools import combinations

fullScreen = False

pygame.init()

black = (0,0,0)
white = (255,255,255)

light_purple = (200, 150, 255)
purple = (110, 40, 125)
background_colour = (34,139,34)
grey = (220,220,220)
black = (0,0,0)
green = (0, 200, 0)
red = (255,0,0)
light_slat = (119,136,153)
dark_slat = (47, 79, 79)
dark_red = (255, 0, 0)

blue = (0, 0, 175)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (background_colour)

car_width = 25

CARD_SIZE = (17, 26)
CARD_CENTER = (9, 13)

money = 200
bet = 0
current_bet = 0
pot = 0

display_width = 240
display_height = 280

displayMode = pygame.FULLSCREEN if fullScreen else 0

gameDisplay = pygame.display.set_mode((display_width,display_height), displayMode)
pygame.display.set_caption("The James Display")
clock = pygame.time.Clock()

cardBack = "cards/Back.png"
cardDict = {
    "As": {
        "image": "cards/As.png",
        "value": 1},
    "2s": {
        "image": "cards/2s.png",
        "value": 2},
    "3s": {
        "image": "cards/3s.png",
        "value": 3},
    "4s": {
        "image": "cards/4s.png",
        "value": 4},
    "5s": {
        "image": "cards/5s.png",
        "value": 5},
    "6s": {
        "image": "cards/6s.png",
        "value": 6},
    "7s": {
        "image": "cards/7s.png",
        "value": 7},
    "8s": {
        "image": "cards/8s.png",
        "value": 8},
    "9s": {
        "image": "cards/9s.png",
        "value": 9},
    "10s": {
        "image": "cards/10s.png",
        "value": 10},
    "Js": {
        "image": "cards/Js.png",
        "value": 10},
    "Qs": {
        "image": "cards/Qs.png",
        "value": 10},
    "Ks": {
        "image": "cards/Ks.png",
        "value": 10},
    "Ac": {
        "image": "cards/Ac.png",
        "value": 1},
    "2c": {
        "image": "cards/2c.png",
        "value": 2},
    "3c": {
        "image": "cards/3c.png",
        "value": 3},
    "4c": {
        "image": "cards/4c.png",
        "value": 4},
    "5c": {
        "image": "cards/5c.png",
        "value": 5},
    "6c": {
        "image": "cards/6c.png",
        "value": 6},
    "7c": {
        "image": "cards/7c.png",
        "value": 7},
    "8c": {
        "image": "cards/8c.png",
        "value": 8},
    "9c": {
        "image": "cards/9c.png",
        "value": 9},
    "10c": {
        "image": "cards/10c.png",
        "value": 10},
    "Jc": {
        "image": "cards/Jc.png",
        "value": 10},
    "Qc": {
        "image": "cards/Qc.png",
        "value": 10},
    "Kc": {
        "image": "cards/Kc.png",
        "value": 10},
    "Ah": {
        "image": "cards/Ah.png",
        "value": 1},
    "2h": {
        "image": "cards/2h.png",
        "value": 2},
    "3h": {
        "image": "cards/3h.png",
        "value": 3},
    "4h": {
        "image": "cards/4h.png",
        "value": 4},
    "5h": {
        "image": "cards/5h.png",
        "value": 5},
    "6h": {
        "image": "cards/6h.png",
        "value": 6},
    "7h": {
        "image": "cards/7h.png",
        "value": 7},
    "8h": {
        "image": "cards/8h.png",
        "value": 8},
    "9h": {
        "image": "cards/9h.png",
        "value": 9},
    "10h": {
        "image": "cards/10h.png",
        "value": 10},
    "Jh": {
        "image": "cards/Jh.png",
        "value": 10},
    "Qh": {
        "image": "cards/Qh.png",
        "value": 10},
    "Kh": {
        "image": "cards/Kh.png",
        "value": 10},
    "Ad": {
        "image": "cards/Ad.png",
        "value": 1},
    "2d": {
        "image": "cards/2d.png",
        "value": 2},
    "3d": {
        "image": "cards/3d.png",
        "value": 3},
    "4d": {
        "image": "cards/4d.png",
        "value": 4},
    "5d": {
        "image": "cards/5d.png",
        "value": 5},
    "6d": {
        "image": "cards/6d.png",
        "value": 6},
    "7d": {
        "image": "cards/7d.png",
        "value": 7},
    "8d": {
        "image": "cards/8d.png",
        "value": 8},
    "9d": {
        "image": "cards/9d.png",
        "value": 9},
    "10d": {
        "image": "cards/10d.png",
        "value": 10},
    "Jd": {
        "image": "cards/Jd.png",
        "value": 10},
    "Qd": {
        "image": "cards/Qd.png",
        "value": 10},
    "Kd": {
        "image": "cards/Kd.png",
        "value": 10},
    }

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
   
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
   
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
       
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
       
    smallText = pygame.font.SysFont("Times New Roman",35)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
   
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay,ic,(x, y, w, h))
       
    smallText = pygame.font.SysFont("Times New Roman",15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
   
def smalltext(f, msg, x, y, w, h):
    smallText = pygame.font.SysFont("Times New Roman",f)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

################################################################################
    
################################################################################
def menu():
    global pause
   
    intro = True
   
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
               
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('Times New Roman',45)
        TextSurf, TextRect = text_objects("Card Games", largeText)
        TextRect.center = ( (90+(60/2)), (50+(15/2)) )
        gameDisplay.blit(TextSurf, TextRect)
       
        smalltext(15, str(money), 120, 5, 180, 25)
       
        button("BlackJack", 20, 100, 200, 50, light_purple, purple, blackjack)
        button("Poker", 20, 170, 200, 50, light_purple, purple, poker)
        
        mouse = pygame.mouse.get_pos()
       
        pygame.display.update()
        clock.tick(15)
   
###############################################################################   
       
###############################################################################
def blackjack():
    global money
    bet = 0
    
    dealtHit = 0
    dealerHit = 0
    
    stand = True
    playerStand = False
    
    roundOver = "yes"
    solveMoney = "no"
   
    cardTotalP= 0
    cardTotalD = 0
    
    cards = list(cardDict.keys())
    random.shuffle(cards)
                   
    print ("shuffle: ", cards)
   
    dealtCards = False
    
    dealerCards = []
    playerCards = []
    
    startCardIndex = 0
    
    while True:
    
        gameDisplay.fill(background_colour)
        
        largeText = pygame.font.SysFont('Times New Roman',20)
        TextSurf, TextRect = text_objects("BlackJack", largeText)
        TextRect.center = ( (17+(60/2)), (1+(25/2)) )
        gameDisplay.blit(TextSurf, TextRect)
       
        smalltext(17, "Press B to return", 33, 1, 60, 50)
        smalltext(17, str(money), 120, 5, 180, 25)
        smalltext(17, str(bet), 130, 240, 180, 25)
        smalltext(17, "Deal: Z", 6, 220, 50, 25)
        smalltext(17, "Hit: X", 3, 235, 50, 25)
        smalltext(17, "Stand: C", 10, 250, 50, 25)
        
        if dealtCards:
            
            # First two cards (0, 2)
            xOffset = 0
            for i in playerCards:
                cardImg = pygame.image.load(cardDict[cards[i]]["image"])
                gameDisplay.blit(cardImg, (75 + xOffset, 230))
                xOffset += (CARD_SIZE[0] + round(CARD_SIZE[0] * 0.5))
                smalltext(15, str(cardTotalP), 75, 250, 180, 25)
            
            # Second two cards (1, 3)
            xOffset = 0

            for index, cardIndex in enumerate(dealerCards):
                if index == 1 and not playerStand:
                    cardImg = pygame.image.load(cardBack)
                else:
                    cardImg = pygame.image.load(cardDict[cards[cardIndex]]["image"])

                gameDisplay.blit(cardImg, (75 + xOffset, 50))
                xOffset += CARD_SIZE[0] + round(CARD_SIZE[0] * 0.5)
        
            if playerStand:
                smalltext(15, str(cardTotalD), 75, 30, 180, 25)
       
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    menu()
            #Deal
            if roundOver == "yes":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        if not dealtCards:
                            dealtCards = True
                        solveMoney = "no"
                        roundOver = "no"
                        playerStand = False
                        playerCardHit = True
                        bet = 0
                        dealtHit = 0
                        cardTotalP = 0
                        cardTotalD = 0
                        
                        playerCards = [startCardIndex, startCardIndex + 2]
                        dealerCards = [startCardIndex + 1, startCardIndex + 3]
                        startCardIndex += 4
                        
                        cardTotalP = 0
                        for cardIndex in playerCards:
                            cardTotalP += cardDict.get(cards[cardIndex], {}).get("value", 0)
                            
                        
                        
                        if startCardIndex >= len(cards) - 5:
                            startCardIndex = 0
                            random.shuffle(cards)
                            print ("shuffle: ", cards)
 
                        money -= 10
                        bet += 10
            #Hit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if playerCardHit:
                        stand = True
                        playerCards.append(startCardIndex)
                        startCardIndex = startCardIndex + 1
                        dealtHit = dealtHit + 1
                        cardTotalP = 0
                        for cardIndex in playerCards:
                            cardTotalP += cardDict.get(cards[cardIndex], {}).get("value", 0)
                    if cardTotalP > 21:
                        playerCardHit = False
                    if dealtHit == 4:
                        playerCardHit = False
            #Stand
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    playerCardHit = False
                    playerStand = True
                    stand = True
                    roundOver = "yes"
                    
                    if stand:
                        stand = False
                        for i in range(4):
                            if cardTotalD < 17:  
                                cardTotalD = 0
                                for cardIndex in dealerCards:
                                    cardTotalD += cardDict.get(cards[cardIndex], {}).get("value", 0)
                                dealerCards.append(startCardIndex)
                                startCardIndex = startCardIndex + 1
                                
                                cardTotalD = 0
                                for cardIndex in dealerCards:
                                    cardTotalD += cardDict.get(cards[cardIndex], {}).get("value", 0)
                        
                        solveMoney = "go"
                        bet = 0
                            
            #Money
            if solveMoney == "go":
                if cardTotalP > cardTotalD and cardTotalP < 22:
                    money = money + 20
                    solveMoney = "no"
                if cardTotalP < 22 and cardTotalD > 21:
                    money = money + 20     
                    solveMoney = "no"
                if cardTotalP > 21 and cardTotalD > 21:
                    money = money + 10     
                    solveMoney = "no"
                if cardTotalP == cardTotalD:
                    money = money + 10     
                    solveMoney = "no"
                
        pygame.display.update()
        clock.tick(15)
       
################################################################################

################################################################################
        
def get_rank(card):
    return card[:-1]

def get_suit(card):
    return card[-1] 

def rank_value(rank):
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
              '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    return values.get(rank, 0)

def evaluate_hand(cards):
    ranks = [get_rank(c) for c in cards]
    suits = [get_suit(c) for c in cards]
    values = sorted([rank_value(r) for r in ranks], reverse=True)

    def is_flush():
        for s in 'shdc':
            if suits.count(s) >= 5:
                return True, [c for c in cards if get_suit(c) == s]
        return False, []

    def is_straight(vals):
        vals = sorted(set(vals), reverse=True)
        for i in range(len(vals) - 4):
            if vals[i] - vals[i+4] == 4:
                return True, vals[i:i+5]
        if set([14, 2, 3, 4, 5]).issubset(vals):  # Wheel
            return True, [5, 4, 3, 2, 14]
        return False, []

    def classify_hand():
        counts = {v: values.count(v) for v in set(values)}
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))
        count_values = [v for v, c in sorted_counts]

        flush, flush_cards = is_flush()
        straight, straight_vals = is_straight(values)

        if flush and straight:
            flush_vals = sorted([rank_value(get_rank(c)) for c in flush_cards], reverse=True)
            straight_flush, sf_vals = is_straight(flush_vals)
            if straight_flush:
                return ("Straight Flush", 9, sf_vals)
        
        if sorted_counts[0][1] == 4:
            return ("Four of a Kind", 8, count_values)
        if sorted_counts[0][1] == 3 and sorted_counts[1][1] >= 2:
            return ("Full House", 7, count_values)
        if flush:
            return ("Flush", 6, sorted([rank_value(get_rank(c)) for c in flush_cards], reverse=True)[:5])
        if straight:
            return ("Straight", 5, straight_vals)
        if sorted_counts[0][1] == 3:
            return ("Three of a Kind", 4, count_values)
        if sorted_counts[0][1] == 2 and sorted_counts[1][1] == 2:
            return ("Two Pair", 3, count_values)
        if sorted_counts[0][1] == 2:
            return ("One Pair", 2, count_values)
        return ("High Card", 1, values[:5])

    return classify_hand()

def betting_phase(stage, playerCards, dealerCards, middleCards, cards):
    global money, pot, current_bet
    betting = True
    while betting:
        gameDisplay.fill(background_colour)

        # Player cards
        xOffset = 0
        for i in playerCards:
            cardImg = pygame.image.load(cardDict[cards[i]]["image"])
            gameDisplay.blit(cardImg, (80 + xOffset, 200))
            xOffset += CARD_SIZE[0] + round(CARD_SIZE[0] * 0.5)

        # Dealer cards (face down during betting)
        xOffset = 0
        for cardIndex in dealerCards:
            cardImg = pygame.image.load(cardBack)
            gameDisplay.blit(cardImg, (80 + xOffset, 50))
            xOffset += CARD_SIZE[0] + round(CARD_SIZE[0] * 0.5)

        # Table cards
        xOffset = 0
        for cardIndex in middleCards:
            cardImg = pygame.image.load(cardDict[cards[cardIndex]]["image"])
            gameDisplay.blit(cardImg, (80 + xOffset, 125))
            xOffset += CARD_SIZE[0] + round(CARD_SIZE[0] * 0.5)

        largeText = pygame.font.SysFont('Times New Roman',20)
        TextSurf, TextRect = text_objects("Poker", largeText)
        TextRect.center = ( (3+(45/2)), (1+(25/2)) )
        gameDisplay.blit(TextSurf, TextRect)
       
        smalltext(17, "Current Pot: ", 17, 1, 60, 50)
        smalltext(17, str(money), 120, 5, 180, 25)
        smalltext(17, str(pot), 70, 1, 60, 50)
        
        smalltext(17, f"{stage} betting round", 60, 235, 180, 25)
        smalltext(14, "K=Check, C=Call, R=Raise, F=Fold", 40, 250, 180, 25)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k and current_bet == 0:  # Check
                    betting = False
                elif event.key == pygame.K_c:  # Call
                    if current_bet < 10:
                        current_bet += 10
                    money -= current_bet
                    pot += current_bet
                    pot += current_bet
                    betting = False
                elif event.key == pygame.K_r:  # Raise
                    raise_amount = 20
                    money -= (current_bet + raise_amount)
                    pot += (current_bet + raise_amount)
                    current_bet += raise_amount
                    pot += current_bet
                    betting = False
                elif event.key == pygame.K_f:  # Fold
                    pot = 0
                    pot += current_bet
                    betting = False
                    return "fold"
                elif event.key == pygame.K_b:  # Allow back to menu during betting
                    menu()
                    return "fold"

        pygame.display.update()
        clock.tick(15)
    return "continue"

def poker():
    global money, pot, current_bet
    bet = 0
    pot = 0
    current_bet = 0
    
    cards = list(cardDict.keys())
    random.shuffle(cards)
    print("shuffle: ", cards)

    dealtCards = False
    dealerCards = []
    middleCards = []
    playerCards = []
    startCardIndex = 0
    
    while True:
        gameDisplay.fill(background_colour)
        largeText = pygame.font.SysFont('Times New Roman',20)
        TextSurf, TextRect = text_objects("Poker", largeText)
        TextRect.center = ( (3+(45/2)), (1+(25/2)) )
        gameDisplay.blit(TextSurf, TextRect)

        smalltext(17, "Current Pot:", 17, 1, 60, 50)
        smalltext(17, str(money), 120, 5, 180, 25)
        smalltext(17, str(bet), 130, 240, 180, 25)
        smalltext(17, str(pot), 70, 1, 60, 50)

        if dealtCards:
            # Player cards
            xOffset = 0
            for i in playerCards:
                cardImg = pygame.image.load(cardDict[cards[i]]["image"])
                gameDisplay.blit(cardImg, (60 + xOffset, 200))
                xOffset += CARD_SIZE[0] + round(CARD_SIZE[0] * 0.5)

            # Dealer cards (hidden until showdown)
            xOffset = 0
            for cardIndex in dealerCards:
                cardImg = pygame.image.load(cardBack)
                gameDisplay.blit(cardImg, (80 + xOffset, 50))
                xOffset += CARD_SIZE[0] + round(CARD_SIZE[0] * 0.5)

            # Table cards
            xOffset = 0
            for cardIndex in middleCards:
                cardImg = pygame.image.load(cardDict[cards[cardIndex]]["image"])
                gameDisplay.blit(cardImg, (80 + xOffset, 125))
                xOffset += CARD_SIZE[0] + round(CARD_SIZE[0] * 0.5)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    menu()
                # Deal new round
                if not dealtCards and event.key == pygame.K_z:
                    dealtCards = True
                    playerCards = [startCardIndex, startCardIndex + 2]
                    dealerCards = [startCardIndex + 1, startCardIndex + 3]
                    middleCards = []
                    startCardIndex += 4

                    # Ante
                    money -= 10
                    bet += 10
                    pot += 15
                    current_bet = 0

                    # Pre-Flop betting
                    result = betting_phase("Pre-Flop", playerCards, dealerCards, middleCards, cards)
                    if result == "fold":
                        time.sleep(2)
                        dealtCards = False
                        bet = 0
                        pot = 0
                        current_bet = 0
                        continue

                    # Flop
                    for _ in range(3):
                        middleCards.append(startCardIndex)
                        startCardIndex += 1
                    current_bet = 0
                    result = betting_phase("Flop", playerCards, dealerCards, middleCards, cards)
                    if result == "fold":
                        time.sleep(2)
                        dealtCards = False
                        bet = 0
                        pot = 0
                        current_bet = 0
                        continue

                    # Turn
                    middleCards.append(startCardIndex)
                    startCardIndex += 1
                    current_bet = 0
                    result = betting_phase("Turn", playerCards, dealerCards, middleCards, cards)
                    if result == "fold":
                        time.sleep(2)
                        dealtCards = False
                        bet = 0
                        pot = 0
                        current_bet = 0
                        continue

                    # River
                    middleCards.append(startCardIndex)
                    startCardIndex += 1
                    current_bet = 0
                    result = betting_phase("River", playerCards, dealerCards, middleCards, cards)
                    if result == "fold":
                        time.sleep(2)
                        dealtCards = False
                        bet = 0
                        pot = 0
                        current_bet = 0
                        continue

                    # Showdown
                    player_hand = evaluate_hand([cards[i] for i in playerCards + middleCards])
                    dealer_hand = evaluate_hand([cards[i] for i in dealerCards + middleCards])
                    print("Player:", player_hand)
                    print("Dealer:", dealer_hand)
                    if player_hand > dealer_hand:
                        money += pot
                    elif player_hand == dealer_hand:
                        money += pot / 2
                    # reset for next hand
                    time.sleep(2)
                    pot = 0
                    bet = 0
                    dealtCards = False

        pygame.display.update()
        clock.tick(15)
menu()