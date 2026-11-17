# from collections import deque

# deque = deque()
# deque.append("appple")
# deque.append("mango")
# deque.append("banana")

# print(deque)

# first = deque.popleft()
# print(first)
# print(deque)
# print(len(deque))

#priority queue

import heapq

hospital = []

heapq.heappush(hospital,(3,"broken_finger"))
heapq.heappush(hospital,(1,"heartattck"))
heapq.heappush(hospital,(2,"high_feaver"))

print(heapq.heappop(hospital))
print(heapq.heappop(hospital))
print(heapq.heappop(hospital))

