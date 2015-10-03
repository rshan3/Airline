from collections import defaultdict
from model.Edge import Edge
from model.Node import Node
from operator import attrgetter


__author__ = 'Ruihan'

# Graph Class, it deals with all the nodes and edges information
# It also responsible for answering the graph querying
class Graph:
    # I am a constructor
    def __init__(self):
        self.metros = dict()
        self.metro_name_decode = dict()
        self.routes = []
        self.continents = defaultdict(list)

    # Add a single metro
    def add_node(self, node):
        self.metros[node["code"]] = Node(node)
        self.metro_name_decode[node["name"]] = node["code"]
        self.continents[node["continent"]].append(node["name"])

    # Add a list of metros
    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    # Add a single route (including back)
    def add_edge(self, route):
        edge = Edge.fromEdge(route)

        origin = edge.origin

        # We only deal with metros which has our service
        if(origin not in self.metros):
            return

        destination = edge.destination
        if(destination not in self.metros):
            return

        distance = edge.distance

        edge_back = Edge(destination,origin,distance)

        self.routes.append(edge)
        self.routes.append(edge_back)

        self.metros[origin].add_edge(edge)
        self.metros[destination].add_edge(edge_back)

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def get_city_info(self, str):
        if(self.metros.get(str) is not None):
            return self.metros[str]
        elif(self.metro_name_decode.get(str) is not None):
            return self.metros[self.metro_name_decode.get(str)]
        else:
            return None

    def list_metros(self):
        return self.metro_name_decode.keys()


    def get_longest_single_flight(self):
        return max(self.routes, key = attrgetter('distance'))

    def get_shortest_single_flight(self):
        return min(self.routes, key = attrgetter('distance'))

    def get_average_distances_of_flight(self):
        return sum(edge.distance for edge in self.routes)/len(self.routes)

    def get_biggest_city(self):
        return max(self.metros.values(), key = attrgetter('population'))

    def get_smallest_city(self):
        return min(self.metros.values(), key = attrgetter('population'))

    def get_average_population(self):
        return sum(metro.population for metro in self.metros.values())/len(self.metros)

    def get_continent_city(self):
        return self.continents

    def get_hub(self):
        max_routes_num = max(len(metro.edges) for metro in self.metros.values())
        return [metro.name for metro in self.metros.values() if len(metro.edges) == max_routes_num]


