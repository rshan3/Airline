from unittest import TestCase
from controller.Controller import Controller
from model.Graph import Graph

__author__ = 'SwagRuihan'


class TestGraph(TestCase):
  def test_add_nodes(self):
    my_graph = Graph()
    my_controller = Controller(my_graph)

    my_controller.parse_file("F:/rshan3/Airline/content/map_test_data.json")
    self.assertTrue(len(my_graph.metros) == 3)



  def test_add_edges(self):
    my_graph = Graph()
    my_controller = Controller(my_graph)

    my_controller.parse_file("F:/rshan3/Airline/content/map_test_data.json")

    self.assertTrue(len(my_graph.routes) == 2*2)
    self.assertTrue('BOG' not in my_graph.metros)


  def test_get_city_info(self):
    my_graph = Graph()
    my_controller = Controller(my_graph)

    my_controller.parse_file("F:/rshan3/Airline/content/map_test_data.json")

    self.assertTrue(my_graph.get_city_info('LIM') is not None)
    self.assertTrue(my_graph.get_city_info('LIMM') is None)
    self.assertTrue(my_graph.get_city_info("Lima") is not None)

  def test_list_metros(self):
    my_graph = Graph()
    my_controller = Controller(my_graph)

    my_controller.parse_file("F:/rshan3/Airline/content/map_test_data.json")
    #print(my_graph.list_metros())
    self.assertTrue(len(my_graph.list_metros()) == 3 )

  def test_get_single_flight(self):
    my_graph = Graph()
    my_controller = Controller(my_graph)

    my_controller.parse_file("F:/rshan3/Airline/content/map_test_data.json")
    #print(my_graph.list_metros())
    self.assertTrue(my_graph.get_longest_single_flight().distance == 4231 )
    self.assertTrue(my_graph.get_shortest_single_flight().distance == 2453)

  def test_get_average_distances_of_flight(self):
    my_graph = Graph()
    my_controller = Controller(my_graph)

    my_controller.parse_file("F:/rshan3/Airline/content/map_test_data.json")
    #print(my_graph.list_metros())
    self.assertTrue(my_graph.get_average_distances_of_flight() == (4231+2453)/2.0 )
    #self.assertTrue(my_graph.get_shortest_single_flight().distance == 2453)

  def test_get_population(self):
    my_graph = Graph()
    my_controller = Controller(my_graph)

    my_controller.parse_file("F:/rshan3/Airline/content/map_test_data.json")
    self.assertTrue(my_graph.get_biggest_city().code == 'MEX')
    self.assertTrue(my_graph.get_smallest_city().code == 'SCL')


  def test_get_hub(self):
    my_graph = Graph()
    my_controller = Controller(my_graph)

    my_controller.parse_file("F:/rshan3/Airline/content/map_test_data.json")
    self.assertTrue(my_graph.get_hub()[0] == 'Lima')
