from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

print(round(sum(nums) / n)) #산술평균
nums.sort()
print(nums[n//2]) #중간값

cnt = Counter(nums).most_common(2) #빈도수 높은 숫자 2개 

#최빈값
if len(nums) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(nums) - min(nums)) #최댓값 - 최솟값
