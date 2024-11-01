def filter_scores(scores):
    return [score for score in scores if score > 50]

student_scores = [45, 78, 88, 40, 53, 67, 99]
filtered_scores = filter_scores(student_scores)

print("ფილტრირებული ქულები (50-ზე მეტი):", filtered_scores)
