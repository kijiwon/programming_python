def test(x, y=[]): # 기본값으로 자료구조가 들어온 경우 메모리에 남음
    y.append(x) # append: 리스트에 요소를 뒤에 추가
    return y

print(test(1)) # [1]
print(test(2)) # [1, 2]