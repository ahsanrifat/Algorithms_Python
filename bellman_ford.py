from dataclasses import dataclass, field
from typing import List


@dataclass
class BellManFord:

    def __init__(self):
        # this is the result dict which will contain the distance of each node
        self.distance_dict: dict = {}
        # edge list (edge1,edge2,weight)
        # list of tuples (edge1,edge2,weight from 1 to 2)
        self.edge_list: List[tuple] = []

    def add_edge(self, edge1, edge2, weight):
        self.distance_dict[edge1] = float('inf')
        self.distance_dict[edge2] = float('inf')
        self.edge_list.append((edge1, edge2, weight))

    def get_shortest_path(self, source) -> dict:
        # relax all the edges vertices-1 times
        self.distance_dict[source] = 0
        for _ in range(len(self.distance_dict)-1):
            for edge1, edge2, weight in self.edge_list:
                # if current distance is smaller then source's distance plus weight then update
                if self.distance_dict.get(edge1)+weight < self.distance_dict.get(edge2):
                    self.distance_dict[edge2] = self.distance_dict.get(
                        edge1)+weight
        # checking for negative cycle
        # after relaxing number_of_edges-1 times if it changes after one iteration of relaxation then there is a negative cycle

        for edge1, edge2, weight in self.edge_list:
            # print(weight)
            if self.distance_dict.get(edge1)+weight < self.distance_dict.get(edge2):
                print("Contains negative cycle")
        return self.distance_dict


if __name__ == "__main__":
    graph1 = BellManFord()
    graph1.add_edge(0, 1, -1)
    graph1.add_edge(0, 2, 4)
    graph1.add_edge(1, 2, 3)
    graph1.add_edge(1, 3, 2)
    graph1.add_edge(1, 4, 2)
    graph1.add_edge(3, 2, 5)
    graph1.add_edge(3, 1, 1)
    graph1.add_edge(4, 3, -3)

    # Print the solution
    print(graph1.get_shortest_path(0))

    # testing with negative cycle
    graph2 = BellManFord()
    graph2.add_edge("A", "B", 2)
    graph2.add_edge("B", "C", -4)
    graph2.add_edge("C", "A", 1)
    print(graph2.get_shortest_path("A"))
