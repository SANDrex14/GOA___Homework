def better_than_average(class_points, your_points):
    total_class_points = sum(class_points)

    total_students = len(class_points) + 1

    average_score = total_class_points / total_students

    return your_points > average_score
