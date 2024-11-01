def scores_min_max_normal(scores):
    if not scores:
        return "სია ცარიელია"
    
    max_score = max(scores)
    min_score = min(scores)
    normal_score = sum(scores) / len(scores)
    
    return f"მაქსიმალური ქულა: {max_score}, მინიმალური ქულა: {min_score}, საშუალო ქულა: {normal_score:}"

scores = [5 ,10 ,15 ,20 ,25 ,30 ,35 ,40 ,45 ,50 ,55 ,60 ,65 ,70 ,75 ,80 ,85 ,90 ,95 ,100]

result = scores_min_max_normal(scores)
print(result)


