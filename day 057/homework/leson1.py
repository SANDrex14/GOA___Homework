# 1
def positive_sum(arr):
    total = 0
    
    for num in arr:
        if num > 0:
            total += num
    return total

# 2

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        return "არცერთია სწორი"
    
# 3

def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


# 4

def better_than_average(class_points, your_points):
    total_class_points = sum(class_points)

    total_students = len(class_points) + 1

    average_score = total_class_points / total_students

    return your_points > average_score

# 5

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5
    
    return [human_years, cat_years, dog_years]