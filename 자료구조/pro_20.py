my_set = {3, 5, 7, 9} # 셋 -> 중복허용x, 순서없음
my_set.add(5) # my_set = {3, 5, 7, 9}
my_set.add(2) # my_set = {2, 3, 5, 7, 9}
my_set.add(8) # my_set = {8, 2, 3, 5, 7, 9}
my_set.discard(7) # 7삭제 -> my_set = {8, 2, 3, 5, 9}
print(my_set)