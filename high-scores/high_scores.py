def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top = []
    while True:
        a = max(scores)
        top.append(a)
        scores.remove(a)
        if top.__len__() == 3 or scores.__len__() == 0:
            break

    return top