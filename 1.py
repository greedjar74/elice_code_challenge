'''
문제 풀이 방법
- 뒤에서 부터 차례대로 검사 진행
- 현재 위치의 값 보다 앞의 값이 작은 경우 변경 필요
- 기준점을 찾고 앞은 그대로 뒤는 정렬 후 재배치
'''

import time

nums = input()
nums_li = list(int(num) for num in nums)
l = len(nums_li)

start = time.time()

# 기준점 찾기
for i in range(l-1):
    idx = l - i - 1
    if nums_li[idx-1] < nums_li[idx]:
        idx -= 1
        break

num = nums_li[idx] # 기준점
re_li = nums_li[:idx] # 기준점 앞은 순서를 그대로 가져간다.
sorted_num = sorted(nums_li[idx:]) # 기준점 뒤 값들을 오름차순 정렬

# 기준점 값보다 큰 값들 중 가장 작은 값 찾기
for i in range(len(sorted_num)):
    if sorted_num[i] > num:
        num = sorted_num.pop(i) # 기준점 보다 큰 값들 중 가장 작은 값 추출
        sorted_num.insert(0, num) # 가장 앞으로 배치
        break

re_li += sorted_num # 결과에 추가
re = 0
for i in range(len(re_li)):
    re += re_li[i]*(10**(len(re_li)-1-i))

print(re)
print(time.time() - start)