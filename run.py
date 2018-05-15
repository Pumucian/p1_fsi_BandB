# Search methods

import search


def camino (A, B):
    ab = search.GPSProblem(A, B, search.romania)
    ra = search.ram_aco_graph_search(ab).path()
    rah = search.ram_aco_heur_graph_search(ab).path()
    print("Camino desde " + A + " hasta " + B + ": ")
    print("Sin heuristica: " + str(ra[:-1]) + " " + str(ra[-1]))
    print("Con heuristica: " + str(rah[:-1]) + " " + str(rah[-1]))


camino("A", "B")
camino("D", "B")
camino("I", "C")
camino("N", "O")
camino("R", "A")

#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
