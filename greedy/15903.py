import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

cards = [] # heap 생성
card_list = list(map(int, input().split()))

for card in card_list:
    heapq.heappush(cards, card) # 카드의 수들을 리스트로 받고 heap에 저장해준다.

for _ in range(m):
    card1 = heapq.heappop(cards) # heap에서 가장 작은 수를 pop 해준다.
    card2 = heapq.heappop(cards) # heap에서 가장 작은 수를 pop 해준다.

    heapq.heappush(cards, card1 + card2) # heap에 pop한 card1과 card2를 더한 값을 push 해준다.
    heapq.heappush(cards, card1 + card2) # heap에 pop한 card1과 card2를 더한 값을 push 해준다.

print(sum(cards))
