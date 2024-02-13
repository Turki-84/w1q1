from multipledispatch import dispatch

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []  # for graph

class Graph:

    def __init__(self):
        self.nodes = []

    def add_member(self, name, age=0, location=''):
        self.nodes.append(Node(name))

    def add_relationship(self, node1_data, node2_data):

        node1_index = -1
        node2_index = -1
        for i in range(len(self.nodes)):
            if self.nodes[i].data == node1_data:
                node1_index = i

            if self.nodes[i].data == node2_data:
                node2_index = i

        if node1_index != -1 and node2_index != -1:
            self.nodes[node1_index].neighbors.append(self.nodes[node2_index])
            self.nodes[node2_index].neighbors.append(self.nodes[node1_index])

    def find_friends(self, node_data):

        for node in self.nodes:
            if node.data is node_data:

                neighbors = node.neighbors
                neighbors_data = []

                for naighbor in neighbors:
                    neighbors_data.append(naighbor.data)

                return neighbors_data
        return []

    def is_not_in(self, our_node, visited):
        for node in visited:
            if our_node == node:
                return False
        return True

    @dispatch(int, int)
    def shortest_path(self, start_data, goal_data):
        node1_index = -1
        node2_index = -1
        for i in range(len(self.nodes)):
            if self.nodes[i].data == start_data:
                node1_index = i

            if self.nodes[i].data == goal_data:
                node2_index = i

        return self.shortest_path(self.nodes[node1_index], self.nodes[node2_index], [], 0)

    @dispatch(Node, Node, list, int)
    def shortest_path(self, start_node, goal_node, visited, steps):

        if start_node == goal_node:
            return steps

        min = len(self.nodes)

        there_is_away = False

        visited.append(start_node)

        for neighbor in start_node.neighbors:

            if self.is_not_in(neighbor, visited):
                there_is_away = True
                nodes_shortest_path = self.shortest_path(neighbor, goal_node, visited.copy(), (steps + 1))

                if nodes_shortest_path != -1 and min > nodes_shortest_path:
                    min = nodes_shortest_path

        if not there_is_away:
            return -1

        return min