
temperatures = [72, 68, 75, 70, 78, 74, 71]

max_temp = max(temperatures)
print("Highest temperature:", max_temp)

min_temp = min(temperatures)
print("Lowest temperature:", min_temp)

average_temp = sum(temperatures) / len(temperatures)
print("Average temperature:", average_temp)

above_70 = [temp for temp in temperatures if temp > 70]
print("Temperatures above 70:", above_70)
