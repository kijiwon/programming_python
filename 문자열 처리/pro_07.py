text = "ABCDEFGHIJ"
print(text[1:8:2])
# 1번 인덱스부터 8번 인덱스 전까지 2간격으로 출력 -> BDFH
print(text[-1:-6:-1])
# -1번 인덱스부터 -6번 인덱스 전까지 역순출력 -> JIHGF
print(text[5:1:-1])
# 5번 인덱스부터 1번 인덱스 전까지 역순출력 -> FEDC