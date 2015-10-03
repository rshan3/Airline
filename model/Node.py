__author__ = 'Ruihan'

# Here, Node contains all the information related to our city
class Node:
    # I am a constructor
    def __init__(self, metro):
        self.edges = []
        self.code = metro['code']
        self.name = metro['name']
        self.country = metro['country']
        self.continent = metro['continent']
        self.timezone = metro['timezone']
        self.coordinates = metro['coordinates']
        self.population = metro['population']
        self.region = metro['region']

    def __repr__(self):
        return str("Metro: {}\n"
                   "Name: {}\n"
                   "Country: {}\n"
                   "Continent: {}\n"
                   "Timezone: {}\n"
                   "Coordinate: {}\n"
                   "Population: {}\n"
                   "Region: {}\n".format(
                    self.code,
                    self.name,
                    self.country,
                    self.continent,
                    self.timezone,
                    self.coordinates,
                    self.population,
                    self.region
                ))

    def add_edge(self, edge):
        self.edges.append(edge)


    def remove_edge(self, edge):
        # TODO implement this
        pass








