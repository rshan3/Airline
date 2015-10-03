from controller.Controller import Controller
from model.Graph import Graph

__author__ = 'Ruihan'


my_graph = Graph()
my_controller = Controller(my_graph)

my_controller.parse_file("content/map_data.json")
my_controller.start()

