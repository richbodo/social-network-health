import math, random

# adjacency as sets
G = {1:{2,3}, 2:{1,3}, 3:{1,2,4}, 4:{3,5}, 5:{4}}
nodes = list(G)

theta_edges, theta_tri = -1.5, 1.0

def common_neighbors(i, j):
    return len(G[i] & G[j])

def tie_prob(i, j):
    c = common_neighbors(i, j)
    logit = theta_edges * 1 + theta_tri * c   # delta_edges is always 1
    return 1 / (1 + math.exp(-logit)), c

def gibbs_step():
    i, j = random.sample(nodes, 2)
    p, c = tie_prob(i, j)
    u = random.random()
    add = u < p
    # apply the resample
    if add:
        G[i].add(j); G[j].add(i)
    else:
        G[i].discard(j); G[j].discard(i)
    print(f"dyad {i}-{j}: common={c}, p={p:.3f}, u={u:.3f} -> "
          f"{'edge present' if add else 'edge absent'}")

def stats():
    edges = sum(len(v) for v in G.values()) // 2
    tri = sum(1 for a in nodes for b in G[a] for c in G[a]&G[b] if a<b<c)
    return edges, tri

print("start:", stats())
for _ in range(10):
    gibbs_step()
print("end:", stats())


