import numpy as np
import os
os.system('cls')

def setParent(parent, from_, to_, n) :

    if from_ < to_ :    
        for i in range(n) :
            if parent[i] == to_:
                parent[i] = parent[from_]
    else :
        for i in range(n) :
            if parent[i] == from_ :
                parent[i] = parent[to_]

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])

    for from_, to_, cost_ in costs :
        if parent[from_] != parent[to_] :
            print("Before : ",parent, from_, to_)
            answer += cost_
            setParent(parent, from_, to_, n)
            print("After : ",parent, from_, to_)
            print("="*40)
    return answer

print(solution(5, [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]))
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))