# 🌟일부 아이디어 별표
# 화폐종류 N개, M원 만드는 최소화폐사용개수. N개 화폐 원 알려줌

N,M = map(int, input().split())
value = [int(input()) for _ in range(N)]

d = [10001]*(M+1) # 10001최소로 잡고, 🌟M개수만큼만 배열 만들어놓으면 됨
d[0] = 0

for i in range(M+1):  #M+1 +1 안해서 틀림. M까지 돌려야됨.
    for j in value:
        if i>=j and d[i-j] != 10001:
            d[i] = min(d[i], d[i-j]+1)

print(-1 if d[M]==10001 else d[M])