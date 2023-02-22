import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n)]

for i in range(n):
    a,b,c = input().split()
    graph[ord(a)-65] = [ord(b)-65, ord(c)-65]

def preorder(root):
    if root<0:
        return
    print(chr(root+65), end="")
    left, right = graph[root]
    # print(root, left, right)
    preorder(left)
    preorder(right)

def inorder(root):
    if root<0:
        return
    left, right = graph[root]
    # print(root, left, right)
    inorder(left)
    print(chr(root+65), end="")
    inorder(right)

def postorder(root):
    if root<0:
        return
    left, right = graph[root]
    # print(root, left, right)
    postorder(left)
    postorder(right)
    print(chr(root+65), end="")

preorder(0)
print()
inorder(0)
print()
postorder(0)
print()