import numpy as np
import os
os.system('cls')

def setParent(parent, from_, to_, n) :

    if parent[from_] < parent[to_] :    
        for i in range(n) :
            if parent[i] == parent[to_] and i != to_:
                parent[i] = parent[from_]
        parent[to_] = parent[from_]
    else :
        for i in range(n) :
            if parent[i] == parent[from_] and i != from_:
                parent[i] = parent[to_]
        parent[from_] = parent[to_]

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])

    for from_, to_, cost_ in costs :
        if parent[from_] != parent[to_] :
            #print("Before : ",parent, from_, to_)
            answer += cost_
            setParent(parent, from_, to_, n)
            #print("After : ",parent, from_, to_)
            #print("="*40)
    return answer

print(solution(5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]), 6)
print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]), 15)
print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]), 8)
print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]]), 9)
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]), 104)
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]), 11)
print(solution(5, [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]), 8)
print(solution(5, [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]]), 8)
print(solution(5, [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]))
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))