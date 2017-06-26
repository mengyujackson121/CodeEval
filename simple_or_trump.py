import sys

f = open(sys.argv[-1], 'r').readlines()

order_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
for line in f:
    cards, trump_suites = line.strip().split('| ')
    first_card, second_card = cards.strip().split(' ')
    first_rank, first_suit = first_card[:-1],first_card[-1]
    second_rank, second_suit = second_card[:-1],second_card[-1]
    if first_suit != second_suit and first_suit == trump_suites:
        print first_card
    elif first_suit != second_suit and second_suit == trump_suites:
        print second_card
    elif first_rank == second_rank:
        print first_card,second_card
    else:
        if order_list.index(first_rank) > order_list.index(second_rank):
            print first_card
        else:
            print second_card
