my_dict = {'apple': 2, 'banana': 3, 'cherry': 1} # 딕셔너리 -> 순서o, 키는 중복x, 값은 중복o
my_dict['pear'] = 4 # 새로운 키-값 추가 -> my_dict = {'apple': 2, 'banana': 3, 'cherry': 1, 'pear':4} 마지막에 추가
del my_dict['banana'] # banana에 해당하는 키-값쌍 제거
print(my_dict) # my_dict = {'apple': 2, 'cherry': 1, 'pear':4}