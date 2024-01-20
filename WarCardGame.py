import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = dict()

for i in range(15):
    if i == 0 or i == 1:
        pass
    
    values[ranks[i-2]] = i

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
class Player:
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_Cards):
        if(type(new_Cards) == type([])):
            self.all_cards.extend(new_Cards)
        else:
            self.all_cards.append(new_Cards)
    
    def __str__(self) -> str:
        return f'Player {self.name} has {len(self.all_cards)} cards'
    
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
in_progress = True

round_num = 0

while in_progress:
    round_num += 1
    print(f'Round: {round_num}')
    
    if len(player_one.all_cards) == 0:
        print("Player one out of cards! Game Over")
        print("Player two wins!")
        break
    
    if len(player_two.all_cards) == 0:
        print("Player two out of cards! Game Over")
        print("Player one wins!")
        break
    
    player_one_played_cards = []
    player_one_played_cards.append(player_one.remove_one())
    player_two_played_cards = []
    player_two_played_cards.append(player_two.remove_one())
    
    at_war = True
    
    while at_war:
        
        if player_one_played_cards[-1].value < player_two_played_cards[-1].value:
            print(f'Fight Between {player_one_played_cards[-1]} and {player_two_played_cards[-1]}')
            player_two.add_cards(player_one_played_cards)
            player_two.add_cards(player_two_played_cards)
            print(f'Player one cards left: {len(player_one.all_cards)}')
            print(f'Player two cards left: {len(player_two.all_cards)}')
            at_war = False
            
        elif player_one_played_cards[-1].value > player_two_played_cards[-1].value:
            print(f'Fight Between {player_one_played_cards[-1]} and {player_two_played_cards[-1]}')
            player_one.add_cards(player_one_played_cards)
            player_one.add_cards(player_two_played_cards)
            print(f'Player one cards left: {len(player_one.all_cards)}')
            print(f'Player two cards left: {len(player_two.all_cards)}')
            at_war = False
        
        else:
            print(f'WAR! Between {player_one_played_cards[-1]} and {player_two_played_cards[-1]}')
            if len(player_one.all_cards) < 4 :
                print(f'Player One has {len(player_one.all_cards)} cards left! Game Over!')
                print("Player Two Wins! Player One Loses!")
                in_progress = False
                break
            
            elif len(player_two.all_cards) < 4 :
                print(f'Player Two has {len(player_two.all_cards)} cards left! Game Over!')
                print("Player One Wins! Player Two Loses!")
                in_progress = False
                break
            
            else:
                for num in range(4):
                    player_one_played_cards.append(player_one.remove_one())
                    player_two_played_cards.append(player_two.remove_one())