from deck import Deck
from hand import Hand
from chips import Chips

suits=['Черьви','БубЕны','ПикА','КрестЫ']
ranks=['2','3','4','5','6','7','8','9','10','Валет', 'Дама','Корол','ТуС']
values={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Валет':10, 'Дама':10,'Корол':10,'ТуС':11}

playing=True


def takeBet(chips):
    while True:
        try:
            chips.bet=int(input('Введите свою ставку: '))
        except:
            print ('Введи целое число!')
        else:
            if chips.bet>chips.total:
                print(f'Баланса не хватает:) У тебя всего {chips.total}')
            else:
                break
def hit(deck,hand):
    hand.addCard(deck.deal())
    hand.adjAces()

def hit_or_stand(deck, hand):
    global playing
    while True:
        x=input('Берем карту исчо(hit,h) или хватает(stand,s)?')
        if x=='h':
            hit(deck,hand)
        elif x=='s':
            print('Ну чтоже... Ход компа)) ')
            playing=False
        else:
            print ('Непонятный ответ, введи h или s')
            continue
        break
def player_busts(player, dealer, chips):
    print ('\nПеребрал карты! сумма больше 21! Очко))')
    chips.lose_bet()

def player_win(player, dealer, chips):
    print ('\nА ты выиграл!))')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print ('\nА ты выиграл!)), Комп набрал больше, чем нужно(')
    chips.win_bet()

def dealer_win (player, dealer, chips):
    print ('\nЯ выиграл!!!!')
    chips.lose_bet()

def push(player, dealer):
    print ('\nНичья(')

def show_card(player, dealer):
    print ('\n Карты компа:')
    print (' карта скрыта)))')
    print (' ', dealer.cards[1])
    print ('\n Твои карты: ', *player.cards, sep='\n ')
def show_cards(player, dealer):
    print ('\n Карты компа: ', *dealer.cards, sep='\n ')
    print ('набранные очки: ', dealer.value)
    print ('\n Твои карты: ', *player.cards, sep='\n ')
    print ('набранные очки: ', player.value)

# ИИИИИгра!!!!!!!!!!!!!!!!!!
while True:
    print ('ИИИИ мы НАЧИНАЕМ!!!\n')

    deck=Deck(ranks,suits)
    deck.shuffle()

    player_hand=Hand(values)
    player_hand.addCard(deck.deal())
    player_hand.addCard(deck.deal())

    dealer_hand=Hand(values)
    dealer_hand.addCard(deck.deal())
    dealer_hand.addCard(deck.deal())

    player_chips=Chips()
    takeBet(player_chips)

    show_card(player_hand, dealer_hand)
    while playing:
        hit_or_stand(deck, player_hand)
        show_card(player_hand, dealer_hand)
        if player_hand.value>21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    if player_hand.value<=21:
        while dealer_hand.value<17:
            hit(deck, dealer_hand)
        show_cards(player_hand, dealer_hand)

        if dealer_hand.value>21:
            dealer_busts(player_hand, dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_win(player_hand, dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_win(player_hand, dealer_hand,player_chips)
        else:
            push(player_hand, dealer_hand)
    print (f'\n Твои очки: {player_hand.value}')

    new_game=input ('Играем снова? y или n ')
    if new_game=='y':
        playing=True
        continue
    else:
        print ('\nНу или ладно....')
        
    break

    