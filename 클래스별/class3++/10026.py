import sys
import deque
input = sys.stdin.readline
n = int(input())
paint = []

for i in range(n):
    temp = input().rstrip()
    paint.append(temp)

queue_r = deque()
queue_g = deque()
queue_b = deque()

