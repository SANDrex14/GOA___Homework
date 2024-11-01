def initialize_names(name):
    name_parts = name.split()
    
    if len(name_parts) <= 2:
        return name
    
    for i in range(1, len(name_parts) - 1):
        name_parts[i] = name_parts[i][0] + '.'
    
    return ' '.join(name_parts)
