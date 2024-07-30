class Node:
    def __init__(self, value) -> None:
        self.value = value


class Graph:

    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        node = Node(node)

        if node.value not in self.adjacent_list:
            self.adjacent_list[node.value] = []
            self.number_of_nodes += 1

        return self

    def add_edge(self, node1, node2):
        node1 = Node(node1)
        node2 = Node(node2)

        if node1.value in self.adjacent_list:
            if node2.value not in self.adjacent_list[node1.value]:
                self.adjacent_list[node1.value].append(node2.value)
        if node2.value in self.adjacent_list:
            if node1.value not in self.adjacent_list[node2.value]:
                self.adjacent_list[node2.value].append(node1.value)

        return self


    def show_connections(self):
        print("\n".join([f"{key} --> {value}" for key, value in self.adjacent_list.items()]))

if __name__ == "__main__":

    ## Adjacency List Representation
    graph = Graph()
    graph.add_vertex("0")
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_vertex("4")
    graph.add_vertex("5")
    graph.add_vertex("6")

    graph.add_edge('3', '1')
    graph.add_edge('3', '4')
    graph.add_edge('4', '2')
    graph.add_edge('4', '5')
    graph.add_edge('1', '2')
    graph.add_edge('1', '0')
    graph.add_edge('0', '2')
    graph.add_edge('6', '5')

    graph.show_connections()

    



