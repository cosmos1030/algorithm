n, r, c = map(int, input().split())


def recur_row(num, cnt):
    q = num//2
    remainder = num % 2
    if q==0:
        return remainder*(2**(cnt*2))*2
    else:
        return recur_row(q, cnt+1) + remainder*(2**(cnt*2))*2

def recur_col(num, cnt):
    q = num//2
    remainder = num % 2
    if q==0:
        return remainder*(2**(cnt*2))
    else:
        return recur_col(q, cnt+1) + remainder*(2**(cnt*2))


# print(recur_row(r,0))
# print(recur_col(c,0))
print(recur_row(r,0)+recur_col(c, 0))
