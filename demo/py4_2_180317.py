# coding=utf-8
L = ['test', 1.23, 222]
print(L)
L.sort()
print(L)
L.pop(1)
print(L)
L.reverse()
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
L = [raw[1] for raw in M if raw[1] % 2 == 0]
print(L)
print'raw=', raw
G = (sum(raw) for raw in M)
print next(G)
tmap = list(map(sum, M))
print(tmap)
tmap = (map(sum, M))
print(tmap)
print {sum(raw) for raw in M}
print({1, 2, 3, 3, 3, 3})
print({i: sum(M[i]) for i in range(3)})
print([ord(x) for x in 'hello'])
