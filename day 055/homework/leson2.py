# 2) გადმოგეცემათ სია რომელშიც იქნება რიცხვები არეულად ( 1 , 8 ,5 , 0) და დაამატეთ ახალ სიაში დალაგებულად


def add_to_list(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
    return list3

list1 = [1, 8, 5, 0]
list2 = [2, 7, 4, 3]

