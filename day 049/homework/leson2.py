def analyze_scores(scores):
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    return max_score, min_score, avg_score

student_scores = [45, 78, 88, 92, 53, 67, 99]
max_score, min_score, avg_score = analyze_scores(student_scores)

print(f"მაქსიმალური ქულა: {max_score}")
print(f"მინიმალური ქულა: {min_score}")
print(f"საშუალო ქულა: {avg_score:.2f}")
