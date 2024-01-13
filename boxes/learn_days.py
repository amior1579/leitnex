import random


def day_1(Q_box):

    learn_cards = Q_box.card_box.all()
    random_10_cards = random.sample(list(learn_cards), 10)

    return random_10_cards