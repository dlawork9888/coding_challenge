import math

# # 예제 입력
# T = 3
# line1 = "0 0 13 40 0 37"
# line2 = "0 0 3 0 7 4"
# line3 = "1 1 1 1 1 5"

def sol(line):
    x1, y1, r1, x2, y2, r2 = [int(x) for x in line.split()]
    # 무한대 경우 => 중심이 같고 반지름도 같을때
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1
    dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
    # 한 원의 중심이 다른 원의 외부
    if max(r1,r2) < dist:
        if dist > r1 + r2: return 0
        if dist == r1 + r2: return 1
        if dist < r1 + r2: return 2
    else: # 내부 
        if dist > max(r1,r2) - min(r1,r2): return 2
        if dist == max(r1,r2) - min(r1,r2): return 1
        if dist < max(r1,r2) - min(r1,r2): return 0 
for _ in range(int(input())):
    print(sol(input()))