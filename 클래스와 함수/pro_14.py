def mix_values(a, b=[], c=10): # b의 기본값으로 배열이 들어옴 -> 메모리에 남음
    b.append(a)
    return b, c # 반환값이 2개 이상인 경우 튜플 형태()로 전달. 리스트->[], 튜플->()

print(mix_values(1))
# a = 1을 넘기면 b = [1] , c = 10(기본값) => ([1], 10)
print(mix_values(2, c=20))
# a = 2를 넘기면 b = [1, 2], c = 20(인자로 넘김) => ([1, 2], 20)
print(mix_values(3))
# a = 3을 넘기면 b = [1, 2, 3], c = 10(기본값) => ([1, 2, 3], 10)