import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())
inorder = list(map(int, input().split())) # left root right
postorder = list(map(int, input().split())) # left right root
# preorder: root left right

inindex = [0 for i in range(n+1)]
for i in range(n):
    inindex[inorder[i]] = i

def preorder(instart, inend, poststart, postend):
    if instart > inend or poststart > postend:
        return
    rootvalue = postorder[postend]
    print(rootvalue, end=" ")
    rootindex = inindex[rootvalue]
    leftnode = rootindex - instart
    rightnode = inend - rootindex
    preorder(instart, instart+leftnode-1, poststart, poststart+leftnode-1)
    preorder(inend-rightnode+1, inend, postend-rightnode, postend-1)

preorder(0, n-1, 0, n-1)