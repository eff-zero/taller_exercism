def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    for i, score in enumerate(student_scores):
        student_scores[i] = round(score)
    return student_scores


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    counter = 0
    for score in student_scores:
        if score <= 40:
            counter += 1
    return counter


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    top_scores = []
    for score in student_scores:
        if score >= threshold:
            top_scores.append(score)
    return top_scores


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """
    min_score = 41  # F
    limit = (highest // 4) - 10
    scores = [min_score]
    for i in range(3):
        letter_score = scores[i] + limit
        scores.append(letter_score)
    return scores


def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    ranking = []
    for indice, score in enumerate(student_scores):
        format_ = f'{indice + 1}. {student_names[indice]}: {score}'
        ranking.append(format_)
    return ranking


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    for score in student_info:
        if 100 in score:
            return score
    return 'No perfect score.'
