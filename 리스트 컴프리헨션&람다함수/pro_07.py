country = ['Korea', 'Spain', 'Germany', 'Canada', 'france', 'Serbia']

print(max(country)) 
# max()는 사전 순(알파벳 순)으로 비교 -> 문자열의 비교는 ASCII코드 값 기준 (A=65, a=97)
# 소문자가 대문자보다 큼 => france
print(max(country, key=lambda x: x[2]))
# 2번 인덱스 요소를 기준으로 비교
# r, a, r, n, a, r -> 동일한 문자가 있는 경우 다음 문자를 비교 => e, m, b 이 중 가장 먼저 나타나는 단어(e) => Korea
print(max(country, key=lambda i: i.lower()))
# 각 단어를 모두 소문자로 변경 후 비교 => 가장 나중의 알파벳 => Spain