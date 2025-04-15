tuples = [(1, 2), (1, 1), (5, 7), (7, 5)]
sorted_t = sorted(tuples) # 오름차순 정렬(기본) => [(1, 1), (1, 2), (5, 7), (7, 5)]
print(sorted_t)
sorted_t = sorted(tuples, key=lambda x: x[1]) # 1번 인덱스 요소를 기준으로 정렬 => [(1, 1), (1, 2), (7, 5), (5, 7)]
print(sorted_t)