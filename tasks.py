# Подсчитывает общую сумму расходов
# Находит категорию, на которую было потрачено больше всего денег

import json

with open("task1.json", encoding='utf-8') as file:
    data = json.load(file)
    # print(data)

# total_sum = sum(item['сумма'] for item in data)

# for item in data:
#     total_sum += item['сумма']

# print(total_sum)

# # "развлечения"
# cats = {}
# for item in data:
#     if item["категория"] in cats:
#         cats[item["категория"]] += item["сумма"]
        
#     else:
#         cats[item["категория"]] = item["сумма"]
   
# #  Категория с наибольшими тратами    
# print (cats)
# max_category = max(cats, key=cats.get)  
# print(max_category)

# # Самый дорогой день

# # должен вывести 2023-11-15

days = {}
for item in data:
    
    if item["дата"] in days:
        
        days[item["дата"]] += item["сумма"]
    else:
        days[item["дата"]] = item["сумма"]

max_day = max(days, key=days.get)
print(max_day)