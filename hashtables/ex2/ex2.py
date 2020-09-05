#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    route = [None] * length

    d = {}

    for i in tickets:
        d[i.source] = i.destination

    togo = d['NONE']
    
    for i in range(length):
        route[i] = togo
        togo = d[togo]
        
    return route
