'''
부모님과 함께 놀러간 영일이는
설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
(잉어, 붕어, 용 등 여러 가지가 적혀있다.)

격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
'''
# d = []
# h, w = input().split()
# h = int(h)
# w = int(w)
# n = int(input())
# for i in range(h):
#     d.append([])
#     for j in range(w):
#         d[i].append(0) # [ [0, 0 , 0, 0, 0], ... ]
    
# for i in range(n):
#     l, d, x, y = input().split()
#     l = int(l)
#     d = int(d)
#     x = int(x)
#     y = int(y)
#     if d == 0:  # 가로
#         d[x-1][y-1:y+l-1] = 1       
#     else : # 세로
#         d[x-1:x+l-1][y-1] = 1       

# for i in range(h):
#     for j in range(w):
#         print(d[i][j], end = " ")
#     print()
    
'''
'int' object is not subscriptable
python의 list는 도저히 모르겠다. 직관적이지 않은 느낌?
아무리 디버깅을 해도 d[0]~d[1]은 list로 뜨고, 그 상황에서 한 번 더 접근하려는데 왜 접근 불가인지도 모르겠다.

... 그냥 변수명이 겹쳐서 그런 거였다. 간단하게 풀려다 더 망해버린...
그럼에도 불구하고 직관적이지 않은 느낌은 분명하다. 뭐 적응하면 괜찮아질 수도 있지만 적어도 지금은 바로 떠올리기는 힘들다.
'''
d = []
h, w = input().split()
h = int(h)
w = int(w)
n = int(input())
for i in range(h):
    d.append([])
    for j in range(w):
        d[i].append(0) # [ [0, 0 , 0, 0, 0], ... ]

for i in range(n):
    l, dir, x, y = input().split()
    l = int(l)
    dir = int(dir)
    x = int(x)
    y = int(y)
    if dir == 0:  # 가로
        for j in range(l):
            d[x-1][y-1] = 1
            y += 1       
    else : # 세로
        for j in range(l):
            d[x-1][y-1] = 1       
            x += 1
for i in range(h):
    for j in range(w):
        print(d[i][j], end = " ")
    print()
    