def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    rounds = [number]
    for i in range(2):
        rounds.append(rounds[i] + 1)
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    all_rounds = rounds_1[:]
    all_rounds.extend(rounds_2)
    return all_rounds


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """
    hand_ = hand[:]
    if 0 in hand:
        hand_.remove(0)
    first_card = hand_[0]
    last_card = hand_[-1]
    avg_first_last = round((first_card + last_card) / 2)
    avg_hand = sum(hand) / len(hand)
    if avg_first_last == avg_hand:
        return True
    return False


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_cards = []
    odds_cards = []
    for i, card in enumerate(hand):
        if i % 2 == 0:
            even_cards.append(card)
        else:
            odds_cards.append(card)
    avg_even_cards = sum(even_cards) / len(even_cards)
    avg_odds_cards = sum(odds_cards) / len(odds_cards)
    if avg_even_cards == avg_odds_cards:
        return True
    return False


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    hand_ = hand[:]
    if hand[-1] == 11:
        hand_[-1] = 11*2
    return hand_
