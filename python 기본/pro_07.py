for i in range(10): # 10 이전까지 반복
    if i == 5:
        break # i가 5이면 반복문 종료
    elif i % 2 == 0: 
        continue # i % 2 == 0이면 아래 코드를 실행하지 않고 다음 반복으로 넘어감
    print(i, end=",") # end -> 이어서 출력
    # [실행 결과] 1,3,