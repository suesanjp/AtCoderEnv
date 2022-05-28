# 整数の入力
from posixpath import split

a = int(input())

# スペース区切りの整数の入力
a, b = map(int, input().split())


# スペース区切りの整数の入力をリストにする
a = list(map(int, input().split()))

# スペース区切りの文字列の入力をリストにする
s = input().split()

# n個の要素をリストに格納
n = int(input())
s = [input() for _ in range(n)]

