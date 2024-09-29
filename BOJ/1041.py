n = int(input())
dices = list(map(int,input().split()))

# 5개의 면의 합이 최소가 되게 배치해야함
# 가장 낮은 값을 
min_af = min(dices[0], dices[5])
min_be = min(dices[1], dices[4])
min_cd = min(dices[2], dices[3])

if n == 1:
    print(sum(dices) - max(dices))
else:
    three_dimension = min_af+min_be+min_cd
    two_dimension = three_dimension - max(min_af , max(min_be , min_cd))
    one_dimension = min(min(min_af, min_be), min_cd)

    result = one_dimension * (4 * (n-2)* (n-1) + (n-2) * (n-2)) + two_dimension * (4*(n-1) + 4 * (n-2)) + three_dimension * 4

    print(result)


# n == 2 일때 1면 0개  2면 4개 3면 4개
# 1층 : 1 : 0  2 : 4
# 2층 : 1 : 0  2 : 0  3 : 4

# n == 3 일때 1면 9개  2면 12개(4 + 8) 3면 4개 9 + 24 + 12   45개
# 1층  1 : 4  2 : 4 
# 2층  1 : 4  2 : 4
# 3층  1 : 1  2 : 4 3 : 4 

# n == 4 일때 1면 28개 2면 20개(4 + 8 + 8) 3면 4개 28 + 40 + 12 80
# 1층  1 : 8  2 : 4
# 2층  1 : 8  2 : 4
# 3층  1 : 8  2 : 4
# 4층  1 : 4  2 : 8  3 : 4 

