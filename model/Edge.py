__author__ = 'Ruihan'

# Edge denotes the routes
# The edge is directed
class Edge:
  def __init__(self, origin, destination, distance):
    self.origin = origin
    self.destination = destination
    self.distance = distance

  @classmethod
  def fromEdge(cls, edge):
      return cls(edge["ports"][0], edge["ports"][1], edge["distance"])

  def __repr__(self):
    return "Ports: [" + self.origin + ", " + self.destination + "]  Distance: " + str(self.distance) + "km"