list_pre = []
list_for_task =[]
numbers = 0

while numbers <= 1000:
    if numbers % 2 != 0:
        list_pre.append(numbers)
    numbers += 1

for i in list_pre:
    i = i ** 3
    list_for_task.append(i)
print(list_for_task)








