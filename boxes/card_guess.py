


def guess_day_1(Q_box,desired_card,guess):
    partition = Q_box.partitions.all()[0]
    section = partition.choise_section.all()[0]
    section_card = section.choise_cards

    if guess == "True":
        section_card.add(desired_card)

    elif guess == "False":
        pass
    
    print(section.choise_cards.all())
