n, m, q = map(int, input().split())
listM = []
listQ = []
infected = []

for i in range(m):
    u, v = map(int, input().split())

for i in range(q):
    


for node in listQ:
    

def deepSearch(node, listM, infected):
    count = 0

    for i in range(n):
        if infected.count(i) == 0 and listM.count((i, node)) + listM.count((node, i)) == 0:
            infected.append(i)
            return deepSearch(node, listM, infected)+1

    return count