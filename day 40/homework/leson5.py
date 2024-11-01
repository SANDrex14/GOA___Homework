def averages(numbers):
    if numbers is None or len(numbers) < 2:
        return []
    
    averages_list = []
    
    for i in range(len(numbers) - 1):
        avg = (numbers[i] + numbers[i + 1]) / 2 
        averages_list.append(avg) 
    
    return averages_list 
