def bumps(road):
    bump_count = road.count('n')
    
    if bump_count <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"