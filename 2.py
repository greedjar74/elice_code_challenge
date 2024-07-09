n, m = map(int, input().split())
nums = list(map(int, input().split()))

works = list()
for _ in range(m):
    works.append(tuple(map(int, input().split())))

for i in range(m):
    start, end = works[i][0] - 1, works[i][1]
    idx = works[i][2] - 1
    tmp = sorted(nums[start:end])
    print(tmp[idx])