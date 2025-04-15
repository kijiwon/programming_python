def default_behavior(x, y=[]):
    y.append(x)
    return len(y)

print(default_behavior(1))
# x = 1으로  y = [1](메모리에 저장) => len(y) = 1
print(default_behavior(2))
# x = 2으로 y = [1, 2](메모리에 저장) => len(y) = 2
print(default_behavior(3,[10, 20]))
# x = 3, y = [10, 20, 3] -> 새로운 리스트(새로운 메모리에 저장) => len(y) = 3
print(default_behavior(4))
# x = 4으로 y = [1, 2, 4](이전에 메모리에 저장된 기본 리스트) => len(y) = 3