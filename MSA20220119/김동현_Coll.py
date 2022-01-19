#1번
dic_score = { '국어' : 95, '영어' : 90, '수학' : 80, '과학' : 50}
average = sum(dic_score.values())/4
print(average)

#2번
set3 = {i for i in range(1,101) if i % 3 == 0}
set5 = {i for i in range(1,101) if i % 5 == 0}
print(set3&set5) # 3과5의 공배수
print(set3|set5) # 합집합

#3번
listData = range(7, -8, -2)
print(list(listData))

#4번
tupleData = tuple(listData)
print(tupleData)