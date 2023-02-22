# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[0..N-1]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

num = int(input("Введите количество элементов списка: "))
list1 = [0]*num
for i in range (len(list1)):
    list1[1] = int(input (f"Введите {i} элемент списка: "))
search_number = int (input ("Введите число: "))
while search_number not in list1:
    search_number = int(input ("Введите число еще раз: "))
count = 0
for list in list1:
    if list == search_number:
        count+=1
print (f"число {search_number} встречается {count} раз.")
