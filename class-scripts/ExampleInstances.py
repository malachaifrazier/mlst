# <codecell>

G1 = nx.wheel_graph(5)
nx.draw(G1)

# <codecell>

nx.draw(unityMST(G1))

# <codecell>

nx.draw(degBasedMST(G1))

# <codecell>

G2 = nx.hypercube_graph(3)
nx.draw(G2)

# <codecell>

nx.draw(unityMST(G2))

# <codecell>

nx.draw(degBasedMST(G2))

# <codecell>

G3 = nx.barbell_graph(4,2)
nx.draw(G3)

# <codecell>

nx.draw(unityMST(G3))

# <codecell>

nx.draw(degBasedMST(G3))

# <codecell>

G4 = nx.complete_graph(6)
nx.draw(G4)

# <codecell>

nx.draw(unityMST(G4))

# <codecell>

nx.draw(degBasedMST(G4))

# <codecell>

G5 = nx.complete_bipartite_graph(3,5)
nx.draw(G5)

# <codecell>

nx.draw(unityMST(G5))

# <codecell>

nx.draw(degBasedMST(G5))

# <codecell>

G6 = nx.cycle_graph(5)
nx.draw(G6)

# <codecell>

nx.draw(unityMST(G6))

# <codecell>

nx.draw(degBasedMST(G6))

# <codecell>

G7 = nx.lollipop_graph(5,3)
nx.draw(G7)

# <codecell>

nx.draw(unityMST(G7))

# <codecell>

nx.draw(degBasedMST(G7))

# <codecell>

G8 = nx.circular_ladder_graph(5)
nx.draw(G8)

# <codecell>

nx.draw(unityMST(G8))

# <codecell>

nx.draw(degBasedMST(G8))

# <codecell>

G9 = nx.star_graph(5)
nx.draw(G9)

# <codecell>

nx.draw(unityMST(G9))

# <codecell>

nx.draw(degBasedMST(G9))

# <codecell>

G10 = nx.gnp_random_graph(8,.5)
nx.draw(G10)

# <codecell>

nx.draw(unityMST(G10))

# <codecell>

nx.draw(degBasedMST(G10))

# <codecell>
