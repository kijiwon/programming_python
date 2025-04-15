# 리스트 -> 가변객체
# 튜플 -> 불변객체

def modify_tuple(value, fixed=(1, 2)): # fixed -> 불변!! (1, 2)가 유지됨
    fixed = fixed + (value,)
    return fixed

print(modify_tuple(3))
# value = 3, fixed = (1, 2, 3) -> 새로운 튜플 생성
print(modify_tuple(4))
# value = 4, fixed = (1, 2, 4) -> 기본값 튜플 사용. 새로운 튜플 생성
print(modify_tuple(5, fixed=(10,)))
# value = 5, fixed = (10, 5) -> 인자로 전달된 튜플 사용