import json
import webbrowser
from model.Graph import Graph

__author__ = 'Ruihan'



class Controller:
    def __init__(self, graph):
        self.graph = graph
        self.view = None

    def parse_file(self, file):
        with open(file) as data_file:
            data = json.load(data_file)
            self.graph.add_nodes(data['metros'])
            self.graph.add_edges(data['routes'])



    def start(self):
        print("Welcome using the query system of CSAir!")
        while(True):
            print()
            print("Enter 1 for querying a city")
            print("Enter 2 for querying other information")
            print("Enter 3 for listing all the cities on CSAir")
            print("Enter 4 for showing the map")
            print("Enter 0 for quiting")

            user_input = input()

            if user_input == '0':
                print("Bye!")
                break
            elif user_input == '1':
                self.city_query()
            elif user_input == '2':
                self.info_query()
            elif user_input == '3':
                print(self.graph.list_metros())
            elif user_input == '4':
                self.show_map()
            else:
                print("Sorry, please input a valid input")

    def city_query(self):
        while(True):
            print()
            print("Enter a city's name or its code, enters 0 to return to the main menu")
            user_input = input()
            if user_input == '0':
                return
            city_info = self.graph.get_city_info(user_input)
            if city_info is not None:
                self.display(city_info)
            else:
                print("Sorry, cant find {}, try again, or enter 0 to the main menu".format(user_input))


    def info_query(self):
        option = {
            'a': self.graph.get_longest_single_flight,
            'b': self.graph.get_shortest_single_flight,
            'c': self.graph.get_average_distances_of_flight,
            'd': self.graph.get_biggest_city,
            'e': self.graph.get_smallest_city,
            'f': self.graph.get_average_population,
            'g': self.graph.get_continent_city,
            'h': self.graph.get_hub
        }


        while(True):
            print()
            print("What information you want get?")
            print("Enter a , the longest single flight in the network")
            print("Enter b , the shortest single flight in the network")
            print("Enter c , the average distance of all the flights in the network")
            print("Enter d , the biggest city (by population) served by CSAir")
            print("Enter e , the smallest city (by population) served by CSAir")
            print("Enter f , the average size (by population) of all the cities served by CSAir")
            print("Enter g , a list of the continents served by CSAir and which cities are in them")
            print("Enter h , identifying CSAir's hub cities, the cities that have the most direct connections.")
            print("Enter 0 , Return to the main menu")

            user_input = input()
            user_input = user_input.lower()

            if user_input == '0':
                return
            elif user_input in ['a','b','c','d','e','f','g','h']:
                print(option[user_input]())
            else:
                print("Sorry, please enter a valid input or enter 0 to return to the main menu")




    def display(self, city_info):
        print('code : {} ,'.format(city_info.code))
        print('name : {} ,'.format(city_info.name))
        print('country : {} ,'.format(city_info.country))
        print('continent : {} ,'.format(city_info.continent))
        print('timezone : {} ,'.format(city_info.timezone))
        print('coordinates : {} ,'.format(city_info.coordinates))
        print('population : {} ,'.format(city_info.population))
        print('region : {} ,'.format(city_info.region))
        for edge in city_info.edges:
            print("To: {}, {}km".format(edge.destination, edge.distance))

    def show_map(self):
        my_url = 'http://www.gcmap.com/mapui?P='
        for edge in self.graph.routes:
            origin = edge.origin
            destination = edge.destination
            my_url = my_url + "+" + origin + "-" + destination + ","

        webbrowser.open_new(my_url)



