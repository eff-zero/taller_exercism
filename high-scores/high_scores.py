def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores):
    scores.sort(reverse=True)
    top_three = []
    for i, score in enumerate(scores):
        if i != 3:
            top_three.append(score)
        else:
            break
    return top_three
