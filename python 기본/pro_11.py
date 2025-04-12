dec = 13
bin = ''
while(dec > 0):
    rmd = dec % 2 # 2로 나눈 나머지
    dec = dec // 2 # 2로 나눈 몫
    bin = str(rmd) + bin # 문자열로 변환 후 더하기(문자열 합침)
print(bin)

# dec = 13          6       3       1       0 -> 반복문 종료
# rmd = 1           0       1       1
# dec = 6           3       1       0
# bin = '1'        '01'    '101'    '1101'
# [실행 결과] 1101