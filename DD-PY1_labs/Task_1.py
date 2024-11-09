numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

num_1 = numbers[:4] #Список до None
num_2 = numbers[5:] #Список после None
sum_num = num_1 + num_2 #Список без None
None_1 =round(sum(sum_num)/len(numbers), 2)
numbers[4] = None_1

print("Измененный список:", numbers)
